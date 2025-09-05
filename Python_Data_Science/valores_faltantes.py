import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Cargar datos
data = pd.read_csv('Automobile_data.csv')
print('Datos cargados:')
print(data.head()) ## Muestra las primeras filas del DataFrame

valores_faltantes = data.isnull().sum()
print('Cantidad de valores faltantes por columna: \n', valores_faltantes)

total_valores_faltantes = valores_faltantes.sum()
print('Total de valores faltantes en el DataFrame:\n', total_valores_faltantes)

columnas_numericas = data.select_dtypes(include=[np.number]).columns
media_columns = data[columnas_numericas].mean()
print('Media de las columnas numericas:\n', media_columns)

