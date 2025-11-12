from turtle import Turtle, Screen
from random import randint

#turtle = Turtle()
#turtle.speed('fastest')
screen = Screen()
screen.setup(width=500, height=400)
bet = screen.textinput(title="Make your bet",
                       prompt='Which turtle will win the race? (Red, Orange, Yellow, Green, Blue, Purple): ').lower()
colors = ['red', 'orange', 'yellow3', 'green', 'blue', 'purple']
turtles = []

# def move_left():
#     turtle.setheading(180)
#     turtle.forward(10)
#
# def move_right():
#     turtle.setheading(0)
#     turtle.forward(10)
#
# def move_up():
#     turtle.setheading(90)
#     turtle.forward(10)
#
# def move_down():
#     turtle.setheading(270)
#     turtle.forward(10)
#
#
# def clear():
#     turtle.clear()
#     turtle.penup()
#     turtle.home()
#     turtle.pendown()
#
# screen.listen()
# screen.onkey(key='Left', fun=move_left)
# screen.onkey(key='Right', fun=move_right)
# screen.onkey(key='Up', fun=move_up)
# screen.onkey(key='Down', fun=move_down)
# screen.onkey(key='c', fun=clear)


def create_turtles():
    x_cor = -230
    y_cor = -100
    for i in colors:
        turtle = Turtle(shape='turtle')
        turtle.color(i)
        turtle.penup()
        turtle.goto(x_cor, y_cor)
        turtles.append(turtle)
        y_cor += 40

create_turtles()
running = True
while running:
    for t in turtles:
        t.forward(randint(0, 10))

        if t.xcor() > 230:
            winner = t.pencolor()
            if winner == bet:
                print(f'Your turtle has won! The winner is {winner}.')
            else:
                print(f'Your turtle has lost! The winner is {winner}')
            running = False
            break


screen.exitonclick()
