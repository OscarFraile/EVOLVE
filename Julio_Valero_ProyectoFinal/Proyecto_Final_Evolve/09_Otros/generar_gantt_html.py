from datetime import datetime, timedelta

OUTPUT_HTML = r"C:\Users\Oscar\OneDrive - FM4\Escritorio\EVOLVE\Data Science\EVOLVE\Julio_Valero_ProyectoFinal\Proyecto_Final_Evolve\09_Otros\gantt_airbnb.html"

def d(s): return datetime.strptime(s, "%Y-%m-%d")
def end(s, dur): return d(s) + timedelta(days=dur - 1)

PALETA = {
    "B1": "#1565C0", "B2": "#6A1B9A", "B3": "#006064", "B4": "#BF360C",
    "B5": "#2E7D32", "B6": "#283593", "B7": "#AD1457", "B8": "#455A64",
    "B9": "#00695C", "B10": "#0277BD", "B11": "#512DA8", "B12": "#558B2F",
    "B13": "#00838F", "B14": "#EF6C00", "B15": "#C2185B", "M": "#B71C1C",
}
PALETA_LIGHT = {
    "B1": "#90CAF9", "B2": "#CE93D8", "B3": "#80DEEA", "B4": "#FFAB91",
    "B5": "#A5D6A7", "B6": "#9FA8DA", "B7": "#F48FB1", "B8": "#90A4AE",
    "B9": "#80CBC4", "B10": "#81D4FA", "B11": "#B39DDB", "B12": "#C5E1A5",
    "B13": "#80DEEA", "B14": "#FFCC80", "B15": "#F8BBD0", "M": "#EF9A9A",
}

