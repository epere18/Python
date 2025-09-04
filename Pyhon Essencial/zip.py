# Trabajando con zip

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

marcas_modelo = list(zip(marcas_autos, modelos_autos))
print(marcas_modelo)

marcas_modelo_unzip, modelos_autos_unzip = zip(*marcas_modelo)
print(marcas_modelo_unzip)
print(modelos_autos_unzip)

for marcas_autos, modelos_autos in zip(marcas_autos, modelos_autos):
    print(marcas_autos,'-', modelos_autos)
