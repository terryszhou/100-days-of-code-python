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

# higher_lower()

# DAY 15: LOCAL DEVELOPMENT ENVIRONMENTS AND COFFEE MACHINE PROJECT
MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "milk": 0,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

def coffee_machine():
    resources = {
        "water": 300,
        "milk": 200,
        "coffee": 100,
    }
    money = 0
    machine_on = True
    while machine_on:
        coffee_type = input("What would you like? (espresso/latte/cappuccino): ")
        if coffee_type == "report":
            for resource in resources:
                if resource == "coffee":
                    print(f"{resource.title()}: {resources[resource]}g")
                else:
                    print(f"{resource.title()}: {resources[resource]}ml")
            print(f"Money: ${money:.2f}")
        else:
            insufficient = []
            for item in MENU[coffee_type]["ingredients"]:
                if MENU[coffee_type]["ingredients"][item] > resources[item]:
                    insufficient.append(item)
                    print(f"Sorry, there is not enough {item}.")
                    machine_on = False
            if insufficient == []:
                print("Please insert coins.")
                quarters = int(input("How many quarters?: "))
                dimes = int(input("How many dimes?: "))
                nickels = int(input("How many nickels?: "))
                pennies = int(input("How many pennies?: "))
                user_money = quarters*.25 + dimes*.1 + nickels*.05 + pennies*.01
                if user_money < MENU[coffee_type]["cost"]:
                    print("Sorry, that's not enough money. Money refunded.")
                    machine_on = False
                else:
                    for resource in resources:
                        resources[resource] -= MENU[coffee_type]["ingredients"][resource]
                    money += MENU[coffee_type]["cost"]
                    if user_money - MENU[coffee_type]["cost"] != 0:
                        print(f"Here is ${user_money - MENU[coffee_type]['cost']:.2f} in change.")
                    print(f"Here is your {coffee_type}. Enjoy!")

# coffee_machine()

# DAY 16: OBJECT-ORIENTED PROGRAMMING (OOP)
# from turtle import Turtle, Screen
# timmy = Turtle()
# timmy.shape('turtle')
# timmy.color('red')
# timmy.fd(100)

# my_screen = Screen()
# my_screen.exitonclick()

# from prettytable import PrettyTable

# poke_table = PrettyTable(["Pokemon Name", "Type"])
# poke_table.add_row(["Pikachu", "Electric"])
# poke_table.add_row(["Squirtle", "Water"])
# poke_table.add_row(["Charmander", "Fire"])
# poke_table.align = "l"

# print(poke_table)

from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()

def oop_coffee_machine():
    machine_on = True
    while machine_on:
        my_choice = input(f"What would you like? ({menu.get_items()}): ")
        if my_choice == "off":
            machine_on = False
        elif my_choice == "report":
            coffee_maker.report()
            money_machine.report()
        else:
            my_coffee = menu.find_drink(my_choice)
            if coffee_maker.is_resource_sufficient(my_coffee):
                if money_machine.make_payment(my_coffee.cost):
                    coffee_maker.make_coffee(my_coffee)

oop_coffee_machine()