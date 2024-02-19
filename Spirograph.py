import turtle as t 
import random

""" La tortuga realiza un recorrido de diversos angulos """
tortuga = t.Turtle()   
t.colormode(255)

t.colormode(255) 
def random_color(): 
    r = random.randint(0, 255) 
    g = random.randint(0, 255) 
    b = random.randint(0, 255) 
    random_color = (r, g, b) 
    return random_color

tortuga.speed("fastest")    
def draw_spirograph(size_of_gap):
    for _ in range(int(360 / size_of_gap)):
        tortuga.color(random_color())
        tortuga.circle(100)  
        tortuga.setheading(tortuga.heading()  + size_of_gap) 
 
draw_spirograph(5)

screen = t.Screen() 
screen.exitonclick()