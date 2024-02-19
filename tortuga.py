import turtle as t 
import random

""" La tortuga realiza un recorrido de diversos angulos """
tortuga = t.Turtle()  
colors = ["magenta", "dark slate blue", "dark slate gray", "black", "saddle brown", "midnight blue"] 

""" La tortuga realiza un recorrido de diversos angulos """
#def dibujar_forma(numero_angulos):
    #angulo = 360 / numero_angulos 
    #for _ in range(numero_angulos): 
        #tortuga.forward(100) 
        #tortuga.right(angulo) 
    
    #for lado_forma_n in range(3, 11):   
        #tortuga.color(random.choice(colors))
        #dibujar_forma(lado_forma_n) 

######## 
""" La tortuga realiza un recorrido aleatorio donde cambia tambien de color y de tamaño dudante el mismo"""  
t.colormode(255) 
def random_color(): 
    r = random.randint(0, 255) 
    g = random.randint(0, 255) 
    b = random.randint(0, 255) 
    random_color = (r, g, b) 
    return random_color

direcciones = [0, 90, 180, 270]  
tamaño = [1, 2, 5, 8, 10] 
t.speed("fastest") 
for _ in range(200): 
    tortuga.color(random_color()) 
    tortuga.pensize(random.choice(tamaño))
    tortuga.forward(30) 
    tortuga.setheading(random.choice(direcciones)) 


