# Guía de Patrones para Proyectos de IA Generativa

## 📋 Resumen Ejecutivo

Esta guía presenta **6 patrones fundamentales** para construir proyectos de IA Generativa, organizados en un flujo de decisión que te ayuda a elegir el patrón correcto según tu problema específico.

> **Nota clave:** Estos 6 patrones son los principales, pero pueden combinarse entre sí para crear soluciones más complejas. No son excluyentes — son bloques de construcción.

---

## 🌳 Diagrama de Decisión: ¿Qué Patrón Necesito?

```
┌─────────────────────────────────────────────────────────────────────────┐
│                    ¿QUÉ TIPO DE PROBLEMA TIENES?                        │
└─────────────────────────────────────────────────────────────────────────┘
                                    │
                    ┌───────────────┼───────────────┐
                    ▼               ▼               ▼
            ┌───────────┐   ┌───────────┐   ┌───────────┐
            │  DATOS    │   │   TEXTO   │   │  TEXTO +  │
            │ TABULARES │   │   LIBRE   │   │  TABULAR  │
            │  (números)│   │ (emails,  │   │  (mixto)  │
            │           │   │ reseñas)  │   │           │
            └─────┬─────┘   └─────┬─────┘   └─────┬─────┘
                  │               │               │
                  ▼               ▼               ▼
        ┌─────────────────┐ ┌─────────────────┐ ┌─────────────────┐
        │ ¿Necesitas      │ │ ¿Quieres extraer│ │ ¿Tienes texto   │
        │ explicar        │ │ datos de texto  │ │ que enriquece   │
        │ predicciones ML?│ │ para análisis?  │ │ tus datos       │
        │                 │ │                 │ │ tabulares?      │
        └────────┬────────┘ └────────┬────────┘ └────────┬────────┘
                 │                   │                   │
            SÍ ──┘              SÍ ──┘              SÍ ──┘
                 │                   │                   │
                 ▼                   ▼                   ▼
        ┌─────────────────┐ ┌─────────────────┐ ┌─────────────────┐
        │   PATRÓN A      │ │   PATRÓN B      │ │   PATRÓN C      │
        │ ML + Explicación│ │ Extracción      │ │ Feature Eng.    │
        │                 │ │ Estructurada    │ │ Semántico       │
        │ El modelo       │ │                 │ │                 │
        │ predice, el     │ │ Texto → JSON    │ │ Texto →         │
        │ LLM explica     │ │ → ML downstream │ │ features → ML   │
        └─────────────────┘ └─────────────────┘ └─────────────────┘

┌─────────────────────────────────────────────────────────────────────────┐
│                    OTROS ESCENARIOS ESPECÍFICOS                         │
└─────────────────────────────────────────────────────────────────────────┘
                                    │
        ┌───────────────────────────┼───────────────────────────┐
        ▼                           ▼                           ▼
┌───────────────┐         ┌─────────────────┐         ┌─────────────────┐
│ ¿Necesitas    │         │ ¿Necesitas      │         │ ¿Necesitas      │
│ una interfaz  │         │ moderar mucho   │         │ evaluar calidad │
│ conversacional│         │ contenido con   │         │ de respuestas   │
│ sobre datos?  │         │ presupuesto     │         │ LLM sin         │
│               │         │ limitado?       │         │ anotadores?     │
└───────┬───────┘         └────────┬────────┘         └────────┬────────┘
    SÍ │                      SÍ │                         SÍ │
        ▼                           ▼                           ▼
┌─────────────────┐         ┌─────────────────┐         ┌─────────────────┐
│   PATRÓN D      │         │   PATRÓN E      │         │   PATRÓN F      │
│ Agente con      │         │ Moderación      │         │ LLM-as-Judge    │
│ Herramientas    │         │ en Cascada      │         │                 │
│                 │         │                 │         │                 │
│ LLM que decide  │         │ Reglas → ML →   │         │ Un LLM evalúa   │
│ qué herramienta │         │ LLM (ahorro     │         │ la calidad de   │
│ usar para cada  │         │ 85% coste)      │         │ otro LLM        │
│ pregunta        │         │                 │         │                 │
└─────────────────┘         └─────────────────┘         └─────────────────┘
```

