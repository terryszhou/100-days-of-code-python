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
scoreboard = Scoreboard()

def turtle_crosser():
    screen.listen()
    screen.onkey(player.up, "Up")
    screen.onkey(player.down, "Down")
    game_is_on = True
    while game_is_on:
        screen.update()
        player.reset()
        scoreboard.update_scoreboard()
        car.move()
        
        # Detect Next Level
        if player.ycor() > 280:
            scoreboard.next_level()

        # Detect Car Collision
        for vehicle in car.car_list:
            if player.distance(vehicle) < 20:
                game_is_on = False
                scoreboard.game_over()



turtle_crosser()

screen.exitonclick()