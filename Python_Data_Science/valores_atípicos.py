import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Cargar datos
data = pd.read_csv('Automobile_data.csv')
print('Datos cargados:')
print(data.head()) ## Muestra las primeras filas del DataFrame

columnas_num = data[['wheel-base', 'length', 'width', 'height', 'compression-ratio']]

Q1 = columnas_num.quantile(0.25)
Q3 = columnas_num.quantile(0.75)
IQR = Q3 - Q1

umbral = 1.5
for col in columnas_num.columns:
    valor_bajo = Q1[col] - umbral * IQR[col]
    valor_alto = Q3[col] + umbral * IQR[col]
    atipico = (
        columnas_num[(columnas_num[col] < valor_bajo) | 
        (columnas_num[col] > valor_alto)]
        ) & columnas_num.notnull()
    
    if columnas_num[atipico][col].any():
        print(f'Valores atípicos en la columna {col}:')
        print(columnas_num[atipico][col])
