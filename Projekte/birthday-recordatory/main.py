import json
from datetime import datetime

def load_birthdays():
    try:
        with open('birthdays.json', 'r') as f:
            birthdays = json.load(f)
    except FileNotFoundError:
        birthdays = {}
    return birthdays

def save_birthdays(birthdays):
    with open('birthdays.json', 'w') as f:
        json.dump(birthdays, f)

def add_birthday(name, date, birthdays):
    birthdays[name] = date
    save_birthdays(birthdays)
    print(f"¡Cumpleaños de {name} agregado!")

def check_birthdays(today, birthdays):
    for name, date_str in birthdays.items():
        birth_date = datetime.strptime(date_str, '%Y-%m-%d')
        if (today.month, today.day) == (birth_date.month, birth_date.day):
            print(f"Hoy es el cumpleaños de {name}!")

def main():
    birthdays = load_birthdays()

    while True:
        print("\n--- Menú ---")
        print("1. Agregar cumpleaños")
        print("2. Verificar cumpleaños hoy")
        print("3. Salir")
        choice = input("Seleccione una opción: ")

        if choice == '1':
            name = input("Ingrese el nombre: ")
            date = input("Ingrese la fecha de cumpleaños (YYYY-MM-DD): ")
            add_birthday(name, date, birthdays)

        elif choice == '2':
            today = datetime.now()
            check_birthdays(today, birthdays)

        elif choice == '3':
            print("Saliendo del programa...")
            break

        else:
            print("Opción inválida. Intente nuevamente.")

if __name__ == "__main__":
    main()
