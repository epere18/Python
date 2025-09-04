import importlib

def validar_modulo(ruta_modulo):
    try:
        modulo = importlib.import_module(ruta_modulo)
        print(f"El modulo {ruta_modulo} si existe")
        return modulo
    except ModuleNotFoundError:
        print(f"El modulo {ruta_modulo} no existe")
        return


def invocar_function(ruta_modulo, nombre_function, *args, **kwargs):
    modulo = validar_modulo(ruta_modulo)
    if nombre_function not in dir(modulo):
        print("La funcion no existe en el modulo")
        return
    
    funcion = getattr(modulo, nombre_function)
    if not hasattr(funcion, "_call_"):
        print("No es posible invocar la funcion")
        return
    
    funcion(*args, **kwargs)

    return

ruta_modulo = "leer_google_sheets"
nombre_function = "leer_sheet_publica"
invocar_function(ruta_modulo, nombre_function)