# <h1 align=center> **PROYECTO INDIVIDUAL Nº1** </h1>

<p align=center><img src=https://d31uz8lwfmyn8g.cloudfront.net/Assets/logo-henry-white-lg.png><p>

## **Introducción**

El PI-01 del BootCamp de DataScien de Henry consiste en la realización de una API (Application Programming Interface) que devuelva un resultado a cuatro consultas predefinidas, tomando como base datos de las plataformas de streaming Netflix, Hulu, Amazon Prime Video y Disney Plus

## Estapas del proyecto

### EDA y ETL

- Incialmente se realiza la importación de los datos de cada plataforma en un dataframe por medio de la librería pandas.
- Se eploran los datos para determinar las integridad de los diferentes dataframes, las columnas con datos nulos el contenido de las columnas.
- Se comparan las columnas de los dataframes para verificar si es posibles concatenarlos
- Se busca valores que no se encuentren adecuados para las columnas en las que se encuentran ubicados.
- Se reubican los valores a la columna de donde corresponden como en el caso de Hulu y Netflix.
- Se concatenan los dataframes en uno solo a fin de optimizar la transformación, teniendo presente que no seria necesario repetir el proceso 4 veces.
- Se eliminan las columnas que no son necesarias o que no representan información importante para dar respuesta a la información requerida.
- Se ajusta la columna 'duration' para facilitar la consulta de los datos.
  -Se buscan duplicados para determinar si es necesario la eliminación de estos.
- Se exporta el dataframe a una base de datos SQL para ser consultado por la API.

### Creación de la API

- Se decargan las librerias FastAPI y Uvicorn
- Se definen importan las librerias necesarias
- Se crea un motor para consultar la base de datos con SQLite
- Se definen las funciones para resolver las consignas por medio de las consultas "get_max_duration", "get_count_plataform", "get_listedin" y "get_actor".

### Realizar consultas a la API

Las consultas se realizan siguiendo los siguientes parámetros una vez la API ya se encuentre ejecutandose:

- Entrando al link `localhost:80:80/docs` y rellenando la información de acuerdo a la información que se requiera
- `localhost:80:80/get_max_duration(año, plataforma, [min o season])`
- `localhost:80:80/get_count_plataform(plataforma)`
- `localhost:80:80/get_listedin(genero)`
- `localhost:80:80/get_actor(plataforma, año)`

## Herramientas utilizadas

- VsCode
- Python
- Docker
- SQLite
- Fast API
