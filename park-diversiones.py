""" Proyecto de Parque de diversiones """

print("Bienvenido a la super montaña rusa")

altura = int(input("Ingrese su altura: "))
precio = 0

if altura >= 120:
    print("Puedes ingresar a la montaña rusa")
    edad = int(input("Ingresar la edad: "))
    if edad < 12:
        precio = 5
        print("debes pagar $5")
    elif edad <= 18:
        precio = 7
        print("debes pagar $7")
    elif edad >= 45 and edad <= 50:
        print("Paseo gratis!")
    else:
        precio = 12
        print("debes pagar $12")

    foto = input("Queres que te saquemos fotos? Y or N.")
    if foto == "Y":
        precio += 3

    print(f"Su precio final es ${precio}")

else:
    print("No puedes ingresar")