ROWS = [
    ("B1",    "B1 · Definición y planificación del proyecto",         "block",     d("2025-11-01"), end("2025-11-01",20), 100, "B1"),
    ("T101",  "Definición del objetivo de negocio",                   "task",      d("2025-11-01"), end("2025-11-01", 4), 100, "B1"),
    ("T102",  "Identificación de palancas de rentabilidad",           "task",      d("2025-11-05"), end("2025-11-05", 3), 100, "B1"),
    ("T103",  "Definición de KPIs por palanca",                       "task",      d("2025-11-08"), end("2025-11-08", 3), 100, "B1"),
    ("T104",  "Identificación de entidades y fuentes de datos",       "task",      d("2025-11-11"), end("2025-11-11", 4), 100, "B1"),
    ("T105",  "Formulación de preguntas semilla por eje de análisis", "task",      d("2025-11-15"), end("2025-11-15", 6), 100, "B1"),
    ("M901",  "Hito: Primeras ideas de proyecto fin de máster",       "milestone", d("2025-11-21"), d("2025-11-21"),      100, "M"),
    ("B2",    "B2 · Configuración del entorno y setup del proyecto",  "block",     d("2025-11-21"), end("2025-11-21",21), 100, "B2"),
    ("T201",  "Creación del entorno Conda con versiones específicas", "task",      d("2025-11-21"), end("2025-11-21", 9), 100, "B2"),
    ("T202",  "Importación y verificación de librerías",              "task",      d("2025-11-30"), end("2025-11-30", 5), 100, "B2"),
    ("T203",  "Creación de estructura de directorios",                "task",      d("2025-12-05"), end("2025-12-05", 7), 100, "B2"),
    ("M902",  "Hito: Definición del MVP",                            "milestone", d("2025-12-12"), d("2025-12-12"),      100, "M"),
    ("B3",    "B3 · Adquisición y exploración inicial de datos",      "block",     d("2025-12-12"), end("2025-12-12",15), 100, "B3"),
    ("T301",  "Carga y exploración de ficheros AirBnB disponibles",   "task",      d("2025-12-12"), end("2025-12-12", 5), 100, "B3"),
    ("T302",  "Decisión sobre qué tablas usar y descartar",           "task",      d("2025-12-17"), end("2025-12-17", 3), 100, "B3"),
    ("T303",  "Obtención datos precio m2 (web scraping Idealista)",   "task",      d("2025-12-20"), end("2025-12-20", 4), 100, "B3"),
    ("T304",  "Creación base de datos SQLite y carga de tablas",      "task",      d("2025-12-24"), end("2025-12-24", 3), 100, "B3"),
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
    ("B5",    "B5 · Preparación de variables para análisis",          "block",     d("2026-01-21"), end("2026-01-21",13), 100, "B5"),
    ("T501",  "Creación KPI precio_total (lógica por tipo alquiler)", "task",      d("2026-01-21"), end("2026-01-21", 3), 100, "B5"),
    ("T502",  "Creación KPI ocupación desde availability_365",        "task",      d("2026-01-21"), end("2026-01-21", 2), 100, "B5"),
    ("T503",  "Discretización manual bedrooms (Estudio,1,2,3,4+)",   "task",      d("2026-01-24"), end("2026-01-24", 2), 100, "B5"),
    ("T504",  "Discretización automática percentiles",                "task",      d("2026-01-24"), end("2026-01-24", 2), 100, "B5"),
    ("T505",  "Estimación de m2 por número de dormitorios",           "task",      d("2026-01-26"), end("2026-01-26", 2), 100, "B5"),
    ("T506",  "Cálculo precio_compra estimado (m2 x precio_m2 x dto)","task",     d("2026-01-28"), end("2026-01-28", 2), 100, "B5"),
    ("T507",  "Distancia geoespacial a Puerta del Sol (Haversine)",   "task",      d("2026-01-28"), end("2026-01-28", 2), 100, "B5"),
    ("T508",  "Creación variable target pisos_rentables (umbral 10a)","task",     d("2026-01-30"), end("2026-01-30", 3), 100, "B5"),
    ("T509",  "Guardado del dataset preparado en base de datos",      "task",      d("2026-02-02"), end("2026-02-02", 1), 100, "B5"),
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
    ("B7",    "B7 · Comunicación de resultados",                      "block",     d("2026-02-20"), end("2026-02-20", 9), 100, "B7"),
    ("T701",  "Redacción del contexto y objetivos del análisis",      "task",      d("2026-02-20"), end("2026-02-20", 2), 100, "B7"),
    ("T702",  "Elaboración de conclusiones ejecutivas",               "task",      d("2026-02-22"), end("2026-02-22", 2), 100, "B7"),
    ("T703",  "Construcción de 5 exhibits gráficos de soporte",       "task",      d("2026-02-24"), end("2026-02-24", 3), 100, "B7"),
    ("T704",  "Recomendaciones para equipo de valoraciones",          "task",      d("2026-02-27"), end("2026-02-27", 2), 100, "B7"),
    ("B8",    "B8 · Exploración, calidad de datos y EDA para ML",     "block",     d("2026-03-01"), end("2026-03-01",15), 100, "B8"),
    ("T801",  "Carga dataset y eliminación de columnas de la target", "task",      d("2026-03-01"), end("2026-03-01", 1), 100, "B8"),
    ("T802",  "[BLOQ] Separación dataset validación 30%",             "blocker",   d("2026-03-02"), end("2026-03-02", 1), 100, "B8"),
    ("T803",  "[BLOQ] Separación dataset de trabajo 70%",             "blocker",   d("2026-03-02"), end("2026-03-02", 1), 100, "B8"),
    ("T804",  "Exploración inicial: dimensiones, tipos y únicos",     "task",      d("2026-03-03"), end("2026-03-03", 2), 100, "B8"),
    ("T805",  "Separación en datasets numérico y categórico",         "task",      d("2026-03-05"), end("2026-03-05", 1), 100, "B8"),
    ("T806",  "Identificación y gestión de nulos en categóricas",     "task",      d("2026-03-06"), end("2026-03-06", 2), 100, "B8"),
    ("T807",  "Agrupación de categorías poco frecuentes en OTROS",    "task",      d("2026-03-08"), end("2026-03-08", 2), 100, "B8"),
    ("T808",  "Normalización de valores inconsistentes",              "task",      d("2026-03-10"), end("2026-03-10", 1), 100, "B8"),
    ("T809",  "Análisis estadístico de variables numéricas",          "task",      d("2026-03-11"), end("2026-03-11", 2), 100, "B8"),
    ("T810",  "EDA categóricas: frecuencias y gráficos de barras",    "task",      d("2026-03-11"), end("2026-03-11", 2), 100, "B8"),
    ("T811",  "EDA numéricas: estadísticos ampliados y distribución", "task",      d("2026-03-13"), end("2026-03-13", 2), 100, "B8"),
    ("T812",  "Guardado de datasets tras calidad de datos y EDA",     "task",      d("2026-03-15"), end("2026-03-15", 1), 100, "B8"),
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
    ("B10",   "B10 · Preselección de variables",                      "block",     d("2026-04-01"), end("2026-04-01",11), 0,   "B10"),
    ("T1001", "[BLOQ] Separación de predictoras y target",            "blocker",   d("2026-04-01"), end("2026-04-01", 1), 0,   "B10"),
    ("T1002", "Mutual Information",                                   "task",      d("2026-04-02"), end("2026-04-02", 2), 0,   "B10"),
    ("T1003", "Recursive Feature Elimination (RFE)",                  "task",      d("2026-04-02"), end("2026-04-02", 2), 0,   "B10"),
    ("T1004", "Permutation Importance",                               "task",      d("2026-04-02"), end("2026-04-02", 2), 0,   "B10"),
    ("T1005", "Combinación de métodos mediante Super Ranking",        "task",      d("2026-04-04"), end("2026-04-04", 2), 0,   "B10"),
    ("T1006", "Análisis de correlaciones entre variables",            "task",      d("2026-04-06"), end("2026-04-06", 2), 0,   "B10"),
    ("T1007", "Eliminación de variables con exceso de correlación",   "task",      d("2026-04-08"), end("2026-04-08", 2), 0,   "B10"),
    ("T1008", "Selección método final y guardado dataset preselec.",  "task",      d("2026-04-10"), end("2026-04-10", 2), 0,   "B10"),
    ("B11",   "B11 · Balanceo",                                       "block",     d("2026-04-12"), end("2026-04-12", 8), 0,   "B11"),
    ("T1101", "Análisis de la distribución de clases de la target",   "task",      d("2026-04-12"), end("2026-04-12", 1), 0,   "B11"),
    ("T1102", "Evaluación sin balanceo como línea base",              "task",      d("2026-04-13"), end("2026-04-13", 1), 0,   "B11"),
    ("T1103", "Undersampling aleatorio (RandomUnderSampler)",         "task",      d("2026-04-14"), end("2026-04-14", 2), 0,   "B11"),
    ("T1104", "Oversampling aleatorio (RandomOverSampler)",           "task",      d("2026-04-14"), end("2026-04-14", 2), 0,   "B11"),
    ("T1105", "SMOTE-Tomek (técnica combinada)",                      "task",      d("2026-04-14"), end("2026-04-14", 2), 0,   "B11"),
    ("T1106", "Penalización por peso en el modelo (class_weight)",    "task",      d("2026-04-14"), end("2026-04-14", 2), 0,   "B11"),
    ("T1107", "Comparación de resultados y selección método final",   "task",      d("2026-04-16"), end("2026-04-16", 2), 0,   "B11"),
    ("T1108", "Guardado del dataset final balanceado",                "task",      d("2026-04-18"), end("2026-04-18", 2), 0,   "B11"),
    ("B12",   "B12 · Modelización",                                   "block",     d("2026-04-20"), end("2026-04-20",15), 0,   "B12"),
    ("T1201", "[BLOQ] Separación train y validación interna",         "blocker",   d("2026-04-20"), end("2026-04-20", 1), 0,   "B12"),
    ("T1202", "Regresión Logística (línea base)",                     "task",      d("2026-04-21"), end("2026-04-21", 2), 0,   "B12"),
    ("T1203", "Random Forest",                                        "task",      d("2026-04-21"), end("2026-04-21", 2), 0,   "B12"),
    ("T1204", "XGBoost y Gradient Boosting",                         "task",      d("2026-04-21"), end("2026-04-21", 2), 0,   "B12"),
    ("T1205", "Hist Gradient Boosting",                               "task",      d("2026-04-21"), end("2026-04-21", 2), 0,   "B12"),
    ("T1206", "Optimización hiperparámetros (Grid/Random Search+CV)", "task",      d("2026-04-23"), end("2026-04-23", 4), 0,   "B12"),
    ("T1207", "Evaluación: ROC AUC, Precision, Recall, F1, Matriz",  "task",      d("2026-04-27"), end("2026-04-27", 2), 0,   "B12"),
    ("T1208", "Reporting: Gain Chart, Lift Chart, Curva ROC",         "task",      d("2026-04-29"), end("2026-04-29", 2), 0,   "B12"),
    ("T1209", "Selección del modelo final",                           "task",      d("2026-05-01"), end("2026-05-01", 4), 0,   "B12"),
    ("B13",   "B13 · Preparación del código de producción",           "block",     d("2026-05-05"), end("2026-05-05",15), 0,   "B13"),
    ("T1301", "Encapsulación de transformaciones en FunctionTransf.", "task",      d("2026-05-05"), end("2026-05-05", 3), 0,   "B13"),
    ("T1302", "Creación y serialización de pipelines por etapa",      "task",      d("2026-05-08"), end("2026-05-08", 3), 0,   "B13"),
    ("T1303", "Definición de la lista de variables finales del modelo","task",     d("2026-05-08"), end("2026-05-08", 2), 0,   "B13"),
    ("T1304", "Instanciación del modelo final con hiperparms óptimos","task",     d("2026-05-10"), end("2026-05-10", 2), 0,   "B13"),
    ("T1305", "Construcción del ColumnTransformer completo",          "task",      d("2026-05-12"), end("2026-05-12", 2), 0,   "B13"),
    ("T1306", "Creación del pipeline completo preprocesamiento+modelo","task",     d("2026-05-14"), end("2026-05-14", 2), 0,   "B13"),
    ("T1307", "Entrenamiento pipeline sobre dataset completo",        "task",      d("2026-05-16"), end("2026-05-16", 2), 0,   "B13"),
    ("T1308", "Serialización del pipeline con cloudpickle",           "task",      d("2026-05-18"), end("2026-05-18", 2), 0,   "B13"),
    ("B14",   "B14 · Código de reentrenamiento",                      "block",     d("2026-05-20"), end("2026-05-20", 7), 0,   "B14"),
    ("T1401", "Definición de la estrategia de reentrenamiento",       "task",      d("2026-05-20"), end("2026-05-20", 2), 0,   "B14"),
    ("T1402", "Código modular para reentrenar ante nuevos datos",     "task",      d("2026-05-22"), end("2026-05-22", 3), 0,   "B14"),
    ("T1403", "Validación de que el reentrenamiento reproduce result.","task",     d("2026-05-25"), end("2026-05-25", 2), 0,   "B14"),
    ("B15",   "B15 · Aplicación en producción y validación temporal", "block",     d("2026-05-27"), end("2026-05-27", 5), 0,   "B15"),
    ("T1501", "Carga de datos de nuevo periodo temporal",             "task",      d("2026-05-27"), end("2026-05-27", 1), 0,   "B15"),
    ("T1502", "Aplicación de pipelines serializados sobre nuevos datos","task",    d("2026-05-28"), end("2026-05-28", 1), 0,   "B15"),
    ("T1503", "Obtención del scoring mediante predicción del modelo", "task",      d("2026-05-29"), end("2026-05-29", 1), 0,   "B15"),
    ("T1504", "Cálculo de métricas de negocio sobre las predicciones","task",     d("2026-05-30"), end("2026-05-30", 1), 0,   "B15"),
    ("T1505", "Análisis comparativo de resultados entre periodos",    "task",      d("2026-05-30"), end("2026-05-30", 1), 0,   "B15"),
    ("T1506", "Identificación de los casos más rentables por scoring","task",     d("2026-05-31"), end("2026-05-31", 1), 0,   "B15"),
    ("M905",  "Hito: Entrega final del proyecto",                     "milestone", d("2026-06-01"), d("2026-06-01"),      0,   "M"),
]

