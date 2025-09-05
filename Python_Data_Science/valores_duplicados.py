import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Cargar datos
data = pd.read_csv('Automobile_data.csv')
print('Datos cargados:')
print(data.head()) ## Muestra las primeras filas del DataFrame

duplicado = data.duplicated()
print('Valores duplicados en el DataFrame:\n', duplicado)

data1 = data.drop_duplicates()
duplicado1 = data1.duplicated()
print('DataFrame sin valores duplicados:\n', data1)
