# Agente RAG Experto en Motores de Combustión

## 1. Breve Descripción

Asistente inteligente basado en **Retrieval-Augmented Generation (RAG)** que responde preguntas técnicas sobre motores de combustión interna. El agente recupera información relevante de una base de datos vectorial indexada (ChromaDB) y genera respuestas precisas usando Google Gemini, manteniendo memoria conversacional mediante `thread_id` de LangGraph.

---

## 2. Dominio Elegido

- **Tema principal:** Motores de combustión interna (2 y 4 tiempos)
- **Base de conocimiento:** 4 documentos PDF especializados (158 páginas, 632 párrafos indexados)
- **Tipo de respuestas:** Técnicas, factuales, fundamentadas en documentos
- **Casos de uso:** Educación técnica, referencia rápida, análisis comparativo de ciclos motores
- **Limitación deliberada:** Solo responde si encuentra información en los documentos (sin invención)

---

## 3. Stack Utilizado

| Componente | Tecnología | Justificación |
|---|---|---|
| **LLM** | Google Gemini 2.5-Flash / 2.0-Flash / 1.5-Pro | Acceso vía API, failover automático, modelos rápidos |
| **Embeddings** | HuggingFace (sentence-transformers multilingual MiniLM) | Open-source, local, sin costos API, multilingüe |
| **Base vectorial** | ChromaDB | Ligero, indexado, acceso local rápido |
| **Orquestación** | LangGraph | Control explícito del flujo RAG, memoria conversacional |
| **Framework LLM** | LangChain | Integración limpia con modelos y vectorstores |
| **Interfaz** | Streamlit | Web responsiva, deployment simple, demo en vivo |
| **Python** | 3.11+ | Compatibilidad con todas las librerías |

---

## 4. Guía de Ejecución

### 4.1 Instalación

#### Opción 1: Desde `requirements.txt` (RECOMENDADO)

```bash
# Crear virtual environment
python -m venv venv_proyecto
source venv_proyecto/bin/activate  # Linux/Mac
# o: venv_proyecto\Scripts\activate  # Windows

# Instalar todas las dependencias
pip install -r requirements.txt
```

#### Opción 2: Instalación manual

Si no tienes `requirements.txt`, instala manualmente:

```bash
pip install langgraph langchain-google-genai langchain-chroma langchain-community \
            langchain-huggingface streamlit python-dotenv sentence-transformers chromadb pypdf
```

#### Verificar instalación

```bash
python -c "import langgraph, langchain, streamlit; print('✅ Todas las dependencias instaladas')"
```

### 4.2 Configuración API Key (IMPORTANTE)

**El código requiere una API key de Google Gemini (GRATIS).**

#### Paso 1: Obtener la API Key

1. Accede a: https://aistudio.google.com/app/apikey
2. Haz clic en **"Create API Key"** (botón azul)
3. Selecciona **"Create API key in a new project"**
4. Se abrirá un popup con tu clave
5. **Copia la clave completa**

#### Paso 2: Crear archivo `.env`

En la carpeta del proyecto (misma carpeta que `app.py`), crea un archivo llamado `.env`:

```
GEMINI_API_KEY_001=tu-clave-completa-aqui
```

**Ejemplo:**
```
GEMINI_API_KEY_001=AIzaSyDxxx...xxxxx
```

#### Paso 3: Verificar configuración

Ejecuta:
```python
python
>>> import os
>>> from dotenv import load_dotenv
>>> load_dotenv()
>>> api_key = os.getenv("GEMINI_API_KEY_001")
>>> print("✅ API Key configurada" if api_key else "❌ API Key no encontrada")
```

#### IMPORTANTE - Seguridad

**NUNCA subas `.env` a GitHub o lo compartas.** Contiene tu API key privada.

En el `.gitignore` del proyecto ya está incluido:
```
.env
```

### 4.3 Ejecución

**Interfaz web (Streamlit):**
```bash
streamlit run app.py
# Se abre en http://localhost:8501
```

**Desde Python directo:**
```python
from agente_rag_langgraph_completo import chat_rag

respuesta = chat_rag(
    pregunta="¿Cómo funciona un motor de 4 tiempos?",
    thread_id="sesion-001"
)
print(respuesta)
```

---

## 5. Justificación del System Prompt

### Prompt actual:
```
"Eres un asistente experto en motores de combustión que responde preguntas 
basándote en documentos específicos. Tu objetivo es proporcionar respuestas 
precisas y fundamentadas. Si la información no está disponible, lo indicarás 
claramente."
```

### Decisiones de diseño:

**a) Rol específico ("experto en motores")**
- El modelo sabe su dominio = respuestas más relevantes
- Evita divagaciones a temas generales

**b) "Basándote en documentos específicos"**
- Prioriza el contexto recuperado (RAG)
- No inventa información
- Respuestas verificables

**c) "Si no está disponible, dilo claramente"**
- Honestidad sobre limitaciones
- Previene alucinaciones
- Usuario sabe cuándo no hay respuesta

**d) Temperature 0.0 (determinista)**
- Respuestas factuales, no creativas
- Crítico en dominio técnico
- Reproducibilidad

---

## 6. Arquitectura del Grafo

