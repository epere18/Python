# Trabajando con enumerate

marcas_autos = [
    'Audi',
    'Ford',
    'Chevrolet',
    'BMW'
]

modelos_autos = [
    'Audi A1',
    'Ford KA',
    'Onix',
    'X50'
]

marcas_enumeradas = list(enumerate(marcas_autos))
print(marcas_enumeradas)

modelos_enumarados = list(enumerate(modelos_autos))
print(modelos_enumarados)

for indice, marcas_enumeradas in enumerate(marcas_autos):
    print(indice,'--', marcas_enumeradas)