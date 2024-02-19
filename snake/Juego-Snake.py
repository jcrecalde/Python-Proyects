from turtle import Turtle, Screen  
import time  
import random
 
UP = 90 
DOWN = 270 
LEFT = 180 
RIGHT = 0   
 
ALIGNMENT = "center" 
FONT = ("Arial", 24, "normal")
 
class Score(Turtle): 
     
     
    def __init__(self): 
        super().__init__() 
        self.score = 0    
        with open("data.txt") as data: 
            self.high_score = int(data.read())
        self.color("white")  
        self.penup()
        self.goto(0, 270)
        self.hideturtle()   
        self.actualizacion_score()

    def actualizacion_score(self):   
        self.clear()
        self.write(f"Puntaje: {self.score} Mayor Puntaje: {self.high_score}", align=ALIGNMENT, font=FONT)   
     
    def reset(self):  
        if self.score > self.high_score: 
            self.high_score = self.score  
            with open("data.txt", mode="w") as data:  
                data.write(f"{self.heading_score}")

        self.score = 0 
        self.actualizacion_score()

    #def perdiste_juego(self):  
        #self.goto(0, 0)
        #self.write(f"PERDISTE!!!", align=ALIGNMENT, font=FONT)  

    def incrementar_score(self): 
        self.score += 1   
        self.clear()
        self.actualizacion_score()


 
class Food(Turtle): 
 
     def __init__(self): 
        super().__init__() 
        self.shape("circle") 
        self.penup()   
        self.shapesize(stretch_len=0.5, stretch_wid=0.5) 
        self.color("blue") 
        self.speed("fastest")  
        self.refresh() 
      
     def refresh(self):  
        random_x = random.randint(-280, 280)  
        random_y = random.randint(-280, 280) 
        self.goto(random_x, random_y) 


class Snake: 
    def __init__(self): 
        self.segmentos = [] 
        self.create_snake()   
        self.head = self.segmentos[0]
 
    def create_snake(self): 
        for posicion in comienzo_posiciones:  
            self.add_segmento(posicion)
    
     
    def add_segmento(self, posicion):  
        nuevo_segmento = Turtle("square") 
        nuevo_segmento.color("white")  
        nuevo_segmento.penup()
        nuevo_segmento.goto(posicion) 
        self.segmentos.append(nuevo_segmento)     
     
    def reset(self):  
        for seg in self.segmentos: 
            seg.goto(1000, 1000)
        self.segmentos.clear() 
        self.create_snake() 
        self.head = self.segmentos[0]

     
    def extend(self): 
        # agregar un nuevo segmento en la snake  
        self.add_segmento(self.segmentos[-1].position())


     
    def move(self): 
        for seg_num in range(len(self.segmentos) - 1, 0, -1): 
            nueva_x = self.segmentos[seg_num - 1].xcor()  
            nueva_y = self.segmentos[seg_num - 1].ycor() 
            self.segmentos[seg_num].goto(nueva_x, nueva_y) 
        self.head.forward(mueve_distancia) 

    def up(self):   
        if self.head.heading() != DOWN:
            self.head.setheading(UP) 
     
    def down(self):  
        if self.head.heading() != UP:
            self.head.setheading(DOWN)
    
    def left(self):  
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)
     
    def right(self):  
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

screen = Screen() 
screen.setup(width=600, height=600) 
screen.bgcolor("black") 
screen.title("My Snake Game")   
screen.tracer(0)

juego_perdido = True

comienzo_posiciones = [(0, 0), (-20, 0), (-40, 0)]  
mueve_distancia = 20

snake = Snake()    
food = Food() 
score = Score()

screen.listen() 
screen.onkey(snake.up, "Up") 
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left") 
screen.onkey(snake.right, "Right")

while juego_perdido: 
    screen.update() 
    time.sleep(0.1)  
    snake.move() 

    # Detectar cuando toma la comida.
    if snake.head.distance(food) < 15: 
        food.refresh()  
        snake.extend()
        score.incrementar_score() 
     
    # Detectar colision con la pared.   
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280: 
        score.reset() 
        snake.reset()
    # Detectar colision con la cola   
    for segmento in snake.segmentos[1:]:
        if snake.head.distance(segmento) < 10:  
            score.reset() 
            snake.reset()
  
    
    # Si colisiona con cualquier segmento en la cola  
        #Trigger game over 






screen.exitonclick() 
