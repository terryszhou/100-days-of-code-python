from turtle import Turtle
from random import choice, randint

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 5

class CarManager:
    def __init__(self):
        self.car_list = []
        self.create_cars()

    def create_cars(self):
        for i in range(15):
            self.add_car()

    def add_car(self):
        car = Turtle(shape="square")
        car.shapesize(stretch_wid=1, stretch_len=2)
        car.color(choice(COLORS))
        car.penup()
        car.goto(randint(-280,281), randint(-280,281))
        self.car_list.append(car)

    def move(self):
        for car in self.car_list:
            new_x = car.xcor() - STARTING_MOVE_DISTANCE
            car.goto(new_x, car.ycor())
            if car.xcor() < -310:
                car.color(choice(COLORS))
                car.goto(300, randint(-280,281))

    def speed_up(self, level):
        for car in self.car_list:
            new_x  = car.xcor() - STARTING_MOVE_DISTANCE - MOVE_INCREMENT*level
            car.goto(new_x, car.ycor())


