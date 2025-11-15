from turtle import Turtle

MOVE_DISTANCE = 20

class Paddle(Turtle):
    def __init__(self, position):
        super().__init__()
        self.shape('square')
        self.color('white')
        self.turtlesize(stretch_wid=5, stretch_len=1)
        self.penup()
        self.goto(position)

    def move_up(self):
        if self.ycor() < 280:
            self.goto(self.xcor(), self.ycor() + MOVE_DISTANCE)

    def move_down(self):
        if self.ycor() > -280:
            self.goto(self.xcor(), self.ycor() - MOVE_DISTANCE)