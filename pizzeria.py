""" Proyecto pizzeria """

print("Bienvenido a pizza deliveri!")
tipo_pizza = input("que tamaño de pizza quieres? S, M, or L ")
agregar_peperoni = input("Le agregamos peperoni? Y or N ")
queso_extra = input("Con queso extra? Y o N ")

costo = 0

if tipo_pizza == "S":
    costo += 15
elif tipo_pizza == "M":
    costo += 20
elif tipo_pizza == "L":
    costo += 25

if agregar_peperoni == "Y":
    if tipo_pizza == "S":
        costo += 2
    else:
        costo += 3

if queso_extra == "Y":
    costo += 1

print(f"El precio final es de: ${costo}.")
