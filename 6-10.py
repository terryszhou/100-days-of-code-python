import random

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

player_lives()
