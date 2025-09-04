import numpy as np

lista = [1,2,3]
lista_anidada = [[1,2,3], [4,5,6], [7,8,9]]

arreglo = np.array(lista)
print(arreglo)
print("---------------------------------")

matriz = np.array(lista_anidada)
print(matriz)
print("---------------------------------")

matriz1 = np.matrix(lista_anidada)
print(matriz1)
print("---------------------------------")

matriz_ceros = np.zeros(lista)
print(matriz_ceros)

