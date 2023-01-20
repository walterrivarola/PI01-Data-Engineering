'''
Primeramente importamos la libreria fastAPI para poder
crear la API de forma exitosa y poder realizar consultas
a traves de un servidor.
Luego importamos sqldf desde pandasql que nos ayudará
a realizar consultas sql y database es el archivo donde estará
las configuraciones pertinentes.
'''

from fastapi import FastAPI
from pandasql import sqldf
from database import *


app = FastAPI()

@app.get("/")
def hello():
    return "Bienvenido al sistema de consultas personalizada"

# Aquí configuramos las direcciones URL que se utilizarán para hacer las consultas

# En esta función utilizamos la palabra 'word' que ayudará a conseguir la consulta desde la URL
# para poder buscar la palabra clave entre todos los titulos y dependiendo de la plataforma
@app.get("/query/1/{plataforma}/{word}")
def get_word_count(plataforma: str, word: str):
    q = f"SELECT plataform, count(title) as quantity FROM df WHERE plataform='{plataforma}' title LIKE '%{word}%'"
    return sqldf(q,  globals())

# En este caso creamos la ruta para poder buscar la cantidad de registros que tengan un mayor
# puntaje y un año determinado. Todo esto será ingresado en la URL


@app.get('/query/2/{plataforma},{puntuacion},{anio}')
def get_score_count(plataforma: str,puntuacion: int, anio: int):
    q = f'SELECT plataform, score FROM df WHERE plataform="{plataforma}" type="movie" AND score={puntuacion} AND release_year={anio}'
    resultado = sqldf(q, globals())
    return resultado

#Esta parte es para poder consultar la película que más duró según año, plataforma y tipo de duración

@app.get('/query/3/{plataforma},{duration_type},{anio}')
def get_longest(plataforma: str, duration_type: str,anio: int):
    q = f'SELECT title, MAX(duration_int), duration_type FROM df WHERE plataform = "{plataforma}" AND release_year={anio} AND duration_type="{duration_type}"'
    resultado = sqldf(q, globals())
    return resultado

#Y por ultimo tenemos esta ruta que nos mostrará la cantidad de series y películas que hay rating ingresado
@app.get('/query/4/{rating}')
def get_rating_count(rating: str):
    q = f'SELECT COUNT(type), rating FROM df WHERE rating = "{rating}"'
    resultado = sqldf(q, globals())
    return resultado