from turtle import Turtle, Screen   
import time 

class Score(Turtle): 
     
    def __init__(self): 
        super().__init__() 
        self.color("white") 
        self.penup() 
        self.hideturtle() 
        self.i_score = 0 
        self.d_score = 0   
        self.actualizacion_puntaje()
     
    def actualizacion_puntaje(self):   
        self.clear()
        self.goto(-100, 200) 
        self.write(self.i_score, align="center", font=("Courier", 80, "normal")) 
        self.goto(100, 200) 
        self.write(self.d_score, align="center", font=("Courier", 80, "normal")) 
     
    def i_puntaje(self): 
        self.i_score += 1 
        self.actualizacion_puntaje() 
     
    def d_puntaje(self): 
        self.d_score += 1 
        self.actualizacion_puntaje()

class Paleta(Turtle): 

    def __init__(self, posicion): 
        super().__init__() 
        self.shape("square")  
        self.color("white")
        self.shapesize(stretch_wid=5, stretch_len=1) 
        self.penup() 
        self.goto(posicion)    
     
    def ir_arriba(self): 
        nueva_y = self.ycor() + 20
        self.goto(self.xcor(), nueva_y) 

    def ir_abajo(self): 
        nueva_y = self.ycor() - 20
        self.goto(self.xcor(), nueva_y)   
 
class Pelota(Turtle): 
     
     def __init__(self): 
        super().__init__() 
        self.shape("circle") 
        self.color("white") 
        self.penup()  
        self.x_move = 10 
        self.y_move = 10 
        self.move_speed = 0.1
     
     def move(self): 
        nueva_x = self.xcor() + self.x_move
        nueva_y = self.ycor() + self.y_move 
        self.goto(nueva_x, nueva_y) 
     
     def rebotar_y(self): 
         self.y_move *= -1 

     def rebotar_x(self): 
        self.x_move *= -1  
        self.move_speed *= 0.9
     
     def reset_posicion(self):  
        self.goto(0, 0)  
        self.move_speed = 0.1
        self.rebotar_x()

 
screen = Screen() 
screen.setup(width=800, height=600) 
screen.bgcolor("Black") 
screen.title("Pong Game")   
screen.tracer(0) 
 
i_paleta = Paleta((350, 0))
d_paleta = Paleta((-350, 0)) 
pelota = Pelota()  
puntaje = Score()
 

screen.listen() 
screen.onkey(i_paleta.ir_arriba, "Up") 
screen.onkey(i_paleta.ir_abajo, "Down") 
screen.onkey(d_paleta.ir_arriba, "w") 
screen.onkey(d_paleta.ir_abajo, "s")
 
juego_encendido = True  
while juego_encendido:  
    time.sleep(pelota.move_speed)
    screen.update() 
    pelota.move() 
     
    # Detectar la colision con la pared. 
    if pelota.ycor() > 280 or pelota.ycor() < -280: 
        #necesita rebotar   
        pelota.rebotar_y() 
         
        # Detectar colision con paleta 
    if pelota.distance(i_paleta) < 50 and pelota.xcor() > 320 or pelota.distance(d_paleta) < 50 and pelota.xcor() < -320:   
         pelota.rebotar_x()
         
        # Detectar cuando la paleta derecha falla.  
    if pelota.xcor() > 380:  
        pelota.reset_posicion()  
        puntaje.i_puntaje()

        # Detectar cuando la paleta izquierda falla. 
    if pelota.xcor() < -380: 
        pelota.reset_posicion() 
        puntaje.d_puntaje()




screen.exitonclick() 