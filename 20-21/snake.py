from turtle import Turtle

POSITIONS = [(0,0), (-20,0), (-40,0)]

class Snake:
    '''Snake Class'''
    def __init__(self):
        self.snek_list = []
        self.create_snake()
        self.head = self.snek_list[0]
        self.move_distance = 20

    def create_snake(self):
        for position in POSITIONS:
            self.add_segment(position)

    def add_segment(self, position):
        snek = Turtle(shape="square")
        snek.color("white")
        snek.penup()
        snek.goto(position)
        self.snek_list.append(snek)

    def extend(self):
        self.add_segment(self.snek_list[-1].position())

    def move(self):
        for seg_num in range(len(self.snek_list) - 1, 0, -1):
            new_x = self.snek_list[seg_num - 1].xcor()
            new_y = self.snek_list[seg_num - 1].ycor()
            self.snek_list[seg_num].goto(new_x, new_y)
        self.head.forward(self.move_distance)

    def up(self):
        if self.head.heading() != 270:
            self.head.setheading(90)

    def left(self):
        if self.head.heading() != 0:
            self.head.setheading(180)

    def down(self):
        if self.head.heading() != 90:
            self.head.setheading(270)

    def right(self):
        if self.head.heading() != 180:
            self.head.setheading(0)