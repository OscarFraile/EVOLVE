import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.patches import FancyBboxPatch, Polygon
import matplotlib.dates as mdates
import numpy as np
from datetime import datetime, timedelta

TODAY = datetime(2026, 3, 16)
OUTPUT = r"C:\Users\Oscar\OneDrive - FM4\Escritorio\EVOLVE\Data Science\EVOLVE\Julio_Valero_ProyectoFinal\Proyecto_Final_Evolve\09_Otros\gantt_airbnb.png"

# ── PALETA POR BLOQUE (header_dark, task_light, progress_mid) ──────────────
PALETA = {
    "B1":  ("#0D47A1", "#90CAF9", "#1565C0"),
    "B2":  ("#4A148C", "#CE93D8", "#6A1B9A"),
    "B3":  ("#006064", "#80DEEA", "#00838F"),
    "B4":  ("#BF360C", "#FFAB91", "#D84315"),
    "B5":  ("#1B5E20", "#A5D6A7", "#2E7D32"),
    "B6":  ("#1A237E", "#9FA8DA", "#283593"),
    "B7":  ("#880E4F", "#F48FB1", "#AD1457"),
    "B8":  ("#37474F", "#90A4AE", "#455A64"),
    "B9":  ("#004D40", "#80CBC4", "#00695C"),
    "B10": ("#01579B", "#81D4FA", "#0277BD"),
    "B11": ("#4A148C", "#B39DDB", "#512DA8"),
    "B12": ("#33691E", "#C5E1A5", "#558B2F"),
    "B13": ("#006064", "#80DEEA", "#00838F"),
    "B14": ("#E65100", "#FFCC80", "#EF6C00"),
    "B15": ("#880E4F", "#F8BBD0", "#C2185B"),
    "M":   ("#B71C1C", "#EF9A9A", "#C62828"),
}

def d(s): return datetime.strptime(s, "%Y-%m-%d")
def end(s, dur): return d(s) + timedelta(days=dur - 1)

