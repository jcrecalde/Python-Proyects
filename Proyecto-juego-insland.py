print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Bienvenido a Treasure Island.")
print("Tu misión es encontrar el tesoro.")

pregunta1 = input(
    'Estas en una encrucijada, ¿adónde quieres ir? escribe "derecha" o "izquierda".').lower()

if pregunta1 == "izquierda":
    pregunta2 = input(
        'Ahora debes ir hacia una isla, que elijes?. Escribe "esperar" o en "nadar"').lower()
    if pregunta2 == "esperar":
        pregunta3 = input(
            'Ya te encuentras en la isla, ahora debes elejir entre 3 puertas. Una roja, otra amarilla y otra azul ').lower()
        if pregunta3 == "rojo":
            print("Esa puerta contiene fuego, perdiste :( !")
        elif pregunta3 == "yellow":
            print("Felicitaciones, encontraste el tesoro!!! :D")
        elif pregunta3 == "azul":
            print("Esta puerta esta cuidada por un gigante, perdiste!!! :( !")
        else:
            print("Ese color de puerta no existe, perdiste :( !")
    else:
        print("Fuiste atacado por un tiburon, perdiste :(!")
else:
    print("Te caiste en una trampa, perdiste! :(")
