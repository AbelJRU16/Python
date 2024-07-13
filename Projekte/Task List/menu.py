import inquirer

def accion_opcion1():
    print("Acción para opción 1")

def accion_opcion2():
    print("Acción para opción 2")

def accion_opcion3():
    print("Acción para opción 3")

def salir():
    print("Saliendo...")

opciones = {
    'Opción 1': accion_opcion1,
    'Opción 2': accion_opcion2,
    'Opción 3': accion_opcion3,
    'Salir': salir
}

questions = [
    inquirer.List('opcion',
                  message="Selecciona una opción",
                  choices=['Opción 1', 'Opción 2', 'Opción 3', 'Salir'],
              ),
]

respuesta = inquirer.prompt(questions)
opciones[respuesta['opcion']]()
