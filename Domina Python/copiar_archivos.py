import shutil

def copiar_archivo(ubicacion_actual, ubicacion_nueva):
    try: 
        shutil.copy(ubicacion_actual, ubicacion_nueva)
    except Exception as e:
        print(e)

copiar_archivo("Domina Python/Consorcios.jpeg", "Consorcios.jpeg")