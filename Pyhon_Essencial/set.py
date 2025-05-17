# Trabajando con sets

repuestos_autos = {'Paragolpes','Faros','Parrilla'}
repuestos_autos.add('Llanta')
repuestos_autos.add('Calandra')
repuestos_autos.add('Faros de Niebla')

print(repuestos_autos)

repuestos_autos.discard('Faros de Niebla')
print(repuestos_autos)
print(len(repuestos_autos))