# Programa de subastas
from replit import clear

logo = '''
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\\
                       .-------------.
                      /_______________\\
'''

ofertas = {}
licitacion_terminada = False


def buscar_mejor_postor(registro_ofertas):
    apuesta_mas_alta = 0
    ganador = ""
    for licitador in registro_ofertas:
        cantidad_oferta = registro_ofertas[licitador]
        if cantidad_oferta > apuesta_mas_alta:
            apuesta_mas_alta = cantidad_oferta
            ganador = licitador
    print(f"El ganador es {ganador} con una oferta de ${apuesta_mas_alta}")


while not licitacion_terminada:
    nombre = input("Cual es tu nombre?: ")
    precio = int(input("Cual es tu oferta?: $"))
    ofertas[nombre] = precio
    continuar = input("hay otros postores? Escriba 'si' o 'no': ")
    if continuar == 'no':
        licitacion_terminada = True
        buscar_mejor_postor(ofertas)
    elif continuar == 'si':
        clear()
