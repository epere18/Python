import os

def borrar_archivo(ruta_archivo):
    try:
        os.remove(ruta_archivo)
    except Exception as e:
        print(e)

borrar_archivo("Domina Python/archivo.txt")