TODAY = datetime(2026, 3, 16)
DATE_MIN = datetime(2025, 10, 25)
DATE_MAX = datetime(2026, 6, 15)
TOTAL_DAYS = (DATE_MAX - DATE_MIN).days

def pct_pos(dt):
    return (dt - DATE_MIN).days / TOTAL_DAYS * 100

# Build month headers
months = []
cur = datetime(2025, 11, 1)
while cur < DATE_MAX:
    nxt = (cur.replace(day=28) + timedelta(days=4)).replace(day=1)
    left = pct_pos(cur)
    width = pct_pos(min(nxt, DATE_MAX)) - left
    months.append((cur.strftime("%b %Y"), left, width))
    cur = nxt

# Build week lines
weeks = []
w = datetime(2025, 11, 3)
while w < DATE_MAX:
    weeks.append(pct_pos(w))
    w += timedelta(days=7)

today_pct = pct_pos(TODAY)

# Build rows HTML
ROW_H = 28
rows_html = ""
prev_bk = None
for i, row in enumerate(ROWS):
    rid, name, tipo, start, end_d, pct, bk = row
    dark = PALETA[bk]
    light = PALETA_LIGHT[bk]

    # separator
    sep = ""
    if tipo == "block" and prev_bk is not None:
        sep = '<div style="height:6px;background:#0F0F1A;"></div>'
    prev_bk = bk

    bg = "#1A1A2E" if i % 2 == 0 else "#16213E"

    if tipo == "milestone":
        mp = pct_pos(start)
        status = "✔ Completado" if pct == 100 else "Pendiente"
        rows_html += f"""
        {sep}
        <div class="gantt-row" style="background:{bg};">
          <div class="label-cell milestone-label">◆ {name}</div>
          <div class="bar-cell">
            <div class="milestone-diamond" style="left:calc({mp}% - 8px);" title="{name} · {start.strftime('%d/%m/%Y')} · {status}"></div>
          </div>
        </div>"""
        continue

    s_pct = pct_pos(start)
    e_pct = pct_pos(end_d + timedelta(days=1))
    w_pct = e_pct - s_pct
    prog_w = w_pct * pct / 100

    if tipo == "block":
        label_style = f"font-weight:700;font-size:12px;color:#fff;"
        bar_style = f"background:{dark};border:1px solid {light}33;"
        h = 22
    elif tipo == "blocker":
        label_style = f"font-size:11px;color:#FF9800;font-weight:600;"
        bar_style = f"background:#FF6F0033;border:1.5px solid #FF6F00;"
        h = 16
    else:
        label_style = f"font-size:11px;color:#ccc;"
        bar_style = f"background:{light}33;border:1px solid {dark};"
        h = 16

    tooltip = f"{name} · {start.strftime('%d/%m/%Y')} → {end_d.strftime('%d/%m/%Y')} · {pct}%"
    date_label = f"{start.strftime('%d/%m')}–{end_d.strftime('%d/%m')}"

    rows_html += f"""
    {sep}
    <div class="gantt-row" style="background:{bg};">
      <div class="label-cell" style="{label_style}">{"" if tipo=="block" else "  · "}{name}</div>
      <div class="bar-cell">
        <div class="bar-track" style="left:{s_pct}%;width:{w_pct}%;height:{h}px;top:calc(50% - {h//2}px);{bar_style}" title="{tooltip}">
          <div class="bar-progress" style="width:{pct}%;background:{dark};opacity:0.75;height:100%;"></div>
          <span class="bar-label">{date_label}{f" · {pct}%" if pct>0 else ""}</span>
        </div>
      </div>
    </div>"""

