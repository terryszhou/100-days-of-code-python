# try:
#     file = open("a_file.txt")
#     a_dictionary = {"key": "value"}
#     print(a_dictionary["key"])
# except FileNotFoundError:
#     file = open("a_file.txt", "w")
#     file.write("Something")
# except KeyError as error_message:
#     print(f"The key {error_message} does not exist")
# else:
#     content = file.read()
#     print(content)
# finally:
#     file.close()
#     print("File was closed.")
# 
# height = float(input("Height: "))
# weight = int(input("Weight: "))

# if height > 3:
#     raise ValueError("Human Height should not be over 3 meters.")

# bmi = weight / height ** 2
# print(bmi)

# - - - - - - - EXERCISE 1 - - - - - - - #
fruits = ["Apple", "Pear", "Orange"]

def make_pie(index):
    try: 
        fruit = fruits[index]
    except IndexError:
        print("Pie not found.")
    else:
        print(fruit + " pie")

# make_pie(4)

# - - - - - - - EXERCISE 2 - - - - - - - #
facebook_posts = [
    {'Likes': 21, 'Comments': 2}, 
    {'Likes': 13, 'Comments': 2, 'Shares': 1}, 
    {'Likes': 33, 'Comments': 8, 'Shares': 3}, 
    {'Comments': 4, 'Shares': 2}, 
    {'Comments': 1, 'Shares': 1}, 
    {'Likes': 19, 'Comments': 3}
]

def like_counter():
    total_likes = 0
    for post in facebook_posts:
        try:
            total_likes = total_likes + post['Likes']
        except KeyError:
            pass
    print(total_likes)

# like_counter()

# - - - - - - - EXERCISE 3 - - - - - - - #
import pandas

data = pandas.read_csv("nato_phonetic_alphabet.csv")
phonetic_dict = {row["letter"]: row["code"] for (_, row) in data.iterrows()}

def nato_alpha():

    word = input("Enter a word: ").upper()
    try:
        output_list = [phonetic_dict[letter] for letter in word]
    except KeyError:
        print("Sorry, only letters in the alphabet please.")
        nato_alpha()
    else:
        print(output_list)

# nato_alpha()