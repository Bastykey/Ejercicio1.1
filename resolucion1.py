import csv
import json

def clasificarEmpresa(ventas):
    if ventas < 100000000:
        return 'Pequenio contribuyente'
    elif 100000001 <= ventas <= 200000000:
        return 'Mediano contribuyente'
    else:
        return 'Gran Contribuyente'


empresas = []
with open('listadoRutEmpresa.csv', mode='r') as archivo:
    reader = csv.reader(archivo) # DictReader Para diccionarios | reader para filas/matrices
    header = next(reader)
    for fila in reader:
        rut = fila[0]
        nombre = fila[1]
        ventas = int(fila[2])
        clasificacion = clasificarEmpresa(ventas)
        empresas.append([rut, nombre, ventas, clasificacion])

# Estructura json
empresasJson = []
for empresa in empresas:
    empresaData = {
        "rut": empresa[0],
        "nombre": empresa[1],
        "ventas": empresa[2],
        "clasificacionEmpresa": empresa[3]
    }

    empresasJson.append(empresaData)

#Guardar en un archivo
with open('segmentacionEmpresas.json', 'w') as json_file:
    json.dump(empresasJson, json_file, indent=4)

print("Archivo creado con éxito")