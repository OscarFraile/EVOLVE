
/* ============================================================
	PROYECTO SQL - ANÁLISIS DE BASE DE DATOS (IMDB)
	ARCHIVO: 03_EDA.sql
	DESCRIPCIÓN: Análisis exploratorio de los datos
   ============================================================ */
   
-- Funciones de fecha.
-- Top 5 años con mas estrenos de películas
SELECT 
    year, COUNT(year) 'YearCount'
FROM
    movies
GROUP BY year
ORDER BY YearCount DESC
LIMIT 5;

-- Agregaciones (SUM, COUNT).
-- Media de Prob por género contando que AvgProb siempre sea superior a 0.5
SELECT 
    genre, 
    ROUND(AVG(prob), 1) 'AvgProb'
FROM
    directors_genres
GROUP BY genre
HAVING AvgProb > 0.5;

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


-- Uso de la función 'movie_category' donde debemos darle el id de una película y nos devuelve su título y categoría según la categorización que hicimos anteriormente en el CASE con la lógica aplicada
SELECT name, movie_category(id) 'Categoria'
FROM movies
WHERE id = 12345;

/* ============================================================
	EDA KPI Personales
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
	- Densidad de Reparto: La industria tiende a que los repartos de las películas sean mas amplios 
	- Tasa de Especialización de actores: Hay una especialización relativamente baja, lo que sugiere que los actores ven necesario ser vérsatiles para poder estár en la industria
	- Tasa de Especialización de Directores: Los directores son mas afines a permanecer en un género que los actores
============================================================ */