"""
AGENTE RAG CON LANGGRAPH + CHROMA + GEMINI
===========================================
Pipeline completo con Gemini Haiku (modelo más barato y rápido)
"""

import os
from typing import Annotated, TypedDict

# LangGraph
from langgraph.graph import StateGraph, START, END
from langgraph.graph.message import add_messages
from langgraph.checkpoint.memory import MemorySaver

# LangChain
from langchain_core.messages import BaseMessage, HumanMessage, SystemMessage
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_chroma import Chroma

# ============================================================================
# 1. CONFIGURACIÓN
# ============================================================================

from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv("GEMINI_API_KEY_001")
if not API_KEY:
    raise ValueError("❌ GEMINI_API_KEY_001 no configurada. Verifica .env")

CHROMA_PATH = "./chroma_db_motores"

# Lista de modelos Gemini (en orden de preferencia)
MODELOS_GEMINI = [
    "gemini-2.5-flash",
    "gemini-2.0-flash",
    "gemini-1.5-pro"
]

# ============================================================================
# 2. INICIALIZAR LLM CON FAILOVER
# ============================================================================

def inicializar_llm_con_failover():
    """Intenta modelos en orden. Si uno falla, usa el siguiente."""
    print("Inicializando Gemini con failover...")
    
    for modelo in MODELOS_GEMINI:
        try:
            print(f"  Intentando: {modelo}...", end=" ")
            llm = ChatGoogleGenerativeAI(
                model=modelo,
                temperature=0.0,
                google_api_key=API_KEY
            )
            print(f"✅ {modelo} disponible")
            return llm
        except Exception as e:
            print(f"❌ Fallo")
            continue
    
    raise RuntimeError("❌ No hay modelos Gemini disponibles.")

llm = inicializar_llm_con_failover()

embeddings = HuggingFaceEmbeddings(
    model_name="sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2"
)

print(f"✅ LLM: {llm.model_name if hasattr(llm, 'model_name') else 'Gemini'}")
print(f"✅ Embeddings: HuggingFace (local)")

# ============================================================================
# 3. CARGAR VECTORSTORE
# ============================================================================

def cargar_vectorstore():
    """Carga ChromaDB ya indexado."""
    if not os.path.exists(CHROMA_PATH):
        raise FileNotFoundError(
            f"❌ ChromaDB no encontrado en {CHROMA_PATH}. "
            f"Primero debes procesar los PDFs."
        )
    
    vectorstore = Chroma(
        persist_directory=CHROMA_PATH,
        embedding_function=embeddings
    )
    return vectorstore

try:
    vectorstore = cargar_vectorstore()
    print(f"✅ ChromaDB cargado: {CHROMA_PATH}")
except FileNotFoundError as e:
    print(f"⚠️  {e}")
    vectorstore = None

# ============================================================================
# 4. ESTADO DEL AGENTE
# ============================================================================

class EstadoAgente(TypedDict):
    """Estado que fluye a través del grafo."""
    pregunta: str
    contexto_documentos: list[str]
    mensajes: Annotated[list[BaseMessage], add_messages]
    respuesta: str

# ============================================================================
# 5. NODOS DEL AGENTE RAG
# ============================================================================

def nodo_retrieval(estado: EstadoAgente) -> dict:
    """Recupera documentos relevantes de ChromaDB."""
    if not vectorstore:
        return {"contexto_documentos": []}
    
    pregunta = estado["pregunta"]
    docs = vectorstore.similarity_search(pregunta, k=3)
    contexto = [doc.page_content for doc in docs]
    
    return {"contexto_documentos": contexto}

