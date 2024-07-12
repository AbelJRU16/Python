#Task list application

#Imports
import json
from datetime import datetime

#Glabal variables
projekt_name = "Aplicacion - Lista de tareas por hacer";
option_one = "Opcion #1: Crear una tarea"
option_two = "Opcion #2: Editar una tarea"
option_three = "Opcion #3: Eliminar una tarea"
option_fouth = "Opcion #4: Ver las tareas"
option_fifth = "Opcion #5: salir"

#Functions
def load_tasks():
    try:
        with open('task-list.json', 'r') as f:
            task_list = json.load(f)
    except FileNotFoundError:
        task_list = {"tasks": []}
    return task_list

def getDataInt(text, min=1, max=1000):
    data = 0
    while data == 0 or data<min or data>max:
        try:
            data = int(input(text))
            if(data<min or data>max):
                print("Debe ingresar una opcion valida")
        except:
            print("Debe ingresar una opcion valida")
    return data

def getData(text):
    data = ""
    while data == "":
        try:
            data = input(text)
        except:
            print('Ha ocurrido un error')
    return data

def makeDescription(name, date, status):
    return f'Nombre: {name} - Fecha: {date} - Estado: {status}'

#Updating IDs
def updateIds():
    tasks = load_tasks()
    count = 1
    for task in tasks['tasks']:
        task['id'] = count
        count = count + 1
    save_tasks(tasks)

#creating a new task

def save_tasks(tasks):
    with open('task-list.json', 'w') as f:
        json.dump(tasks, f, indent = 4)

def createTask():
    tasks = load_tasks()

    name     = getData("\nIngrese el nombre de la tarea: ")
    date     = getData("Ingrese la fecha de la tarea (YYYY-MM-DD): ")
    status   = getData("Ingrese el estado de la tarea: ")
    new_task = {
        "id"          : len(tasks["tasks"]) + 1,
        "name"        : name,
        "date"        : date,
        "status"      : status,
        "description" : makeDescription(name, date, status),
    }

    tasks["tasks"].append(new_task)
    save_tasks(tasks)

    print("\nTarea creada exitosamente...")

def showAllTask():
    tasks = load_tasks()
    if(len(tasks) == 0):
        print("\nNo hay Tareas para mostrar")
    else:
        print()
        for task in tasks['tasks']:
            print(f'Tarea #{task['id']} - {task['description']}')

def updateTask():
    tasks = load_tasks()
    task_id = 0

    if(len(tasks) == 0):
        print("\nNo hay Tareas para mostrar")
    else:
        showAllTask()
        task_id = getDataInt("\nSeleccione una Tarea para editar (id): ", 1, len(tasks["tasks"]))
        for task in tasks["tasks"]:
            if task["id"] == task_id:
                print("\nTarea seleccionada", task['description'])
                task['name'] = input("\nIngrese el nombre de la tarea: ")
                task['date'] = input("Ingrese la fecha de la tarea (YYYY-MM-DD): ")
                task['status'] = input("Ingrese el estado de la tarea: ")
                task['description'] = makeDescription(task['name'], task['date'], task['status'])

        save_tasks(tasks)
        print("\nTarea actualizada exitosamente...")

def deleteTask():
    tasks = load_tasks()
    task_id = 0

    if(len(tasks) == 0):
        print("\nNo hay Tareas para mostrar")
    else:
        showAllTask()
        task_id = getDataInt("\nSeleccione una Tarea para eliminar (id): ", 1, len(tasks["tasks"]))
        for task in tasks["tasks"]:
            if task["id"] == task_id:
                tasks["tasks"].remove(task)

        save_tasks(tasks)
        print("\nTarea eliminada exitosamente...")

    updateIds()

def main():
    tasks = load_tasks()['tasks']

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
        option = getDataInt('Seleccione una opcion: ', 1, 5)
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

if __name__ == "__main__":
    main()
