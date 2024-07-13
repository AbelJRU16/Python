#creating a dictionary
diccionario_vacio = {}
diccionario_con_elementos = {"clave1": "valor1", "clave2": "valor2"}

#accesing values
diccionario = {"clave1": "valor1", "clave2": "valor2"}
print(diccionario["clave1"])  # Output: valor1

#adding und updating elements
diccionario = {"clave1": "valor1"}
diccionario["clave2"] = "valor2"
diccionario["clave1"] = "nuevo_valor1"
print(diccionario)  # Output: {'clave1': 'nuevo_valor1', 'clave2': 'valor2'}

#deleting eleements
diccionario = {"clave1": "valor1", "clave2": "valor2"}
del diccionario["clave1"]
print(diccionario)  # Output: {'clave2': 'valor2'}

#keys
diccionario = {"clave1": "valor1", "clave2": "valor2"}
print(diccionario.keys())  # Output: dict_keys(['clave1', 'clave2'])

#values
diccionario = {"clave1": "valor1", "clave2": "valor2"}
print(diccionario.values())  # Output: dict_values(['valor1', 'valor2'])

#items
diccionario = {"clave1": "valor1", "clave2": "valor2"}
print(diccionario.items())  # Output: dict_items([('clave1', 'valor1'), ('clave2', 'valor2')])

#pop
diccionario = {"clave1": "valor1"}
valor = diccionario.pop("clave1")
print(valor)           # Output: valor1
print(diccionario)     # Output: {}

#update
diccionario = {"clave1": "valor1"}
diccionario.update({"clave2": "valor2", "clave1": "nuevo_valor1"})
print(diccionario)  # Output: {'clave1': 'nuevo_valor1', 'clave2': 'valor2'}

#itering
diccionario = {"clave1": "valor1", "clave2": "valor2"}
for clave, valor in diccionario.items():
    print(clave, valor)
# Output:
# clave1 valor1
# clave2 valor2

#error handling
diccionario = {"clave1": "valor1"}
try:
    valor = diccionario["clave2"]
except KeyError:
    print("La clave no existe.")

#Nested Dictionaries
diccionario = {
    "clave1": {"subclave1": "subvalor1"},
    "clave2": {"subclave2": "subvalor2"}
}
print(diccionario["clave1"]["subclave1"])  # Output: subvalor1
