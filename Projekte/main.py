#Task list application

#Glabal variables
projekt_name = "Aplicacion - Lista de tareas por hacer";
option_one = "Opcion #1: Crear una tarea"
option_two = "Opcion #2: Editar una tarea"
option_three = "Opcion #3: Eliminar una tarea"
option_fouth = "Opcion #4: Ver las tareas"
option_fifth = "Opcion #5: salir"

tasks = []

#Functions
def init():
    menu()

def getDataInt(text, error):
    data = ""
    while data == "":
        try:
            data = int(input(text))
        except:
            data = ""
            print(error)
    return data

def getData(name):
    data = ""
    while data == "":
        try:
            data = input(f"{name}: ")
        except:
            data = ""
            print(f'{name} Deberia ser un texto')
    return data

def getId():
    if(len(tasks) == 0):
        return 1
    else:
        return (tasks[len(tasks) - 1]['id'] + 1)

def getTaskById(id):
    index = 0
    for task in tasks:
        if(task['id'] == id):
            break
        else:
            index = index + 1
    return index

def makeDescription(task):
    return f'Tarea #{task['id']}: Nombre: {task['name']} - Fecha: {task['date']} - Estado: {task['status']}'

def createTask():
    print()
    newTask = dict()
    newTask['id'] = getId()
    newTask['name'] = input("Ingrese el nombre de la tarea: ")
    newTask['date'] = input("Ingrese la fecha de la tarea: ")
    newTask['status'] = input("Ingrese el estado la tarea: ")
    newTask['description'] = makeDescription(newTask)
    tasks.append(newTask)
    print("Tarea creada exitosamente...")

def showAllTask():
    if(len(tasks) == 0):
        print("\nNo hay Tareas para mostrar")
    else:
        print()
        for task in tasks:
            print(task['description'])

def updateTask():
    id = 0
    if(len(tasks) == 0):
        print("\nNo hay Tareas para mostrar")
    else:
        showAllTask()
        id = getDataInt("\nSeleccione una Tarea para editar (id): ", "Debe ingresar una opcion valida")
        index = getTaskById(id)
        print("\nTarea seleccionada", tasks[index]['description'])
        tasks[index]['name'] = input("Ingrese el nombre de la tarea: ")
        tasks[index]['date'] = input("Ingrese la fecha de la tarea: ")
        tasks[index]['status'] = input("Ingrese el estado la tarea: ")
        tasks[index]['description'] = makeDescription(tasks[index])
        print("Tarea actualizada exitosamente...")

def deleteTask():
    id = 0
    if(len(tasks) == 0):
        print("\nNo hay Tareas para mostrar")
    else:
        showAllTask()
        id = getDataInt("\nSeleccione una Tarea para eliminar (id): ", "Debe ingresar una opcion valida")
        index = getTaskById(id)
        tasks.pop(index)
        print("\nTarea eliminada exitosamente...")

def menu():
    option = 0
    while True:
        print(
            "\n" +
            projekt_name + "\n" +
            option_one + "\n" +
            option_two + "\n" +
            option_three + "\n" +
            option_fouth + "\n" +
            option_fifth + "\n"
            )
        option = getDataInt('Seleccione una opcion: ', 'Debe ingresar una opcion valida')
        if(option == 1):
            createTask()
        elif(option == 2):
            updateTask()
        elif(option == 3):
            deleteTask()
        elif(option == 4):
            showAllTask()
        elif(option == 5):
            break
        else:
            print("Ingrese una opcion valida")


#Start
menu()
