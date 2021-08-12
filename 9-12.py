import random

# DAY 9: DICTIONARIES, NESTING, AND THE SECRET AUCTION
student_scores = {
    "Harry": 81,
    "Ron": 78,
    "Hermione": 99,
    "Draco": 74,
    "Neville": 62,
}

def score_grader(dict):
    student_grades = {}
    for student in dict:
        if dict[student] >= 91:
            student_grades[student] = "Outstanding"
        elif dict[student] >= 81:
            student_grades[student] = "Exceeds Expectations"
        elif dict[student] >= 71:
            student_grades[student] = "Acceptable"
        else:
            student_grades[student] = "Fail"
    print(student_grades)

# score_grader(student_scores)

# SIMPLE DICTIONARY
capitals = {
    "France": "Paris",
    "Germany": "Berlin",
}

# NESTING LISTS IN DICTIONARIES
travel_log = {
    "France": ["Paris", "Lille", "Fontainebleau"],
    "Germany": ["Berlin", "Hamburg", "Stuttgart"]
}

# NESTING DICTIONARIES IN DICTIONARIES
travel_log2 = {
    "France": {"cities_visited": ["Paris", "Lille", "Fontainebleau"]},
    "Germany": {"cities_visited": ["Berlin", "Hamburg", "Stuttgart"]},
}

# NESTING DICTIONARIES IN LISTS
travel_log3 = [
    {
        "country": "France", 
        "visits": 12,
        "cities_visited": ["Paris", "Lille", "Dijon"],
    },
    {
        "country": "Germany",
        "visits": 5,
        "cities_visited": ["Berlin", "Hamburg", "Stuttgart"],
    },
]

def add_new_country(country, visits, cities_visited):
    travel_log3.append(
        {
            "country": country,
            "visits": visits,
            "cities_visited": cities_visited
        },
    )
    print(travel_log3)

# add_new_country("Russia", 2, ["Moscow", "Saint Petersburg"])

bid_dict = {}

def highest_bid():
    print("Welcome to the Secret Auction Program")
    max_bid = 0
    name = input("What is your name?\n").title()
    bid = int(input("What is your bid? (enter number)\n"))
    if bid > max_bid:
        max_bid = bid
    bid_dict[name] = f"${bid}"
    other_bidder = input("Are there any other bidders? (yes/no)\n").lower()
    if other_bidder == "yes":
        highest_bid()
    else:
        for bidder in bid_dict:
            if int(bid_dict[bidder][1:]) == max_bid:
                print(f"The winner is {bidder} with a bid of {bid_dict[bidder]}!")

# highest_bid()

# DAY 10: FUNCTIONS WITH OUTPUTS
def days_in_month():
    '''Enter a year and month and return the 
    number of days in that month of that year'''
    month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    year = int(input("Enter a year: "))
    month = int(input("Enter a month (1-12): "))
    days = month_days[month - 1]
    if year % 4 == 0:
        if year % 100 != 0 or year % 400 == 0:
            days = 29
    return days

# print(days_in_month())

def calculator():
    n1 = int(input("What's the first number?\n"))
    continue_calc = True
    while continue_calc:
        operation = input("What's the operation? (+, -, *, /)\n")
        n2 = int(input("What's the next number?\n"))
        operations = {
            "+": n1 + n2,
            "-": n1 - n2,
            "*": n1 * n2,
            "/": n1 / n2
        }
        answer = operations[operation]
        print(f"{n1} {operation} {n2} = {answer}")
        again = input(f"Continue calculating with {answer}? (yes/no/new)\n").lower()
        if again == "yes": n1 = answer
        elif again == "new": calculator()
        else: return "Bye!"

# print(calculator())

def blackjack():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    game_active = True
    play_game = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ").lower()
    while game_active:
        if play_game == "y":
            player_cards = []
            computer_cards = []
            for i in range (0,2):
                player_cards.append(random.choice(cards))
                computer_cards.append(random.choice(cards))
        else: return
        print(f"Your cards: {player_cards}. Current score: {sum(player_cards)}")
        print(f"Computer's first card: {computer_cards[0]}")
        next_card = input("Type 'y' to get another card, type 'n' to pass: ").lower()
        if next_card == "y":
            player_cards.append(random.choice(cards))
        computer_cards.append(random.choice(cards))
        if sum(player_cards) > 21 or sum(computer_cards) > 21:
            print(f"Your final hand: {player_cards}. Final score: {sum(player_cards)}")
            print(f"Computer's final hand: {computer_cards}. Final score: {sum(computer_cards)}")
            if sum(player_cards) > 21:
                print("You went over. You lose!")
            else:
                print("The computer went over. You win!")
            another_game = input("Do you want to play another game of Blackjack? Type 'y' or 'n': ").lower()
            if another_game == "y":
                # player_cards = computer_cards = []
                play_game = "y"
            else: return

blackjack()




