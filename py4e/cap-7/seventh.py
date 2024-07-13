#creating a list
lista_vacia = []
lista_con_elementos = [1, 2, 3, "cuatro", 5.0]

#append
lista = [1, 2, 3]
lista.append(4)
print(lista)  # Output: [1, 2, 3, 4]

#extend
lista = [1, 2, 3]
lista.extend([4, 5])
print(lista)  # Output: [1, 2, 3, 4, 5]

#insert
lista = [1, 2, 3]
lista.insert(1, "nuevo")
print(lista)  # Output: [1, 'nuevo', 2, 3]

#remove
lista = [1, 2, 3, 2, 4]
lista.remove(2)
print(lista)  # Output: [1, 3, 2, 4]

#pop
lista = [1, 2, 3]
ultimo = lista.pop()
print(ultimo)  # Output: 3
print(lista)   # Output: [1, 2]

#sort
lista = [3, 1, 4, 1, 5, 9]
lista.sort()
print(lista)  # Output: [1, 1, 3, 4, 5, 9]
lista.sort(reverse=True)
print(lista)  # Output: [9, 5, 4, 3, 1, 1]

#reverse
lista = [1, 2, 3]
lista.reverse()
print(lista)  # Output: [3, 2, 1]

#in and not ib
lista = [1, 2, 3]
print(2 in lista)     # Output: True
print(4 not in lista) # Output: True

#Concatenación y Repetición
lista1 = [1, 2]
lista2 = [3, 4]
concatenada = lista1 + lista2
repetida = lista1 * 3
print(concatenada)  # Output: [1, 2, 3, 4]
print(repetida)     # Output: [1, 2, 1, 2, 1, 2]

#enumerate#
lista = ['a', 'b', 'c']
for indice, valor in enumerate(lista):
    print(indice, valor)
# Output:
# 0 a
# 1 b
# 2 c

#range fuction
print(range(4))
