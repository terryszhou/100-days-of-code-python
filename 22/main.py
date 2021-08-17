from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
from score import Scoreboard

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("My Pong Game")
screen.tracer(0)

l_paddle = Paddle((-350,0))
r_paddle = Paddle((350,0))
ball = Ball()
scoreboard = Scoreboard()

def pong():
    screen.listen()
    screen.onkey(l_paddle.go_up, "w")
    screen.onkey(l_paddle.go_down, "s")
    screen.onkey(r_paddle.go_up, "Up")
    screen.onkey(r_paddle.go_down, "Down")
    game_is_on = True
    while game_is_on:
        screen.update()
        ball.move()
        ball.bounce_wall()
        if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
            ball.bounce_paddle()
        if ball.xcor() > 380:
            scoreboard.l_point()
            ball.reset()
        elif ball.xcor() < -380:
            scoreboard.r_point()
            ball.reset()

pong()

screen.exitonclick()
