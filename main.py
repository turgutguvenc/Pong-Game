from turtle import Screen, Turtle
import time
from paddle import Paddle
from ball import Ball
from scoreboard import ScoreBoard

screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.tracer(0)  # turning off the tracer
screen.title("Pong")
r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball = Ball((0, 0))
score = ScoreBoard()

screen.listen()
screen.onkey(l_paddle.up, "w")
screen.onkey(l_paddle.down, "s")
screen.onkey(r_paddle.up, "Up")
screen.onkey(r_paddle.down, "Down")

game_is_on = True

while game_is_on:
    screen.update()  # once each time snake move we get to screen update
    time.sleep(0.1)
    ball.move()

    # Detecting the collision with the walls
    if ball.ycor() > 285 or ball.ycor() < -285:
        ball.bounce_y()

    # Detect collision with paddle
    if (ball.distance(r_paddle) < 50 and ball.xcor() > 320) or (ball.distance(l_paddle) < 50 and ball.xcor() > -320):
        ball.bounce_x()


    # Detect R paddle misses
    if ball.xcor() > 380:
        ball.reset_position()
        score.l_point()

    # Detect L paddle misses
    if ball.xcor() < -380:
        ball.reset_position()
        score.r_point()



screen.exitonclick()
