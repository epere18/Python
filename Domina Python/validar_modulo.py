import importlib

def validar_modulo(ruta_modulo):
    try:
        modulo = importlib.import_module(ruta_modulo)
        print(f"El modulo {ruta_modulo} si existe")
        print(modulo)
    except ModuleNotFoundError:
        print(f"El modulo {ruta_modulo} no existe")

ruta_modulo = "leer_google_sheets"
validar_modulo(ruta_modulo)