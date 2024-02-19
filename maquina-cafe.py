MENU = {
    "espresso": {
        "ingredientes": {
            "agua": 50,
            "cafe": 18,
        },
        "costo": 1.5,
    },
    "latte": {
        "ingredientes": {
            "agua": 200,
            "leche": 150,
            "cafe": 24,
        },
        "costo": 2.5,
    },
    "cappuccino": {
        "ingredientes": {
            "agua": 250,
            "leche": 100,
            "cafe": 24,
        },
        "costo": 3.0,
    }
}
ganancia = 0
recursos = {
    "agua": 300,
    "leche": 200,
    "cafe": 100,
}


def recursos_suficientes(orden_ingredientes):
    """ Devuelve True cuando la orden se puede realizar y False cuando no"""
    es_suficiente = True
    for elemento in orden_ingredientes:
        if orden_ingredientes[elemento] >= recursos[elemento]:
            print(f"Disculpas, no tenemos suficiente {elemento}")
            es_suficiente = False
    return es_suficiente


def proceso_menedas():
    """ devuelve el total calculado a partir de la inserción de monedas """
    print("Inserte monedas")
    total = int(input("cuantos trimestres?: ")) * 0.25
    total += int(input("cuantas monedas de diez centavos?: ")) * 0.1
    total += int(input("cuantas monedas de cinco centavos?: ")) * 0.05
    total += int(input("Cuantos centavos?: ")) * 0.01
    return total


def transaccion_exitosa(monto_recibido, costo_bebida):
    """ Devolver True cuando el pago es aceptado y falso cuando es rechazado. Dinero insuficiente """
    if monto_recibido >= costo_bebida:
        cambio = round(monto_recibido - costo_bebida, 2)
        print(f"Aqui hay esta cantidad de dolares en cambio: ${cambio}")
        global ganancia
        ganancia += costo_bebida
        return True
    else:
        print("Disculpa tu dinero es insuficiente para realizar el pago")
        return False


def hacer_cafe(bebida_nombre, ingredientes_orden):
    """ Deducir los ingredientes de los recursos """
    for elementos in ingredientes_orden:
        recursos[elementos] -= ingredientes_orden[elementos]
    print(f"Aqui esta tu {bebida_nombre}")


esta_prendida = True

while esta_prendida:
    eleccion = input("Que te gustaria: espresso/latte/cappuchino: ")
    if eleccion == "apagado":
        esta_prendida = False
    elif eleccion == "informe":
        print(f"Agua: {recursos['agua']}ml")
        print(f"Leche: {recursos['leche']}ml")
        print(f"Cafe: {recursos['cafe']}g")
        print(f"Dinero: ${ganancia}")
    else:
        bebida = MENU[eleccion]
        if recursos_suficientes(bebida["ingredientes"]):
            pago = proceso_menedas()
            transaccion_exitosa(pago, bebida["costo"])
            hacer_cafe(eleccion, bebida["ingredientes"])
