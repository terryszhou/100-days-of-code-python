from turtle import Screen, Turtle

STARTING_POSITION = (0,-280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280

class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.color("green")
        self.goto(STARTING_POSITION)
        self.setheading(90)

    def up(self):
        self.setheading(90)
        new_y = self.ycor() + MOVE_DISTANCE
        self.goto(self.xcor(), new_y)

    def down(self):
        self.setheading(270)
        new_y = self.ycor() - MOVE_DISTANCE
        if self.ycor() > -270:
            self.goto(self.xcor(), new_y)

    def reset(self):
        if self.ycor() > 280:
            self.goto(STARTING_POSITION)