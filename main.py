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
    height = float(input("Enter your height in m: "))
    weight = float(input("Enter your weight in kg: "))
    bmi = round(weight / height ** 2)
    
    print(f"Your BMI is {bmi}.")
    if bmi < 18.5: print("You are underweight.")
    elif bmi < 25: print("You have a normal weight.")
    elif bmi < 30: print("You are overweight.")
    elif bmi < 35: print("You are obese.")
    else: print("You are clinically obese.")

bmi_calculator()