import psutil

def recursos_usados():
    nucleo = psutil.cpu_count(logical=False)
    print("Cantidad de nucleos: ", nucleo)

    carga = psutil.getloadavg()
    print("Carga promedio: ", carga)

    uso = psutil.cpu_percent(interval=5, percpu=True)
    print("Porcentaje de uso de la CPU: ", uso)

recursos_usados()

