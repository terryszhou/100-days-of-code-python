from turtle import Turtle

class Snake:
    '''Snake Class'''
    def __init__(self):
        self.snek_list = []
        self.create_snake()

    def create_snake(self):
        for i in range(0,3):
            snek = Turtle(shape="square")
            snek.color("white")
            snek.penup()
            snek.goto(0 - 20*i, 0)
            self.snek_list.append(snek)

    def move(self):
        for seg_num in range(len(self.snek_list) - 1, 0, -1):
            new_x = self.snek_list[seg_num - 1].xcor()
            new_y = self.snek_list[seg_num - 1].ycor()
            self.snek_list[seg_num].goto(new_x, new_y)
        self.snek_list[0].forward(20)