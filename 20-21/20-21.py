from turtle import Screen, Turtle
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

def snake_game():
    snek_list = []
    for i in range(0,3):
        snek = Turtle(shape="square")
        snek.color("white")
        snek.penup()
        snek.goto(0 - 20*i, 0)
        snek_list.append(snek)
    game_is_on = True
    while game_is_on:
        screen.update()
        time.sleep(1)
        for snek in snek_list:
            snek.forward(20)


snake_game()


screen.exitonclick()