import turtle  
import pandas as pd
  
screen = turtle.Screen() 
screen.title("U.S States games")  
image = "blank_states_img.gif" 
screen.addshape(image) 
turtle.shape(image) 

#def get_mouse_click_coor(x, y): 
    #print(x, y) 
 
#turtle.onscreenclick(get_mouse_click_coor) 
#turtle.mainloop()  
 
data = pd.read_csv("50_states.csv")  
estados = data["state"].to_list()
preguntas_estados = []
  
while len(preguntas_estados) < 50:
    respuesta_estado = screen.textinput(title=f"{len(preguntas_estados)}/50 estados correctos", prompt="Cual es el nombre del estado?").title()
     
    if respuesta_estado == "Salir":  
        estados_no_encontrado = [estado for estado in estados if estado not in preguntas_estados] 
        nueva_data = pandas.DataFrame(estados_no_encontrado) 
        nueva_data.to_csv("estados_a_aprender.csv")
        break 

    if respuesta_estado in estados:  
        preguntas_estados.append(respuesta_estado)
        t = turtle.Turtle() 
        t.hideturtle()    
        t.penup()
        estado_data = data[data.state == respuesta_estado]
        t.goto(int(estado_data.x), int(estado_data.y)) 
        t.write(respuesta_estado) 
