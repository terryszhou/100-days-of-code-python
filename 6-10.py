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
    else:
        print("Yes it is!")

# random_word()
