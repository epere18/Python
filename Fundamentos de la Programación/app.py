#Primer Ejerecicio
valor = input('ingrese su edad: ')
print('Ahora calcularemos su año de nacimiento')
año = input('ingrese el año actual: ')
print(f'Usted ingreso que su edad es: {valor}')
valor_int = int(valor)
año_int = int(año)
print(f'Su año de nacimiento es: {año_int - valor_int}')

# Segundo ejercicio

primer_nombre = 'oscar'
primer_apellido = 'perez'
nota = 'El mejor jugador del mundo es: ????'

primer_nombre_cap = primer_nombre.capitalize()
primer_apellido_cap = primer_apellido.capitalize()
ubicacion_carater = nota.find('mejor')
texto = nota[9:11]

print(primer_nombre_cap)
print(primer_apellido_cap)
print(ubicacion_carater)
print(texto)