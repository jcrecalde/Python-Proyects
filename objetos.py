"""contruyó un objeto prettytable utilizando PyPi"""
# from turtle import Turtle, Screen

# timmy = Turtle()
# print(timmy)
# timmy.shape("turtle")
# timmy.color("red")
# timmy.forward(100)

# my_screen = Screen()
# print(my_screen.canvheight)
# my_screen.exitonclick()

from prettytable import PrettyTable

tabla = PrettyTable()

tabla.add_column("Pokemon name", ["Pikachu", "Squartle", "Charmander"])
tabla.add_column("Type", ["Electric", "Water", "Fire"])

tabla.align = "l"

print(tabla)
