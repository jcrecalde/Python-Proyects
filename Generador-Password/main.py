from tkinter import *  
from tkinter import messagebox 
from random import choice, randint, shuffle, random 
import pyperclip 
import json
 
# ---------------------------- Generador de password ------------------------------- # 
 
def generar_contraseña():
    letras = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x',
            'y', 'z', 'A', 'B', 'C', 'D', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

    numeros = ['1', '2', '3', '4', '5', '6', '7', '8', '9']

    simbolos = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letras = [choice(letras) for _ in range(randint(8, 10))] 
    password_simbolos = [choice(simbolos) for _ in range(randint(2, 4))]  
    password_numeros = [choice(letras) for _ in range(randint(2, 4))] 

    password_lista = password_letras + password_simbolos + password_numeros

    shuffle(password_lista)

    password = "".join(password_lista)
    password_entrada.insert(0, password) 
    pyperclip.copy(password)

# ---------------------------- Guardar password------------------------------- # 
def guardar():   
     
    sitioweb = sitio_web_entrada.get() 
    email = email_entrada.get() 
    password = password_entrada.get()   
    nueva_data = { 
        sitioweb:{ 
            "email": email, 
            "password": password, 
        }
    }

    if len(sitioweb) == 0 or len(password) == 0:  
        messagebox.showinfo(title="Ops", message="Asegurese que no ha dejado ningun campo vacio") 
    else: 
        try:
            with open("data.json", "r") as data_archivo: 
                #Leemos los datos antiguos
                data = json.load(data_archivo)   
                #Actualizamos la data antigua a la nueva data
        except FileNotFoundError: 
            with open("data.json", "w") as data_archivo: 
                json.dump(nueva_data, data_archivo, indent=4)    
        else:
            data.update(nueva_data)      

            with open("data.json", "w") as data_archivo:
                #Guardamos los datos actualizados
                json.dump(data, data_archivo, indent=4)  
        finally:
            sitio_web_entrada.delete(0, END) 
            email_entrada.delete(0, END) 
 
# ---------------------------- Buscar Password ------------------------ #  
def buscar():
    sitioweb = sitio_web_entrada.get()
    try:
        with open("data.json") as data_archivo:
            data = json.load(data_archivo)
    except FileNotFoundError:
        messagebox.showinfo(title="Error", message="No hay data de este sitio")
    else:
        if sitioweb in data:
            email = data[sitioweb]["email"]
            password = data[sitioweb]["password"]
            messagebox.showinfo(title="Sitio web encontrado", message=f"Email: {email}, Password: {password}\n")
        else:
            messagebox.showinfo(title="Error", message=f"No se encontraron datos para el sitio web '{sitioweb}'")
    finally:
        sitio_web_entrada.delete(0, END)



# ---------------------------- UI SETUP ------------------------------- # 
window = Tk() 
window.title("Generador de contraseñas")   
window.config(padx=50, pady=50)


canvas = Canvas(width=200, height=200)  
candado_imagen = PhotoImage(file="logo.png") 
canvas.create_image(100, 100, image=candado_imagen)   
canvas.grid(row=0, column=1)

#Labels 
sitio_web_label = Label(text="SitioWeb:")     
sitio_web_label.grid(row=1, column=0)
email_label = Label(text="Email/NombreUsuario:")  
email_label.grid(row=2, column=0)
password_label = Label(text="password:") 
password_label.grid(row=3, column=0) 

#Entries 
sitio_web_entrada = Entry(width=21)  
sitio_web_entrada.grid(row=1, column=1) 
sitio_web_entrada.focus()
email_entrada = Entry(width=35)  
email_entrada.grid(row=2, column=1, columnspan=2) 
email_entrada.insert(0, "ejemplo@gmail.com")
password_entrada = Entry(width=21) 
password_entrada.grid(row=3, column=1) 
 
#Botones 
generar_password_boton = Button(text="Generar password", command=generar_contraseña) 
generar_password_boton.grid(row=3, column=2) 
 
agregar_boton = Button(text="Agregar", width=36, command=guardar) 
agregar_boton.grid(row=4, column=1, columnspan=2) 
 
buscar_boton = Button(text="Buscar", width=14, command=buscar) 
buscar_boton.grid(row=1, column=2)


window.mainloop()