```
┌─────────────────┐
│  PREGUNTA USER  │
└────────┬────────┘
         │
         ▼
┌──────────────────────────────────────┐
│   NODO RETRIEVAL                     │
│ • Convierte pregunta a vector        │
│ • Busca en ChromaDB (k=3)            │
│ • Recupera párrafos relevantes       │
└────────┬─────────────────────────────┘
         │
         ▼
    ┌─────────────┐
    │  CONTEXTO   │ ← 3 párrafos más similares
    └─────────────┘
         │
         ▼
┌──────────────────────────────────────────────┐
│   NODO GENERACION                            │
│ • System prompt + contexto + pregunta        │
│ • Invoca Gemini con failover                 │
│ • Si falla por cuota → intenta siguiente     │
│ • Devuelve respuesta + historial             │
└────────┬─────────────────────────────────────┘
         │
         ▼
┌──────────────────┐
│  RESPUESTA + MEM │ ← Guardada con thread_id
└──────────────────┘

FLUJO MEMORIA:
thread_id = "usuario-001"
├─ Pregunta 1 → Respuesta 1 → Guardada
├─ Pregunta 2 → Recuerda Q1 → Respuesta 2
└─ Pregunta 3 → Recuerda Q1, Q2 → Respuesta 3

thread_id = "usuario-002"  ← SIN memoria de usuario-001
```

---

## 7. Dependencias

### Librerías principales:

```python
# LangGraph + LangChain
langgraph>=0.0.64
langchain-google-genai>=1.0.0
langchain-chroma>=0.1.0
langchain-community>=0.0.0
langchain-huggingface>=0.0.0

# Embeddings local
sentence-transformers>=2.2.0

# Interfaz web
streamlit>=1.28.0

# Utilidades
python-dotenv>=1.0.0
```

### ChromaDB incluido:
```
chroma_db_motores/
├── data/
├── index/
└── requirements.txt (generado por ChromaDB)
```

### PDFs procesados:
```
pdf_conocimiento/
├── 7044599-Funcionamiento-y-Preparacion-Del-Motor-2-Tiempos.pdf (49 pág)
├── 585888634-Motores.pdf (7 pág)
├── curs_2T_08.pdf (8 pág)
└── Motores de combustión interna.pdf (94 pág)
TOTAL: 158 páginas → 632 párrafos indexados
```

---

## Ejemplos de Uso

### Ejemplo 1: Pregunta simple
```python
respuesta = chat_rag("¿Qué es un motor de 2 tiempos?", thread_id="demo")
# Respuesta: Explicación técnica de ciclo de 2 tiempos
```

### Ejemplo 2: Comparación
```python
respuesta = chat_rag("¿Diferencias entre 2 y 4 tiempos?", thread_id="demo")
# Respuesta: Análisis comparativo con ciclos, eficiencia, aplicaciones
```

### Ejemplo 3: Seguimiento (con memoria)
```python
# Primera pregunta
chat_rag("¿Cuáles son las fases de un motor 4T?", thread_id="sesion-1")
# Segunda pregunta (recuerda la anterior)
chat_rag("¿Qué ocurre en la fase de compresión?", thread_id="sesion-1")
# El modelo sabe que habla de 4T porque lo recuerda
```

---

## Parámetros Ajustables

**En `agente_rag_langgraph_completo.py`:**

```python
# Número de documentos recuperados
k=3  # Aumentar para más contexto, disminuir para precisión

# Temperatura del LLM
temperature=0.0  # 0.0 = determinista, 1.0 = creativo

# Modelos fallover (en orden de preferencia)
MODELOS_GEMINI = [
    "gemini-2.5-flash",   # Intenta primero
    "gemini-2.0-flash",   # Si falla, intenta este
    "gemini-1.5-pro"      # Si falla, intenta este
]
```

---

## Criterios de Evaluación

| Requisito | Cumplimiento | Detalles |
|-----------|---|---|
| Base de conocimiento | ✅ | 4 PDFs, 158 páginas, 632 párrafos |
| Embeddings | ✅ | HuggingFace multilingual (open-source) |
| RAG funcional | ✅ | Retrieval + Generación con Gemini |
| System prompt justificado | ✅ | Documentado en sección 5 |
| Memoria conversacional | ✅ | LangGraph + thread_id |
| Interacción en notebook | ✅ | Jupyter con función chat_rag() |
| 5 ejemplos | ✅ | Documentados arriba |
| Interfaz web | ✅ | Streamlit funcional |
| Failover automático | ✅ | 3 modelos con fallback por cuota |

---

## Troubleshooting

**Error: GEMINI_API_KEY_001 no encontrada**
→ Crear `.env` con la clave. Ejemplo: `GEMINI_API_KEY_001=sk-...`

**Error: ChromaDB no encontrado**
→ Verificar que `chroma_db_motores/` existe en la carpeta del proyecto

**Respuestas muy lentas**
→ Normal en primera ejecución (descarga modelos). Siguiente: <1 segundo

**Respuestas genéricas**
→ Aumentar `k` en `nodo_retrieval` de 3 a 5

**Cuota excedida en Gemini 2.5-flash**
→ Sistema intenta automáticamente 2.0-flash, luego 1.5-pro

---

## Estructura del Proyecto

```
Proyecto_Modulo_IAGen/
├── .env                              # API Key (NO subir a repo)
├── agente_rag_langgraph_completo.py  # Lógica RAG + LangGraph
├── app.py                            # Interfaz Streamlit
├── README.md                         # Este archivo
├── Agente_RAG_Explicado_Simple.ipynb # Notebook con ejemplos
├── chroma_db_motores/                # BD vectorial indexada
│   ├── data/
│   └── index/
└── pdf_conocimiento/                 # PDFs originales (referencia)
    ├── 7044599-Funcionamiento...pdf
    ├── 585888634-Motores.pdf
    ├── curs_2T_08.pdf
    └── Motores de combustión interna.pdf
```

---

**Última actualización:** Mayo 2025  
**Módulo:** IA Generativa  
**Proyecto Final:** Agente RAG con LangGraph + Gemini
