import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Cargar datos
data = pd.read_csv('Automobile_data.csv')
print('Datos cargados:')
print(data.head()) ## Muestra las primeras filas del DataFrame

plt.figure()
sns.heatmap(data.isnull(), cbar=False)
plt.title('Mapa de calor de valores nulos')
plt.show()