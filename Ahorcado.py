""" Ahorcado """

import random
from replit import clear

stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

logo = ''' 
 _                                             
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |                      
                   |___/    '''

print(logo)

palabras = ["pelota", "automovil", "casa", "camino", "playa", "futbol", "juego", "auto", "bardo", "bandera", "argentina"
            "arbol", "cama", "perro", "gato"]

vidas = 6

palabra_elejida = random.choice(palabras)
# print(f"La palabra elejida es: {palabra_elejida}")

pantalla = []
longitud_palabra = len(palabra_elejida)
for _ in range(longitud_palabra):
    pantalla += "_"

final_juego = False
while not final_juego:
    letra_ingresada = input("Adivine una letra: ").lower()

    clear()

    if letra_ingresada in pantalla:
        print(f"Ya has adivinado esa letra{letra_ingresada}")

    for posicion in range(longitud_palabra):
        letra = palabra_elejida[posicion]
        if letra == letra_ingresada:
            pantalla[posicion] = letra

    if letra_ingresada not in palabra_elejida:
        print("La letra ingresada no se encuentra. Se resta una vida")
        vidas -= 1
        if vidas == 0:
            final_juego = True
            print("Perdiste!")

    print(stages[vidas])
    print(f"{''.join(pantalla)}")

    if "_" not in pantalla:
        final_juego = True
        print("Ganaste!")
