""" Programa cifrado Cesar """

logo = """           
 ,adPPYba, ,adPPYYba,  ,adPPYba, ,adPPYba, ,adPPYYba, 8b,dPPYba,  
a8"     "" ""     `Y8 a8P_____88 I8[    "" ""     `Y8 88P'   "Y8  
8b         ,adPPPPP88 8PP"""""""  `"Y8ba,  ,adPPPPP88 88          
"8a,   ,aa 88,    ,88 "8b,   ,aa aa    ]8I 88,    ,88 88          
 `"Ybbd8"' `"8bbdP"Y8  `"Ybbd8"' `"YbbdP"' `"8bbdP"Y8 88   
            88             88                                 
           ""             88                                 
                          88                                 
 ,adPPYba, 88 8b,dPPYba,  88,dPPYba,   ,adPPYba, 8b,dPPYba,  
a8"     "" 88 88P'    "8a 88P'    "8a a8P_____88 88P'   "Y8  
8b         88 88       d8 88       88 8PP""""""" 88          
"8a,   ,aa 88 88b,   ,a8" 88       88 "8b,   ,aa 88          
 `"Ybbd8"' 88 88`YbbdP"'  88       88  `"Ybbd8"' 88          
              88                                             
              88           
"""
print(logo)

alfabeto = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p",
            "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "a", "b", "c", "d", "e", "f",
            "g", "h", "i", "j", "k", "l", "m", "n", "o", "p",
            "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]


def cesar(texto_inicio, cant_cambio, direccion_cifrado):
    texto_final = ""
    if direccion_cifrado == "decodificado":
        cant_cambio *= -1
    for caracter in texto_inicio:
        if caracter in alfabeto:
            posicion = alfabeto.index(caracter)
            nueva_posicion = posicion + cant_cambio
            texto_final += alfabeto[nueva_posicion]
        else:
            texto_final += caracter
    print(f"El {direccion} result: {texto_final}")


deberia_continuar = True
while deberia_continuar:
    direccion = input(
        "escriba 'codificado' para cifrar, escriba 'decodificado' para desifrar:\n")
    texto = input("Ingrese su mensaje:\n").lower()
    cambio = int(input("Escriba el numero de turno:\n"))

    cambio = cambio % 26

    cesar(texto_inicio=texto, cant_cambio=cambio, direccion_cifrado=direccion)

    resultado = input(
        "escriba 'sí' si desea volver a ir. de lo contrario escriba 'no'\n")

    if resultado == "no":
        deberia_continuar = False
        print("Hasta luego! :D ")
