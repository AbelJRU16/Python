#function
def thing():
    print("Hello")
    print("Fun")

#getData function
def getData(name):
    data = ""
    while data == "":
        try:
            data = int(input(f"{name}: "))
        except:
            data = ""
            print(f'{name} should be a number')
    return data

# print(f"Age: {getData("Age")}")

print(max("Hello World"))
#print(min("Hello World"))

#Defining a function
def print_lyrics():
    print("I'm a lumberjack, and I'm okay.")
    print("I sleep all night and I work all day.")

#Invoking a function
print_lyrics()

#greet function
def greet(lang):
    greetment = ""
    if lang == 'es':
        greetment = "Hola"
    elif lang == 'fr':
        greetment = "Bonjour"
    elif lang == 'de':
        greetment = "Hallo"
    else:
        greetment = "Hello"

    return greetment

print(f"{greet('de')} Abel")
