# Trabajando con Ciclo for

for i in range(10):
    print(i)

Marcas_autos = [
    'Audi',
    'Ford',
    'Chevrolet',
    'BMW'
]

for auto in Marcas_autos:
    print(auto)

concesionario = {
    'Audi': ['Audi A1', 'Audi A3'],
    'Chevrolte': 'Onix 1.4',
    'BMW': 'X50',
    'Ford': 'Ford KA'
}

for modelo in concesionario.items():
    print(modelo)

for modelo in concesionario.values():
    print(modelo)

for modelo in concesionario.keys():
    print(modelo)