# ── DATOS (id, nombre, tipo, start, end_date, complete%, bloque_key) ────────
# tipo: 'milestone' | 'block' | 'task' | 'blocker'
ROWS = [
    # ── BLOQUE 1 ────────────────────────────────────────────────────────────
    ("B1",    "B1 · Definición y planificación del proyecto",         "block",     d("2025-11-01"), end("2025-11-01",20), 100, "B1"),
    ("T101",  "Definición del objetivo de negocio",                   "task",      d("2025-11-01"), end("2025-11-01", 4), 100, "B1"),
    ("T102",  "Identificación de palancas de rentabilidad",           "task",      d("2025-11-05"), end("2025-11-05", 3), 100, "B1"),
    ("T103",  "Definición de KPIs por palanca",                       "task",      d("2025-11-08"), end("2025-11-08", 3), 100, "B1"),
    ("T104",  "Identificación de entidades y fuentes de datos",       "task",      d("2025-11-11"), end("2025-11-11", 4), 100, "B1"),
    ("T105",  "Formulación de preguntas semilla por eje de análisis", "task",      d("2025-11-15"), end("2025-11-15", 6), 100, "B1"),
    ("M901",  "Hito: Primeras ideas de proyecto fin de máster",       "milestone", d("2025-11-21"), d("2025-11-21"),      100, "M"),
    # ── BLOQUE 2 ────────────────────────────────────────────────────────────
    ("B2",    "B2 · Configuración del entorno y setup del proyecto",  "block",     d("2025-11-21"), end("2025-11-21",21), 100, "B2"),
    ("T201",  "Creación del entorno Conda con versiones específicas", "task",      d("2025-11-21"), end("2025-11-21", 9), 100, "B2"),
    ("T202",  "Importación y verificación de librerías",              "task",      d("2025-11-30"), end("2025-11-30", 5), 100, "B2"),
    ("T203",  "Creación de estructura de directorios",                "task",      d("2025-12-05"), end("2025-12-05", 7), 100, "B2"),
    ("M902",  "Hito: Definición del MVP",                            "milestone", d("2025-12-12"), d("2025-12-12"),      100, "M"),
    # ── BLOQUE 3 ────────────────────────────────────────────────────────────
    ("B3",    "B3 · Adquisición y exploración inicial de datos",      "block",     d("2025-12-12"), end("2025-12-12",15), 100, "B3"),
    ("T301",  "Carga y exploración de ficheros AirBnB disponibles",   "task",      d("2025-12-12"), end("2025-12-12", 5), 100, "B3"),
    ("T302",  "Decisión sobre qué tablas usar y descartar",           "task",      d("2025-12-17"), end("2025-12-17", 3), 100, "B3"),
    ("T303",  "Obtención datos precio m2 (web scraping Idealista)",   "task",      d("2025-12-20"), end("2025-12-20", 4), 100, "B3"),
    ("T304",  "Creación base de datos SQLite y carga de tablas",      "task",      d("2025-12-24"), end("2025-12-24", 3), 100, "B3"),
    # ── BLOQUE 4 ────────────────────────────────────────────────────────────
    ("B4",    "B4 · Creación del datamart analítico",                 "block",     d("2025-12-27"), end("2025-12-27",24), 100, "B4"),
    ("T401",  "Eliminación de variables irrelevantes o redundantes",  "task",      d("2025-12-27"), end("2025-12-27", 2), 100, "B4"),
    ("T402",  "Normalización de nombres de columnas",                 "task",      d("2025-12-29"), end("2025-12-29", 1), 100, "B4"),
    ("T403",  "Imputación nulos price (media por barrio y aforo)",    "task",      d("2025-12-30"), end("2025-12-30", 2), 100, "B4"),
    ("T404",  "Imputación nulos beds (regla por accommodates)",       "task",      d("2026-01-01"), end("2026-01-01", 2), 100, "B4"),
    ("T405",  "Imputación nulos bedrooms (regla por beds)",           "task",      d("2026-01-03"), end("2026-01-03", 2), 100, "B4"),
    ("T406",  "Tratamiento bathrooms y bathrooms_text",               "task",      d("2026-01-05"), end("2026-01-05", 2), 100, "B4"),
    ("T407",  "Imputación variables de reviews (scores y fechas)",    "task",      d("2026-01-07"), end("2026-01-07", 2), 100, "B4"),
    ("T408",  "Tratamiento host_response_time y acceptance_rate",     "task",      d("2026-01-09"), end("2026-01-09", 2), 100, "B4"),
    ("T409",  "Binarización de license y has_availability",           "task",      d("2026-01-11"), end("2026-01-11", 1), 100, "B4"),
    ("T410",  "Imputación host_is_superhost por condiciones negocio", "task",      d("2026-01-12"), end("2026-01-12", 2), 100, "B4"),
    ("T411",  "Eliminación registros con demasiados nulos (thresh)",  "task",      d("2026-01-14"), end("2026-01-14", 1), 100, "B4"),
    ("T412",  "Análisis y eliminación de duplicados",                 "task",      d("2026-01-15"), end("2026-01-15", 1), 100, "B4"),
    ("T413",  "Conversión de variables de fecha a formato uniforme",  "task",      d("2026-01-16"), end("2026-01-16", 1), 100, "B4"),
    ("T414",  "Detección y tratamiento atípicos (price, min/max)",    "task",      d("2026-01-17"), end("2026-01-17", 2), 100, "B4"),
    ("T415",  "Eliminación de hoteles y hostels del dataset",         "task",      d("2026-01-19"), end("2026-01-19", 1), 100, "B4"),
    ("T416",  "Limpieza precio m2 (unidades y separadores de miles)", "task",      d("2026-01-17"), end("2026-01-17", 2), 100, "B4"),
    ("T417",  "Join listings, listings_det y precio_m2 por distrito", "task",      d("2026-01-20"), end("2026-01-20", 2), 100, "B4"),
    ("T418",  "Resolución de inconsistencias en nombres de distritos","task",      d("2026-01-18"), end("2026-01-18", 2), 100, "B4"),
    ("T419",  "Guardado del datamart en base de datos",               "task",      d("2026-01-20"), end("2026-01-20", 1), 100, "B4"),
    ("M903",  "Hito: Diseño del flujo de la solución y MVP",          "milestone", d("2026-01-13"), d("2026-01-13"),      100, "M"),
    # ── BLOQUE 5 ────────────────────────────────────────────────────────────
    ("B5",    "B5 · Preparación de variables para análisis",          "block",     d("2026-01-21"), end("2026-01-21",13), 100, "B5"),
    ("T501",  "Creación KPI precio_total (lógica por tipo alquiler)", "task",      d("2026-01-21"), end("2026-01-21", 3), 100, "B5"),
    ("T502",  "Creación KPI ocupación desde availability_365",        "task",      d("2026-01-21"), end("2026-01-21", 2), 100, "B5"),
    ("T503",  "Discretización manual bedrooms (Estudio, 1, 2, 3, 4+)","task",     d("2026-01-24"), end("2026-01-24", 2), 100, "B5"),
    ("T504",  "Discretización automática percentiles",                "task",      d("2026-01-24"), end("2026-01-24", 2), 100, "B5"),
    ("T505",  "Estimación de m2 por número de dormitorios",           "task",      d("2026-01-26"), end("2026-01-26", 2), 100, "B5"),
    ("T506",  "Cálculo precio_compra estimado (m2 × precio_m2 × dto)","task",     d("2026-01-28"), end("2026-01-28", 2), 100, "B5"),
    ("T507",  "Distancia geoespacial a Puerta del Sol (Haversine)",   "task",      d("2026-01-28"), end("2026-01-28", 2), 100, "B5"),
    ("T508",  "Creación variable target pisos_rentables (umbral 10a)","task",      d("2026-01-30"), end("2026-01-30", 3), 100, "B5"),
    ("T509",  "Guardado del dataset preparado en base de datos",      "task",      d("2026-02-02"), end("2026-02-02", 1), 100, "B5"),
    # ── BLOQUE 6 ────────────────────────────────────────────────────────────
    ("B6",    "B6 · Análisis e Insights",                             "block",     d("2026-02-03"), end("2026-02-03",17), 100, "B6"),
    ("T601",  "Estadísticos descriptivos y rango de precios",         "task",      d("2026-02-03"), end("2026-02-03", 2), 100, "B6"),
    ("T602",  "Ranking de distritos y barrios por precio mediano",    "task",      d("2026-02-05"), end("2026-02-05", 2), 100, "B6"),
    ("T603",  "Análisis caso atípico San Blas (eventos deportivos)",  "task",      d("2026-02-07"), end("2026-02-07", 2), 100, "B6"),
    ("T604",  "Scatter precio_compra vs precio_total por zona",       "task",      d("2026-02-09"), end("2026-02-09", 2), 100, "B6"),
    ("T605",  "Minicubo precio: bedrooms, beds, accommodates",        "task",      d("2026-02-09"), end("2026-02-09", 3), 100, "B6"),
    ("T606",  "Análisis relación número de camas vs precio",          "task",      d("2026-02-12"), end("2026-02-12", 2), 100, "B6"),
    ("T607",  "Análisis distancia puntos de interés vs precio",       "task",      d("2026-02-12"), end("2026-02-12", 2), 100, "B6"),
    ("T608",  "Análisis ocupación: estadísticos y ranking distritos", "task",      d("2026-02-14"), end("2026-02-14", 2), 100, "B6"),
    ("T609",  "Minicubo ocupación: bedrooms, beds, accommodates",     "task",      d("2026-02-14"), end("2026-02-14", 2), 100, "B6"),
    ("T610",  "Visualización geográfica en mapa interactivo (Folium)","task",      d("2026-02-16"), end("2026-02-16", 2), 100, "B6"),
    ("T611",  "Síntesis de 8 insights de negocio accionables",        "task",      d("2026-02-18"), end("2026-02-18", 2), 100, "B6"),
    # ── BLOQUE 7 ────────────────────────────────────────────────────────────
    ("B7",    "B7 · Comunicación de resultados",                      "block",     d("2026-02-20"), end("2026-02-20", 9), 100, "B7"),
    ("T701",  "Redacción del contexto y objetivos del análisis",      "task",      d("2026-02-20"), end("2026-02-20", 2), 100, "B7"),
    ("T702",  "Elaboración de conclusiones ejecutivas",               "task",      d("2026-02-22"), end("2026-02-22", 2), 100, "B7"),
    ("T703",  "Construcción de 5 exhibits gráficos de soporte",       "task",      d("2026-02-24"), end("2026-02-24", 3), 100, "B7"),
    ("T704",  "Recomendaciones para equipo de valoraciones",          "task",      d("2026-02-27"), end("2026-02-27", 2), 100, "B7"),
    # ── BLOQUE 8 ────────────────────────────────────────────────────────────
    ("B8",    "B8 · Exploración, calidad de datos y EDA para ML",     "block",     d("2026-03-01"), end("2026-03-01",15), 100, "B8"),
    ("T801",  "Carga dataset y eliminación de columnas de la target", "task",      d("2026-03-01"), end("2026-03-01", 1), 100, "B8"),
    ("T802",  "[BLOQ] Separación y guardado dataset validación 30%",  "blocker",   d("2026-03-02"), end("2026-03-02", 1), 100, "B8"),
    ("T803",  "[BLOQ] Separación y guardado dataset de trabajo 70%",  "blocker",   d("2026-03-02"), end("2026-03-02", 1), 100, "B8"),
    ("T804",  "Exploración inicial: dimensiones, tipos y únicos",     "task",      d("2026-03-03"), end("2026-03-03", 2), 100, "B8"),
    ("T805",  "Separación en datasets numérico y categórico",         "task",      d("2026-03-05"), end("2026-03-05", 1), 100, "B8"),
    ("T806",  "Identificación y gestión de nulos en categóricas",     "task",      d("2026-03-06"), end("2026-03-06", 2), 100, "B8"),
    ("T807",  "Agrupación de categorías poco frecuentes en OTROS",    "task",      d("2026-03-08"), end("2026-03-08", 2), 100, "B8"),
    ("T808",  "Normalización de valores inconsistentes",              "task",      d("2026-03-10"), end("2026-03-10", 1), 100, "B8"),
    ("T809",  "Análisis estadístico de variables numéricas",          "task",      d("2026-03-11"), end("2026-03-11", 2), 100, "B8"),
    ("T810",  "EDA categóricas: frecuencias y gráficos de barras",    "task",      d("2026-03-11"), end("2026-03-11", 2), 100, "B8"),
    ("T811",  "EDA numéricas: estadísticos ampliados y distribución", "task",      d("2026-03-13"), end("2026-03-13", 2), 100, "B8"),
    ("T812",  "Guardado de datasets tras calidad de datos y EDA",     "task",      d("2026-03-15"), end("2026-03-15", 1), 100, "B8"),
    # ── BLOQUE 9 ────────────────────────────────────────────────────────────
    ("B9",    "B9 · Transformación de datos",                         "block",     d("2026-03-16"), end("2026-03-16",16), 0,   "B9"),
    ("T9001", "Separación de la variable target",                     "task",      d("2026-03-16"), end("2026-03-16", 1), 0,   "B9"),
    ("T9002", "One Hot Encoding (variables nominales sin orden)",      "task",      d("2026-03-17"), end("2026-03-17", 2), 0,   "B9"),
    ("T9003", "Ordinal Encoding (variables con orden natural)",        "task",      d("2026-03-17"), end("2026-03-17", 2), 0,   "B9"),
    ("T9004", "Target Encoding (variables con alta cardinalidad)",     "task",      d("2026-03-19"), end("2026-03-19", 2), 0,   "B9"),
    ("T9005", "Tratamiento variables de fecha (antigüedad, diffs)",   "task",      d("2026-03-19"), end("2026-03-19", 2), 0,   "B9"),
    ("T9006", "Tratamiento texto amenities (tokenización, binarias)", "task",      d("2026-03-21"), end("2026-03-21", 3), 0,   "B9"),
    ("T9007", "Transformación numéricas: discretización y normaliz.", "task",      d("2026-03-21"), end("2026-03-21", 3), 0,   "B9"),
    ("T9008", "Reescalado (MinMax / Standard / Robust según algos)",  "task",      d("2026-03-24"), end("2026-03-24", 3), 0,   "B9"),
    ("T9009", "Unificación en tablón analítico y eliminación nulos",  "task",      d("2026-03-27"), end("2026-03-27", 3), 0,   "B9"),
    ("T9010", "Guardado del tablón analítico",                        "task",      d("2026-03-30"), end("2026-03-30", 2), 0,   "B9"),
    ("M904",  "Hito: Plan de desarrollo de producto",                 "milestone", d("2026-03-24"), d("2026-03-24"),      0,   "M"),
    # ── BLOQUE 10 ───────────────────────────────────────────────────────────
    ("B10",   "B10 · Preselección de variables",                      "block",     d("2026-04-01"), end("2026-04-01",11), 0,   "B10"),
    ("T1001", "[BLOQ] Separación de predictoras y target",            "blocker",   d("2026-04-01"), end("2026-04-01", 1), 0,   "B10"),
    ("T1002", "Mutual Information",                                   "task",      d("2026-04-02"), end("2026-04-02", 2), 0,   "B10"),
    ("T1003", "Recursive Feature Elimination (RFE)",                  "task",      d("2026-04-02"), end("2026-04-02", 2), 0,   "B10"),
    ("T1004", "Permutation Importance",                               "task",      d("2026-04-02"), end("2026-04-02", 2), 0,   "B10"),
    ("T1005", "Combinación de métodos mediante Super Ranking",         "task",      d("2026-04-04"), end("2026-04-04", 2), 0,   "B10"),
    ("T1006", "Análisis de correlaciones entre variables",             "task",      d("2026-04-06"), end("2026-04-06", 2), 0,   "B10"),
    ("T1007", "Eliminación de variables con exceso de correlación",   "task",      d("2026-04-08"), end("2026-04-08", 2), 0,   "B10"),
    ("T1008", "Selección método final y guardado dataset preselec.",   "task",      d("2026-04-10"), end("2026-04-10", 2), 0,   "B10"),
    # ── BLOQUE 11 ───────────────────────────────────────────────────────────
    ("B11",   "B11 · Balanceo",                                       "block",     d("2026-04-12"), end("2026-04-12", 8), 0,   "B11"),
    ("T1101", "Análisis de la distribución de clases de la target",   "task",      d("2026-04-12"), end("2026-04-12", 1), 0,   "B11"),
    ("T1102", "Evaluación sin balanceo como línea base",              "task",      d("2026-04-13"), end("2026-04-13", 1), 0,   "B11"),
    ("T1103", "Undersampling aleatorio (RandomUnderSampler)",         "task",      d("2026-04-14"), end("2026-04-14", 2), 0,   "B11"),
    ("T1104", "Oversampling aleatorio (RandomOverSampler)",           "task",      d("2026-04-14"), end("2026-04-14", 2), 0,   "B11"),
    ("T1105", "SMOTE-Tomek (técnica combinada)",                      "task",      d("2026-04-14"), end("2026-04-14", 2), 0,   "B11"),
    ("T1106", "Penalización por peso en el modelo (class_weight)",    "task",      d("2026-04-14"), end("2026-04-14", 2), 0,   "B11"),
    ("T1107", "Comparación de resultados y selección método final",   "task",      d("2026-04-16"), end("2026-04-16", 2), 0,   "B11"),
    ("T1108", "Guardado del dataset final balanceado",                "task",      d("2026-04-18"), end("2026-04-18", 2), 0,   "B11"),
    # ── BLOQUE 12 ───────────────────────────────────────────────────────────
    ("B12",   "B12 · Modelización",                                   "block",     d("2026-04-20"), end("2026-04-20",15), 0,   "B12"),
    ("T1201", "[BLOQ] Separación train y validación interna",         "blocker",   d("2026-04-20"), end("2026-04-20", 1), 0,   "B12"),
    ("T1202", "Regresión Logística (línea base)",                     "task",      d("2026-04-21"), end("2026-04-21", 2), 0,   "B12"),
    ("T1203", "Random Forest",                                        "task",      d("2026-04-21"), end("2026-04-21", 2), 0,   "B12"),
    ("T1204", "XGBoost y Gradient Boosting",                          "task",      d("2026-04-21"), end("2026-04-21", 2), 0,   "B12"),
    ("T1205", "Hist Gradient Boosting",                               "task",      d("2026-04-21"), end("2026-04-21", 2), 0,   "B12"),
    ("T1206", "Optimización hiperparámetros (Grid/Random Search+CV)", "task",      d("2026-04-23"), end("2026-04-23", 4), 0,   "B12"),
    ("T1207", "Evaluación: ROC AUC, Precision, Recall, F1, Matriz",  "task",      d("2026-04-27"), end("2026-04-27", 2), 0,   "B12"),
    ("T1208", "Reporting: Gain Chart, Lift Chart, Curva ROC",         "task",      d("2026-04-29"), end("2026-04-29", 2), 0,   "B12"),
    ("T1209", "Selección del modelo final",                           "task",      d("2026-05-01"), end("2026-05-01", 4), 0,   "B12"),
    # ── BLOQUE 13 ───────────────────────────────────────────────────────────
    ("B13",   "B13 · Preparación del código de producción",           "block",     d("2026-05-05"), end("2026-05-05",15), 0,   "B13"),
    ("T1301", "Encapsulación de transformaciones en FunctionTransf.", "task",      d("2026-05-05"), end("2026-05-05", 3), 0,   "B13"),
    ("T1302", "Creación y serialización de pipelines por etapa",      "task",      d("2026-05-08"), end("2026-05-08", 3), 0,   "B13"),
    ("T1303", "Definición de la lista de variables finales del modelo","task",     d("2026-05-08"), end("2026-05-08", 2), 0,   "B13"),
    ("T1304", "Instanciación del modelo final con hiperparms óptimos","task",      d("2026-05-10"), end("2026-05-10", 2), 0,   "B13"),
    ("T1305", "Construcción del ColumnTransformer completo",          "task",      d("2026-05-12"), end("2026-05-12", 2), 0,   "B13"),
    ("T1306", "Creación del pipeline completo preprocesamiento+modelo","task",     d("2026-05-14"), end("2026-05-14", 2), 0,   "B13"),
    ("T1307", "Entrenamiento pipeline de ejecución sobre dataset completo","task", d("2026-05-16"), end("2026-05-16", 2), 0,   "B13"),
    ("T1308", "Serialización del pipeline con cloudpickle",           "task",      d("2026-05-18"), end("2026-05-18", 2), 0,   "B13"),
    # ── BLOQUE 14 ───────────────────────────────────────────────────────────
    ("B14",   "B14 · Código de reentrenamiento",                      "block",     d("2026-05-20"), end("2026-05-20", 7), 0,   "B14"),
    ("T1401", "Definición de la estrategia de reentrenamiento",       "task",      d("2026-05-20"), end("2026-05-20", 2), 0,   "B14"),
    ("T1402", "Código modular para reentrenar ante nuevos datos",     "task",      d("2026-05-22"), end("2026-05-22", 3), 0,   "B14"),
    ("T1403", "Validación de que el reentrenamiento reproduce result.","task",     d("2026-05-25"), end("2026-05-25", 2), 0,   "B14"),
    # ── BLOQUE 15 ───────────────────────────────────────────────────────────
    ("B15",   "B15 · Aplicación en producción y validación temporal", "block",     d("2026-05-27"), end("2026-05-27", 5), 0,   "B15"),
    ("T1501", "Carga de datos de nuevo periodo temporal",             "task",      d("2026-05-27"), end("2026-05-27", 1), 0,   "B15"),
    ("T1502", "Aplicación de pipelines serializados sobre nuevos datos","task",    d("2026-05-28"), end("2026-05-28", 1), 0,   "B15"),
    ("T1503", "Obtención del scoring mediante predicción del modelo", "task",      d("2026-05-29"), end("2026-05-29", 1), 0,   "B15"),
    ("T1504", "Cálculo de métricas de negocio sobre las predicciones","task",     d("2026-05-30"), end("2026-05-30", 1), 0,   "B15"),
    ("T1505", "Análisis comparativo de resultados entre periodos",    "task",      d("2026-05-30"), end("2026-05-30", 1), 0,   "B15"),
    ("T1506", "Identificación de los casos más rentables por scoring","task",     d("2026-05-31"), end("2026-05-31", 1), 0,   "B15"),
    ("M905",  "Hito: Entrega final del proyecto",                     "milestone", d("2026-06-01"), d("2026-06-01"),      0,   "M"),
]

