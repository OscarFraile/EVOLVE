"""
INTERFAZ STREAMLIT - Agente RAG de Motores (Con Claude + Failover)
==================================================================
Ejecutar: streamlit run app.py
"""

import streamlit as st
from agente_rag_langgraph_completo import chat_rag

# ============================================================================
# CACHEAR AGENTE
# ============================================================================

@st.cache_resource
def cargar_agente():
    """Cachea el agente para que no se recargue cada vez"""
    from agente_rag_langgraph_completo import app, vectorstore
    return app, vectorstore

try:
    app, vectorstore = cargar_agente()
except Exception as e:
    st.error(f"❌ Error cargando agente: {e}")

# ============================================================================
# CONFIGURACIÓN DE PÁGINA
# ============================================================================

st.set_page_config(
    page_title="Experto en Motores",
    page_icon="🔧",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ============================================================================
# HEADER
# ============================================================================

st.title("🔧 Asistente Experto en Motores 2T y 4T")
st.markdown("""
**Agente RAG** basado en documentos técnicos sobre motores de 2 y 4 tiempos.

Haz preguntas y obtén respuestas fundamentadas en los documentos indexados.
""")

# ============================================================================
# SIDEBAR
# ============================================================================

with st.sidebar:
    st.header("ℹ️ Información")
    
    st.subheader("📚 Base de Conocimiento")
    st.write("""
    - **4 documentos PDF**
    - **158 páginas**
    - **632 párrafos** indexados
    - **Tema:** Motores de combustión interna
    """)
    
    st.subheader("⚙️ Configuración")
    
    # Thread ID para mantener conversación
    thread_id = st.text_input(
        "ID de sesión (para memoria)",
        value="conversacion-001",
        help="Usa el mismo ID para mantener memoria de la conversación"
    )
    
    # Parámetros avanzados
    with st.expander("Parámetros avanzados"):
        st.write("*Nota: Estos parámetros requieren modificar el código*")
        
        try:
            from agente_rag_langgraph_completo import MODELO_USADO
            modelo_activo = MODELO_USADO
        except:
            modelo_activo = "Desconocido"
        
        st.info(f"""
        - **k (documentos):** Actualmente 3
        - **Temperature:** Actualmente 0.0 (bajo = factual)
        - **Modelo activo:** 2.5 Flash / 2.5 Pro""")

    st.divider()
    
    st.subheader("💡 Ejemplos de preguntas")
    ejemplos = [
        "¿Cómo funciona un motor de 4 tiempos?",
        "¿Cuál es la diferencia entre motores de 2 y 4 tiempos?",
        "¿Qué es la fase de compresión?",
        "¿Cuáles son las fases del motor de 2 tiempos?",
        "¿Qué es la preparación del motor?"
    ]
    
    for ejemplo in ejemplos:
        if st.button(f"📝 {ejemplo}", key=ejemplo, use_container_width=True):
            st.session_state.pregunta_seleccionada = ejemplo

# ============================================================================
# INICIALIZAR SESSION STATE
# ============================================================================

if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

if "pregunta_seleccionada" not in st.session_state:
    st.session_state.pregunta_seleccionada = ""

# ============================================================================
# MOSTRAR HISTORIAL DE CHAT
# ============================================================================

for mensaje in st.session_state.chat_history:
    with st.chat_message(mensaje["role"]):
        st.markdown(mensaje["content"])

# ============================================================================
# INPUT DEL USUARIO
# ============================================================================

pregunta = st.chat_input("Haz una pregunta sobre motores...", key="chat_input")

# ============================================================================
# PROCESAR PREGUNTA SELECCIONADA DEL SIDEBAR
# ============================================================================

if st.session_state.pregunta_seleccionada:
    pregunta = st.session_state.pregunta_seleccionada
    st.session_state.pregunta_seleccionada = ""

# ============================================================================
# PROCESAR RESPUESTA
# ============================================================================

if pregunta:
    # Añadir pregunta al historial
    st.session_state.chat_history.append({
        "role": "user",
        "content": pregunta
    })
    
    # Mostrar pregunta
    with st.chat_message("user"):
        st.markdown(pregunta)
    
    # Generar respuesta
    with st.chat_message("assistant"):
        with st.spinner("🤖 Analizando documentos..."):
            respuesta = chat_rag(pregunta, thread_id=thread_id)
        
        st.markdown(respuesta)
    
    # Añadir respuesta al historial
    st.session_state.chat_history.append({
        "role": "assistant",
        "content": respuesta
    })

# ============================================================================
# FOOTER
# ============================================================================

st.divider()

col1, col2, col3 = st.columns(3)

with col1:
    if st.button("🗑️ Limpiar conversación"):
        st.session_state.chat_history = []
        st.rerun()

with col2:
    st.caption(f"📌 Sesión: {thread_id}")

with col3:
    st.caption("v4.0 - Proyecto Final IA Generativa")
