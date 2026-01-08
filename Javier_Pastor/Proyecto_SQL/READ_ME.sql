/* ============================================================
   PROYECTO SQL - ANÁLISIS DE BASE DE DATOS (IMDB)
   Descripción del modelo y sus relaciones

Objetivo y origen: Diseña, implementa y analiza una base de datos relacional y explicación de su origen
La base de datos que se va a analizar en este proyecto es una db descargada de imdb donde hay información y valoraciones sobre películas 
variadas, por lo que no he decidido yo la estructura, composición ni el contenido de la misma, pero voy a intentar adaptar el objetivo del 
proyecto lo máximo posible explicado los pasos que se irán dando para llegar a los objetivos

Por ejemplo en ranking no está bien identificado y tiene demasiados nulos, por lo que vamos a usar las columnas prob para hacer mediciones numéricas aunque los resultados solamente
servirán a nivel didáctico y no tendrán valor de negocio porque la información no corresponde con el uso que se le va a dar

El script de carga de cada una de las tablas está en el archivo imdb pero la información sobre lo que hay contenida dentro de cada tabla,
la composición de cada una de ellas con sus primary keys, foreign keys, constrains y relaciones la hemos incluido en el archivo 01_schema 

El script con todos los registros de la base de datos es demasiado pesado, por lo que se ha comprimido en un .rar para poder subirlo al repositorio de github

Composición: La base de datos está formada por 7 tablas:
- actors
- directors
- directors_genres
- movies
- movies_directors
- movies_genres
- roles
   ============================================================ */









