from turtle import Turtle, Screen  
import random
 
is_race_on = False
tortuga = Turtle()  
screen = Screen() 
screen.setup(width=500, height=400) 
user_bet = screen.textinput(title="Haz tu apuesta", prompt="Que tortuga gana la carrera? ingrese un color: ") 
print(user_bet)  
colors = ["red", "orange", "yellow", "green", "blue", "purple"]  
y_positions = [-70, -40, -10, 20, 50, 80] 
all_turtles = []

for turtle_index in range(0, 6):
    new_turtle = Turtle(shape="turtle")   
    new_turtle.color(colors[turtle_index])
    new_turtle.penup()
    new_turtle.goto(x=-230, y=y_positions[turtle_index])  
    all_turtles.append(new_turtle)
   
""" Si el usuario realizo la apuesta """
if user_bet: 
    is_race_on = True  
 
while is_race_on:   
     
    for turtle in all_turtles:  
        if turtle.xcor() > 230:  
            is_race_on = False
            winning_color = turtle.pencolor() 
            if winning_color == user_bet: 
               print(f"has ganado! El {winning_color} es el ganador")   
            else: 
               print(f"has perdido! El {winning_color} es el ganador")   
           

        
        rand_distance = random.randint(0, 10) 
        turtle.forward(rand_distance)



screen.exitonclick()