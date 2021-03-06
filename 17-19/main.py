# DAY 17: THE QUIZ PROJECT & THE BENEFITS OF OOP
class User:
    '''First Test Class'''
    def __init__(self, id, username):
        self.id = id
        self.username = username
        self.followers = 0
        self.following = 0

    def follow(self, user):
        user.followers += 1
        self.following += 1

user_1 = User("001", "Terry")
user_2 = User("002", "Angela")
user_1.follow(user_2)

# print(user_1.following, user_2.followers)

from question_data import question_data
from question_models import Question, QuizBrain

question_bank = []
for i in question_data:
    question_bank.append(Question(i["question"], i["correct_answer"]))

quiz_brain = QuizBrain(question_bank)

def quiz_game():
    while quiz_brain.still_has_questions():
        quiz_brain.next_question()
    print("You've completed the quiz!")
    print(f"Your final score was {quiz_brain.score}/{len(quiz_brain.question_list)}.")

# quiz_game()

# DAY 18: TURTLE & THE GRAPHICAL USER INTERFACE
from turtle import Turtle, Screen
from random import randint, randrange, choice

timmy = Turtle()
screen = Screen()
screen.colormode(255)

def random_color():
    R = randrange(256)
    G = randrange(256)
    B = randrange(256)
    timmy.color(R,G,B)

def draw_shape(num_sides):
    timmy.shape("turtle")
    random_color()
    angle = 360/num_sides
    for _ in range(num_sides):
        timmy.forward(100)
        timmy.right(angle)

# for shape_side_n in range(3, 10):
#     draw_shape(shape_side_n)

def random_walk(num_walks):
    timmy.shape("circle")
    timmy.speed("fastest")
    timmy.pensize(10)
    degree_range = [1,2,3,4]
    for _ in range(num_walks):
        random_color()
        timmy.forward(30)
        timmy.right(90 * choice(degree_range))

# random_walk(50)

def spirograph(turn_degree):
    timmy.hideturtle()
    timmy.speed("fastest")
    for _ in range(int(360/turn_degree)):
        random_color()
        timmy.circle(100)
        timmy.setheading(timmy.heading() + turn_degree)

# spirograph(6)

import colorgram

color_list = [(54, 39, 31), (56, 34, 40), (142, 55, 83), (203, 74, 114), (242, 220, 74), (231, 148, 85), (129, 37, 63), (71, 85, 139), (249, 242, 222), (109, 184, 129), (69, 107, 72), (128, 86, 54), (117, 151, 207), (38, 40, 58), (208, 119, 159), (88, 118, 184), (238, 95, 45), (35, 52, 33), (82, 157, 102), (208, 244, 216), (54, 57, 89), (49, 75, 46), (81, 73, 28), (165, 145, 63), (105, 44, 33), (148, 218, 163), (244, 223, 239), (243, 153, 184), (214, 226, 245), (158, 184, 237)]
# colors = colorgram.extract('image.jpg', 30)
# for color in colors:
#     color_list.append((color.rgb[0],color.rgb[1],color.rgb[2]))
# print(color_list)

def hirsch_painting():
    timmy.speed("fastest")
    timmy.penup()
    for i in range(0,10):
        timmy.setpos(-225,-250 + 50*i)
        for _ in range(10):
            timmy.pendown()
            timmy.color(choice(color_list))
            timmy.begin_fill()
            timmy.circle(10)
            timmy.end_fill()
            timmy.penup()
            timmy.forward(50)

# hirsch_painting()

# DAY 19: INSTANCES, STATE, AND HIGHER ORDER FUNCTIONS

def etch_a_sketch():
    def move_forward():
        timmy.forward(10)

    def move_backward():
        timmy.backward(10)

    def turn_left():
        timmy.setheading(timmy.heading() + 10)

    def turn_right():
        timmy.setheading(timmy.heading() - 10)

    def clear():
        timmy.clear()
        timmy.penup()
        timmy.home()
        timmy.pendown()

    screen.listen()
    screen.onkey(key="w", fun=move_forward)
    screen.onkey(key="a", fun=turn_left)
    screen.onkey(key="s", fun=move_backward)
    screen.onkey(key="d", fun=turn_right)
    screen.onkey(key="c", fun=clear)

# etch_a_sketch()

def turtle_race():
    is_race_on = False
    timmy.hideturtle()
    screen.setup(width=500, height=400)
    user_bet = screen.textinput(title="Make Your Bet", prompt="Which turtle will win the race? Enter a color: ")
    colors = ["red", "orange", "yellow", "green", "blue", "purple"]
    all_turtles = []
    for turtle_index in range(0,6):
        new_turtle = Turtle(shape="turtle")
        new_turtle.color(colors[turtle_index])
        new_turtle.penup()
        new_turtle.goto(x=-230, y=-100 + turtle_index*42)
        all_turtles.append(new_turtle)
    
    if user_bet: is_race_on = True

    while is_race_on:
        for turtle in all_turtles:
            if turtle.xcor() > 230:
                is_race_on = False
                winning_color = turtle.pencolor()
                if winning_color == user_bet:
                    print(f"You've won! The {winning_color} turtle is the winner!")
                else:
                    print(f"You've lost! The {winning_color} turtle is the winner!")
            else:
                turtle.forward(randint(0,10))

# turtle_race()

screen.exitonclick()

