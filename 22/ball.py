from turtle import Turtle

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.color("white")
        self.x_move = 5
        self.y_move = 5

    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def bounce_wall(self):
        if self.ycor() > 280 or self.ycor() < -280:
            self.y_move *= -1

    def bounce_paddle(self):
        self.x_move *= -1
    
    def reset(self):
        self.goto(0,0)
        self.x_move *= -1