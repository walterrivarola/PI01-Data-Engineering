# <h1 align=center> **PROYECTO INDIVIDUAL Nº1 - SOY HENRY** </h1>

# <h1 align=center>**`Data Engineering`**</h1>

<p align="center">
<img src="https://files.realpython.com/media/What-is-Data-Engineering_Watermarked.607e761a3c0e.jpg"  height=300>
</p>

## **Descripción del proyecto**

Como Ingeniero de Datos de una empresa ficticia, me proporcionaron 4 datasets de distintas plataformas de streaming, donde debo realizar un análisis exploratorio sobre cada uno de los datos y realizar las correcciones pertinentes como los valores nulos, normalización, tipo de datos, entre otros.

## Explicación del desarrollo
Primeramente tuve que realizar el trabajo de *Extract, Transform and Load*(ETL) a los archivos que me entregaron, luego desarrolle una API con el framework fastAPI para poder disponibilizar los datos, después hice el deployment a traves de Deta.

Las consultas solicitadas por la empresa fueron:
+ Cantidad de veces que aparece una palabra clave en el título de peliculas/series, por plataforma.

+ Cantidad de películas por plataforma con un puntaje mayor a XX en determinado año.

+ Película que más apareció según año, plataforma y tipo de duración.

+ Cantidad de series y películas por rating.

## Estructura del proyecto**
En la raiz principal podemos encontrar a **`database.py`** que es el que se encarga de configurar todo el entorno de la API, luego tenemos a **`main.py`** que es que realiza la parte frontend de la aplicación, **`requeriments.txt`**, que sirve para instalar las dependecias necesarias para el proyecto y por último tenemos **`limpieza.py`** que es el archivo que se encarga de realizar toda la limpieza y normalización de los datos.

Además de eso, hay una carpeta llamada **`src`** donde se encuentran alojados los archivos en crudo que fueron proveidos por la empresa, a parte del archivo ya limpiado con todos los datos.

## Librerias utilizadas**

+ FastAPI
pip install fastapi

+ Deta
pip install deta

+ Pandas
pip install pandas

+ Pandasql
pip install pandas

## IMPORTANTE**
Para poder ejecutar el archivo **`limpieza.py`** y poder tener todos los registros listos para ser utilizado con la API, se debe realizar el siguiente comando desde la consola:

python limpieza.py

## Adicional**
**`Video explativo del codigo`**: 
<br/>
https://youtu.be/xszQy9cDzEw
<br/>

**`Guia de usuario`**: 
Para poder realizar las consultas anteriormente mencionadas, se debe realizar de la siguiente manera:

* Cantidad de veces que aparece una keyword en el título de peliculas/series, por plataforma
    /get_word_count/{plataforma}/{word}

* Cantidad de películas por plataforma con un puntaje mayor a XX en determinado año
    /get_score_count/{plataforma}/{puntuacion}/{anio}

* Película que más duró según año, plataforma y tipo de duración
    /get_longest/{plataforma}/{duration_type}/{anio}

* Cantidad de series y películas por rating
    /get_rating_count/{rating}
<br/>


<br/>

**`Enlaces de prueba`**:
https://nmvpq0.deta.dev/get_word_count/netflix/love

https://nmvpq0.deta.dev/get_score_count/netflix/85/2010

https://nmvpq0.deta.dev/get_longest/netflix/min/2016

https://nmvpq0.deta.dev/get_rating_count/18+