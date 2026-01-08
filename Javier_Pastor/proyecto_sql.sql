/* ============================================================
   PROYECTO SQL - ANÁLISIS DE BASE DE DATOS (IMDB)
   Descripción del modelo y sus relaciones

1 y 2. Objetivo y origen: Diseña, implementa y analiza una base de datos relacional y explicación de su origen
La base de datos que se va a analizar en este proyecto es una db descargada de imdb donde hay información y valoraciones sobre películas 
variadas, por lo que no he decidido yo la estructura, composición ni el contenido de la misma, pero voy a intentar adaptar el objetivo del 
proyecto lo máximo posible explicado los pasos que se irán dando para llegar a los objetivos

Por ejemplo en ranking no está bien identificado y tiene demasiados nulos, por lo que vamos a usar las columnas prob para hacer mediciones numéricas aunque los resultados solamente
servirán a nivel didáctico y no tendrán valor de negocio porque la información no corresponde con el uso que se le va a dar

Vamos a traer el script de carga de cada una de las tablas e iremos explicando la información que hay contenida dentro de cada tabla,
la composición de cada una de ellas con sus primary keys, foreign keys, constrains y relaciones. 

El script con todos los registros de la base de datos sería demasiado extenso para incorporarlo como parte de la resolución del caso, por lo que lo dejaremos disponible para su ejecución y
dejamos aquí la carga de las tablas para su explicación

Composición: La db está formada por 7 tablas:
- actors
- directors
- directors_genres
- movies
- movies_directors
- movies_genres
- roles
   ============================================================ */

/* ============================================================
   PROYECTO SQL - ANÁLISIS DE BASE DE DATOS (IMDB)
   DESCRIPCIÓN DE TABLAS, CLAVES Y RELACIONES
   ============================================================ */


/* ============================================================
   TABLA: actors
   ------------------------------------------------------------
   FUNCIÓN:
   Almacena la información básica de los actores.

   CLAVES:
   - PRIMARY KEY:
       id

   RELACIONES:
   - El campo id es utilizado como FOREIGN KEY en la tabla roles.

   CONSTRAINTS:
   - PRIMARY KEY sobre id
   - Índices sobre first_name y last_name para optimizar búsquedas
   ============================================================ */
SET FOREIGN_KEY_CHECKS = 0;

