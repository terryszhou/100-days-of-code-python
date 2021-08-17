from turtle import Screen
from turt import Turt

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("white")
screen.title("Turtle Crosser")
screen.tracer(0)

turt = Turt()

def turtle_crosser():
    screen.listen()
    screen.onkey(turt.up, "Up")
    screen.onkey(turt.down, "Down")
    game_is_on = True
    while game_is_on:
        screen.update()

turtle_crosser()

screen.exitonclick()