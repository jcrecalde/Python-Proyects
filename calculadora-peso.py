""" Programa para calcular que peso tiene una persona. """
height = float(input("Ingresa su altura: "))
weight = float(input("Ingresa su peso: "))

BMI = round(weight / height ** 2)

if BMI < 18.5:
    print(f"Su BMI es de {BMI}, peso bajo")
elif BMI < 25:
    print(f"Su BMI es de {BMI}, peso normal")
elif BMI < 30:
    print(f"Su BMI es de {BMI}, sobre peso")
elif BMI < 35:
    print(f"Su BMI es de {BMI}, obeso")
else:
    print(f"Su BMI es de {BMI}, clinicamente obeso")
