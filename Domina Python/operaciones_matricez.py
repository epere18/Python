import numpy as np

matriz_a = np.array([[1,2], [3,4]])
matriz_b = np.array([[1,2], [3,4]])

suma = np.add(matriz_a, matriz_b)
print(suma)
print("---------------------------------")

resta = np.subtract(matriz_a, matriz_b)
print(resta)
print("---------------------------------")

multiplica = matriz_a.dot(matriz_b)
print(multiplica)

