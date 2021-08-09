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

tip_calculator()