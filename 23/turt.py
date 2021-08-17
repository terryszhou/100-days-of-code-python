from turtle import Turtle

class Turt(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.color("green")
        self.goto(0,-280)
        self.setheading(90)