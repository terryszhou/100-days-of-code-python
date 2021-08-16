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
from random import random, randrange, choice

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
    timmy.speed("fastest")
    for _ in range(int(360/turn_degree)):
        random_color()
        timmy.circle(100)
        timmy.setheading(timmy.heading() + turn_degree)

spirograph(6)



screen.exitonclick()

