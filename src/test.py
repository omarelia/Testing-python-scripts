import urllib.request, json
import settings
import os

url = os.getenv("URL_DATA")

response = urllib.request.urlopen(url)

data = json.loads(response.read())

total_sueldos = 0

nombre_persona = []
sueldo_persona = []

meses = ['enero', 'febrero', 'marzo', 'abril', 'mayo']
sueldos_mensuales = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

for archivo in data['archivos']:
    print('Nombre: ', archivo['nombre'])
    print('Mes: ', archivo['mes'])
    print('Sueldo: ', archivo['sueldo'])
    print('')

    total_sueldos += int(archivo['sueldo'])
    sueldos_mensuales[meses.index(archivo['mes'])] += int(archivo['sueldo'])

    if archivo['nombre'] not in nombre_persona:
        nombre_persona.append(archivo['nombre'])
        sueldo_persona.append(int(archivo['sueldo']))
    else:
        sueldo_persona[nombre_persona.index(archivo['nombre'])] += int(archivo['sueldo'])

for nombre in nombre_persona:
    print('Sueldo total de ', nombre, ': ', sueldo_persona[nombre_persona.index(nombre)])    
print('')

for mes in meses:
    print('Sueldos totales del mes de ' + mes +': ', sueldos_mensuales[meses.index(mes)])
print('')

print('Total de sueldos:', total_sueldos)
print('')

sueldo_promedio = total_sueldos / len(archivo)

print('Sueldo promedio:', sueldo_promedio)
print('')
