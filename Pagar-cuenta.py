""" Programa para seleccionar aleatoriamente a quien le corresponde pagar la cuenta. """
""" Nota: Se realizo sin utilizar choice """

import random
ingresar_nombres = input("Ingrese las personas separadas por una coma: ")
lista_nombres = ingresar_nombres.split(", ")

long_nombres = len(lista_nombres)

random_index = random.randint(0, long_nombres - 1)

persona_elegida = lista_nombres[random_index]

print(persona_elegida + " debe pagar la cuenta hoy.")
