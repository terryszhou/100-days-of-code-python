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
from question_model import Question
from quiz_brain import QuizBrain

question_bank = []
for i in question_data:
    question_bank.append(Question(i["question"], i["correct_answer"]))

quiz_brain = QuizBrain(question_bank)

def quiz_game():
    while quiz_brain.still_has_questions():
        quiz_brain.next_question()
    print("You've completed the quiz!")
    print(f"Your final score was {quiz_brain.score}/{len(quiz_brain.question_list)}.")

quiz_game()


