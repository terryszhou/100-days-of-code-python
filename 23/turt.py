from turtle import Turtle

class Turt(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.color("green")
        self.goto(0,-280)
        self.setheading(90)

    def up(self):
        self.setheading(90)
        new_y = self.ycor() + 20
        self.goto(self.xcor(), new_y)

    def down(self):
        self.setheading(270)
        new_y = self.ycor() - 20
        self.goto(self.xcor(), new_y)