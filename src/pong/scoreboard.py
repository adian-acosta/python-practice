from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color('white')
        self.penup()
        self.hideturtle()
        self.left_player_score = 0
        self.right_player_score = 0
        self.update_score()
        self.draw_middle()

    def update_score(self):
        self.clear()
        self.goto(-100, 200)
        self.write(self.left_player_score, align='center', font=('Courier', 80, 'normal'))
        self.goto(100, 200)
        self.write(self.right_player_score, align='center', font=('Courier', 80, 'normal'))
        self.draw_middle()

    def draw_middle(self):
        self.goto(0, -300)
        self.setheading(90)
        self.pensize(5)
        for x in range(-300, 300 + 1):
            pos = (x + 300) % 30
            if pos < 10:
                self.pendown()
            else:
                self.penup()
            self.forward(1)
        self.penup()