---

## 📖 Los 6 Patrones en Detalle

### 🔷 PATRÓN A: Clasificación + Explicación
**"El modelo predice, el LLM explica"**

#### ¿Cuándo usarlo?
- Tienes un modelo de ML que hace predicciones (churn, fraude, aprobación de crédito)
- Los usuarios necesitan entender **por qué** se tomó esa decisión
- El público objetivo no es técnico (negocio, clientes, reguladores)

#### Flujo del proceso
```
Datos del cliente (features numéricas/categóricas)
         ↓
  Modelo ML entrenado
         ↓
  Predicción (sí/no) + Probabilidad (0-100%)
         ↓
  Prompt con: datos + predicción + probabilidad
         ↓
  LLM genera explicación en lenguaje natural
         ↓
  Respuesta: "Su solicitud fue rechazada porque..."
```

#### Ejemplo práctico
Un banco usa ML para decidir si aprueba préstamos. El modelo dice "rechazado", pero el cliente quiere saber por qué. El LLM explica: *"Su solicitud fue rechazada porque su ratio deuda/ingresos (45%) supera el límite del 40% y tiene 3 pagos atrasados en el último año."*

#### Componentes necesarios
- Modelo ML entrenado (Random Forest, XGBoost, etc.)
- Prompt con contexto del negocio
- LLM con temperatura baja (0.1-0.3) para consistencia

---

### 🔷 PATRÓN B: Extracción Estructurada
**"Del texto caótico a datos limpios"**

#### ¿Cuándo usarlo?
- Recibes texto no estructurado (emails, tickets de soporte, formularios libres)
- Necesitas convertir ese texto en **datos tabulares** para análisis
- Quieres automatizar el procesamiento de documentos

#### Flujo del proceso
```
Texto libre (email, ticket, formulario)
         ↓
  Prompt de extracción con formato JSON especificado
         ↓
  LLM identifica y extrae campos específicos
         ↓
  JSON estructurado
         ↓
  DataFrame / Base de datos
         ↓
  Análisis ML, dashboards, respuestas automáticas
```

#### Ejemplo práctico
Una empresa recibe emails de soporte como: *"Hola, soy María González, llevo 3 días sin acceder a mi cuenta premium. Mi email es maria@email.com y mi teléfono 555-1234. Estoy muy frustrada."* El LLM extrae: `{"nombre": "María González", "problema": "acceso cuenta", "plan": "premium", "urgencia": "alta", "sentimiento": "frustrado"}`.

#### Componentes necesarios
- Prompt con campos a extraer y formato JSON
- Parser JSON robusto (manejo de errores)
- Temperatura = 0 (máxima determinación)

---

### 🔷 PATRÓN C: Feature Engineering Semántico
**"El LLM como generador de features para ML"**

#### ¿Cuándo usarlo?
- Tienes datos mixtos: columnas numéricas + columnas de texto
- El ML clásico ignora el texto porque no sabe procesarlo
- Quieres que el LLM genere **features numéricas con significado de negocio**

#### Flujo del proceso
```
Features numéricas (precio, días, cantidad)
         ↓
         ├──→ Modelo ML baseline (sin usar texto)
         │
Texto (reseña, comentario, descripción)
         ↓
  LLM genera features semánticas:
  - score_sentimiento: -1 a +1
  - intencion_recompra: 0 a 1
  - menciona_devolucion: sí/no
  - nivel_frustracion: 0 a 1
         ↓
  Concatenar: features numéricas + features semánticas
         ↓
  Modelo ML enriquecido (mejor performance)
```

#### Ejemplo práctico
Un e-commerce predice si un cliente volverá a comprar. Además del precio y días de envío, el LLM analiza la reseña y genera: `score_sentimiento=0.8`, `intencion_recompra=0.9`, `menciona_calidad=True`. El modelo ML usa estos números para mejorar sus predicciones.

#### Componentes necesarios
- Dataset con columna de texto
- Prompt que especifica qué features generar
- Modelo ML que combine ambos tipos de features

