import random
from replit import clear

logo = """
.------.            _     _            _    _            _    
|A_  _ |.          | |   | |          | |  (_)          | |   
|( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
| \  /|K /\  |     | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
|  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   < 
`-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\\
      |  \/ K|                            _/ |                
      `------'                           |__/           
"""

""" Devuelve una carta aleatoria del maso."""


def maso_cartas():
    cartas = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    carta = random.choice(cartas)
    return carta


def calcular_puntaje(cartas):
    """ Tome una lista de tarjetas y devuelva la puntuación calculada a partir de las tarjetas. """
    if sum(cartas) == 21 and len(cartas) == 2:
        return 0

    if 11 in cartas and sum(cartas) > 21:
        cartas.remove(11)
        cartas.append(1)

    return sum(cartas)


def comparar(usuario_puntaje, computadora_puntaje):
    if usuario_puntaje == computadora_puntaje:
        return "Empate"
    elif computadora_puntaje == 0:
        return "Perdiste, el oponente tiene Black Jack"
    elif usuario_puntaje == 0:
        return "Ganaste tienes Black Jack"
    elif usuario_puntaje > 21:
        return "Perdiste!"
    elif computadora_puntaje > 21:
        return "Ganaste!"
    elif usuario_puntaje > computadora_puntaje:
        return "Ganaste!"
    else:
        return "Perdiste!"


def inicio_juego():

    print(logo)

    usuario_cartas = []
    computadora_cartas = []
    game_over = False

    for _ in range(2):
        usuario_cartas.append(maso_cartas())
        computadora_cartas.append(maso_cartas())

    while not game_over:
        usuario_puntaje = calcular_puntaje(usuario_cartas)
        computadora_puntaje = calcular_puntaje(computadora_cartas)
        print(
            f"Tus cartas: {usuario_cartas}, el puntaje es: {usuario_puntaje}")
        print(f"Computadora cartas: {computadora_cartas[0]}")

        if usuario_puntaje == 0 or computadora_puntaje == 0 or usuario_puntaje > 21:
            game_over = True
        else:
            eleccion = input(
                "Ingrese 's' si quieres otra carta, Ingrese 'n' si quiere pasar: ")
            if eleccion == "s":
                usuario_cartas.append(maso_cartas())
            else:
                game_over = True

    while computadora_puntaje != 0 and computadora_puntaje > 17:
        computadora_cartas.append(maso_cartas())
        computadora_puntaje = calcular_puntaje(computadora_cartas)

    print(
        f"Tu mano final es de: {usuario_cartas}, puntaje final: {usuario_puntaje}")
    print(
        f"Mano de la computadora: {computadora_cartas}, puntaje final: {computadora_puntaje}")
    print(comparar(usuario_puntaje, computadora_puntaje))


while input("Quieres jugar otro Black Jack, escriba 's' o 'n': ") == "s":
    clear()
    inicio_juego()
