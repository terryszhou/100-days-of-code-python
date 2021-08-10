# DAY 1: WORKING WITH VARIABLES IN PYTHON TO MANAGE DATA
def band_name_generator():
    print("Welcome to the Band Name Generator.")
    city = input("What's the name of the city you grew up in?\n")
    pet = input("What's your pet's name?\n")
    print(f"Your band name could be {city.capitalize()} {pet.capitalize()}.")

# band_name_generator()

# DAY 2: UNDERSTANDING DATA TYPES AND HOW TO MANIPULATE STRINGS
def tip_calculator():
    print("Welcome to the tip calculator.")
    bill = float(input("What was the total bill? $"))
    tip = float(input("What percentage tip would you like to give? %"))
    split = float(input("How many people are splitting the bill?\n"))
    print(f"Each person should pay: ${'{:.2}'.format(((bill+bill*(tip/100))/split))}")

# tip_calculator()

# DAY 3: CONTROL FLOW AND LOGICAL OPERATORS
def bmi_calculator():
    print("Welcome to the BMI calculator.")
    height = float(input("Enter your height in m: "))
    weight = float(input("Enter your weight in kg: "))
    bmi = round(weight / height ** 2)

    print(f"Your BMI is {bmi}.")
    if bmi < 18.5: print("You are underweight.")
    elif bmi < 25: print("You have a normal weight.")
    elif bmi < 30: print("You are overweight.")
    elif bmi < 35: print("You are obese.")
    else: print("You are clinically obese.")

# bmi_calculator()

def leap_year():
    print("Welcome to the Leap Year calculator.")
    year = int(input("Which year do you want to check?\n"))
    if year % 4 == 0:
        if year % 100 != 0 or year % 400 == 0:
            print(f"The year {year} is a leap year.")
        else: 
            print(f"The year {year} is not a leap year.")
    else: 
        print(f"The year {year} is not a leap year.")

# leap_year()

def pizza_order():
    print("Welcome to Python Pizza Deliveries!")
    size = input("What size pizza do you want? S, M, or L\n").upper()
    add_pepperoni = input("Do you want pepperoni? Y/N\n").upper()
    extra_cheese = input("Do you want extra cheese? Y/N\n").upper()
    final_price = 0

    if size == "S": final_price += 15
    elif size == "M": final_price += 20
    elif size == "L": final_price += 25

    if add_pepperoni == "Y":
        if size == "S": final_price += 2
        else: final_price += 3

    if extra_cheese == "Y": final_price += 1

    if size not in "SML" or add_pepperoni not in "YN" or extra_cheese not in "YN":
        reorder = input("Looks like you ordered wrong, pardner! Wanna try again? Y/N\n").upper()
        if reorder == "Y": pizza_order()
        else: print("Seeya, loser!")
    else:
        print(f"Your final price is ${final_price}.")

# pizza_order()

def love_calculator():
    print("Welcome to the Love Calculator!")
    dict1 = {"t": 0, "r": 0, "u": 0, "e": 0}
    dict2 = {"l": 0, "o": 0, "v": 0, "e": 0}
    name1 = input("What is your name?\n").lower()
    name2 = input("What is their name?\n").lower()

    for i in name1:
        if i in dict1: dict1[i] += 1
        if i in dict2: dict2[i] += 1

    for j in name2:
        if j in dict1: dict1[j] += 1
        if j in dict2: dict2[j] += 1

    num1 = str(sum(dict1.values()))
    num2 = str(sum(dict2.values()))
    love_score = int(num1 + num2)

    if love_score < 10 or love_score > 90:
        print(f"Your love score is {love_score}%. You go together like Coke and Mentos.")
    elif love_score > 40 and love_score < 50:
        print(f"Your love score is {love_score}%. Y'all are all right together.")
    else:
        print(f"Your true love match is {love_score}%")

# love_calculator()

def treasure_island():
    print('''
    *******************************************************************************
            |                   |                  |                     |
    _________|________________.=""_;=.______________|_____________________|_______
    |                   |  ,-"_,=""     `"=.|                  |
    |___________________|__"=._o`"-._        `"=.______________|___________________
            |                `"=._o`"=._      _`"=._                     |
    _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
    |                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
    |___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
            |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
    _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
    |                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
    |___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
    ____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
    /______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
    ____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
    /______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
    ____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
    /______/______/______/______/______/______/______/______/______/______/______/_
    *******************************************************************************
    ''')
    print(("Welcome to Treasure Island").upper())
    print("Your mission is to find the treasure.")
    left_right = input("You're at a crossroads. Where do you want to go? Type LEFT or RIGHT.\n").lower()
    if left_right == "right":
        print("You wandered into a forest of flesh-eating trees. Game Over.")
    else:
        wait_swim = input("You come to a lake. There is an island in the middle of the lake. Do you WAIT for a boat or SWIM across?\n").lower()
        if wait_swim == "swim":
            print("The lake is full of sleeping draught. You become sleepier and sleepier as you cross, until you sink and drown. Game Over.")
        else:
            ryb = input("you arrive at the island unharmed. There is a house with three doors: one RED, one YELLOW, and one BLUE. Which color do you chose?\n").lower()
            if ryb == "blue":
                print("You enter a room full of beasts. Game Over.")
            elif ryb == "red":
                print("You enter a room full of nothing. Absolutely nothing. You fall into nothingness forever. Game Over.")
            else:
                print("You discover a room with a golden chest in the middle. You win!")

    if left_right != "left" or wait_swim != "wait" or ryb != "yellow":
        play_again = input("Do you want to play again? YES/NO\n").lower()
        if play_again == "yes":
            treasure_island()

