
/* ============================================================
	PROYECTO SQL - ANÁLISIS DE BASE DE DATOS (IMDB)
	ARCHIVO: 02_data.sql
	DESCRIPCIÓN: Gestión de datos y demostración de integridad transaccional.
   ============================================================ */

-- Iniciamos una transacción para asegurar la atomicidad de las operaciones.
-- Esto garantiza que, si algo falla, la base de datos no quede en un estado inconsistente.
START TRANSACTION;

-- 1. INSERCIÓN (INSERT)
-- Añadimos un nuevo registro a la tabla de dimensiones 'actors'.
-- No especificamos el 'id' porque es una Primary Key con AUTO_INCREMENT.
INSERT INTO actors (first_name, last_name, gender) 
VALUES ('Paquito', 'El de los Palotes', 'M'); -- Usamos 'M' para mantener consistencia con tipos estándar

-- 2. ACTUALIZACIÓN (UPDATE)
-- Modificamos los datos de un actor específico utilizando su Primary Key (id).
-- El uso de la PK en el WHERE es vital para no afectar a otros registros accidentalmente.
UPDATE actors 
SET 
    first_name = 'Lola',
    last_name = 'La de los chicles'
WHERE id = 845466;

-- 3. BORRADO (DELETE)
-- Eliminamos un registro específico. 
-- NOTA: En un entorno real, esto fallaría si el actor tiene roles asignados 
-- debido a las restricciones de Foreign Key (FK).
DELETE FROM actors 
WHERE id = 845466;

-- 4. FINALIZACIÓN
-- Si todas las sentencias anteriores se ejecutan sin errores, guardamos los cambios.
COMMIT;

-- En caso de error manual durante las pruebas, usaríamos:
-- ROLLBACK;

