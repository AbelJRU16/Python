#Task list application

#Imports
import json
import inquirer
from datetime import datetime

#Glabal variables
projekt_name = "Aplicacion - Lista de tareas por hacer";

main_options = [
    inquirer.List('option',
                  message="Selecciona un opcion",
                  choices=[
                        "Opcion #1: Crear una tarea",
                        "Opcion #2: Editar una tarea",
                        "Opcion #3: Eliminar una tarea",
                        "Opcion #4: Ver las tareas",
                        "Opcion #5: salir"
                    ],
              ),
]

questions = [
    inquirer.List('option',
                  message="Selecciona un estado",
                  choices=['Por realizar', 'Iniciado', 'Para despues', 'Completado'],
              ),
]

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

def getData(text, isaDate=False):
    data = ""
    while data == "":
        try:
            data = input(text)
            if isaDate and validateDate(data) == False:
                print('\nIngrese una fecha correcta!\n')
                data = ""
        except:
            print('Ha ocurrido un error')
    return data

def validateDate(date, format="%Y-%m-%d"):
    try:
        datetime.strptime(date, format)
        return True
    except ValueError:
        return False

def makeDescription(name, date, status):
    return f'Nombre: {name} - Fecha: {date} - Estado: {status}'

def getTaskAsInquiring():
    tasks = load_tasks()
    task_list = [
        inquirer.List('option',
                      message = "Selecciona una tarea",
                      choices = [f'{task["id"]}: {task["name"]}' for task in tasks["tasks"]],
                  ),
    ]
    choice = inquirer.prompt(task_list)["option"]
    return choice.split(":")[0]

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

    name     = getData("Ingrese el nombre de la tarea: ")
    date     = getData("Ingrese la fecha de la tarea (YYYY-MM-DD): ", True)
    status   = inquirer.prompt(questions)
    new_task = {
        "id"          : len(tasks["tasks"]) + 1,
        "name"        : name,
        "date"        : date,
        "status"      : status['option'],
        "description" : makeDescription(name, date, status['option']),
    }

    tasks["tasks"].append(new_task)
    save_tasks(tasks)

    print("Tarea creada exitosamente...")

def showAllTask():
    tasks = load_tasks()
    if(len(tasks) == 0):
        print("No hay Tareas para mostrar")
    else:
        for task in tasks['tasks']:
            print(f'Tarea #{task['id']} - {task['description']}')

def updateTask():
    tasks = load_tasks()
    task_id = 0

    if(len(tasks) == 0):
        print("No hay Tareas para mostrar")
    else:
        #showAllTask()
        #task_id = getDataInt("\nSeleccione una Tarea para editar (id): ", 1, len(tasks["tasks"]))
        task_id = int(getTaskAsInquiring())

        for task in tasks["tasks"]:
            if task["id"] == task_id:
                print("Tarea seleccionada", task['description'])
                task['name'] = input("\nIngrese el nombre de la tarea: ")
                task['date'] = getData("Ingrese la fecha de la tarea (YYYY-MM-DD): ", True)
                task['status'] = inquirer.prompt(questions)['option']
                task['description'] = makeDescription(task['name'], task['date'], task['status'])

        save_tasks(tasks)
        print("Tarea actualizada exitosamente...")

def deleteTask():
    tasks = load_tasks()
    task_id = 0

    if(len(tasks) == 0):
        print("No hay Tareas para mostrar")
    else:
        #showAllTask()
        #task_id = getDataInt("\nSeleccione una Tarea para eliminar (id): ", 1, len(tasks["tasks"]))
        task_id = int(getTaskAsInquiring())

        for task in tasks["tasks"]:
            if task["id"] == task_id:
                tasks["tasks"].remove(task)

        save_tasks(tasks)
        print("Tarea eliminada exitosamente...")

    updateIds()

def main():
    tasks = load_tasks()['tasks']

    opciones = {
        'Opcion #1: Crear una tarea'    : createTask,
        'Opcion #2: Editar una tarea'   : updateTask,
        'Opcion #3: Eliminar una tarea' : deleteTask,
        'Opcion #4: Ver las tareas'     : showAllTask,
    }

    option = 0
    while True:
        print()
        option = inquirer.prompt(main_options)["option"]
        if(option == "Opcion #5: salir"):
            break
        else:
            opciones[f'{option}']()

if __name__ == "__main__":
    main()
