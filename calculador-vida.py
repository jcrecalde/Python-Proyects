""" Programa para calcular cuanto le queda a una persona de vida si vivimos hasta los 90 """

edad = input("Ingresar tu edad actual: ")

edad_int = int(edad)

años_restantes = 90 - edad_int

dias_restantes = años_restantes * 360
semanas_restantes = años_restantes * 52
meses_restantes = años_restantes * 12

mensaje = f"te quedan {dias_restantes}, {semanas_restantes} semanas, y {meses_restantes} meses restantes"
print(mensaje)
