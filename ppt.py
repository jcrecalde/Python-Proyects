import random

piedra = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

papel = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

tijera = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
imagenes = [piedra, papel, tijera]

eleccion = int(
    input("¿Que elijes?, Escribe 0 para piedra, 1 para papel y 2 para tijera: "))

if eleccion >= 3 or eleccion < 0:
    print("El numero que ingresaste no corresponde, perdiste!")
else:
    print(imagenes[eleccion])

computadora = random.randint(0, 2)
print("La eleccion de la computadora: ")
print(imagenes[computadora])

if eleccion == 0:
    if computadora == 0:
        print("Empate, el contricante elijio piedra")
    elif computadora == 1:
        print("Perdiste, papel le gana a piedra")
    else:
        print("Ganaste, piedra le gana a tijera")


elif eleccion == 1:
    if computadora == 1:
        print("Empate, el contricante elijio papel")
    elif computadora == 0:
        print("Ganaste, papel le gana a piedra")
    else:
        print("Perdiste, piedra le gana a tijera")

elif eleccion == 2:
    if computadora == 2:
        print("Empate, tu contrincante elijio tijera")
    elif computadora == 1:
        print("Ganaste, tijera le gana a papel")
    else:
        print("Perdiste, piedra le gana a tijera")
