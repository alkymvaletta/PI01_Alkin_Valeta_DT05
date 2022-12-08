# Se importa lo necesario

from fastapi import FastAPI
from typing import Union
import sqlalchemy as sql
from typing import Union
import pandas as pd

# Se crea el motor a la base de datos
engine = sql.create_engine("sqlite:///../database/all_platforms.db")
SQL_DATABASE_URL = "sqlite:///database/all_platforms.db"


description = """Descripción

    Esta API es el resultado del PI01 del bootcamp de DataScience de Henry.

    Devuelve resultado a las consultas de máxima duración, cantidad de peliculas
    y series, cantidad de veces que se repite un género y el actor que más se 
    repite de acuerdo a una database de las plataformas de streaming Netflix,
    Amazon Prime, Hulu y Disney Plus
    """

app = FastAPI(
    title="API - PI01 Alkin Valeta",
    description=description,
    contact={
        "name": "Alkin Valeta",
        "url": "https://www.linkedin.com/in/alkinvaleta/",
        "email": "alkymvaletta@gmail.com",
    },
)


# Se agrega un saludo en la pagina principal de la API
@app.get("/")
def saludo():
    mensaje = "Bienvenido a mi API. Ve a http://127.0.0.1:8000/docs"

    return mensaje


# Máxima duración según tipo de film (película/serie), por plataforma y por año:
# El request debe ser: get_max_duration(año, plataforma, [min o season])


@app.get("/get_max_duration({year},{plataforma},{time})")
async def duration(year: int, plataforma: str, time: str):
    if time == "min":
        time = "Movie"
    else:
        time = "TV Show"
    df_resp1 = pd.read_sql(
        f"""
        SELECT  title , MAX( duration ) as Duration 
        FROM platforms 
        WHERE platform= "{plataforma}" and release_year = {year} and type = "{time}"
        """,
        con=engine,
    )
    resp1 = df_resp1.to_dict()
    return resp1


# Cantidad de películas y series (separado) por plataforma
# El request debe ser: get_count_plataform(plataforma)


@app.get("/get_count_plataform({plataforma})")
async def count(plataforma: str):
    df_resp2 = pd.read_sql(
        f"""
        SELECT type as "Tipo_Contenido", COUNT( * ) as "Cantidad" 
        FROM platforms 
        WHERE platform = "{plataforma}"
        GROUP BY type""",
        con=engine,
    )
    resp2 = df_resp2.to_dict("index")
    return resp2


# Cantidad de veces que se repite un género y plataforma con mayor frecuencia del mismo.
# El request debe ser: get_listedin(genero)


@app.get("/get_listedin({genero})")
async def listedin(genero: str):
    df_resp3 = pd.read_sql(
        f"""
        SELECT platform, COUNT( listed_in) as "Cantidad"
        FROM platforms 
        WHERE listed_in LIKE "%{genero}%" 
        GROUP BY platform LIMIT 1
        """,
        con=engine,
    )
    resp3 = df_resp3.to_dict("index")
    return resp3


# Actor que más se repite según plataforma y año.
# El request debe ser: get_actor(plataforma, año)


@app.get("/get_actor({plataforma},{year})")
async def actor(plataforma: str, year: int):
    df_resp4 = pd.read_sql(
        f"""SELECT * 
    FROM platforms
    WHERE platform = "{plataforma}" and release_year = {year}""",
        con=engine,
    )
    if plataforma == "hulu":
        return "no se encuentran datos"
    else:
        df_cast = df_resp4["cast"].str.split(pat=",", expand=True)

        df_cast = pd.concat(
            objs=[df_cast[i] for i in range(len(df_cast.columns))], ignore_index=True
        )
        counts = df_cast.value_counts()
        respuesta = counts.index[0]
        return respuesta