---

### 🔷 PATRÓN D: Agente con Herramientas
**"LLM que orquesta funciones ML como herramientas"**

#### ¿Cuándo usarlo?
- Quieres una **interfaz conversacional** sobre tus datos
- Los usuarios hacen preguntas en lenguaje natural
- Las preguntas requieren diferentes análisis (estadísticas, clustering, predicción)

#### Flujo del proceso
```
Pregunta del usuario en lenguaje natural
         ↓
  Agente LLM analiza la pregunta
         ↓
  Decide qué herramienta(s) usar:
  - obtener_estadisticas()
  - comparar_regiones()
  - segmentar_clientes()
  - predecir_ventas()
         ↓
  Ejecuta herramienta(s) y recibe resultados
         ↓
  Sintetiza respuesta en lenguaje natural
         ↓
  "La región Norte tiene 23% más ventas que el Sur..."
```

#### Ejemplo práctico
Un director de ventas pregunta: *"¿Qué región está performando mejor y por qué?"* El agente llama a `comparar_regiones()`, ve que Norte lidera, luego llama a `segmentar_clientes()` para entender el perfil de esos clientes, y responde: *"La región Norte lidera con $2.3M en ventas, impulsada principalmente por clientes enterprise del segmento tecnológico."*

#### Componentes necesarios
- Funciones Python con decorador `@tool`
- System prompt que define la personalidad del agente
- AgentExecutor para gestionar el loop de decisiones

---

### 🔷 PATRÓN E: Moderación en Cascada
**"Reglas → ML → LLM: el estándar de producción"**

#### ¿Cuándo usarlo?
- Necesitas procesar **grandes volúmenes** de contenido (millones de items/día)
- El presupuesto es limitado (no puedes llamar al LLM para todo)
- Quieres **optimizar coste** sin sacrificar calidad

#### Flujo del proceso
```
100% de los comentarios/tickets/emails
         ↓
┌─────────────────────────────────────────────────────────────┐
│ CAPA 1: REGLAS (gratis, instantáneo)                        │
│ Busca palabras prohibidas explícitas                        │
│ • Si encuentra → rechaza inmediatamente                     │
│ • Si no encuentra → pasa a Capa 2                           │
└─────────────────────────────────────────────────────────────┘
         ~40% resueltos aquí
         ↓ 60% restantes
┌─────────────────────────────────────────────────────────────┐
│ CAPA 2: ML (barato, ~1ms)                                   │
│ TF-IDF + Regresión Logística                                │
│ • Si confianza > 85% → decide (aprueba/rechaza)             │
│ • Si confianza < 85% → pasa a Capa 3                        │
└─────────────────────────────────────────────────────────────┘
         ~45% resueltos aquí
         ↓ 15% restantes (casos difíciles)
┌─────────────────────────────────────────────────────────────┐
│ CAPA 3: LLM (caro, ~2s)                                     │
│ Análisis contextual profundo                                │
│ • Entiende ironía, contexto cultural, matices               │
│ • Siempre decide → resultado final                          │
└─────────────────────────────────────────────────────────────┘
         ~15% resueltos aquí

RESULTADO: Ahorro del ~85% en costes de API
```

#### Ejemplo práctico
Una red social recibe 1 millón de comentarios/día. Las reglas capturan insultos obvios (40%). El ML clasifica los casos claros restantes (45%). Solo el 15% más ambiguo llega al LLM, reduciendo el coste de $1,000/día a $150/día.

#### Componentes necesarios
- Lista de palabras/frases prohibidas (Capa 1)
- Modelo TF-IDF + Logistic Regression entrenado (Capa 2)
- Prompt de moderación con criterios claros (Capa 3)
- Sistema de métricas para tracking por capa

---

### 🔷 PATRÓN F: LLM-as-Judge
**"Cómo medir calidad cuando no hay respuesta única correcta"**

#### ¿Cuándo usarlo?
- La salida del sistema es **texto libre** (no hay un único "correcto")
- Necesitas comparar diferentes prompts, modelos o configuraciones
- Contratar anotadores humanos es caro o lento
- Quieres evaluar de forma **automática y escalable**

