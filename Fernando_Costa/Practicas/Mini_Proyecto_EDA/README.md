README 

Fuente de datos: https://catalog.data.gov/dataset/crime-data-from-2020-to-present

ESTRUCTURA Y CONTENIDO DE CADA CARPETA
Mini_Proyecto_EDA
- 01_notebooks: Carpeta con los notebooks de cada fase
    - 000_Enunciado: Notebook con el enunciado del ejercicio
    - 001_Calidad_de_datos: Análisis, formateo y generación de variables
    - 002_EDA: Análisis de posibles aplicaciones de cambios, tratamiento de problemas y aplicación de modificaciones y estadísticos
    - 003_Visualizaciones: Generación de tablas de frecuencia y estadísticos descriptivos con visualizaciones genéricas para la búsqueda de patrones subyacentes y posteriores generaciónes de tablas y visualizaciones específicas con objetivo de realizar un análisis profundo de la información
- 02_archivos: Carpeta con los arhivos resultantes de la realización de cada una de las fases de análisis del proyecto
- 99_data: Carpta con el dataset original de datos comprimido para su mejor manejo

ANÁLISIS
El análisis realizado sobre el dataset de delitos hemos comprobado que tenía posibilidades para sacar conclusiones después de trabajar los datos, por lo que hemos comprobado las dimensiones, que había nulos, diferentes tipos de datos, nombres de columnas a modificar y seguidamente hemos seguido el patrón de:

- Análisis de cada variable según el significado de las variables facilitado por la web de LAPD
- Generación de nuevas columnas desde las variables originales para alcanzar las necesidades
- Formateo de las variables en función de las necesidades específicas
- Tratamiento y análisis de las variables y aplicación de modificaciones y estadísticos
- Generación de visualizaciones acordes

El significado de las columnas según el LAPD sería el siguiente:

- dr_no: Número de expediente oficial compuesto por un año de 2 dígitos, un ID de área y 5 dígitos.
- date_rptd: Fecha de Reporte. Indica el día en que el crimen o incidente fue oficialmente reportado (MM/DD/AAAA)
- date_occ: Fecha de Ocurrencia. Indica el día real en que el crimen tuvo lugar (MM/DD/AAAA)
- time_occ: Hora de Ocurrencia en horario militar de 24 horas.
- area: Áreas Geográficas o Divisiones de Patrulla numeradas secuencialmente del 1 al 21.
- area_name: Nombre de las áreas Geográficas o Divisiones de Patrulla
- rpt_dist_no: Número de distrito de la patrulla del oficial que informó el incidente.
- part_1_2: Indica si el incidente es un crimen de la Parte 1 (crímenes más graves) o de la Parte 2 (crímenes menos graves).
- crm_cd: Código de delito de 3 dígitos del crimen cometido.
- crm_cd_desc: Descripción del delito del crimen cometido.
- mocodes: Modus Operandi o la manera distintiva o característica en que una persona lleva a cabo una actividad criminal.
- vict_age: Edad de la víctima
- vict_sex: Sexo de la víctima.
- vict_descent: Denominación de la descendencia de la víctima
- premis_cd: El Código de Instalación es un código de 3 dígitos que identifica el tipo de lugar donde ocurrió el incidente
- premis_desc: Descripción de la Instalación.
- weapon_used_cd: El Código de Arma es un código de 3 dígitos que identifica el tipo de arma utilizada en el incidente
- weapon_desc: Descripción del Arma.
- status: Estado del caso. (IC es el valor predeterminado)
- status_desc: Define el Código de Estado proporcionado.
- crm_cd_1: Indica el crimen cometido. El Código de Crimen 1 es el principal y el más grave. Los Códigos de Crimen 2, 3 y 4 son, respectivamente, delitos menos graves. Los números de clase de crimen más bajos son más graves.
- crm_cd_2: Puede contener un código para un crimen adicional, menos grave que el Código de Crimen 1.
- crm_cd_3: Puede contener un código para un crimen adicional, menos grave que el Código de Crimen 1.
- crm_cd_4: Puede contener un código para un crimen adicional, menos grave que el Código de Crimen 1.
- location: Dirección postal del incidente del crimen redondeada al centenar de la cuadra más cercana para mantener el anonimato.
- cross_street: El nombre de la calle que se cruza con la calle principal donde ocurrió el incidente.
- lat: Latitud.
- lon: Longitud.

De estas columnas, nosotros hemos hecho las siguientes acciones:

- Hemos asignado dr_no como índice después de comprobar que tenía todos los valores únicos
- De las columnas fecha y hora, hemos extraido year, month y day a nuevas columnas, sin eliminar la variable, para usar la extracción como variables categóricas, hemos eliminado la hora porque no aportaba información y hemos convertido en datetime para futuros análisis
- Hemos generado la columna 'time_to_report' para determinar el gap entre que se comete el delito y se reporta con objetivo de hacer segmentos de horas que se tarda en reportar un delito y su frecuencia
- Hemos generado la columna 'hour_occ' desde 'time_occ' para extraer la hora cuando se ocurrió el delito para determinar las horas mas peligrosas por zona
- Hemos transforamdo todas las variables numéricas a categóricas ya que no tiene sentido aplicarle cálculos numéricos o estadísticos porque son variables identificativas de códigos de delitos, zonas, áreas, status, etc. Las únicas que se han quedado como numéricas son 'time_to_report' y 'vict_age'
- Reorganización de las variables por mayor comodidad
- Localizamos, analizamos y eliminamos duplicados ya que vemos que tienen duplicadas todas las variables

