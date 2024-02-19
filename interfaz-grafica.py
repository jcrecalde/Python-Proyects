from tkinter import *

#Creando una nueva ventana y configuraciones.
window = Tk()
window.title("Ejemplos de widgets")
window.minsize(width=500, height=500)

#Labels
label = Label(text="Este es un texto antiguo.")
label.config(text="Este es un texto nuevo")
label.pack()

#Botones
def action():
    print("Hacer algo")

#llama a la acción() cuando se presiona
button = Button(text="Clickear", command=action)
button.pack()

#Entradas
entry = Entry(width=30)
#Añade algo de texto para empezar.
entry.insert(END, string="Algo de texto para empezar")
#Obtiene texto en la entrada
print(entry.get())
entry.pack()

#Texto
text = Text(height=5, width=30)
#Colocar el cursor en el cuadro de texto.
text.focus()
#Agrega algo de texto para comenzar.
text.insert(END, "Ejemplo de entrada de texto de varias líneas.")
#Obtenga el valor actual en el cuadro de texto en la línea 1, carácter 0
print(text.get("1.0", END))
text.pack()

#Caja giratoria
def spinbox_used():
    #obtiene el valor actual en el cuadro de giro.
    print(spinbox.get())
spinbox = Spinbox(from_=0, to=10, width=5, command=spinbox_used)
spinbox.pack()

#Escala
#Llamado con el valor de escala actual.
def scale_used(value):
    print(value)
scale = Scale(from_=0, to=100, command=scale_used)
scale.pack()

#Checkbutton
def checkbutton_used():
    #Imprime 1 si el botón Activado está marcado; de lo contrario, 0.
    print(checked_state.get())
#variable para mantener el estado marcado, 0 está desactivado, 1 está activado.
checked_state = IntVar()
checkbutton = Checkbutton(text="¿Está encendido?", variable=checked_state, command=checkbutton_used)
checked_state.get()
checkbutton.pack()

#Radiobutton
def radio_used():
    print(radio_state.get())
#Variable para mantener el valor del botón de opción marcado.
radio_state = IntVar()
radiobutton1 = Radiobutton(text="Option1", value=1, variable=radio_state, command=radio_used)
radiobutton2 = Radiobutton(text="Option2", value=2, variable=radio_state, command=radio_used)
radiobutton1.pack()
radiobutton2.pack()


#Listbox
def listbox_used(event):
    # Obtiene la selección actual del cuadro de lista
    print(listbox.get(listbox.curselection()))

listbox = Listbox(height=4)
fruits = ["Apple", "Pear", "Orange", "Banana"]s
for item in fruits:
    listbox.insert(fruits.index(item), item)
listbox.bind("<<ListboxSelect>>", listbox_used)
listbox.pack()
window.mainloop()