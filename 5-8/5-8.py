import random
import math
import string
import hangman_art
import hangman_words

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

def password_generator():
    print("Welcome to the PyPassword Generator!")

    alpha_list = list(string.ascii_letters)
    sym_list = list(string.punctuation)
    num_list = list(string.digits)

    pass_len = int(input("How many characters would you like in your password?\n"))
    sym_len = int(input("How many symbols would you like?\n"))
    num_len = int(input("How many numbers?\n"))

    password = ""

    for i in range(pass_len - sym_len - num_len):
        password += random.choice(alpha_list)
    for j in range(sym_len):
        password += random.choice(sym_list)
    for k in range(num_len):
        password += random.choice(num_list)

    shuffled_password = "".join(random.sample(password, len(password)))
    print(f"Your random password is {shuffled_password}")

# password_generator()

# DAY 6: PYTHON LOOPS: PYTHON FUNCTIONS AND KAREL
# n/a; all online

# DAY 7: HANGMAN
def random_word():
    word_list = ["aardvark", "baboon", "camel"]
    chosen_word = random.choice(word_list)
    guess_letter = input("Guess a letter, and I'll tell you if it's in my randomly chosen word!\n").lower()
    
    if guess_letter not in chosen_word:
        print("Nope!")
    else: print("Yes it is!")

# random_word()

def replace_blank():
    word_list = ["aardvark", "baboon", "camel"]
    chosen_word = random.choice(word_list)
    display = []
    for letter in chosen_word:
        display += "_"
    print(f"I'm thinking of a word!\n{display}")
    guess = input("Guess a letter, and I'll tell you if it's in my word!\n").lower()
    for position, letter in enumerate(chosen_word):
        if guess == letter:
            display[position] = guess
    print(display)

# replace_blank()

def check_win():
    win = False
    word_list = ["aardvark", "baboon", "camel"]
    chosen_word = random.choice(word_list)

    display = []
    for letter in chosen_word:
        display += "_"

    print(f"I'm thinking of a word!\n{display}")

    while win == False:
        guess = input("Guess a letter, and I'll tell you if it's in my word!\n").lower()
        for position, letter in enumerate(chosen_word):
            if guess == letter:
                display[position] = guess
        print(display)
        if "_" not in display:
            win = True

    answer = "".join(display)

    if win == True:
        print(f"You win! The word was '{answer}'!")

# check_win()

def player_lives():
    end_of_game = False
    word_list = ["aardvark", "baboon", "camel"]
    chosen_word = random.choice(word_list)
    lives = 6
    display = []
    for letter in chosen_word:
        display += "_"
    answer = "".join(display)

    print(f"I'm thinking of a word!\n{display}")

    while end_of_game == False:
        guess = input("Guess a letter, and I'll tell you if it's in my word!\n").lower()
        for position, letter in enumerate(chosen_word):
            if guess == letter:
                display[position] = guess
        if guess not in display:
            lives -= 1
        print(display)
        print(f"You have {lives} lives left.")
        if "_" not in display:
            end_of_game = True
            print(f"You win! The word was '{answer}'!")
        if lives == 0:
            end_of_game = True
            print(f"You lose! The word was '{answer}'!")

# player_lives()

def hangman():
    end_of_game = False
    chosen_word = random.choice(hangman_words.word_list)
    lives = 6
    display = []
    for letter in chosen_word:
        display += "_"

    print(hangman_art.logo)
    while end_of_game == False:
        guess = input("Guess a letter, and I'll tell you if it's in my word!\n").lower()
        if guess in display:
            print("You've already guessed that!")
        for position, letter in enumerate(chosen_word):
            if guess == letter:
                display[position] = guess
        if guess not in display:
            lives -= 1
        print(hangman_art.stages[lives])
        print(display)
        if "_" not in display:
            end_of_game = True
            print(f"You win! The word was '{chosen_word}'!")
        if lives == 0:
            end_of_game = True
            print(f"You lose! The word was '{chosen_word}'!")

# hangman()

# DAY 8:  FUNCTION PARAMETERS & CAESAR CIPHER

def paint_calc():
    test_h = int(input("Height of wall: "))
    test_w = int(input("Width of wall: "))
    coverage = 5
    num_of_cans = math.ceil(test_h*test_w/coverage)
    print(f"You'll need {num_of_cans} cans of paint.")

# paint_calc()

def prime_checker():
    non_prime = []
    num_input = int(input("Enter a number to check if it's prime: "))
    for i in range(2, num_input):
        if num_input % i == 0:
            non_prime += str(i)
    if non_prime != []:
        print(f"{num_input} is NOT a prime number.")
    else:
        print(f"{num_input} is a prime number.")

# prime_checker()

def caesar_cipher():
    alpha_list = string.ascii_lowercase
    direction = input("What do you want to do? (encode/decode)\n").lower()
    text = list(input("Type your message:\n").lower())
    shift = int(input("Type the shift number: "))
    answer = []
    for char in text:
        if char in alpha_list:
            pos = alpha_list.index(char)
            if direction == "encode":
                if pos + shift <= 25:
                    answer.append(alpha_list[pos + shift])
                else:
                    answer.append(alpha_list[-(25 - (pos + shift))])
            else:
                if pos - shift >= 0:
                    answer.append(alpha_list[pos - shift])
                else:
                    answer.append(alpha_list[25 + (pos - shift)])
        else:
            answer.append(char)

    if direction == "encode":
        print(f"The encoded text is '{''.join(answer)}'.")
    else:
        print(f"The decoded text is '{''.join(answer)}'.")

    again = input("Do you want to go again? (yes/no)\n").lower()
    if again == "yes": caesar_cipher()

# caesar_cipher()