NULOS
- Sobre los nulos, localizamos y analizamos valores pero tomamos como norma dejarlos como NaN porque tienen sentido como tal, ya que no era necesario rellenarlos 
    - 'crm_cd_4', 'crm_cd_3' y 'crm_cd_2' son los códigos de los crímenes secundarios. Entendemos que son nulos porque no hubo crímenes secundarios pero si que hemos rellenado los nulos de 'crm_cd_1' con los delitos de 'crm_cd_2' del mismo registro porque entendemos que no puede haber un delito secundario sin el principal 
    - 'weapon_used_cd' y 'weapon_desc': Habla de las armas usadas. Entendemos que no hubo armas
    - 'cross_street': Identifica si el crimen se cometió en un cruce. Entendemos que no fue en un cruce
    - mocodes: Habla del modus operandi específico del crimen. Entendemos que no encontraron un patrón identificable y podríamos dejarlo como NaN pero lo hemos puesto como '9999' por hacer una acción diferente a efectos de practicar código
    - 'premis_cd' y 'premis_desc' contienen información sobre las instalaciones donde se produjo el crimen (código y descripción). Desconocemos el significado de los códigos, pero observamos que los registros de (df.premis_cd.notna())&(df.premis_desc.isna()) se concentran en unos cuantos códigos y habría que investigarlos con una persona de dentro de la organización para obtener mas información. De momento:
        - 'premis_cd' podrían ser que no lo hayan escrito o que no tengan código para ese sitio concreto y habría que investigarlo con alguien de dentro
        - 'premis_desc' que son nulos son los mismos que premis_cd por lo que los dejamos como nulos
    - En el caso de 'status', los vamos a borrar porque no hay información en casi ninguna variable y solamente es un caso 

MODIFICACIONES
- 'vict_descent' y 'vict_sex' tenían valores '-' que hemos eliminado
- 'vict_sex' aparecen registros con ['M', 'F', nan, 'X', 'H', '-']. Vamos a dejar solamente M: Male, F: Female y U: Unknown. En este caso si que modificamos los nulos

ELIMINACIÓN DE VARIABLES
- Por baja frecuencia (<2%) ya que no podemos agrupar los datos para sacer estadísticos ni conclusiones de grupo
    - location
    - cross_street
- Por no aportar información: 'time_occ'. Hemos generado 'time_to_report' explicada antes.
    NOTA: Si nos metieramos a hacer un análisis mas profundo, habría que segmentar esta variable en tramos para estudiar todos los casos que superan el percentil 75% que son muchos pero, para el caso de estudio y el objetivo del ejercicio, entiendo que no vamos a entrar en análisis tan profundo 

VALORES ATÍPICOS
- Localizamos y analizamos los valores atípicos, llegando a la conclusión que las siguientes variables contienen suficientes valores atípicos como para generarles una categoría 'OTROS', con los datos que supongan menos de un 2%, para poder realizar visualizaciones efectivas: 'weapon_used_cd','premis_cd','premis_desc','weapon_used_cd','weapon_desc','crm_cd_1','crm_cd_2','crm_cd_3','crm_cd_4'

WINSORIZACIÓN
- 'vict_age' observamos que existen datos negativos y por encima de 120 años. Hacemos una winsorización manual (0, 100)

VISUALIZACIONES
- Genéricas: Dividimos los datos en categóricos y numéricos, teniendo las tablas CAT y NUM para poder generar análisis especificos por categoría para un primer análisis de la información con intención de encontrar patrones. Desde CAT, generaremos una tabla de frecuencias y desde NUM una tabla de estadísticos

'crm_cd_desc' no se ve en el gráfico de ese tamaño pero lo he querido incluir para tomar medida de la forma correcta de hacerlo

- Específicas: 
    - Delito más frecuente por área
    - Recuento delitos por año

CONCLUSIONES GENÉRICAS
- Categóricas:
    - Descenso de los delitos cometidos en cantidad, siendo 2024 el año con menor delincuencia. 
    - En una gran mayoría de los casos, solamente se reporta un delito por acción ya que 'crm_cd_2', 'crm_cd_3' y 'crm_cd_4' son nulos y los delitos que mas se cometen como principales (No sabemos que significan los códigos)
    - Las frecuencias sobre las denominaciones de descendencia de las victimas, sexo, zona del delito, tipo de arma, etc
    - El mes con mas delitos es enero
    - Se cometen mas delitos principios de los meses y las horas centrales del dia son las mas habituales
- Numéricas:
    - La gran mayoría de los delitos se reportan en las dos primeras horas desde que se cometió (percentil 75%). 22k casos fuera en nuestro dataset que necesitaríamos generar segamentaciones para saber por donde va pero queda fuera del alcance de este ejercicio
    - Observamos una doble barriga en los datos que nos dice que hay una cantidad muy elevada de bebes que sufren agresiones y otro grupo de personas que va desde los 20 años hasta los 60 años que son el grupo que denuncia delitos, teniendo el pico máximo de concentración de delitos en los 30 años

CONCLUSIONES ESPECÍFICAS
- Delito más frecuente por área: En el gráfico podemos observar que el delito mas frecuente que se comete y la zona. Esto ayudaría a destinar recursos específicos
    NOTA: En un análisis mas profundo, se podría segmentar por horas, edad, procedencia de la víctima por zona y horario por ejemplo
- Recuento delitos por año: En el gráfico podemos observar el recuento de los tipos de delitos cometidos por año donde vemos que graves y leves siguen el mismo patrón descendente

Al final de cada notebook se genera un archivo .pickle con el resultado de las modificaciones de ese notebook de cara a poder rescatar el análisis en el punto que se necesite sin necesidad de cargar todo el código. Es decir, al final del notebook de calidad de datos se genera 'trabajo_resultado_calidad.pickle' que será el que se cargue como archivo inicial en el siguiente notebook