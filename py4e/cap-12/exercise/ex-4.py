"""
Ejercicio 4: Cambia el programa urllinks.py para extraer y contar las
etiquetas de párrafo (p) del documento HTML recuperado y mostrar
el total de párrafos como salida del programa. No muestres el texto de
los párrafos, sólo cuéntalos. Prueba el programa en varias páginas web
pequeñas, y también en otras más grandes.
"""

from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl
import re

url_regex = re.compile(
    r'^(?:http|ftp)s?://'  # http:// or https://
    r'(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+(?:[A-Z]{2,6}\.?|[A-Z0-9-]{2,}\.?)|'  # domain...
    r'localhost|'  # localhost...
    r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}|'  # ...or ipv4
    r'\[?[A-F0-9]*:[A-F0-9:]+\]?)'  # ...or ipv6
    r'(?::\d+)?'  # optional port
    r'(?:/?|[/?]\S+)$', re.IGNORECASE)

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

def getTags(url, tagName):
    # Ignorar errores de certificado SSL
    ctx = ssl.create_default_context()
    ctx.check_hostname = False
    ctx.verify_mode = ssl.CERT_NONE

    html = urlopen(url, context=ctx).read()
    sopa = BeautifulSoup(html, "html.parser")

    etiquetas = sopa(tagName)
    return etiquetas

def main():
    url = getUrl()
    html = getTags(url, 'p')
    #print(html[:3000])

    print("\nEtiquetas totales:", len(html))

main()
