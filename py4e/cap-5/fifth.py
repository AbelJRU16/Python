s = 'Monty Python'
print(s[0:4])  #Mont
print(s[6:7])  #P
print(s[6:20]) #Python
print(s[:2]) #Mo
print(s[8:]) #thon
print(s[:]) #Monty Python

a = 'Hello'
b = a + 'There'
c = a + ' ' + b

fruit = 'Banana'
'n' in fruit #true

print(fruit.lower())

#Uppercase and Lowercase
text = "Hola Mundo"
print(texto.upper())  # Output: "HOLA MUNDO"
print(texto.lower())  # Output: "hola mundo"

#Capitalize
texto = "hola mundo"
print(texto.capitalize())  # Output: "Hola mundo"

#title
texto = "hola mundo"
print(texto.title())  # Output: "Hola Mundo"

#strip
texto = "   hola mundo   "
print(texto.strip())  # Output: "hola mundo"

#replace
texto = "hola mundo"
print(texto.replace("mundo", "Python"))  # Output: "hola Python"

#split
texto = "hola mundo"
print(texto.split())  # Output: ['hola', 'mundo']

#join
lista = ["hola", "mundo"]
print(" ".join(lista))  # Output: "hola mundo"

#find
texto = "hola mundo"
print(texto.find("mundo"))  # Output: 5

#isdigit
texto = "12345"
print(texto.isdigit())  # Output: True

#isalpha
texto = "hola"
print(texto.isalpha())  # Output: True

#isalnum
texto = "hola123"
print(texto.isalnum())  # Output: True

#count
texto = "hola mundo, hola Python"
print(texto.count("hola"))  # Output: 2

#f-strings
nombre = "Juan"
edad = 30
print(f"Me llamo {nombre} y tengo {edad} años")  # Output: "Me llamo Juan y tengo 30 años"

#caracters escaping
texto = "Ella dijo: \"Hola Mundo\""
print(texto)  # Output: Ella dijo: "Hola Mundo"

#Multiline strings
texto = """Esto es
una cadena
multilínea"""
print(texto)
