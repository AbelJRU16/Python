tupla = (1, 2, 3)
tupla_sin_parentesis = 1, 2, 3

print(tupla[0])  # 1
print(tupla[1])  # 2

print(len(tupla))  # 3

print(tupla.count(2))  # 1

print(tupla.index(3))  # 2

a, b, c = tupla
print(a)  # 1
print(b)  # 2
print(c)  # 3

def coordenadas():
    return (10, 20)

x, y = coordenadas()
print(x)  # 10
print(y)  # 20

tupla1 = (1, 2)
tupla2 = (3, 4)
tupla_concatenada = tupla1 + tupla2
print(tupla_concatenada)  # (1, 2, 3, 4)

tupla_repetida = tupla1 * 3
print(tupla_repetida)  # (1, 2, 1, 2, 1, 2)

# Intentar modificar una tupla dará un error
# tupla[0] = 10  # Error

tupla_anidada = (1, (2, 3), (4, 5))
print(tupla_anidada[1])  # (2, 3)
print(tupla_anidada[1][0])  # 2

lista = [1, 2, 3]
tupla_desde_lista = tuple(lista)
print(tupla_desde_lista)  # (1, 2, 3)

lista_desde_tupla = list(tupla)
print(lista_desde_tupla)  # [1, 2, 3]

diccionario = {(1, 2): "par 1", (3, 4): "par 2"}
print(diccionario[(1, 2)])  # "par 1"

for elemento in tupla:
    print(elemento)

print(min(tupla))  # 1
print(max(tupla))  # 3
print(sum(tupla))  # 6

tupla = (1, 2, 3, 4)
a, *b, c = tupla
print(a)  # 1
print(b)  # [2, 3]
print(c)  # 4
