"""
Ejercicio 3: Utiliza urllib para rehacer el ejercicio anterior de modo que
(1) reciba el documento de una URL, (2) muestre hasta 3000 caracteres,
y (3) cuente la cantidad total de caracteres en el documento. No te
preocupes de las cabeceras en este ejercicio, simplemente muesta los
primeros 3000 caracteres del contenido del documento.
"""

import urllib.request
import urllib.parse
import urllib.error
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
        except ValueError as e:
            print("Ha ocurrido un error:",e)

    return url

def getHtml(url):
    # Realizar la solicitud
    html = ""
    try:
        with urllib.request.urlopen(url) as response:
            # Leer el contenido de la respuesta
            html = response.read().decode('utf-8')
    except urllib.error.URLError as e:
        print(f'Error al realizar la solicitud: {e.reason}')

    return html

def main():
    url = getUrl()
    html = getHtml(url)
    print(html[:3000])

    print("\n\nCaracteres totales:", len(html))

main()
