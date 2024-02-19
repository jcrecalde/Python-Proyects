from turtle import Turtle, Screen 

tortuga = Turtle() 
screen = Screen() 
 
def move_forwards(): 
    tortuga.forward(10) 
 
def move_backward(): 
    tortuga.backward(10)  
 
def turn_left(): 
    new_heading = tortuga.heading() + 10 
    tortuga.setheading(new_heading)
 
def turn_right(): 
    new_heading = tortuga.heading() - 10 
    tortuga.setheading(new_heading) 
 
def clear():  
    tortuga.clear()  
    tortuga.penup()
    tortuga.home() 
    tortuga.pendown()


screen.listen()  
screen.onkey(key="w", fun=move_forwards)  
screen.onkey(key="s", fun=move_backward) 
screen.onkey(key="a", fun=turn_right) 
screen.onkey(key="d", fun=turn_left) 
screen.onkey(key="c", fun=clear)
 
screen.exitonclick()
