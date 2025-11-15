from turtle import Screen
from time import sleep

from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=800, height=600)
screen.title('Pong')
screen.bgcolor('black')
screen.tracer(0)

left_paddle = Paddle(position=(-350, 0))
right_paddle = Paddle(position=(350, 0))
ball = Ball()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(key='w', fun=left_paddle.move_up)
screen.onkey(key='s', fun=left_paddle.move_down)
screen.onkey(key='Up', fun=right_paddle.move_up)
screen.onkey(key='Down', fun=right_paddle.move_down)

running = True
while running:
    sleep(ball.get_ball_speed())
    screen.update()
    ball.move()

    if (ball.distance(left_paddle) < 50 and ball.xcor() < -320) or (
            ball.distance(right_paddle) < 50 and ball.xcor() > 320):
        ball.bonk()

    if ball.xcor() > 410:
        scoreboard.left_player_score += 1
        scoreboard.update_score()
        ball.reset()
        screen.update()
        sleep(1)
    elif ball.xcor() < -410:
        scoreboard.right_player_score += 1
        scoreboard.update_score()
        ball.reset()
        screen.update()
        sleep(1.5)

screen.exitonclick()
