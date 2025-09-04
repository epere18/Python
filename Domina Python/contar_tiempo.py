import time

def contar_tiempo(function):
    def medir_duracion(*args, **kwargs):
        inicio = time.time()
        resultado = function(*args, **kwargs)
        print("Tiempo (s):", time.time()-inicio)
        return resultado
    return medir_duracion

@contar_tiempo
def crear_diccionario():
    diccionario = {
        "nombre" : "Ana",
        "apellido": "Pérez" 
    }
    time.sleep(2)
    return diccionario

crear_diccionario()