from datetime import date
from pydantic import BaseModel
from deta import Deta
import pandas

df = pandas.read_csv('./src/stream.csv')


deta = Deta() # configure your Deta project
db = deta.Base('Engineering')  # access your DB

class Stream(BaseModel):
    id: str
    type: str
    title: str
    director: str
    cast: str
    country: str
    date_added: date
    release_year: int
    rating: str
    listed_in: str
    description: str
    score: int
    duration_int: int
    duration_type: str

class UpdateStream(BaseModel):
    id: str = None
    type: str = None
    title: str = None
    director: str = None
    cast: str = None
    country: str = None
    date_added: date = None
    release_year: int = None
    rating: str = None
    listed_in: str = None
    description: str = None
    score: int = None
    duration_int: int = None
    duration_type: str = None