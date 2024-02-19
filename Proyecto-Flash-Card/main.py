from tkinter import *  
import pandas as pd 
import random 

BACKGROUND_COLOR = "#B1DDC6"  
tarjeta_actual = {} 
a_aprender = {}

#------------------------------------------ Funciones ------------------------------------#   
try:
    data = pd.read_csv("data/palabras_a_aprender.csv")  
except FileNotFoundError: 
    data_original = pd.read_csv("data/french_words.csv")  
    a_aprender = data_original.to_dict(orient="records")
else:
    a_aprender = data.to_dict(orient="records") 


def siguiente_carta():    
    global tarjeta_actual, hora_de_voltear 
    window.after_cancel(hora_de_voltear)
    tarjeta_actual = random.choice(a_aprender) 
    canvas.itemconfig(carta_titulo, text="French", fill="Black") 
    canvas.itemconfig(carta_palabra, text=tarjeta_actual["French"], fill="Black")  
    canvas.itemconfig(carta_fondo, image=imagen_frente) 
    hora_de_voltear = window.after(3000, func=carta_invertida)
 
def carta_invertida(): 
    canvas.itemconfig(carta_titulo, text="English", fill="white") 
    canvas.itemconfig(carta_palabra, text=tarjeta_actual["English"], fill="white") 
    canvas.itemconfig(carta_fondo, image=imagen_atras) 

def es_conocido(): 
    a_aprender.remove(tarjeta_actual)  
    data2 = pd.DataFrame(a_aprender) 
    data2.to_csv("data/palabras_a_aprender.csv", index=False) 


    siguiente_carta()

#----------------------------------------- UI SETUP----------------------------------------# 

window = Tk()
window.title("Flashy") 
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR )  

hora_de_voltear = window.after(3000, func=carta_invertida)

canvas = Canvas(width=800, height=526) 
imagen_frente = PhotoImage(file="images\card_front.png")  
imagen_atras = PhotoImage(file="images\card_back.png")
carta_fondo = canvas.create_image(400, 263, image=imagen_frente)  
carta_titulo = canvas.create_text(400, 150, text="", font=("Arial", 40, "italic")) 
carta_palabra = canvas.create_text(400, 263, text="", font=("Arial", 60, "bold"))
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(row=0, column=0, columnspan=2) 
 
#-------------------------- Botones --------------------------# 
imagen_x = PhotoImage(file="images/wrong.png")
boton_x = Button(image=imagen_x,  highlightthickness=0, command=siguiente_carta) 
boton_x.grid(row=1, column=0) 

imagen_check = PhotoImage(file="images/right.png") 
boton_check = Button(image=imagen_check, highlightthickness=0, command=es_conocido) 
boton_check.grid(row=1, column=1) 

siguiente_carta()



window.mainloop()