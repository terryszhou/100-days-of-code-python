from tkinter import *
from tkinter import messagebox
from random import choice
import pandas

# -------------------- CONSTANTS -------------------- #
BACKGROUND_COLOR = "#B1DDC6"
LANG_FONT = ("Arial", 40, "italic")
WORD_FONT = ("Arial", 60, "bold")
word_data = pandas.read_csv("data/chinese_words.csv")
word_dict = word_data.to_dict(orient="records")
current_card = {}

# -------------------- FUNCTIONS -------------------- #
def next_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = choice(word_dict)
    canvas.itemconfig(canvas_card, image=FLASHCARD_FRONT)
    canvas.itemconfig(card_title, text="Chinese", fill="black")
    canvas.itemconfig(card_word, text=current_card["character"], fill="black")
    flip_timer = window.after(3000, flip_card)


def flip_card():
    canvas.itemconfig(canvas_card, image=FLASHCARD_BACK)
    canvas.itemconfig(card_title, text="English", fill="white")
    canvas.itemconfig(card_word, text=current_card["translation"],  fill="white")

# -------------------- UI SETUP -------------------- #
window = Tk()
window.title("Chinese Flashcards")
window.config(width=900, height=800, padx=50, pady=50, bg=BACKGROUND_COLOR)
flip_timer = window.after(3000, flip_card)

FLASHCARD_FRONT = PhotoImage(file="images/card_front.png")
FLASHCARD_BACK = PhotoImage(file="images/card_back.png")
WRONG = PhotoImage(file="images/wrong.png")
RIGHT = PhotoImage(file="images/right.png")

canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
canvas_card = canvas.create_image(400,263, image=FLASHCARD_FRONT)
card_title = canvas.create_text(400,150, text="Chinese", font=LANG_FONT, fill="black")
card_word = canvas.create_text(400,263, text="", font=WORD_FONT, fill="black")
canvas.grid(column=0, row=0, columnspan=2)

wrong_button = Button(image=WRONG, highlightbackground=BACKGROUND_COLOR, command=next_card)
wrong_button.grid(column=0, row=1)
right_button = Button(image=RIGHT, highlightbackground=BACKGROUND_COLOR, command=next_card)
right_button.grid(column=1, row=1)

next_card()

window.mainloop()

