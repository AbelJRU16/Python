"""
Ejercicio 1: Cambia el programa del socket socket1.py para que le pida al
usuario la URL, de modo que pueda leer cualquier página web. Puedes
usar split('/') para dividir la URL en las partes que la componen, de
modo que puedas extraer el nombre del host para la llamada a connect
del socket. Añade comprobación de errores utilizando try y except para
contemplar la posibilidad de que el usuario introduzca una URL mal
formada o inexistente.
"""

import socket
import re

url_regex = re.compile(
    r'^(?:http|ftp)s?://'  # http:// or https://
    r'(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+(?:[A-Z]{2,6}\.?|[A-Z0-9-]{2,}\.?)|'  # domain...
    r'localhost|'  # localhost...
    r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}|'  # ...or ipv4
    r'\[?[A-F0-9]*:[A-F0-9:]+\]?)'  # ...or ipv6
    r'(?::\d+)?'  # optional port
    r'(?:/?|[/?]\S+)$', re.IGNORECASE)

# Función para validar una URL
def is_valid_url(url):
    if re.match(url_regex, url):
        return True
    else:
        return False

def getUrl():
    url = ""
    while True:
        try:
            url = input("Ingresa la url: ")
            if is_valid_url(url): break
            else: print("Ingrese una opcion valida")
        except e:
            print("Ha ocurrido un error:",e)

    return url

def connect(url):
    host = url.split('/')[2]
    misock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    misock.connect((host, 80))
    cmd = f'GET {url} HTTP/1.0\r\n\r\n'.encode()
    misock.send(cmd)
    return misock

def main():
    url = getUrl()
    misock = connect(url)
    data = ""
    while True:
        datos = misock.recv(1024)
        if len(datos) < 1: break
        data = data + datos.decode()
        print(data[:400],end='')

    print("\n\nCaracteres totales:", len(data))
    misock.close()

main()
