/* ============================================================
   PROYECTO SQL - ANÁLISIS DE BASE DE DATOS (IMDB)
   Descripción del modelo y sus relaciones

1. Objetivo y origen: Diseña, implementa y analiza una base de datos relacional y explicación de su origen
	La base de datos que se va a analizar en este proyecto es una db descargada de imdb donde hay información y valoraciones sobre películas 
	variadas, por lo que no he decidido yo la estructura, composición ni el contenido de la misma, pero voy a intentar adaptar el objetivo del 
	proyecto lo máximo posible explicado los pasos que se irán dando para llegar a los objetivos

	Por ejemplo en ranking no está bien identificado y tiene demasiados nulos, por lo que vamos a usar las columnas prob para hacer mediciones numéricas aunque los resultados solamente
	servirán a nivel didáctico y no tendrán valor de negocio porque la información no corresponde con el uso que se le va a dar

	El script de carga de cada una de las tablas está en el archivo imdb pero la información sobre lo que hay contenida dentro de cada tabla,
	la composición de cada una de ellas con sus primary keys, foreign keys, constrains y relaciones la hemos incluido en el archivo 01_schema 

	El script con todos los registros de la base de datos es demasiado pesado, por lo que se ha comprimido en un .rar para poder subirlo al repositorio de github

2. Modelo de Datos y Arquitectura
	Composición: La base de datos está formada por 7 tablas:
	- actors: Almacena la información básica de los actores.
	- directors: Contiene la información básica de los directores.
	- directors_genres: Tabla intermedia que relaciona directores con géneros.
	- movies: Almacena la información principal de las películas.
	- movies_directors: Relaciona películas y directores.
	- movies_genres: Relaciona películas con sus géneros.
	- roles: Relaciona actores con películas e indica el rol interpretado.
    
3. Implementación Técnica
	Integridad y Optimización
	- Constraints: Se han implementado Primary Keys (PK) en todas las tablas y Foreign Keys (FK) para asegurar la integridad referencial en las relaciones N:M (como en roles y movies_directors).
	- Índices: Se incluye un índice en la columna year de la tabla movies para optimizar los filtros temporales.
	- Vistas (Views): Se han creado vistas como director_performance para pre-calcular métricas de éxito y mejorar la velocidad de carga en datasets extensos.

	Procesamiento de Datos
	- Transacciones: Las operaciones de carga y actualización de registros (en 02_data.sql) se ejecutan bajo bloques START TRANSACTION para garantizar que los cambios sean atómicos y seguros.

4. Análisis y Métricas Clave (EDA)
	El núcleo del análisis se centra en:
	- Índice de Especialización: Mediante CTEs encadenadas, calculamos el porcentaje de actores que trabajan en un solo género frente a los polifacéticos.
	- Rendimiento Relativo: Uso de Funciones Ventana para saber la puntuación de una película según la información aportada.
	- Categorización Automática: Implementación de una Función personalizada y lógica CASE para clasificar películas según su rankscore.

5. Conclusiones de Negocio
	Siendo el dueño de una productora de cine, buscaría contratar a alguien que fuera versátil para poder hacer muchas variaciones y 
	también tener a actores especializados que tengan un alto ranking en géneros específicos
	- Densidad de Reparto: La industria tiende a que los repartos de las películas sean mas amplios 
	- Tasa de Especialización de actores: Hay una especialización relativamente baja, lo que sugiere que los actores ven necesario ser vérsatiles para poder estár en la industria
	- Tasa de Especialización de Directores: Los directores son mas afines a permanecer en un género que los actores

Estructura de archivos en este repositorio:
	- 01_schema.sql: Definición de tablas, constraints, vistas y funciones.
	- 02_data.sql: Carga de datos, limpieza y ejemplos de transacciones.
	- 03_eda.sql: Consultas de análisis, CTEs y resultados de negocio.
	- imdb_model.png: Diagrama Entidad-Relación del proyecto.
    - Enunciado_Proyecto_SQL: Información básica del propósito de este proyecto
    - imdb.rar: Script de carga con las tablas y su contenido
    

   ============================================================ */