N = len(ROWS)
ROW_H   = 0.68
FIG_W   = 28
FIG_H   = N * ROW_H * 0.38 + 3.5

fig, ax = plt.subplots(figsize=(FIG_W, FIG_H))
fig.patch.set_facecolor("#0F0F1A")
ax.set_facecolor("#0F0F1A")

DATE_MIN = datetime(2025, 10, 25)
DATE_MAX = datetime(2026, 6, 15)

def to_num(dt): return mdates.date2num(dt)

# ── FONDO DE MESES ──────────────────────────────────────────────────────────
cur = datetime(2025, 11, 1)
toggle = False
while cur < DATE_MAX:
    nxt_month = (cur.replace(day=28) + timedelta(days=4)).replace(day=1)
    ax.axvspan(to_num(cur), to_num(nxt_month),
               color="#1A1A2E" if toggle else "#16213E", alpha=1.0, zorder=0)
    toggle = not toggle
    cur = nxt_month

# ── GRID VERTICAL (semanas) ─────────────────────────────────────────────────
week = datetime(2025, 11, 3)
while week < DATE_MAX:
    ax.axvline(to_num(week), color="#FFFFFF", alpha=0.04, linewidth=0.4, zorder=1)
    week += timedelta(days=7)

# ── SEPARADORES HORIZONTALES DE BLOQUE ──────────────────────────────────────
prev_bk = None
for i, row in enumerate(ROWS):
    bk = row[6]
    if bk != prev_bk and prev_bk is not None and row[2] == "block":
        ax.axhline(i - 0.5, color="#FFFFFF", alpha=0.12, linewidth=1.2, zorder=2)
    prev_bk = bk

