import requests

username = 'AbelJRU16'
url = f'https://api.github.com/users/{username}'

response = requests.get(url)
data = response.json()

if response.status_code == 200:
    print(data)
    print(f"Usuario: {data['login']}")
    print(f"Nombre: {data['name']}")
    print(f"Ubicación: {data['location']}")
    print(f"Repositorios públicos: {data['public_repos']}")
else:
    print("Error al obtener la información del usuario.")
