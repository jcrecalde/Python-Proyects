from turtle import Turtle, Screen     
import time 
import random

comienzo_posicion = (0, -280) 
distancia_movimiento_tortuga = 10
linea_final_y = 280  

colores = ["red", "orange", "yellow", "green", "blue", "purple"] 
comienza_movimiento_auto = 5   
movimiento_incrementa = 10 

FONT = ("Courier", 24, "normal")



class Tortuga(Turtle):  
     
    def __init__(self): 
        super().__init__()
        self.shape("turtle")  
        self.penup()
        self.color("black") 
        self.ir_al_comienzo() 
        self.setheading(90) 
     
    def movimiento(self): 
        self.forward(distancia_movimiento_tortuga)   

    def ir_al_comienzo(self): 
        self.goto(comienzo_posicion) 
        
    def linea_final(self):  
        if self.ycor() > linea_final_y:  
            return True 
        else: 
            return False

 
class Autos:  
    def __init__(self): 
        self.autos_generados = []    
        self.autos_rapidez = distancia_movimiento_tortuga
     
    def crear_auto(self):   
        oportunidad_random = random.randint(1, 6) 
        if oportunidad_random == 1:
            nuevo_auto = Turtle("square") 
            nuevo_auto.shapesize(stretch_wid= 1, stretch_len= 2) 
            nuevo_auto.penup()  
            nuevo_auto.color(random.choice(colores))  
            random_y = random.randint(-250, 250) 
            nuevo_auto.goto(300, random_y) 
            self.autos_generados.append(nuevo_auto) 

    def mover_autos(self):  
        for auto in self.autos_generados:  
            auto.backward(self.autos_rapidez) 
     
    def nivel(self): 
        self.autos_rapidez += movimiento_incrementa 

class Puntuacion(Tortuga):  
      
    def __init__(self): 
        super().__init__()  
        self.nivel = 1
        self.hideturtle() 
        self.penup()   
        self.goto(-280, 280) 
        self.actualizar_puntuacion()

    def actualizar_puntuacion(self):   
        self.clear()
        self.write(f"Nivel: {self.nivel}", align="left", font=FONT)

     
    def aumentar_nivel(self):  
        self.nivel += 1 
        self.actualizar_puntuacion() 
     
    def juego_perdido(self):  
        self.goto(0, 0)  
        self.write(f"GAME OVER!: {self.nivel}", align="center", font=FONT)





screen = Screen() 
screen.setup(width=600, height=600) 
screen.tracer(0)  

tortuga = Tortuga()  
autos_generados = Autos() 
puntuacion = Puntuacion()
 
screen.listen()
screen.onkey(tortuga.movimiento, "Up")
 

juego_encendido = True 
while juego_encendido: 
    time.sleep(0.1) 
    screen.update() 
     
    autos_generados.crear_auto() 
    autos_generados.mover_autos() 

    #Detectar choque de la tortuga con el auto.  
    for auto in autos_generados.autos_generados: 
        if auto.distance(tortuga) < 20:  
            juego_encendido = False  
            puntuacion.juego_perdido()
     
    #Detectar cuando cruzamos exitosamente 
    if tortuga.linea_final():  
        tortuga.ir_al_comienzo() 
        autos_generados.nivel() 
        puntuacion.aumentar_nivel()
 
screen.exitonclick()