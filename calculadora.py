# Calculadora

logo = """
 _____________________
|  _________________  |
| | Pythonista   0. | |  .----------------.  .----------------.  .----------------.  .----------------. 
| |_________________| | | .--------------. || .--------------. || .--------------. || .--------------. |
|  ___ ___ ___   ___  | | |     ______   | || |      __      | || |   _____      | || |     ______   | |
| | 7 | 8 | 9 | | + | | | |   .' ___  |  | || |     /  \     | || |  |_   _|     | || |   .' ___  |  | |
| |___|___|___| |___| | | |  / .'   \_|  | || |    / /\ \    | || |    | |       | || |  / .'   \_|  | |
| | 4 | 5 | 6 | | - | | | |  | |         | || |   / ____ \   | || |    | |   _   | || |  | |         | |
| |___|___|___| |___| | | |  \ `.___.'\  | || | _/ /    \ \_ | || |   _| |__/ |  | || |  \ `.___.'\  | |
| | 1 | 2 | 3 | | x | | | |   `._____.'  | || ||____|  |____|| || |  |________|  | || |   `._____.'  | |
| |___|___|___| |___| | | |              | || |              | || |              | || |              | |
| | . | 0 | = | | / | | | '--------------' || '--------------' || '--------------' || '--------------' |
| |___|___|___| |___| |  '----------------'  '----------------'  '----------------'  '----------------' 
|_____________________|
"""


def suma(n1, n2):
    return n1 + n2

# Resta


def resta(n1, n2):
    return n1 - n2

# Multiplicacion


def multiplicacion(n1, n2):
    return n1 * n2

# Divicion


def division(n1, n2):
    return n1 / n2


operaciones = {
    "+": suma,
    "-": resta,
    "*": multiplicacion,
    "/": division
}


def calcular():
    num1 = float(input("Cual es el primer numero?: "))

    for simbolo in operaciones:
        print(simbolo)

    deberia_continuar = True

    while deberia_continuar:

        operacion_simbolo = input("Elija una operación: ")
        num2 = float(input("Cual es el proximo numero?: "))
        funcion_de_calculo = operaciones[operacion_simbolo]
        respuesta = funcion_de_calculo(num1, num2)

        print(f"{num1} {operacion_simbolo} {num2} = {respuesta}")

        if input(f"Escriba 's' si deseas continuar calculando {respuesta} o si no deseas seguir calculando escriba 'n' para comenzar un nuevo calculo: ") == 's':
            num1 = respuesta
        else:
            deberia_continuar = False
            calcular()


calcular()
