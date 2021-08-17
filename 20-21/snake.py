from turtle import Turtle

class Snake:
    '''Snake Class'''
    def __init__(self):
        self.snek_list = []
        self.create_snake()
        self.head = self.snek_list[0]
        self.move_distance = 20

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

# class SnakeScreen:
#     def __init__(self):
#         self.screen = Screen()
#         self.screen.setup(width=600, height=600)
#         self.screen.bgcolor("black")
#         self.screen.title("My Snake Game")
#         self.screen.tracer(0)
#         self.snake = Snake()

#     def listen(self):
#         self.screen.listen()

#     def movement(self):
#         self.screen.onkey(self.snake.up, "Up")
#         self.screen.onkey(self.snake.left, "Left")
#         self.screen.onkey(self.snake.down, "Down")
#         self.screen.onkey(self.snake.right, "Right")

#     def update(self):
#         self.screen.update()