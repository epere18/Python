archivoN = open('valores.txt','rt')
archivosS = open('valores_totales.txt','wt')
print('Procesando valores...')
suma = 0
for linea in archivoN:
    suma += int(linea)
    print(linea.rstrip(), file=archivosS)
print('\nTotal: ' + str(suma), file=archivosS)
archivosS.close()
print('Salida Completa!')
