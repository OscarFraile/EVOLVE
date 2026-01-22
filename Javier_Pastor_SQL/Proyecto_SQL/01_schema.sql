
/* ============================================================
	PROYECTO SQL - ANÁLISIS DE BASE DE DATOS (IMDB)
	ARCHIVO: 01_schema.sql
	DESCRIPCIÓN: Descripción de tablas, claves y relaciones
   ============================================================ */
/* ============================================================
	3. Requisitos
		3.1 Modelo y esquema
			- Generamos el script con la creación y el completado de todas las tablas en el archivo imdb por separado debido a que, 
            el volumen de información contenido en imdb hace que se ralentice el funcionamiento.
            - Identificadas las funciones, Primary Key, Foreign Keys, Constraints y las relaciones.
			- Generada tabla DIM_CALENDAR con columnas: Fecha (en formato 01/01/,2025), Día (en formato "1"), Mes (en formato "1"), 
				 Año (en formato "2025")
			- Generadas y explicadas las vistas y funciones
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
VIEWS Y FUNCTIONS: Creación de vistas y funciones principales. 
Las vistas generadas forman parte del EDA que realizaremos posteriormente. Se dejan aquí para que se ejecuten todas de una sola vez en cascada y posteriormente se añadirán al script del EDA a modo explicativo 
   ============================================================ */

-- Vamos a crear una view con GenreAverages y después generaremos una función
-- VIEW: Generamos una vista para guardar los resultados de manera dinámica y la llamaremos director_performance
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

-- VIEW: AvgActorsPerMovie
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

-- VIEW: GenresRanking
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

-- VIEW: Actors1Genre
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

-- VIEW: Directors1Genre
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
