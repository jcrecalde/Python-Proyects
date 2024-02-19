from tkinter import * 
import math
# ---------------------------- COSTANTES ------------------------------- #
ROSA = "#e2979c"
ROJO = "#e7305b"
VERDE = "#9bdeac"
AMARILLO = "#f7f5dd"
FUENTE_NOMBRE = "Courier"
TRABAJO_MIN = 1
BREVE_DESCANSO_MIN= 5
LARGO_DESCANSO_MIN = 20 
repeticiones = 0 
tiempo = None

# ---------------------------- REINICIO DEL TEMPORIZADOR ------------------------------- #   
def reset_tiempo(): 
    window.after_cancel(tiempo) 
    canvas.itemconfig(tiempo_texto, text="00:00") 
    title_label.config(text="Tiempo") 
    check_marca.config(text="") 
    global repeticiones 
    repeticiones = 0

# ---------------------------- MECANISMO DEL TEMPORIZADOR ------------------------------- # 
def comienzo_tiempo():  
    global repeticiones  
    repeticiones +=1 

    trabajo_seg = TRABAJO_MIN * 60
    breve_descanso_seg = BREVE_DESCANSO_MIN * 60 
    largo_descanso_seg = LARGO_DESCANSO_MIN * 60 
      
    if repeticiones % 8 == 0: 
        cuenta_regresiva(largo_descanso_seg)  
        title_label.config(text="Tiempo", fg=ROJO)
    elif repeticiones % 2 == 0:
        cuenta_regresiva(breve_descanso_seg)  
        title_label.config(text="Tiempo", fg=ROSA)
    else:
        cuenta_regresiva(trabajo_seg) 
        title_label.config(text="Trabajo", fg=VERDE)
# ---------------------------- MECANISMO DE CUENTA ATRÁS------------------------------- #   
def cuenta_regresiva(cuenta):  

    contador_min = math.floor(cuenta / 60)   
    contador_seg = cuenta % 60  
    if contador_seg < 0: 
        contador_seg = f"0{contador_seg}"

    canvas.itemconfig(tiempo_texto, text=f"{contador_min}:{contador_seg}")
    if cuenta > 0: 
        global  tiempo
        tiempo = window.after(1000, cuenta_regresiva, cuenta - 1) 
    else: 
        comienzo_tiempo() 
        marcas = "" 
        trabajo_sesiones = math.floor(peteciones/2) 
        for _ in range(trabajo_sesiones): 
            marcas += "✔" 
        check_marcha.config(text=marcas)


# ---------------------------- UI CONFIGURACION ------------------------------- # 
window = Tk()  
window.title("Pomodoro")   
window.config(padx=100, pady=50, bg=AMARILLO)  

title_label = Label(text="Tiempo", fg=VERDE, bg=AMARILLO, font=(FUENTE_NOMBRE, 25)) 
title_label.grid(column=1, row=0)

canvas = Canvas(width=200, height=224, bg=AMARILLO, highlightthickness=0)  
tomate_imagen = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomate_imagen)   
tiempo_texto = canvas.create_text(100, 130, text="00:00", fill="white", font=(FUENTE_NOMBRE, 35, "bold"))  
canvas.grid(column=1, row=1)  


start_boton = Button(text="Start", highlightthickness=0, command=comienzo_tiempo)  
start_boton.grid(column=0, row=2) 

reset_boton = Button(text="Reset", highlightthickness=0, command=reset_tiempo)
reset_boton.grid(column=2, row=2) 
 
check_marca = Label(fg=VERDE, bg=AMARILLO) 
check_marca.grid(column=1, row=3)


window.mainloop()