def nodo_generacion(estado: EstadoAgente) -> dict:
    """Genera respuesta con Gemini. Si falla, intenta otros modelos."""
    pregunta = estado["pregunta"]
    contexto = estado["contexto_documentos"]
    
    if contexto:
        contexto_str = "\n\n".join(contexto)
        prompt_usuario = f"""Basándote en los siguientes documentos, responde la pregunta:

--- DOCUMENTOS ---
{contexto_str}
--- FIN DOCUMENTOS ---

Pregunta: {pregunta}

Instrucciones:
- Responde solo con información del contexto
- Si no encuentras la respuesta, dilo claramente
- Sé conciso y preciso"""
    else:
        prompt_usuario = pregunta
    
    system_prompt = """Eres un asistente experto en motores de combustión que responde preguntas 
basándote en documentos específicos. Tu objetivo es proporcionar respuestas precisas y fundamentadas. 
Si la información no está disponible, lo indicarás claramente."""
    
    mensajes = [SystemMessage(content=system_prompt)] + estado["mensajes"]
    mensajes.append(HumanMessage(content=prompt_usuario))
    
    # Intenta con el LLM actual, si falla por cuota, intenta otros modelos
    for modelo_fallback in MODELOS_GEMINI:
        try:
            respuesta_obj = llm.invoke(mensajes)
            respuesta = respuesta_obj.content
            return {
                "respuesta": respuesta,
                "mensajes": [respuesta_obj]
            }
        except Exception as e:
            if "RESOURCE_EXHAUSTED" in str(e) or "429" in str(e):
                print(f"  Cuota excedida. Intentando siguiente modelo...")
                # Crear nuevo LLM con siguiente modelo
                try:
                    llm_temp = ChatGoogleGenerativeAI(
                        model=modelo_fallback,
                        temperature=0.3,
                        google_api_key=API_KEY
                    )
                    respuesta_obj = llm_temp.invoke(mensajes)
                    respuesta = respuesta_obj.content
                    return {
                        "respuesta": respuesta,
                        "mensajes": [respuesta_obj]
                    }
                except:
                    continue
            else:
                raise
    
    return {
        "respuesta": "Sorry! No es posible responder mas preguntas porque has acabado con la cuota de los 3 modelos de Gemini. Mañana se habrá recargado la cuota y podrás continuar.",
        "mensajes": []
    }

# ============================================================================
# 6. CONSTRUIR GRAFO LANGGRAPH
# ============================================================================

def construir_grafo():
    """Construye el grafo LangGraph."""
    grafo = StateGraph(EstadoAgente)
    grafo.add_node("retrieval", nodo_retrieval)
    grafo.add_node("generacion", nodo_generacion)
    grafo.add_edge(START, "retrieval")
    grafo.add_edge("retrieval", "generacion")
    grafo.add_edge("generacion", END)
    
    memoria = MemorySaver()
    app = grafo.compile(checkpointer=memoria)
    return app

app = construir_grafo()
print("✅ Grafo LangGraph compilado")

# ============================================================================
# 7. FUNCIÓN PRINCIPAL DE CHAT
# ============================================================================

def chat_rag(pregunta: str, thread_id: str = "default") -> str:
    """
    Ejecuta el agente RAG con memoria.
    
    Args:
        pregunta: pregunta del usuario
        thread_id: identificador de la conversación
    
    Returns:
        Respuesta del agente
    """
    if not vectorstore:
        return "❌ ChromaDB no disponible. Base de datos no cargada."
    
    config = {"configurable": {"thread_id": thread_id}}
    
    estado_entrada = {
        "pregunta": pregunta,
        "contexto_documentos": [],
        "mensajes": [HumanMessage(content=pregunta)],
        "respuesta": ""
    }
    
    try:
        resultado = app.invoke(estado_entrada, config=config)
        return resultado["respuesta"]
    except Exception as e:
        return f"⚠️ Error generando respuesta: {str(e)}"

# ============================================================================
# 8. EXPORTAR FUNCIONES
# ============================================================================

__all__ = [
    'chat_rag',
    'vectorstore',
    'llm',
    'embeddings',
    'app'
]

# Exportar el modelo usado
MODELO_USADO = llm.model_name if hasattr(llm, 'model_name') else "Desconocido"

__all__ = [
    'chat_rag',
    'vectorstore',
    'llm',
    'embeddings',
    'app',
    'MODELO_USADO'
]