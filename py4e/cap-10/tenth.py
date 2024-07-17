import re

texto = "Hola mundo"
patron = r"Hola"
resultado = re.match(patron, texto)
if resultado:
    print("Se encontró una coincidencia al principio de la cadena")

texto = "Hola mundo"
patron = r"mundo"
resultado = re.search(patron, texto)
if resultado:
    print("Se encontró una coincidencia en cualquier parte de la cadena")

texto = "Hola mundo, hola universo"
patron = r"hola"
resultados = re.findall(patron, texto, re.IGNORECASE)
print(resultados)  # ['Hola', 'hola']

texto = "Hola mundo, hola universo"
patron = r"hola"
resultados = re.finditer(patron, texto, re.IGNORECASE)
for match in resultados:
    print(match.group())

texto = "Hola mundo, hola universo"
patron = r"hola"
nuevo_texto = re.sub(patron, "adiós", texto, flags=re.IGNORECASE)
print(nuevo_texto)  # Adiós mundo, adiós universo

texto = "uno,dos;tres:cuatro"
patron = r"[,:;]"
partes = re.split(patron, texto)
print(partes)  # ['uno', 'dos', 'tres', 'cuatro']

#.: Coincide con cualquier carácter excepto una nueva línea.
#^: Coincide con el comienzo de la cadena.
#$: Coincide con el final de la cadena.
#*: Coincide con cero o más repeticiones del patrón anterior.
#+: Coincide con una o más repeticiones del patrón anterior.
#?: Coincide con cero o una repetición del patrón anterior.
#{n}: Coincide con exactamente n repeticiones del patrón anterior.
#{n,m}: Coincide con entre n y m repeticiones del patrón anterior.
#[]: Coincide con cualquier carácter dentro de los corchetes.
#|: Actúa como un operador OR.
#(): Agrupa patrones y guarda la coincidencia.

email = "ejemplo@dominio.com"
patron = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
if re.match(patron, email):
    print("Correo electrónico válido")
else:
    print("Correo electrónico no válido")

texto = "Hay 12 manzanas y 24 naranjas."
numeros = re.findall(r'\d+', texto)
print(numeros)  # ['12', '24']

texto = "Este    es   un   texto  con   muchos  espacios."
nuevo_texto = re.sub(r'\s+', ' ', texto)
print(nuevo_texto)  # Este es un texto con muchos espacios.

texto = "uno,dos;tres:cuatro"
patron = r"[,:;]"
partes = re.split(patron, texto)
print(partes)  # ['uno', 'dos', 'tres', 'cuatro']

#Flags (Banderas)
#re.IGNORECASE (o re.I): Ignora mayúsculas y minúsculas.
#re.MULTILINE (o re.M): Permite que ^ y $ coincidan al principio y al final de cada línea.
#re.DOTALL (o re.S): Permite que . coincida con cualquier carácter, incluyendo nuevas líneas.

#Compilación de Expresiones Regulares
#Para mejorar el rendimiento cuando se usan muchas veces la misma expresión regular, puedes compilar la expresión con re.compile().
patron = re.compile(r"\d+")
texto = "Hay 12 manzanas y 24 naranjas."
resultados = patron.findall(texto)
print(resultados)  # ['12', '24']

import re

# Cadena de texto a parsear
texto = "Nombre: Juan Pérez, Edad: 30, Correo: juan.perez@example.com; Nombre: Ana López, Edad: 25, Correo: ana.lopez@example.com; Nombre: Carlos Díaz, Edad: 35, Correo: carlos.diaz@example.com"

# Expresión regular para extraer nombre, edad y correo
patron = re.compile(r"Nombre: ([\w\s]+), Edad: (\d+), Correo: ([\w\.-]+@[\w\.-]+)")

# Buscar todas las coincidencias en el texto
coincidencias = patron.findall(texto)

# Imprimir los resultados
for coincidencia in coincidencias:
    nombre, edad, correo = coincidencia
    print(f"Nombre: {nombre}, Edad: {edad}, Correo: {correo}")
