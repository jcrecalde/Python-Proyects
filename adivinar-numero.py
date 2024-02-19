from random import randint

NIVEL_FACIL_TURNOS = 10
NIVEL_DIFICIL_TURNOS = 5


def chequear_respuesta(adivinar, respuesta, turnos):
    """comprueba la respuesta contra la suposición. Devuelve el número de turnos restantes."""
    if adivinar > respuesta:
        print("Muy alto")
        return turnos - 1
    elif adivinar < respuesta:
        print("Muy bajo")
        return turnos - 1
    else:
        print(f"Adivinaste, el numero es {respuesta}")


def dificultad():
    nivel = input("Elije el nivel, entre facil y dificil: ")
    if nivel == "facil":
        return NIVEL_FACIL_TURNOS
    else:
        return NIVEL_DIFICIL_TURNOS


def juego():
    print("Bienvenido al juegos de adivinar numeros")
    print("Piensa un numero entre el 1 y 100")
    numero_buscado = randint(1, 100)
    # print(f"La respuesta correcta es {numero_buscado}")

    turnos = dificultad()

    numero_ingresado = 0
    while numero_ingresado != numero_buscado:
        print(f"Te quedan {turnos} intentos para adivinar el número.")

        numero_ingresado = int(input("Adivina el numero: "))

        turnos = chequear_respuesta(numero_ingresado, numero_buscado, turnos)
        if turnos == 0:
            print("Perdiste!, se te agotaron las oportunidades")
            return
        elif numero_ingresado != numero_ingresado:
            print("Adivina otra vez.")


juego()
