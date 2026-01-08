Proyecto Módulo SQL: Diseño de Base de Datos Relacional y Análisis Exploratorio en SQL

1. Objetivo
    Diseña, implementa y analiza una base de datos relacional.
    El objetivo es que tu modelo sea coherente, los datos integrales, y puedas extraer insights útiles con SQL.
    Incluye comentarios en el código para explicar decisiones de Primary Key (PK), Foreign Key (FK), constraints y relaciones.
    Crearemos:
    - 1 Tabla principal de Hechos (Ventas, Inscripciones, etc) y 
    - 4 o más tablas secundarias de Dimensiones (Colegios, Provincias, Supermercados). 
    Tip: buscad diferencia entre tabla de hechos y tablas de dimensiones.

2. Datos y dominio de la Tabla Principal (Fact Table)
    Puedes usar distintos tipos de datos, de más real a más ficticio:
        - Bases de datos reales o transaccionales de un ERP
            Ej: exportaciones de contabilidad, CRM o ERP. Datos y relaciones auténticas.
        - Bases de datos públicas o datasets online
            Ej: Kaggle, datos abiertos, CSV. Datos reales, volumen controlado.
        - Base de datos ficticia generada con herramientas
            Ej: ChatGPT para simular un modelo de negocio.
        - Base de datos creada desde cero
            Diseña las tablas y agrega registros con INSERT. Control total del modelo para aprender y probar. 
					AQUÍ VAMOS A HACER UN INSERT DE EN LA TABLA DE ACTORS

    En todos los casos documenta:
        - Qué representa cada tabla y su granularidad.
        - Qué queda dentro/fuera del alcance del proyecto.
        - Por qué elegiste cada PK, FK y constraint.

3. Requisitos
    3.1 Modelo y esquema
        - Mínimo 5 tablas (Dim Tables o Tablas secundarias que generaremos por ChatGPT o a mano).
             Ej. Una tabla DIM_CALENDAR con columnas: Fecha (en formato 01/01/,2025), Día (en formato "1"), Mes (en formato "1"), 
             Año (en formato "2025").
        - Todas con Primary Key.
        - Foreign Keys donde aplique.
        - Constraints (NOT NULL, UNIQUE, CHECK, DEFAULT).
        - Justifica la normalización.
        - Comentarios en SQL explicando decisiones.

    3.2 Implementación en SQL
        - Ejecutable desde cero usando sintaxis de "IF NOT EXITS" y "IF EXIST" para evitar errores en cada uno de los CREATE.
        - Utilizar las sentencias más comunes como mínimo una vez: INSERT, UPDATE, DELETE.
        - Conversión de tipos (CAST) si aplica.
        - Funciones de fecha.
        - Agregaciones (SUM, COUNT).
        - Subqueries.
        - Transacciones (BEGIN / COMMIT / ROLLBACK).
        - Al menos un índice con explicación de su utilidad.

    3.3 EDA en SQL
        - Mínimo 3 JOINs (INNER y LEFT).
        - CASE y lógica condicional.
        - Agregaciones.
        - CTEs (WITH), incluyendo encadenadas.
        - Funciones ventana (OVER (PARTITION BY ...)).
        - 1 VIEW y 1 FUNCIÓN con consultas.
        Tip: comenta los insights y por qué son importantes.

4. Resultado final
    Crea una tabla resumen o vista con:
        - Agrupaciones relevantes.
        - Métricas agregadas (COUNT, SUM).
        - Comentario breve de qué decisiones de negocio permite tomar tu análisis.
Ej. Cuantas ventas se han producido en cada provincia, cual es la media, que categoría es la más vendida, etc etc.

5. Entregables
    - 01_schema.sql (si aplica) — modelo, constraints, índices, vistas y funciones con comentarios.
    - 02_data.sql (si aplica) — carga de datos y limpieza con transacciones.
    - 03_eda.sql — EDA completo con comentarios. Esto es el CORE del entregable: aquí irán todas las consultas una tras otra para poder 
		ejecutar las diferentes funciones y sentencias que hemos visto durante el curso y sacar conclusiones de negocio a ser posible.
    - model.png (opcional) — diagrama ER.
    - READ_ME (opcional) — explicación sobre el modelo de datos y el objetivo de las operaciones y métricas.

6. Criterios de evaluación
    - Código ejecutable desde cero.
    - Comentarios claros: explica tablas, relaciones, constraints, índices, vistas y funciones.
    - Calidad del EDA: métricas y KPIs útiles.
    - Explicación del modelo: justifica decisiones, ventajas y limitaciones del diseño.

7. Entrega
    - La entrega se realizará exclusivamente por Google Classroom, adjuntando el enlace público al repositorio de GitHub.
    - La presentación del proyecto no deberá durar más de 10 minutos.
    - La fecha para presentar será 7/8 de Enero, según si el día 7 tenemos muchas dudas en la sesión de Tutoría o no (si no hay muchas
		dudas, empezaremos a presentar los proyectos el mismo día 7).
	- La entrega final tendrá de deadline el 11 de Enero.

Nota: Puedes usar cualquier motor SQL (SQLite, MySQL, PostgreSQL, etc.) y cualquier IDE (DBeaver, Workbench, TablePlus, VS Code, etc.).'''