# treasure_island()

# DAY 4: RANDOMIZATION AND PYTHON LISTS
import random

def coin_toss():
    if random.randint(0,1) == 1:
        return "Heads"
    return "Tails"

# print(coin_toss())

def banker_roulette():
    banker_list = input("Who is eating today?\n").split(", ")
    randnum = random.randint(1, len(banker_list))
    return f"{banker_list[randnum - 1]} is paying today."

# print(banker_roulette())

def treasure_map():
    row1 = ["◼︎","◼︎","◼︎"]
    row2 = ["◼︎","◼︎","◼︎"]
    row3 = ["◼︎","◼︎","◼︎"]
    map = [row1, row2, row3]
    print("Welcome to Treasure Map!")
    print(f"{row1}\n{row2}\n{row3}")
    print("Where do you want to put the treasure?")
    row_position = int(input("Which row? (1, 2, or 3)\n"))
    col_position = int(input("Which column? (1, 2, or 3)\n"))
    if col_position not in [1, 2, 3] or row_position not in [1, 2, 3]:
        retry = input("Looks like you buried your treasure wrong! Try again? (Yes/No)\n").lower()
        if retry == "yes":
            treasure_map()
    map[row_position - 1][col_position - 1] = "X"
    print(f"{row1}\n{row2}\n{row3}")
    print("Treasure buried!")

# treasure_map()

def rock_paper_scissors():
    print("Welcome to Rock, Paper, Scissors!")
    player_input = input("Which do you choose? Type 'ROCK', 'PAPER', or 'SCISSORS'\n").upper()
    computer_input = random.choice(["ROCK", "PAPER", "SCISSORS"])
    win_state = {"ROCK":"SCISSORS", "SCISSORS":"PAPER", "PAPER":"ROCK"}
    result = f"You chose {player_input}, and the computer chose {computer_input}."

    if player_input not in ("ROCK", "PAPER", "SCISSORS"):
        retry = input("Looks like you entered something wrong! Try again? (YES/NO)\n").upper()
        if retry == "YES": rock_paper_scissors()
        else:  print("Goodbye!")
    elif computer_input == player_input:
        print(result + " Tie!")
    elif computer_input == win_state[player_input]:
        print(result + " You win!")
    else:
        print(result + " You lose!")

# rock_paper_scissors()

# DAY 5: PYTHON LOOPS
def height_calculator():
    print("Welcome to the Average Height Calculator!")
    height_list = input("Enter a list of heights (ie: 180 124 165 etc)\n").split(" ")
    sum = 0
    student_count = 0
    for i in height_list:
        sum += int(i)
        student_count += 1
    print(f"The average height is {round(sum/student_count)}.")

# height_calculator()

def highest_score():
    print("Welcome to the Highest Score Calculator!")
    score_list = input("Enter a list of scores (ie: 78 65 89 etc)\n").split(" ")
    highest_score = 0
    for i in score_list:
        if int(i) > highest_score:
            highest_score = int(i)
    print(f"The highest score was {highest_score}.")

# highest_score()

def even_adder():
    total_sum = 0
    for i in range(0, 100, 2):
        total_sum += i
    print(total_sum)

# even_adder()

def even_adder_2():
    print("Welcome to the Even Number Adder!")
    low_num = int(input("Enter your lowest number.\n"))
    high_num = int(input("Enter your highest number.\n"))
    total_sum = 0
    for i in range (low_num, high_num):
        if i % 2 == 0:
            total_sum += i
    print(f"The sum of all even numbers between {low_num} and {high_num} is {total_sum}.")

# even_adder_2()

def fizzbuzz():
    for i in range(1, 101):
        if i % 3 == 0 and i % 5 == 0:
            print("FizzBuzz")
        elif i % 3 == 0:
            print("Fizz")
        elif i % 5 == 0:
            print("Buzz")
        else: 
            print(i)

# fizzbuzz()

import string

def password_generator():
    print("Welcome to the PyPassword Generator!")

    alpha_list = list(string.ascii_letters)
    sym_list = list(string.punctuation)
    num_list = list(string.digits)

    pass_len = int(input("How many characters would you like in your password?"))
    sym_len = int(input("How many symbols would you like?"))
    num_len = int(input("How many numbers?"))

    password = ""

    for i in range(0, pass_len - sym_len - num_len):
        password += random.choice(alpha_list)
    for j in range(0, sym_len):
        password += random.choice(sym_list)
    for k in range(0, num_len):
        password += random.choice(num_list)

    shuffled_password = "".join(random.sample(password, len(password)))
    print(f"Your random password is {shuffled_password}")

password_generator()



    




