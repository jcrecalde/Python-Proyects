from tkinter import *   

def millas_a_km(): 
    millas = float(millas_entrada.get())
    km = round(millas * 1.609)
    kilometros_resultado_label.config(text=f"{km}")

window = Tk() 
window.title("Convertidor de millas a kilometros")  
window.config(padx=20, pady=20)
 
millas_entrada = Entry(width=7) 
millas_entrada.grid(column=1, row=0)
 
millas_label = Label(text="Millas") 
millas_label.grid(column=2, row=0)

es_igual_a = Label(text="Es igual a") 
es_igual_a.grid(column=0, row=1)
 
kilometros_resultado_label = Label(text="0") 
kilometros_resultado_label.grid(column=1, row=1)
 
kilometros_label = Label(text="km") 
kilometros_label.grid(column=2, row=1)
 
calculate_boton = Button(text="Calcular", command=millas_a_km)
calculate_boton.grid(column=1, row=2)

 
window.mainloop()