#### Flujo del proceso
```
Pregunta del benchmark
         ↓
┌─────────────────────────────────────────┐
│  SISTEMA A (prompt básico)              │
│  SISTEMA B (prompt optimizado)          │
│  SISTEMA C (modelo diferente)           │
└─────────────────────────────────────────┘
         ↓
  Generan respuestas A, B, C
         ↓
  LLM-JUEZ evalúa cada respuesta vs referencia
         ↓
  Puntuaciones multidimensionales:
  - Precisión técnica (1-10)
  - Claridad (1-10)
  - Completitud (1-10)
         ↓
  Comparación: ¿A > B > C?
```

#### Ejemplo práctico
Una empresa educativa genera explicaciones de conceptos de ML. Comparan dos prompts: el básico dice *"Responde esta pregunta"*; el optimizado dice *"Eres un profesor experto. Responde con un ejemplo en máximo 4 oraciones."* El LLM-Juez puntuará ambos y confirmará que el optimizado obtiene mejor puntuación en claridad y completitud.

#### Componentes necesarios
- Benchmark con preguntas y respuestas de referencia
- Prompt del juez con criterios de evaluación
- Dos instancias del LLM: generador (temp 0.7) y juez (temp 0.0)

---

## 🔄 Combinaciones de Patrones

Los patrones no son excluyentes. En proyectos complejos, se combinan:

### Combinación A + B: Extracción + Explicación
```
Email de cliente → Extracción (Patrón B) → Datos estructurados
                                         ↓
                                   Modelo ML predice
                                         ↓
                                   LLM explica (Patrón A)
```

### Combinación C + E: Features + Cascada
```
Texto → Capa 1: Reglas simples
          ↓ no aplica
        Capa 2: ML con features semánticas (Patrón C)
          ↓ ambiguo
        Capa 3: LLM para casos difíciles (Patrón E)
```

### Combinación D + F: Agente + Evaluación
```
Agente responde preguntas (Patrón D)
         ↓
  LLM-Juez evalúa calidad (Patrón F)
         ↓
  Feedback para mejorar el agente
```

---

## 📊 Tabla Comparativa Rápida

| Patrón | Entrada | Salida | Coste | Latencia | Complejidad |
|--------|---------|--------|-------|----------|-------------|
| **A** ML+Explicación | Datos tabulares | Predicción + texto | Medio | Media | Baja |
| **B** Extracción | Texto libre | JSON estructurado | Medio | Media | Media |
| **C** Feature Eng. | Texto + datos | Features numéricas | Medio-Alto | Media | Media |
| **D** Agente | Pregunta natural | Respuesta natural | Alto | Alta | Alta |
| **E** Cascada | Texto | Decisión sí/no | Bajo | Baja-Media | Media |
| **F** LLM-Judge | Respuestas LLM | Puntuación 1-10 | Medio | Media | Baja |

---

## 🎯 Checklist para Elegir tu Patrón

- [ ] **¿Tienes un modelo ML y necesitas explicar sus predicciones?** → Patrón A
- [ ] **¿Tienes texto no estructurado que necesitas convertir a datos?** → Patrón B
- [ ] **¿Tienes texto que podría mejorar un modelo ML tabular?** → Patrón C
- [ ] **¿Quieres una interfaz conversacional sobre datos?** → Patrón D
- [ ] **¿Necesitas procesar mucho contenido con presupuesto limitado?** → Patrón E
- [ ] **¿Necesitas evaluar calidad de respuestas automáticamente?** → Patrón F

---

## 📚 Referencias

Esta guía está basada en los notebooks del módulo de IA Generativa:
- `001_Proceso_IA_Generativa_Claude.ipynb` - Guía metodológica general
- `T4.1` a `T4.6` - Implementaciones prácticas de cada patrón

**Principio fundamental:** *"No hay una estrategia única que funcione mejor en todos los casos; la elección depende de las particularidades del caso de uso. Muchas veces, las técnicas pueden combinarse para obtener mejores resultados."*
