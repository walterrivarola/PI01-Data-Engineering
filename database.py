'''
importamos la libería Deta para poder activar la conexión con nuestro servidor, luego
importamos pandas para poder leer nuestro archivo que actualmente está ubicado en Github.

Lo hacemos así ya que el servidor de Deta posee un limite de máximo 5.5mb por archivo.
'''
from deta import Deta
import pandas as pd

#Guardamos la url en una variable
url = 'https://raw.githubusercontent.com/walterrivarola/PI01-Data-Engineering/main/src/stream.csv'
df = pd.read_csv(url) #leemos el archivo csv desde la variable generada.

deta = Deta() # configure your Deta project