# ── FILAS DE FONDO ALTERNAS ──────────────────────────────────────────────────
for i, row in enumerate(ROWS):
    alpha = 0.06 if i % 2 == 0 else 0.0
    ax.barh(i, to_num(DATE_MAX) - to_num(DATE_MIN), left=to_num(DATE_MIN),
            height=1.0, color="white", alpha=alpha, zorder=1)

# ── BARRAS PRINCIPALES ───────────────────────────────────────────────────────
for i, row in enumerate(ROWS):
    rid, name, tipo, start, end_d, pct, bk = row
    dark, light, mid = PALETA[bk]
    s_num = to_num(start)
    e_num = to_num(end_d + timedelta(days=1))
    dur   = e_num - s_num

    if tipo == "milestone":
        cx = to_num(start)
        cy = i
        size = 0.38
        diamond = plt.Polygon(
            [[cx, cy - size], [cx + size*0.7, cy],
             [cx, cy + size], [cx - size*0.7, cy]],
            closed=True, facecolor=dark, edgecolor="#FFD700",
            linewidth=1.8, zorder=6)
        ax.add_patch(diamond)
        label = f"  ◆ {name}"
        ax.text(cx + size * 0.8, cy, label, va="center", ha="left",
                fontsize=7.2, color="#FFD700", fontweight="bold", zorder=7)
        continue

    if tipo == "block":
        bar_h = 0.78
        # Shadow
        ax.barh(i + 0.07, dur, left=s_num + 0.3, height=bar_h,
                color="#000000", alpha=0.45, zorder=3)
        # Main bar
        ax.barh(i, dur, left=s_num, height=bar_h,
                color=dark, alpha=0.95, zorder=4,
                edgecolor="#FFFFFF", linewidth=0.6)
        # Progress overlay
        if pct > 0:
            ax.barh(i, dur * pct / 100, left=s_num, height=bar_h,
                    color="#00E676", alpha=0.22, zorder=5)
        # Shine strip
        ax.barh(i - 0.17, dur, left=s_num, height=0.12,
                color="#FFFFFF", alpha=0.12, zorder=5)
        # Label
        mid_x = s_num + dur / 2
        ax.text(mid_x, i, name, ha="center", va="center",
                fontsize=7.8, fontweight="bold", color="#FFFFFF", zorder=6)
        # Dates
        ax.text(s_num + 0.3, i + 0.44, start.strftime("%d %b"),
                fontsize=5.8, color="#CCCCCC", va="top", ha="left", zorder=6)
        ax.text(e_num - 0.3, i + 0.44, end_d.strftime("%d %b"),
                fontsize=5.8, color="#CCCCCC", va="top", ha="right", zorder=6)
        continue

    # ── TAREA NORMAL / BLOQUEANTE ────────────────────────────────────────────
    bar_h = 0.54
    bar_color = "#FF6F00" if tipo == "blocker" else light
    edge_color = "#FF6F00" if tipo == "blocker" else dark
    # Shadow
    ax.barh(i + 0.05, dur, left=s_num + 0.2, height=bar_h,
            color="#000000", alpha=0.35, zorder=3)
    # Background track
    full_dur = to_num(DATE_MAX) - s_num
    ax.barh(i, dur, left=s_num, height=bar_h,
            color=bar_color, alpha=0.18, zorder=3,
            edgecolor=edge_color, linewidth=0.8)
    # Progress fill
    if pct > 0:
        ax.barh(i, dur * pct / 100, left=s_num, height=bar_h,
                color=bar_color, alpha=0.85, zorder=4,
                edgecolor=edge_color, linewidth=0.8)
    # Shine
    ax.barh(i - 0.12, dur, left=s_num, height=0.08,
            color="#FFFFFF", alpha=0.15, zorder=5)
    # % label inside bar (if fits)
    pct_label = f"{pct}%" if pct > 0 else ""
    if dur > 1.5 and pct_label:
        lx = s_num + dur * pct / 100 / 2
        ax.text(lx, i, pct_label, ha="center", va="center",
                fontsize=6, color="#FFFFFF", fontweight="bold", zorder=6)
    # Dates
    ax.text(s_num + 0.15, i + 0.32, start.strftime("%d/%m"),
            fontsize=5.2, color="#AAAAAA", va="top", ha="left", zorder=6)
    ax.text(e_num - 0.15, i + 0.32, end_d.strftime("%d/%m"),
            fontsize=5.2, color="#AAAAAA", va="top", ha="right", zorder=6)

