import os

def listar_archivos(ruta):
    lista_archivo = os.listdir(ruta)
    return lista_archivo

ruta_absoluta = os.getcwd()
ruta_relativa = "Domina Python"
archivos = listar_archivos(ruta_relativa)
archivos2 = listar_archivos(ruta_absoluta)

for archivo in archivos:
    print(archivos)

for archivo1 in archivos2:
    print(archivos2)
    