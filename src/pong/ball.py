from turtle import Turtle

SPEED = 10

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.color('white')
        self.x_velocity = SPEED
        self.y_velocity = SPEED
        self.move_speed = 0.1
        self.penup()

    def move(self):
        x_pos = self.xcor() + self.x_velocity
        if self.ycor() > 280 or self.ycor() < -280:
            self.y_velocity *= -1
        y_pos = self.ycor() + self.y_velocity
        self.goto(x_pos, y_pos)

    def bonk(self):
        self.x_velocity *= -1
        self.move_speed *= 0.9

        x_pos = self.xcor() + self.x_velocity
        y_pos = self.ycor() + self.y_velocity
        self.goto(x_pos, y_pos)

    def reset(self):
        self.x_velocity *= -1
        self.move_speed = 0.1

        self.goto(0, 0)

    def get_ball_speed(self):
        return self.move_speed