# ── ETIQUETAS EJE Y ─────────────────────────────────────────────────────────
ytick_labels = []
for row in ROWS:
    rid, name, tipo, *_ = row
    if tipo == "milestone":
        ytick_labels.append("")
    elif tipo == "block":
        ytick_labels.append(name)
    else:
        prefix = "  ⚠ " if tipo == "blocker" else "    · "
        ytick_labels.append(prefix + name)

ax.set_yticks(range(N))
ax.set_yticklabels(ytick_labels, fontsize=7, color="#DDDDDD")
ax.invert_yaxis()

for i, row in enumerate(ROWS):
    tipo = row[2]
    tick = ax.yaxis.get_major_ticks()[i]
    if tipo == "block":
        tick.label1.set_fontweight("bold")
        tick.label1.set_fontsize(8.2)
        tick.label1.set_color("#FFFFFF")
    elif tipo == "blocker":
        tick.label1.set_color("#FF9800")
        tick.label1.set_fontweight("bold")
    elif tipo == "milestone":
        tick.label1.set_visible(False)

# ── LÍNEA HOY ────────────────────────────────────────────────────────────────
today_num = to_num(TODAY)
ax.axvline(today_num, color="#FF1744", linewidth=2.2, linestyle="--",
           zorder=8, alpha=0.9)
