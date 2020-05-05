"""
from pprint import pprint
from octopus import Octopus


def create_request(urls):
    data = []

    otto = Octopus(
           concurrency=4, auto_start=True, cache=True, expiration_in_seconds=10
    )

    def handle_url_response(url, response):
        if "Not found" == response.text:
            print ("URL Not Found: %s" % url)
        else:
            data.append(response.text)


    for url in urls:
        otto.enqueue(url, handle_url_response)

    otto.wait()

    json_data = json.JSONEncoder(indent=None,).encode(data)

    return pprint(json_data)


print(create_request(['http://www.mocky.io/v2/5eae014f2f000058001988d6']))
"""

import urllib.request, json


url = "http://www.mocky.io/v2/5eae014f2f000058001988d6"

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
