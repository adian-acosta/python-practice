from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.color('white')
        self.hideturtle()
        self.teleport(0, 270)
        self.score = 0
        self.update_score()

    def increment_score(self):
        self.score += 1
        self.update_score()

    def update_score(self):
        self.clear()
        self.write(f'Score: {self.score}', align='center', font=('arial', 20, 'normal'))

    def game_over(self):
        self.teleport(0, 0)
        self.write('GAME OVER', align='center', font=('arial', 20, 'normal'))