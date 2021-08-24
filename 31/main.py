from tkinter import *
from tkinter import messagebox
from random import choice

# -------------------- CONSTANTS -------------------- #
BACKGROUND_COLOR = "#B1DDC6"
LANG_FONT = ("Arial", 40, "italic")
WORD_FONT = ("Arial", 60, "bold")

# -------------------- UI SETUP -------------------- #
window = Tk()
window.title("Chinese Flashcards")
window.config(width=900, height=800, padx=50, pady=50, bg=BACKGROUND_COLOR)

FLASHCARD_FRONT = PhotoImage(file="card_front.png")
FLASHCARD_BACK = PhotoImage(file="card_back.png")
WRONG = PhotoImage(file="wrong.png")
RIGHT = PhotoImage(file="right.png")

canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.create_image(400,263, image=FLASHCARD_FRONT)
canvas.grid(column=0, row=0, columnspan=2)

wrong_button = Button(image=WRONG, highlightbackground=BACKGROUND_COLOR)
wrong_button.grid(column=0, row=1)
right_button = Button(image=RIGHT, highlightbackground=BACKGROUND_COLOR)
right_button.grid(column=1, row=1)

lang_label = Label(text="Chinese", font=LANG_FONT, bg="white", fg="black")
lang_label.place(x=320, y=150)

word_label = Label(text="的", font=WORD_FONT, bg="white", fg="black")
word_label.place(x=360, y=263)

window.mainloop()

