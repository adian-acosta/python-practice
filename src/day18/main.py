import colorgram
from turtle import Turtle, Screen
from random import choice

rgb_colors = []
colors = colorgram.extract('image.jpg', 30)
for color in colors:
    r = color.rgb[0]
    g = color.rgb[1]
    b = color.rgb[2]
    tup = (r, g, b)
    rgb_colors.append(tup)


turtle = Turtle()
turtle.penup()
screen = Screen()
screen.colormode(255)

turtle.goto(-150, -150)
row = 1
column = 0
for i in range(100):
    turtle.pencolor(choice(rgb_colors))
    turtle.dot(20)
    turtle.forward(50)
    column += 1
    if column % 10 == 0:
        turtle.goto(-150, -150 + (row * 50))
        row += 1
        column = 0


screen.exitonclick()