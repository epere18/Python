import pandas as pd
import numpy as np

# Cargar datos
data = pd.read_csv('Automobile_data.csv')
print('Datos cargados:')
print(data.head()) ## Muestra las primeras filas del DataFrame
print('Muestra información sobre el DataFrame:')
print(data.info()) ## Muestra información sobre el DataFrame

media = data[['wheel-base', 'length', 'width', 'height', 'compression-ratio']].mean()
print('Media de las columnas seleccionadas:\n', media)

mediana = data[['wheel-base', 'length', 'width', 'height', 'compression-ratio']].median()
print('Mediana de las columnas seleccionadas:\n', mediana)

moda = data[['wheel-base', 'length', 'width', 'height', 'compression-ratio']].mode().iloc[0]
print('Moda de las columnas seleccionadas:\n', moda)

varianza = data[['wheel-base', 'length', 'width', 'height', 'compression-ratio']].var()
print('Varianza de las columnas seleccionadas:\n', varianza)

dev_estand = data[['wheel-base', 'length', 'width', 'height', 'compression-ratio']].std()
print('Desviación Estandar de las columnas seleccionadas:\n', dev_estand)