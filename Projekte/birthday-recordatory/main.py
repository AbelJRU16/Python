import json
import inquirer
from datetime import datetime

# Global variables
main_options = [
    inquirer.List('option',
                  message="Selecciona un opcion",
                  choices=[
                        "Opcion #1: Agregar cumpleaños",
                        "Opcion #2: Editar cumpleaños",
                        "Opcion #3: Eliminar cumpleaños",
                        "Opcion #4: Ver todos los cumpleaños",
                        "Opcion #5: Ver proximos cumpleaños",
                        "Opcion #6: Salir",
                    ],
              ),
]

# Functions
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

def load_birthdays():
    try:
        with open('birthdays.json', 'r') as f:
            birthdays = json.load(f)
    except FileNotFoundError:
        birthdays = {"birthdays": []}
    return birthdays

def save_birthdays(birthdays):

    with open('birthdays.json', 'w') as f:
        json.dump(birthdays, f, indent = 4)

def validateDate(date, format="%Y-%m-%d"):
    try:
        datetime.strptime(date, format)
        return True
    except ValueError:
        return False

def getBirthdayAsInquiring():
    birthdays = load_birthdays()
    birthdays_list = [
        inquirer.List('option',
                      message = "Selecciona una tarea",
                      choices = [f'{birthday["id"]}: {birthday["name"]} - {birthday["date"]}' for birthday in birthdays["birthdays"]],
                  ),
    ]
    choice = inquirer.prompt(birthdays_list)["option"]
    return choice.split(":")[0]

def updateIds():
    birthdays = load_birthdays()
    count = 1
    for birthday in birthdays['birthdays']:
        birthday['id'] = count
        count = count + 1
    save_birthdays(birthdays)

#menu functions

def add_birthday():
    birthdays = load_birthdays()
    name = getData("Ingrese el nombre: ")
    date = getData("Ingrese la fecha de cumpleaños (YYYY-MM-DD): ", True)
    new_birthday = {
        "id"          : len(birthdays["birthdays"]) + 1,
        "name"        : name,
        "date"        : date,
    }
    birthdays["birthdays"].append(new_birthday)
    save_birthdays(birthdays)
    print(f"¡Cumpleaños de {name} agregado!")

def edit_birthday():
    birthdays = load_birthdays()
    birthday_id = 0
    if(len(birthdays["birthdays"]) == 0):
        print("No hay cumpleaños para mostrar")
    else:
        birthday_id = int(getBirthdayAsInquiring())
        for birthday in birthdays['birthdays']:
            if birthday["id"] == birthday_id:
                birthday['name'] = getData("Ingrese el nombre: ")
                birthday['date'] = getData("Ingrese la fecha del cumpleaños (YYYY-MM-DD): ", True)
        save_birthdays(birthdays)
        print("Cumpleaños actualizado exitosamente...")

def delete_birthday():
    birthdays = load_birthdays()
    birthday_id = 0
    if(len(birthdays["birthdays"]) == 0):
        print("No hay cumpleaños para mostrar")
    else:
        birthday_id = int(getBirthdayAsInquiring())
        for birthday in birthdays['birthdays']:
            if birthday["id"] == birthday_id:
                birthdays["birthdays"].remove(birthday)
            save_birthdays(birthdays)
        print("Cumpleaños eliminado exitosamente...")
        updateIds()

def view_all_birthdays():
    birthdays = load_birthdays()
    if(len(birthdays["birthdays"]) == 0):
        print("No hay cumpleaños para mostrar")
    else:
        for birthday in birthdays['birthdays']:
            print(f'{birthday['id']}: {birthday['name']} - {birthday['date']}')

def view_next_birthdays():
    birthdays = load_birthdays()
    if(len(birthdays["birthdays"]) == 0):
        print("No hay cumpleaños para mostrar")
    else:
        show = 0;
        actualDate = datetime.now()
        for birthday in birthdays['birthdays']:
            date = datetime.strptime(birthday['date'], "%Y-%m-%d") #Birthday
            checkDate = datetime(actualDate.year, date.month, date.day)
            if checkDate >= actualDate :
                show = 1
                print(f'{birthday['id']}: {birthday['name']} - {birthday['date']}')
        if show == 0:
            print("No hay mas cumpleaños registrados para este año")

def main():
    birthdays = load_birthdays()

    opciones = {
        'Opcion #1: Agregar cumpleaños'       : add_birthday,
        "Opcion #2: Editar cumpleaños"        : edit_birthday,
        "Opcion #3: Eliminar cumpleaños"      : delete_birthday,
        'Opcion #4: Ver todos los cumpleaños' : view_all_birthdays,
        'Opcion #5: Ver proximos cumpleaños'  : view_next_birthdays,
        'Opcion #6: Salir'                    : 6,
    }

    while True:

        print()
        choice = inquirer.prompt(main_options)["option"]
        if(choice == "Opcion #6: Salir"):
            break
        else:
            opciones[f'{choice}']()

if __name__ == "__main__":
    main()
