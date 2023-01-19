from fastapi import FastAPI
from fastapi.responses import JSONResponse
from database import *
from pandasql import sqldf

app = FastAPI()

#prueba = df.head(1000)

@app.get("/")
def hello():
    return "Hola Mundo"

@app.get("/consultas/{word}")
def get_word_count(word: str):
    q = f"SELECT plataform, count(title) as quantity FROM df WHERE title LIKE '%{word}%' GROUP BY plataform"
    return sqldf(q)

