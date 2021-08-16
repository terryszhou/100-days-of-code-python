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
        time.sleep(0.1)
        for seg_num in range(len(snek_list) - 1, 0, -1):
            new_x = snek_list[seg_num - 1].xcor()
            new_y = snek_list[seg_num - 1].ycor()
            snek_list[seg_num].goto(new_x, new_y)
        snek_list[0].forward(20)
        snek_list[0].left(90)


snake_game()


screen.exitonclick()