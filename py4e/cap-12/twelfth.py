import urllib.request
import urllib.parse
import urllib.error

# URL a la que se va a hacer la solicitud
url = 'http://data.pr4e.org/romeo.txt'

# Realizar la solicitud
try:
    with urllib.request.urlopen(url) as response:
        # Leer el contenido de la respuesta
        html = response.read().decode('utf-8')
        print(html)
except urllib.error.URLError as e:
    print(f'Error al realizar la solicitud: {e.reason}')

from urllib.parse import urlparse, parse_qs

# URL para analizar
url = 'http://www.example.com/path?name=John&age=30'

# Parsear la URL
parsed_url = urlparse(url)
print(f'Esquema: {parsed_url.scheme}')
print(f'Host: {parsed_url.netloc}')
print(f'Path: {parsed_url.path}')
print(f'Query: {parsed_url.query}')

# Parsear la cadena de consulta
query_params = parse_qs(parsed_url.query)
print(f'Parámetros de la consulta: {query_params}')

import urllib.error

# URL incorrecta
url = 'http://www.nonexistentwebsite.com'

# Realizar la solicitud y manejar errores
try:
    with urllib.request.urlopen(url) as response:
        html = response.read().decode('utf-8')
        print(html)
except urllib.error.URLError as e:
    print(f'Error al realizar la solicitud: {e.reason}')
except urllib.error.HTTPError as e:
    print(f'Error HTTP: {e.code} - {e.reason}')
