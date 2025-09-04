import os

def crear_directorio_vacio(ruta_directorio):
    if not os.path.exists(ruta_directorio):
        try:
            os.mkdir(ruta_directorio)
            print(f"Directorio {ruta_directorio} creado correctamente")
        except OSError as e:
            print(f"No se pudo crear el Directorio: {e}")
    else:
        print(f"El directorio {ruta_directorio} ya existe")

crear_directorio_vacio("directorio_vacio")