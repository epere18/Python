import shutil

def mover_archivo(ubicacion_actual, ubicacion_nueva):
    try:
        shutil.move(ubicacion_actual, ubicacion_nueva)
    except Exception as e:
        print(e)

mover_archivo(r"Consorcios.jpeg", r"Domina Python\Consorcios.jpeg")