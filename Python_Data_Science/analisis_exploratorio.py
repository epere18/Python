##Análisis de datos exploratorios con Python##
import pandas as pd
import numpy as np

# Cargar datos
data = pd.read_csv('Automobile_data.csv')
print('Datos cargados:')
print(data.head()) ## Muestra las primeras filas del DataFrame
print('Muestra la forma del DataFrame:')
print(data.shape) ## Muestra la forma del DataFrame
print('Muestra información sobre el DataFrame:')
print(data.info()) ## Muestra información sobre el DataFrame
print('Muestra estadisticas descriptivas:')
print(data.describe()) ## Muestra estadisticas descriptivas
print('Muestra los nombres de las columnas')
print(data.columns) ## Muestra los nombres de las columnas
print('Muestra los tipos de datos de las columnas:')
print(data.dtypes) ## Muestra los tipos de datos de las columnas
print('Muestra la cantidad de valores nulos por columnas:')
print(data.isnull().sum()) ## Muestra la cantidad de valores nulos por columnas
print('Muestra la cantidad de valores unicos por columna')
print(data.nunique()) ## Muestra la cantidad de valores unicos por columna