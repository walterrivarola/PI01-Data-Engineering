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
    mensaje = ("Bienvenido al sistema de consultas personalizada")
    mensaje2= ("Para realizar las consultas por favor seguir las instrucciones: \n")
    mensaje3= ("* Cantidad de veces que aparece una keyword en el título de peliculas/series, por plataforma\n")
    mensaje4= ("/get_word_count/{plataforma}/{word} \n\n")
    mensaje5= ("* Cantidad de películas por plataforma con un puntaje mayor a XX en determinado año \n")
    mensaje6= ("/get_score_count/{plataforma}/{puntuacion}/{anio}\n\n")
    mensaje7= ("Película que más duró según año, plataforma y tipo de duración\n")
    mensaje8= ("/get_longest/{plataforma}/{duration_type}/{anio}\n\n")
    mensaje9= ("Cantidad de series y películas por rating\n")
    mensaje10= ("/get_rating_count/{rating}\n\n\n")
    aviso=("OBSERVACIÓN: REEMPLAZAR LO QUE ESTÁ ENTRE CORCHETES {} POR LOS VALORES QUE DESEA.")

    return (mensaje + mensaje2 + mensaje3 + mensaje4 + mensaje5 + mensaje6 +mensaje7 + mensaje8 + mensaje9 + mensaje10 + aviso)

# Aquí configuramos las direcciones URL que se utilizarán para hacer las consultas

# En esta función utilizamos la palabra 'word' que ayudará a conseguir la consulta desde la URL
# para poder buscar la palabra clave entre todos los titulos y dependiendo de la plataforma
@app.get("/get_word_count/{plataforma}/{word}")
def get_word_count(plataforma, word):
    w = f"SELECT plataform, count(title) as quantity FROM df WHERE plataform='{plataforma}' AND title LIKE '%{word}%'"
    return sqldf(w,  globals()).to_dict()

# En este caso creamos la ruta para poder buscar la cantidad de registros que tengan un mayor
# puntaje y un año determinado. Todo esto será ingresado en la URL


@app.get('/get_score_count/{plataforma}/{puntuacion}/{anio}')
def get_score_count(plataforma,puntuacion, anio):
    p = f'SELECT plataform, COUNT(score) FROM df WHERE plataform="{plataforma}" AND type="movie" AND score={puntuacion} AND release_year={anio}'
    return sqldf(p, globals()).to_dict()

#Esta parte es para poder consultar la película que más duró según año, plataforma y tipo de duración

@app.get('/get_longest/{plataforma}/{duration_type}/{anio}')
def get_longest(plataforma, duration_type,anio):
    d = f'SELECT title, MAX(duration_int), duration_type FROM df WHERE plataform = "{plataforma}" AND release_year={anio} AND duration_type="{duration_type}"'
    return sqldf(d, globals()).to_dict()


#Y por ultimo tenemos esta ruta que nos mostrará la cantidad de series y películas que hay rating ingresado
@app.get('/get_rating_count/{rating}')
def get_rating_count(rating):
    r = f'SELECT COUNT(type), rating FROM df WHERE rating = "{rating}"'
    return sqldf(r, globals()).to_dict()