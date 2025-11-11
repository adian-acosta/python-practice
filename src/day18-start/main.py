from random import choice,randint
from turtle import Turtle, Screen

turtle = Turtle()
turtle.speed('fastest')
turtle.pensize(10)
screen = Screen()
screen.colormode(255)

angle = [0, 90, 180, 270]

for i in range(100):
    r = randint(0, 255)
    g = randint(0, 255)
    b = randint(0, 255)
    turtle.pencolor(r, g, b)
    turtle.setheading(turtle.heading() + 10)
    turtle.circle(100)

screen.exitonclick()