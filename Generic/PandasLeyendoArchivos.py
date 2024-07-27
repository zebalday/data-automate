import pandas as pd
import numpy as np

""" 

DOCS: https://pandas.pydata.org/docs/reference/api/pandas.read_csv.html#pandas.read_csv
Para leer los diferentes tipos de archivos existen los métodos pandas.read_###
read_csv; read_excel; read_json; read_sql; read_sas, etc. 

"""

# Ruta del archivo
path = "Pandas\covid-vaccination-vs-death_ratio.csv"

# Creamos el DF con read_csv(raw path/path object)
df = pd.read_csv(path)

# df.info() ==> Muestra información útil del DataFrame
print(df.info())

# df.describe() ==> Retorna resumen de las columnas numéricas (std, mean, min, max).
print(df['total_vaccinations'].describe())

# df.head(n) ==> Muestra primeros 5 registros por defecto. Puede especificarse otro número.
print(df.head())

# df.tail() ==> Muestra últimos 5 registros
print(df.tail())

# df.loc['id','column'] ==> Muestra registros por id y columna. Puede ser por entero o por etiqueta.
print(df.loc[1:5,'country'])

# df.iloc[] ==> Puramente basado en números.
print(df.loc[0:10])

# df['column'].value_counts() ==> Cuenta las repeticiones de los valores.
print(df['country'].value_counts())

# df.groupby('value')['column'].sum() ==> Suma todos valores de la columna selecionada, agrupados por la columna
# especificada en la función.
print(df.groupby('country')['New_deaths'].sum())

""" 

Ahora ocuparemos funciones del módulo Pandas para hacer operaciones en sobre 
el Dataframe. 
DOCS: https://pandas.pydata.org/docs/reference/general_functions.html#data-manipulations

"""
# df.drop() ==> Permite eliminar Columnas O registros, PERO NO AMBOS A LA VEZ!!

# Eliminando columnas
print(df.drop(columns=['iso_code','ratio', 'population','country']))

# Eliminando registros por index
print(df.drop(df.index[[0,20]]))





