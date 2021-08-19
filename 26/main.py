from random import randint

numbers = [1, 1, 2, 3, 5, 8, 13, 21]
squared_numbers = [n**2 for n in numbers]
even_numbers = [n for n in numbers if n%2 == 0]

def my_solve(file_a, file_b):
    file1_list = []
    file2_list = []

    with open(file_a) as file1:
        for i in file1.read():
            file1_list.append(i)

    with open(file_b) as file2:
        for i in file2.read():
            file2_list.append(i)

    result = [int(n) for n in file1_list if n in file2_list and n != "\n"]
    print(result)

# my_solve("file1.txt", "file2.txt")

names = ["Alex", "Beth", "Catherine", "Delaney", "Elliot", "Francine"]
student_scores = {name:randint(0,101) for name in names}
passed_students = {name:score for (name,score) in student_scores.items() if score >= 70}

sentence = "What is the Airspeed Velocity of an Unladen Swallow?"
sentence_dict = {word:len(word) for word in sentence.split()}

weather_c = {
    "Monday": 12,
    "Tuesday": 14,
    "Wednesday": 15,
    "Thursday": 14,
    "Friday": 21,
    "Saturday": 22,
    "Sunday": 24,
}
weather_f = {day:(temp_c* 9/5) + 32 for (day,temp_c) in weather_c.items()}