ax.text(today_num, -0.9, f" HOY · {TODAY.strftime('%d %b %Y')}",
        color="#FF1744", fontsize=8, fontweight="bold", va="top", ha="left", zorder=9)

# ── EJE X ────────────────────────────────────────────────────────────────────
ax.xaxis_date()
ax.xaxis.set_major_locator(mdates.MonthLocator())
ax.xaxis.set_major_formatter(mdates.DateFormatter("%b\n%Y"))
ax.xaxis.set_minor_locator(mdates.WeekdayLocator(byweekday=0))
ax.tick_params(axis="x", colors="#AAAAAA", labelsize=8, which="both")
ax.tick_params(axis="x", length=5, which="major")
ax.tick_params(axis="x", length=2, which="minor")
ax.xaxis.set_tick_params(pad=4)
ax.set_xlim(to_num(DATE_MIN), to_num(DATE_MAX))

# ── SPINES ──────────────────────────────────────────────────────────────────
for spine in ax.spines.values():
    spine.set_edgecolor("#333355")
    spine.set_linewidth(0.8)

# ── LEYENDA ──────────────────────────────────────────────────────────────────
legend_items = [
    mpatches.Patch(facecolor="#1565C0", label="Bloque completado (100%)",  edgecolor="#90CAF9"),
    mpatches.Patch(facecolor="#00695C", label="Bloque en curso / futuro",  edgecolor="#80CBC4"),
    mpatches.Patch(facecolor="#FF6F00", label="Tarea bloqueante",          edgecolor="#FF6F00"),
    mpatches.Patch(facecolor="#FFD700", label="Hito",                      edgecolor="#FFD700"),
    mpatches.Patch(facecolor="#00E676", alpha=0.5, label="Progreso completado"),
    mpatches.Patch(facecolor="#FF1744", label=f"Hoy · {TODAY.strftime('%d %b %Y')}"),
]
leg = ax.legend(handles=legend_items, loc="lower right",
                fontsize=7.5, framealpha=0.15, facecolor="#1A1A2E",
                edgecolor="#444466", labelcolor="#FFFFFF",
                ncol=2, title="Leyenda", title_fontsize=8)
leg.get_title().set_color("#AAAACC")

# ── TÍTULO ───────────────────────────────────────────────────────────────────
fig.text(0.5, 0.995,
         "PROYECTO FINAL EVOLVE · Análisis de Inversión Inmobiliaria AirBnb Madrid",
         ha="center", va="top", fontsize=13, fontweight="bold", color="#FFFFFF")
fig.text(0.5, 0.987,
         "Master Data Science · Julio Valero",
         ha="center", va="top", fontsize=8.5, color="#8888BB")

plt.tight_layout(rect=[0, 0, 1, 0.985])
fig.savefig(OUTPUT, dpi=160, bbox_inches="tight",
            facecolor=fig.get_facecolor(), edgecolor="none")
plt.close(fig)
print(f"Gantt guardado: {OUTPUT}")
