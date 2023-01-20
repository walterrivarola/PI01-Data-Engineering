import pandas as pd
'''
Importamos tanto la librería como los archivos que vamos a utilizar para
realizar el proceso de ETL
'''
amazon = pd.read_csv('./src/amazon_prime_titles-score.csv')
disney = pd.read_csv('./src/disney_plus_titles-score.csv')
hulu = pd.read_csv('./src/hulu_titles-score.csv')
netflix = pd.read_csv('./src/netflix_titles-score.csv')

'''
Creamos una columna llamada id2, en sus correspondientes DataFrame,
que va a contener los valores 'a' de amazon, 'd' de disney,
'h' de hulu y n de 'netflix'
'''
amazon['id2'] = 'a'
disney['id2'] = 'd'
hulu['id2'] = 'h'
netflix['id2'] = 'n'

'''
Creamos una columna nueva y el valor agregado sería la concatenación de id2(la columna antiguamente creada) y show_id
que cada DF tiene.
'''
amazon['id'] = amazon.id2.str.cat(amazon.show_id)
disney['id'] = disney.id2.str.cat(disney.show_id)
hulu['id'] = hulu.id2.str.cat(hulu.show_id)
netflix['id'] = netflix.id2.str.cat(netflix.show_id)
'''
Creamos una columna para poder identificar los datos a que empresa de streaming corresponde
'''
amazon['plataform'] = 'amazon'
disney['plataform'] = 'disney'
hulu['plataform'] = 'hulu'
netflix['plataform'] = 'netflix'

'''
Eliminamos las columnas que ya no se van a necesitar y actualizamos cada DF
'''
amazon.drop(['show_id', 'id2'], axis=1, inplace=True)
disney.drop(['show_id', 'id2'], axis=1, inplace=True)
hulu.drop(['show_id', 'id2'], axis=1, inplace=True)
netflix.drop(['show_id', 'id2'], axis=1, inplace=True)

'''
Reorganizamos todas las columnas
'''
amazon = amazon[['id', 'type', 'title', 'director', 'cast', 'country', 'date_added', 'release_year', 'rating', 'duration', 'listed_in',
       'description', 'score', 'plataform']]
disney = disney[['id', 'type', 'title', 'director', 'cast', 'country', 'date_added', 'release_year', 'rating', 'duration', 'listed_in',
       'description', 'score', 'plataform']]
hulu = hulu[['id', 'type', 'title', 'director', 'cast', 'country', 'date_added', 'release_year', 'rating', 'duration', 'listed_in',
       'description', 'score', 'plataform']]
netflix = netflix[['id', 'type', 'title', 'director', 'cast', 'country', 'date_added', 'release_year', 'rating', 'duration', 'listed_in',
       'description', 'score', 'plataform']]

'''
Creamos una variable nueva que contendra cada uno de los dataframes para agilizar el trabajo
'''
stream = amazon
stream = pd.concat([amazon, disney, hulu, netflix])

'''
Reemplazamos los valores nulos de la columna rating por G
'''

stream['rating'].fillna('G', inplace=True)

'''
Transformamos el tipo de dato string a fecha de la columna date_added
'''
stream['date_added'] = pd.to_datetime(stream['date_added'])

'''
Realizamos un ciclo para poder transformar cada palabra del DF a minusculas
guidandonos por el tipo de datos O (Object), en caso de ser un int, float u otro,
lo salta.
'''
for column in stream:
    if stream[column].dtype == ('O'):
        stream[column] = stream[column].str.lower()
    else:
        pass

'''
Dividimos la columna 'duration' en dos para poder identificar mejor y realizar
las consultas más adelante de manera mas segura y luego eliminamos dicha columna.
'''
durations = stream["duration"].str.split(expand=True)
durations.columns = ['duration_int', 'duration_type']
stream = pd.concat([stream, durations], axis=1)
stream.drop(['duration'], axis=1, inplace=True)

'''
Verificamos si la columna 'duration_int' tiene valores nulos y lo reemplzamos con cero
'''
stream["duration_int"].isnull().sum()
stream["duration_int"].fillna(0, inplace=True)
stream["duration_int"] = stream["duration_int"].astype(int)

'''
Normalizamos la columna 'duration_type' para que todo sean en singular
'''
stream["duration_type"] = stream["duration_type"].replace('seasons','season',regex=True)

'''
Y por ultimo exportamos todo el trabajo en un archivo CSV
'''
stream.to_csv('./src/stream.csv', index=False, sep=',', encoding='utf-8')
