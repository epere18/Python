import os

def hacer_ping(hostname):
    respuesta = os.system(f"ping {hostname}")
    if respuesta == 0:
        print(f"{hostname} está activo")
    else:
        print(f"{hostname} está inactivo")

hacer_ping("operezseguros.com")