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