# Month headers HTML
months_html = ""
for label, left, width in months:
    months_html += f'<div class="month-cell" style="left:{left}%;width:{width}%;">{label}</div>'

# Week lines HTML
weeks_html = ""
for wp in weeks:
    weeks_html += f'<div class="week-line" style="left:{wp}%;"></div>'

html = f"""<!DOCTYPE html>
<html lang="es">
<head>
<meta charset="UTF-8">
<title>Gantt · Proyecto Final Evolve · AirBnb Madrid</title>
<style>
  * {{ box-sizing: border-box; margin: 0; padding: 0; }}
  body {{ background: #0F0F1A; font-family: 'Segoe UI', sans-serif; color: #ddd; }}

  #header {{
    position: sticky; top: 0; z-index: 100;
    background: #0F0F1A;
    border-bottom: 2px solid #333355;
    padding: 10px 0 6px 0;
  }}
  #title {{
    text-align: center;
    font-size: 15px; font-weight: 700; color: #fff; letter-spacing: 0.5px;
  }}
  #subtitle {{
    text-align: center;
    font-size: 11px; color: #8888BB; margin-top: 2px;
  }}
  #controls {{
    text-align: center; margin-top: 6px;
  }}
  #controls button {{
    background: #1E1E3A; color: #aaa; border: 1px solid #333355;
    padding: 3px 12px; margin: 0 3px; cursor: pointer; border-radius: 4px;
    font-size: 12px;
  }}
  #controls button:hover {{ background: #2a2a50; color: #fff; }}
  #controls span {{ font-size: 12px; color: #777; margin: 0 8px; }}

  #gantt-container {{
    display: flex;
    overflow-x: auto;
  }}

  #label-col {{
    min-width: 300px;
    max-width: 300px;
    flex-shrink: 0;
    position: sticky;
    left: 0;
    z-index: 50;
    background: #0F0F1A;
    border-right: 1px solid #333355;
  }}
  .label-header {{
    height: 32px;
    background: #1A1A2E;
    border-bottom: 1px solid #333355;
    display: flex; align-items: center; padding-left: 10px;
    font-size: 11px; color: #666; font-weight: 600;
  }}

  #chart-col {{
    flex: 1;
    position: relative;
    min-width: 0;
  }}
  #timeline-header {{
    height: 32px;
    position: relative;
    background: #1A1A2E;
    border-bottom: 1px solid #333355;
  }}
  .month-cell {{
    position: absolute; top: 0; height: 100%;
    display: flex; align-items: center; justify-content: center;
    font-size: 11px; font-weight: 600; color: #AAAACC;
    border-left: 1px solid #333355;
  }}
  .week-line {{
    position: absolute; top: 0; bottom: 0;
    width: 1px; background: rgba(255,255,255,0.04); pointer-events: none;
  }}
  .today-line {{
    position: absolute; top: 0; bottom: 0;
    width: 2px; background: #FF1744; opacity: 0.85;
    pointer-events: none; z-index: 10;
  }}
  .today-label {{
    position: absolute; top: 4px;
    font-size: 9px; font-weight: 700; color: #FF1744;
    white-space: nowrap; z-index: 11;
  }}

  .gantt-row {{
    display: flex; height: 28px; align-items: center;
  }}
  .label-cell {{
    width: 300px; min-width: 300px;
    padding: 0 6px 0 10px;
    font-size: 11px; color: #ccc;
    white-space: nowrap; overflow: hidden; text-overflow: ellipsis;
    cursor: default;
  }}
  .milestone-label {{
    color: #FFD700 !important; font-weight: 700; font-size: 11px;
  }}
  .bar-cell {{
    flex: 1; position: relative; height: 100%;
  }}
  .bar-track {{
    position: absolute;
    border-radius: 4px;
    overflow: hidden;
    cursor: pointer;
    transition: filter 0.15s;
  }}
  .bar-track:hover {{ filter: brightness(1.25); }}
  .bar-progress {{
    position: absolute; left: 0; top: 0; bottom: 0;
    border-radius: 4px 0 0 4px;
  }}
  .bar-label {{
    position: absolute; left: 4px; top: 50%;
    transform: translateY(-50%);
    font-size: 9px; color: #fff; font-weight: 600;
    white-space: nowrap; pointer-events: none;
    text-shadow: 0 1px 2px #000;
  }}
  .milestone-diamond {{
    position: absolute; top: 50%; transform: translateY(-50%);
    width: 16px; height: 16px;
    background: #B71C1C;
    border: 2px solid #FFD700;
    rotate: 45deg;
    cursor: pointer;
    transition: filter 0.15s;
  }}
  .milestone-diamond:hover {{ filter: brightness(1.4); }}

  #legend {{
    display: flex; flex-wrap: wrap; gap: 12px;
    padding: 10px 16px;
    background: #1A1A2E;
    border-top: 1px solid #333355;
    font-size: 11px; color: #aaa;
  }}
  .legend-item {{ display: flex; align-items: center; gap: 5px; }}
  .legend-dot {{ width: 12px; height: 12px; border-radius: 3px; }}
</style>
</head>
<body>

<div id="header">
  <div id="title">PROYECTO FINAL EVOLVE · Análisis de Inversión Inmobiliaria AirBnb Madrid</div>
  <div id="subtitle">Master Data Science · Julio Valero &nbsp;|&nbsp; Hoy: {TODAY.strftime('%d/%m/%Y')}</div>
  <div id="controls">
    <button onclick="zoom(-1)">− Zoom</button>
    <span id="zoom-label">100%</span>
    <button onclick="zoom(1)">+ Zoom</button>
    <button onclick="scrollToToday()">Ir a HOY</button>
  </div>
</div>

<div id="gantt-container">
  <div id="label-col">
    <div class="label-header">Tarea</div>
    {"".join(f'<div class="gantt-row" style="background:{"#1A1A2E" if i%2==0 else "#16213E"};"><div class="label-cell" style="{"font-weight:700;font-size:12px;color:#fff;" if ROWS[i][2]=="block" else "color:#FFD700;font-weight:700;" if ROWS[i][2]=="milestone" else "color:#FF9800;font-weight:600;" if ROWS[i][2]=="blocker" else ""}">{ROWS[i][1]}</div></div>' for i in range(len(ROWS)))}
  </div>
  <div id="chart-col">
    <div id="timeline-header">
      {months_html}
    </div>
    <div id="chart-body" style="position:relative;">
      {weeks_html}
      <div class="today-line" id="today-line" style="left:{today_pct}%;"></div>
      <div class="today-label" id="today-label" style="left:calc({today_pct}% + 4px);">HOY</div>
      {rows_html}
    </div>
  </div>
</div>

<div id="legend">
  <div class="legend-item"><div class="legend-dot" style="background:#1565C0;"></div> Completado (100%)</div>
  <div class="legend-item"><div class="legend-dot" style="background:#00695C;"></div> En curso / Futuro</div>
  <div class="legend-item"><div class="legend-dot" style="background:#FF6F00;border:1.5px solid #FF6F00;"></div> Bloqueante</div>
  <div class="legend-item"><div class="legend-dot" style="background:#B71C1C;border:2px solid #FFD700;rotate:45deg;border-radius:0;"></div> Hito</div>
  <div class="legend-item"><div class="legend-dot" style="background:#FF1744;"></div> Hoy · {TODAY.strftime('%d/%m/%Y')}</div>
</div>

<script>
  let zoomLevel = 100;
  const chartCol = document.getElementById('chart-col');

  function zoom(dir) {{
    zoomLevel = Math.max(50, Math.min(400, zoomLevel + dir * 25));
    chartCol.style.minWidth = zoomLevel + 'vw';
    document.getElementById('zoom-label').textContent = zoomLevel + '%';
  }}

  function scrollToToday() {{
    const todayLine = document.getElementById('today-line');
    const container = document.getElementById('gantt-container');
    const labelWidth = 300;
    const chartWidth = chartCol.offsetWidth;
    const todayPct = {today_pct};
    const todayPx = (todayPct / 100) * chartWidth;
    container.scrollLeft = todayPx - (window.innerWidth - labelWidth) / 2;
  }}

  window.addEventListener('load', () => {{
    setTimeout(scrollToToday, 100);
  }});
</script>
</body>
</html>"""

with open(OUTPUT_HTML, "w", encoding="utf-8") as f:
    f.write(html)

print(f"HTML generado: {OUTPUT_HTML}")
