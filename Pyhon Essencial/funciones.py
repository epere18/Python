def saludar(nombre):
    print(f'Hola {nombre}, como estas?')

saludar('Oscar')

def sumar(a,b):
    resultado = a + b
    return resultado

suma = sumar(10,5)
print(f'El resultado de la suma es {suma}')

def ano_nacimiento(edad, ano_actual):
    resultado = ano_actual - edad
    return resultado

anio = ano_nacimiento(41,2025)
print(f'Mi año de nacimiento es {anio}')

def sumar(*args):
    total = 0
    for num in args:
        total += num
    return total

print(sumar(1,2,3))
print(sumar(5,10,15,20))
