class Persona:
    # Constructor de la clase
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    # Método de la clase
    def saludar(self):
        return f"Hola, mi nombre es {self.nombre} y tengo {self.edad} años."

class Empleado(Persona):
    def __init__(self, nombre, edad, salario):
        super().__init__(nombre, edad)  # Llamar al constructor de la superclase
        self.salario = salario

    def mostrar_salario(self):
        return f"Mi salario es {self.salario}."

class CuentaBancaria:
    def __init__(self, titular, saldo):
        self.titular = titular
        self.__saldo = saldo  # Atributo privado

    def depositar(self, cantidad):
        self.__saldo += cantidad

    def retirar(self, cantidad):
        if cantidad <= self.__saldo:
            self.__saldo -= cantidad
        else:
            print("Saldo insuficiente")

    def mostrar_saldo(self):
        return f"El saldo de {self.titular.nombre} es {self.__saldo}"


# Crear una instancia de la clase Persona
persona1 = Persona("Abel", 24)

# Crear una instancia de la clase Empleado
empleado1 = Empleado("Ana", 28, 50000)
print(empleado1.saludar())  # Heredado de Persona
print(empleado1.mostrar_salario())  # Método de Empleado

# Crear una instancia de la clase CuentaBancaria
cuenta = CuentaBancaria(persona1, 10000)
cuenta.depositar(500)
cuenta.retirar(200)
print(cuenta.mostrar_saldo())

class Animal:
    def hacer_sonido(self):
        pass

class Perro(Animal):
    def hacer_sonido(self):
        return "Guau"

class Gato(Animal):
    def hacer_sonido(self):
        return "Miau"

# Usar polimorfismo
animales = [Perro(), Gato()]

for animal in animales:
    print(animal.hacer_sonido())
