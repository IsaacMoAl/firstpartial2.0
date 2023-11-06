import random


def pedir_numero():
    try:
        herramienta = int(input())
        boolean = 1
    except ValueError:
        boolean = 0
        herramienta = 1000000
        print("Jaja, eso no es un numero")
    return herramienta, boolean

print("Caja de herramientas de [tu nombre]")
print("Dile adios al Syntax Error!")
print("Que deseas hacer?")
print("0 - Imprimir una variable")
print("1 - Pedirle algo al usuario")
print("2 - Crear un condicional")
print("3 - Crear un ciclo while")
print("4 - Crear un ciclo for")
print("5 - Crear una lista")
print("6 - Divertirme")

boolean = 0
while boolean == 0:
    herramienta, boolean=pedir_numero()

while herramienta not in list(range(7)):
    print("Escribe un numero valido.")
    print(list(range(7)))
    herramienta, boolean=pedir_numero()
    while boolean == 0:
        herramienta, boolean=pedir_numero()

if herramienta == 0:
    print("Usa la función:")
    print("    print()")
    print("Dentro del paréntesis puedes poner ya sea un texto que quieras entre comillas (dobles o simples funciona bien) o una variable, yeii")
    print("Ejemplos:")
    print("    print('Que ondiux')")
    print("    print('Elegiste el número',numero)")
elif herramienta == 1:
    print("Usa la función:")
    print("    input()")
    print("Dentro del paréntesis puedes poner un texto indicando al usuario que debe de escribir, yeii")
    print("OJO: para usar el dato hay que meterlo dentro de una variable, y no olvides convertirlo al tipo de dato adecuado, awesome!")
    print("Los tipos de datos son número entero int(), número decimal float() y texto str()")
    print("Ejemplos:")
    print("    numero_entero = int(input())")
    print("    numero_decimal = float(input())")
    print("    texto = str(input())")

elif herramienta == 2:
  print("First you need to make clear your variable")
  print("Put the name of your variable that will be given by the user")
  print("Then it depends if its a word you will put: X = input("")")
  print("And if it is a number put: X = int/float(this one for decimal numbers)(input(""))")
  print("With the variable done you will give conditions and posible endings to them")
  print("You will start with if + the variable + the condition (==/<=/!=) + the number or word that you want + :")
  print("To make more posible answers use elif with the same structure of the if")
  print("You can do them more specific")
  print("useing and/or")
  print("Or is used to say the program that chose into different options")
  print("And is used to include other specific condition")
elif herramienta == 3:
  print("First you have to determinated a variable. an put it = 0")
  print("Down you need to put ""while""the vairable""and the number as a limit")
  print("Then you need to add 1 to the vairable x += 1")
  print("And now the condition you put if + variable + the condition you need (==3)")
  print("For the end you need to put continue and down print(the variable)")

elif herramienta == 4:
  print("First make a list with the things you want (Explanation number 5)")
  print("Then in the second line you put ""for x in""and then you write the name of the list")
  print("For being a loop you have to chose a item to become true")
  print("write""if x =="" + the thing you want to be true and two points :")
  print("Down you must put continue")
  print("And last a print(x)")

elif herramienta == 5:
  print("To make a list: first name your list, my suggest put like 3 letters (L.of.T)")
  print("Next you must put a signal equal (=) adn put this things [] (L.of.T=[])")
  print("After, you put the things that you want in this ones (""), and coma after that")
  print("("", "")")
  print("And final, you put print("") with the name of your list on it. :D ")

elif herramienta == 6:
    aleatorio = random.randint(1,3)
    if aleatorio == 1:
        print("Las variables tipo float se llaman así porque en los decimales el punto flota, ja, que gracioso, no?")
    elif aleatorio == 2:
        print("Sabías que las computadoras no entienden las letras ni las palabras, solo entienden 0 y 1, imaginate hablar así, 000111000 jajaja que gracioso.")
    elif aleatorio == 3:
        print("Python tiene además de las listas, unas cosas llamadas tuplas, la única diferencia es que ocupan menos espacio en la memoria, jaja, que manera tan rara de ahorrar")