DROP TABLE IF EXISTS `actors`;
CREATE TABLE `actors` (
  `id` int(11) NOT NULL auto_increment,
  `first_name` varchar(100) DEFAULT NULL,
  `last_name` varchar(100) DEFAULT NULL,
  `gender` char(1) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `actors_first_name` (`first_name`),
  KEY `actors_last_name` (`last_name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;


/* ============================================================
   TABLA: directors
   ------------------------------------------------------------
   FUNCIÓN:
   Contiene la información básica de los directores.

   CLAVES:
   - PRIMARY KEY:
       id

   RELACIONES:
   - El campo id es referenciado como FOREIGN KEY en:
       • directors_genres
       • movies_directors

   CONSTRAINTS:
   - PRIMARY KEY sobre id
   - Índices sobre nombre y apellido
   ============================================================ */

DROP TABLE IF EXISTS `directors`;
CREATE TABLE `directors` (
  `id` int(11) NOT NULL auto_increment,
  `first_name` varchar(100) DEFAULT NULL,
  `last_name` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `directors_first_name` (`first_name`),
  KEY `directors_last_name` (`last_name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;


/* ============================================================
   TABLA: directors_genres
   ------------------------------------------------------------
   FUNCIÓN:
   Tabla intermedia que relaciona directores con géneros.

   CLAVES:
   - PRIMARY KEY compuesta:
       (director_id, genre)

   RELACIONES:
   - FOREIGN KEY:
       director_id → directors(id)

   CONSTRAINTS:
   - Clave primaria compuesta
   - Integridad referencial con borrado y actualización en cascada

   TIPO DE RELACIÓN:
   - Muchos a muchos entre directores y géneros
   ============================================================ */

DROP TABLE IF EXISTS `directors_genres`;
CREATE TABLE `directors_genres` (
  `director_id` int(11) NOT NULL,
  `genre` varchar(100) NOT NULL,
  `prob` float DEFAULT NULL,
  PRIMARY KEY (`director_id`,`genre`),
  KEY `directors_genres_director_id` (`director_id`),
  CONSTRAINT `directors_genres_ibfk_1`
    FOREIGN KEY (`director_id`)
    REFERENCES `directors` (`id`)
    ON DELETE CASCADE
    ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8;


/* ============================================================
   TABLA: movies
   ------------------------------------------------------------
   FUNCIÓN:
   Almacena la información principal de las películas.

   CLAVES:
   - PRIMARY KEY:
       id

   RELACIONES:
   - El campo id es referenciado como FOREIGN KEY en:
       • movies_directors
       • movies_genres
       • roles

   CONSTRAINTS:
   - PRIMARY KEY sobre id
   - Índice sobre el nombre de la película
   ============================================================ */

DROP TABLE IF EXISTS `movies`;
CREATE TABLE `movies` (
  `id` int(11) NOT NULL auto_increment,
  `name` varchar(100) DEFAULT NULL,
  `year` int(11) DEFAULT NULL,
  `rankscore` float DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `movies_name` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;


/* ============================================================
   TABLA: movies_directors
   ------------------------------------------------------------
   FUNCIÓN:
   Relaciona películas y directores.

   CLAVES:
   - PRIMARY KEY compuesta:
       (director_id, movie_id)

   RELACIONES:
   - FOREIGN KEY:
       director_id → directors(id)
       movie_id → movies(id)

   CONSTRAINTS:
   - Clave primaria compuesta
   - Integridad referencial con cascada

   TIPO DE RELACIÓN:
   - Muchos a muchos entre películas y directores
   ============================================================ */

DROP TABLE IF EXISTS `movies_directors`;
CREATE TABLE `movies_directors` (
  `director_id` int(11) NOT NULL,
  `movie_id` int(11) NOT NULL,
  PRIMARY KEY (`director_id`,`movie_id`),
  KEY `movies_directors_director_id` (`director_id`),
  KEY `movies_directors_movie_id` (`movie_id`),
  CONSTRAINT `movies_directors_ibfk_1`
    FOREIGN KEY (`director_id`)
    REFERENCES `directors` (`id`)
    ON DELETE CASCADE
    ON UPDATE CASCADE,
  CONSTRAINT `movies_directors_ibfk_2`
    FOREIGN KEY (`movie_id`)
    REFERENCES `movies` (`id`)
    ON DELETE CASCADE
    ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8;


/* ============================================================
   TABLA: movies_genres
   ------------------------------------------------------------
   FUNCIÓN:
   Relaciona películas con sus géneros.

   CLAVES:
   - PRIMARY KEY compuesta:
       (movie_id, genre)

   RELACIONES:
   - FOREIGN KEY:
       movie_id → movies(id)

   CONSTRAINTS:
   - Clave primaria compuesta
   - Integridad referencial activa

   TIPO DE RELACIÓN:
   - Muchos a muchos entre películas y géneros
   ============================================================ */

DROP TABLE IF EXISTS `movies_genres`;
CREATE TABLE `movies_genres` (
  `movie_id` int(11) NOT NULL,
  `genre` varchar(100) NOT NULL,
  PRIMARY KEY (`movie_id`,`genre`),
  KEY `movies_genres_movie_id` (`movie_id`),
  CONSTRAINT `movies_genres_ibfk_1`
    FOREIGN KEY (`movie_id`)
    REFERENCES `movies` (`id`)
    ON DELETE CASCADE
    ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8;


/* ============================================================
   TABLA: roles
   ------------------------------------------------------------
   FUNCIÓN:
   Relaciona actores con películas e indica el rol interpretado.

   CLAVES:
   - PRIMARY KEY compuesta:
       (actor_id, movie_id, role)

   RELACIONES:
   - FOREIGN KEY:
       actor_id → actors(id)
       movie_id → movies(id)

   CONSTRAINTS:
   - Clave primaria compuesta
   - Integridad referencial con cascada

   TIPO DE RELACIÓN:
   - Muchos a muchos entre actores y películas
   - Relación enriquecida con el atributo "role"
   ============================================================ */

DROP TABLE IF EXISTS `roles`;
CREATE TABLE `roles` (
  `actor_id` int(11) NOT NULL,
  `movie_id` int(11) NOT NULL,
  `role` varchar(100) NOT NULL,
  PRIMARY KEY (`actor_id`,`movie_id`,`role`),
  KEY `actor_id` (`actor_id`),
  KEY `movie_id` (`movie_id`),
  CONSTRAINT `roles_ibfk_1`
    FOREIGN KEY (`actor_id`)
    REFERENCES `actors` (`id`)
    ON DELETE CASCADE
    ON UPDATE CASCADE,
  CONSTRAINT `roles_ibfk_2`
    FOREIGN KEY (`movie_id`)
    REFERENCES `movies` (`id`)
    ON DELETE CASCADE
    ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

SET FOREIGN_KEY_CHECKS = 1;


/* ============================================================
3. Requisitos
    3.1 Modelo y esquema
        - Generada tabla DIM_CALENDAR con columnas: Fecha (en formato 01/01/,2025), Día (en formato "1"), Mes (en formato "1"), 
             Año (en formato "2025")
        - Se han identificado y documentado las Primary Key, Foreign Keys, Constraints y las relaciones.
	
/* ============================================================
   TABLA: dim_calendar
   ------------------------------------------------------------
   Tabla de dimensión temporal.
   Se utiliza para análisis por día, mes y año.
   No pertenece a la base de datos original, se añade con fines didácticos.
   ============================================================ */

DROP TABLE IF EXISTS dim_calendar;
CREATE TABLE dim_calendar (
    fecha DATE PRIMARY KEY,
    dia INT NOT NULL,
    mes INT NOT NULL,
    anio INT NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;


DELIMITER $$
CREATE PROCEDURE fill_calendar()
BEGIN
    DECLARE v_fecha DATE;
    SET v_fecha = '1990-01-01';

    WHILE v_fecha <= '2025-12-31' DO
        INSERT INTO dim_calendar (fecha, dia, mes, anio)
        VALUES (
            v_fecha,
            DAY(v_fecha),
            MONTH(v_fecha),
            YEAR(v_fecha)
        );

        SET v_fecha = DATE_ADD(v_fecha, INTERVAL 1 DAY);
    END WHILE;
END$$
DELIMITER ;

CALL fill_calendar();
DROP PROCEDURE fill_calendar;

/* ============================================================
    3.2 Implementación en SQL
        - CREADO en el archivo imdb: 
			- Ejecutable desde cero usando sintaxis de "IF NOT EXITS" y "IF EXIST" para evitar errores en cada uno de los CREATE.
        - NO APLICA: 
			- Conversión de tipos (CAST) si aplica.
	============================================================ */
-- Utilizadas las sentencias INSERT, UPDATE, DELETE para generar, actualizar y borrar un registro a modo de demostración didáctica
INSERT INTO actors (first_name, last_name, gender) VALUES ('Paquito','El de los Palotes', 'H');

UPDATE actors 
SET 
	first_name = 'Lola',
    last_name = 'La de los chicles'
WHERE id = 845466;

DELETE 
	FROM actors
    WHERE id = 845466;
    
-- Funciones de fecha.
-- Top 5 años con mas estrenos de películas
select 
	year,
	count(year) 'YearCount'
from movies
group by year
order by YearCount desc
limit 5;

-- Agregaciones (SUM, COUNT).
-- Media de Prob por género contando que AvgProb siempre sea superior a 0.5
SELECT 
    genre, 
    ROUND(AVG(prob), 1) 'AvgProb'
FROM
    directors_genres
GROUP BY genre
HAVING AvgProb > 0.5
;

-- Subqueries. Varias subqueries anidadas para extraer la media de prob de los géneros solamente de los directores de aquellos id de películas que tienen un prob > 0.5 en el año 2002
-- El objetivo es simplemente didáctico para demostrar el uso de múltiples subqueries anidadas
SELECT 
	genre 'DirectorGenre',
	ROUND(AVG(prob),1) 'AVG_prob'
FROM directors_genres
WHERE prob > 0.5 AND director_id IN (
									SELECT id
									FROM directors
									WHERE id IN (SELECT director_id
													FROM movies_directors
													WHERE movie_id IN (SELECT id FROM movies WHERE year = 2002)))
GROUP BY genre
ORDER BY 2 ASC;
				 
-- Al menos un índice con explicación de su utilidad.
-- idx_movies_year: Este índice se creó para acelerar el filtrado y agrupamiento temporal de los registros, optimizando la velocidad de las consultas que analizan tendencias por año.
CREATE INDEX idx_movies_year ON movies(year);
-- idx_roles_movie_id: Se implementó para agilizar la unión (JOIN) entre las tablas de películas y roles, reduciendo el tiempo de búsqueda de las participaciones en cada producción.
CREATE INDEX idx_roles_movie_id ON roles(movie_id);
-- idx_roles_actor_id: Su función es optimizar la conexión entre los actores y sus respectivos personajes, permitiendo recuperar el historial de un actor sin escanear toda la tabla de roles.
CREATE INDEX idx_roles_actor_id ON roles(actor_id);
/* ============================================================

    3.3 EDA en SQL

============================================================ */

-- Mínimo 3 JOINs (INNER y LEFT).
-- 1º. Doble JOIN de las películas de cada actor estrenadas en cada año siempre que estrenara mas de una pelicula 
SELECT 
    movies.year,
    actors.id,
    actors.first_name 'Actors',
    COUNT(actors.first_name) 'MoviesPerYear'
FROM
    movies
        JOIN roles ON movies.id = roles.movie_id
        JOIN actors ON actors.id = roles.actor_id
GROUP BY movies.year , actors.id
HAVING COUNT(actors.id) > 1
ORDER BY Actors;

-- 2º. Doble left join para extraer las películas de cada director
SELECT 
    directors.id 'DirectorId',
    CONCAT(directors.first_name, ' ', directors.last_name) 'DirectorName',
    movies.id 'MovieId',
    movies.name 'MovieName'
FROM directors
        LEFT JOIN movies_directors ON directors.id = movies_directors.director_id
        LEFT JOIN movies ON movies.id = movies_directors.movie_id;

-- 3º. Tripe join para extraer el top 5 de las películas que contienen mas géneros con su id, nombre y director en el año 2002
SELECT 
    mg.movie_id 'MovieId',
    COUNT(mg.movie_id) 'CountGenres', 
    m.name 'MovieName',
    concat(d.first_name,' ',d.last_name) 'DirectorName'
FROM
    movies_genres mg
    JOIN movies m ON mg.movie_id = m.id
    JOIN movies_directors md ON m.id = md.movie_id
    JOIN directors d ON d.id = md.director_id
WHERE
    m.year = 2002
GROUP BY mg.movie_id, MovieName, DirectorName
HAVING COUNT(mg.movie_id) > 1
ORDER BY CountGenres DESC
LIMIT 5;

-- CTEs (WITH), incluyendo encadenadas.
-- CASE y lógica condicional.
-- Performance por película ordenado según su prob
WITH GenreAverages AS (
    -- Calculamos el promedio por género primero y nos quedamos con los que están por encima de 0.1 de media
    SELECT 
        genre, 
        ROUND(AVG(prob), 1) AS AvgProb
    FROM directors_genres
    GROUP BY genre
    HAVING AvgProb > 0.1
)
SELECT 
    m.id AS Movie_ID,
    m.name AS Movie_Name,
    dg.genre AS Director_Genre,
    ga.AvgProb,
    CASE -- Reasignamos para darle lógica de negocio 
		WHEN ga.AvgProb < 0.4 THEN 'Bajo'
		WHEN ga.AvgProb BETWEEN 0.4 AND 0.6 THEN 'Promedio'
		WHEN ga.AvgProb BETWEEN 0.6 AND 0.8 THEN 'Alto'
		ELSE 'Excelente'
	END AS PerformanceLevel
FROM movies m
JOIN movies_directors md ON m.id = md.movie_id
JOIN directors d ON md.director_id = d.id
JOIN directors_genres dg ON d.id = dg.director_id
JOIN GenreAverages ga ON dg.genre = ga.genre
ORDER BY AvgProb DESC; -- Unimos con los promedios calculados


-- 1 VIEW y 1 FUNCIÓN con consultas.
-- Vamos a crear una view con GenreAverages y después generaremos una función
-- VIEW: Con la consulta anterior, generamos una vista para guardar los resultados de manera dinámica y la llamaremos director_performance que contendrá la misma información que la consulta
CREATE VIEW director_performance AS
WITH GenreAverages AS (
    -- Calculamos el promedio por género primero
    SELECT 
        genre, 
        ROUND(AVG(prob), 1) AS AvgProb
    FROM directors_genres
    GROUP BY genre
    HAVING AvgProb > 0.1
)
SELECT 
    m.id AS Movie_ID,
    m.name AS Movie_Name,
    dg.genre AS Director_Genre,
    ga.AvgProb,
    CASE
		WHEN ga.AvgProb < 0.4 THEN 'Bajo'
		WHEN ga.AvgProb BETWEEN 0.4 AND 0.6 THEN 'Promedio'
		WHEN ga.AvgProb BETWEEN 0.6 AND 0.8 THEN 'Alto'
		ELSE 'Excelente'
	END AS PerformanceLevel
FROM movies m
JOIN movies_directors md ON m.id = md.movie_id
JOIN directors d ON md.director_id = d.id
JOIN directors_genres dg ON d.id = dg.director_id
JOIN GenreAverages ga ON dg.genre = ga.genre
ORDER BY AvgProb DESC;

-- FUNCTION: Generamos una función que nos permita extraer la información sin la necesidad de realizar todo el código anterior 
DELIMITER //
CREATE FUNCTION movie_category(p_movie_id INT) 
RETURNS VARCHAR(20)
DETERMINISTIC
BEGIN
    DECLARE v_category VARCHAR(20);

    SELECT PerformanceLevel INTO v_category
    FROM director_performance
    WHERE movie_id = p_movie_id
    LIMIT 1;
    
    RETURN v_category;
END //
DELIMITER ;

-- Realizamos la prueba de la extracción de la información donde conseguimos el id de la película y su categoría según la categorización que hicimos anteriormente en el CASE con la lógica aplicada
SELECT name, movie_category(id) 'Categoria'
FROM movies
WHERE id = 12345;

-- Agregaciones: Realizamos una consulta con los mínimos, medias, máximos y recuento de cada uno de los géneros de los directores
SELECT 
    genre, 
	round(min(prob),1) 'Min',
    round(avg(prob),1) 'Avg',
    max(prob) 'Max',
    count(prob) 'Count'
FROM
    directors_genres
GROUP BY genre
ORDER BY 5 DESC;

/* ============================================================
	3.4 EDA KPI Personales
		- Densidad de Reparto: ¿Cuál es el promedio de actores por película en cada década? Un cambio brusco en este número a lo largo de los años podría indicar cambios en la industria.
		- Tasa de Especialización de actores:
			Ranking de actores que han trabajado en mas géneros diferentes
            ¿Qué porcentaje de actores trabajan en un solo género frente a los "multitarea"?
		- Tasa de Especialización de Directores:
			¿Qué porcentaje de directores trabajan en un solo género frente a los "multitarea"?
============================================================ */
-- Densidad de Reparto: ¿Cuál es el promedio de actores por película en cada década?:
CREATE VIEW AvgActorsPerMovie AS
with ActorsPerMovie as (
	select 
		m2.id,
		count(distinct a2.id) 'CountActors'
	from movies m2
	join roles r2 on m2.id = r2.movie_id
	join actors a2 on r2.actor_id = a2.id
	group by m2.id
)
select 
    CASE
		WHEN m.year <= 1900 THEN '<1900'
		WHEN m.year BETWEEN 1901 AND 1910 THEN '1900-1910'
		WHEN m.year BETWEEN 1911 AND 1920 THEN '1910-1920'
		WHEN m.year BETWEEN 1921 AND 1930 THEN '1921-1930'
		WHEN m.year BETWEEN 1931 AND 1940 THEN '1931-1940'
		WHEN m.year BETWEEN 1941 AND 1950 THEN '1941-1950'
		WHEN m.year BETWEEN 1951 AND 1960 THEN '1951-1960'
		WHEN m.year BETWEEN 1961 AND 1970 THEN '1961-1970'
		WHEN m.year BETWEEN 1971 AND 1980 THEN '1971-1980'
		WHEN m.year BETWEEN 1981 AND 1990 THEN '1981-1990'
		WHEN m.year BETWEEN 1991 AND 2000 THEN '1991-2000'
		ELSE '>2000'
	END AS YearLevel,
    round(avg(apm.CountActors),1) 'AvgCountActors'
from movies m
join roles r on m.id = r.movie_id
join actors a on r.actor_id = a.id
join ActorsPerMovie apm on apm.id = m.id
group by YearLevel;

-- Tasa de Especialización de actores: 
-- Ranking de actores que han trabajado en mas géneros diferentes
CREATE VIEW GenresRanking AS
SELECT 
    a.id, COUNT(DISTINCT mg.genre) 'CountGenres'
FROM
    movies m
        JOIN
    roles r ON m.id = r.movie_id
        JOIN
    actors a ON r.actor_id = a.id
        JOIN
    movies_genres mg ON m.id = mg.movie_id
GROUP BY a.id
ORDER BY CountGenres DESC;

-- ¿Qué porcentaje de actores trabajan en un solo género frente a los "multitarea"?
CREATE VIEW Actors1Genre AS
WITH ActorGenreCount AS (
    -- Paso 1: Contamos géneros únicos por cada actor
    SELECT 
        a.id,
        COUNT(DISTINCT mg.genre) AS total_generos_actor
    FROM actors a
    JOIN roles r ON a.id = r.actor_id
    JOIN movies_genres mg ON r.movie_id = mg.movie_id
    GROUP BY a.id
)
-- Paso 2 y 3: Calculamos el porcentaje final
SELECT 
    COUNT(CASE WHEN total_generos_actor = 1 THEN 1 END) AS Actores_Un_Solo_Genero,
    COUNT(*) AS Total_Actores,
    ROUND(
        COUNT(CASE WHEN total_generos_actor = 1 THEN 1 END) * 100.0 / COUNT(*), 
    2) AS Porcentaje_Especializacion
FROM ActorGenreCount;

-- Tasa de Especialización de directores: 
-- ¿Qué porcentaje de directores trabajan en un solo género frente a los "multitarea"?
CREATE VIEW Directors1Genre AS
WITH DirectorGenreCount AS (
    -- Paso 1: Contamos géneros únicos por cada director
    SELECT 
        d.id,
        COUNT(DISTINCT dg.genre) AS total_generos_director
    FROM directors d
    JOIN directors_genres dg ON d.id = dg.director_id
    GROUP BY d.id
)
-- Paso 2 y 3: Calculamos el porcentaje final
SELECT 
    COUNT(CASE WHEN total_generos_director = 1 THEN 1 END) AS Directores_Un_Solo_Genero,
    COUNT(*) AS Total_Directores,
    ROUND(
        COUNT(CASE WHEN total_generos_director = 1 THEN 1 END) * 100.0 / COUNT(*), 
    2) AS Porcentaje_Especializacion
FROM DirectorGenreCount;


/* ============================================================
Conclusiones:
Siendo el dueño de una productora de cine, buscaría contratar a alguien que fuera versátil para poder hacer muchas variaciones y 
también tener a actores especializados que tengan un alto ranking en géneros específicos
============================================================ */






