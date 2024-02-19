import colorgram  
import turtle as turtle_module 
import random
 
"""Extraer los colores"""
#rgb_colors = []
#colors = colorgram.extract('puntos.jpg', 10) 
 
#for color in colors:  
    #r = color.rgb.r 
    #g = color.rgb.g
    #b = color.rgb.b
    #new_color = (r, g, b) 
    #rgb_colors.append(new_color)
 
#print(rgb_colors)  
turtle_module.colormode(255)
juan = turtle_module.Turtle()
juan.speed("fastest") 
juan.penup() 
juan.hideturtle()
color_list = [(103, 90, 240), (98, 241, 132), (228, 79, 189), (214, 233, 84), (89, 181, 239), (241, 144, 83)]  
 
juan.setheading(225) 
juan.forward(300) 
juan.setheading(0) 
number_of_dots = 100
  
for dot_count in range(1, number_of_dots + 1):
    juan.dot(20, random.choice(color_list))  
    juan.forward(50) 
     
    if dot_count % 10 == 0:
        juan.setheading(90) 
        juan.forward(50) 
        juan.setheading(180) 
        juan.forward(500)
        juan.setheading(0) 

screen = turtle_module.Screen() 
screen.exitonclick()