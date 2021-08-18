from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("white")
screen.title("Turtle Crosser")
screen.tracer(0)

player = Player()
car = CarManager()

def turtle_crosser():
    screen.listen()
    screen.onkey(player.up, "Up")
    screen.onkey(player.down, "Down")
    game_is_on = True
    while game_is_on:
        player.reset()
        screen.update()
        car.move()


turtle_crosser()

screen.exitonclick()