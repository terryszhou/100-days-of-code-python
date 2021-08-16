from turtle import Screen, Turtle

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")

for i in range(0,3):
    snek = Turtle(shape="square")
    snek.color("white")
    snek.penup()
    snek.goto(0 - 20*i, 0)

def snake_game():
    pass

# snake_game()


screen.exitonclick()