fhand = open('file.txt', 'r') #get the file
content = fhand.read()        #read the file
print(content)

lines = fhand.readlines()
for line in lines:
    print(line, end='')

fhand.close()

with open('file.txt', 'r') as file:
    content = file.read()
    print(content)

#reading csv
import csv

with open('file.csv', 'r') as archivo_csv:
    lector = csv.reader(archivo_csv)
    for fila in lector:
        print(fila)

#reading json
import json

with open('file.json', 'r') as archivo_json:
    datos = json.load(archivo_json)
    print(datos)

#Error Handling
try:
    with open('file.txt', 'r') as archivo:
        contenido = archivo.read()
        print(contenido)
except FileNotFoundError:
    print("El archivo no fue encontrado.")
except IOError:
    print("Ocurrió un error al leer el archivo.")

#
