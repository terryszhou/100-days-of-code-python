# DAY 13: DEBUGGING
def odd_or_even():
    number = int(input("Which number do you want to check?"))
    if number % 2 == 0: print("This is an even number")
    else: print("This is an odd number.")

# odd_or_even()

def leap_year():
    year = int(input("Which year do you want to check?"))
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                print(f"{year} is a leap year.")
            else: 
                print (f"{year} is not a leap year.")
        else:
            print(f"{year} is a leap year.")
    else: 
        print (f"{year} is not a leap year.")

# leap_year()

def fizzbuzz():
    for number in range(1,101):
        if number % 3 == 0 and number % 5 == 0:
            print("FizzBuzz")
        elif number % 3 == 0:
            print("Fizz")
        elif number % 5 == 0:
            print("Buzz")
        else:
            print(number)

# fizzbuzz()

# DAY 14: HIGHER LOWER GAME PROJECT
from game_data import data
import random

testlist = [1,2]

def higher_lower():
    print("Welcome to Higher/Lower!")
    person_a = random.choice(data)
    game_active = True
    score = 0
    while game_active:
        person_b = random.choice(data)
        if person_b == person_a:
            continue
        answer = ""
        if person_a['follower_count'] > person_b['follower_count']:
            answer += "lower"
        else:
            answer += "higher"
        print("Who has more followers?")
        print(f"{person_a['name']}, a {person_a['description']} from {person_a['country']} with {person_a['follower_count']} followers...?")
        print(f"...Or {person_b['name']}, a {person_b['description']} from {person_b['country']}?")
        you_decide = input(f"Do you think {person_b['name']} has a higher or lower follower count? Type 'higher' or 'lower'.\n").lower()
        if you_decide == answer:
            print("You got it!")
            score += 1
            person_a = person_b
        else:
            print(f"You lose! You scored {score}")
            play_again = input("Play again? Type 'yes' or 'no'.\n").lower()
            if play_again == "yes":
                higher_lower()
            else:
                game_active = False

higher_lower()


