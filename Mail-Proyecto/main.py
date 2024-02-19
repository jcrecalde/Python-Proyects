PALABRA_SUS = "[name]"
    
with open("./Input/Names/invited_names.txt") as nombres_archivos:  
    nombres = nombres_archivos.readlines()

with open("./Input/Letters/starting_letter.txt") as carta_archivos: 
    contenido_carta = carta_archivos.read() 
    for nombre in nombres:  
        strip_nombre = nombre.strip()
        carta_invitacion = contenido_carta.replace(PALABRA_SUS, strip_nombre)  
        print(carta_invitacion) 
        with open(f"./Output/ReadyToSend/carta_por_{strip_nombre}.txt", mode="w") as carta_completada:  
            carta_completada.write(carta_invitacion)



