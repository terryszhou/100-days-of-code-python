from tkinter import *
from tkinter import messagebox
from random import choice

# -------------------- CONSTANTS -------------------- #
BACKGROUND_COLOR = "#B1DDC6"

# -------------------- UI SETUP -------------------- #
window = Tk()
window.title("Chinese Flashcards")
window.config(width=1000, height=800, padx=50, pady=50)

FLASHCARD_FRONT = PhotoImage(file="card_front.png")
FLASHCARD_BACK = PhotoImage(file="card_back.png")
canvas = Canvas(width=800, height=526)
canvas.create_image(400,263, image=FLASHCARD_FRONT)
canvas.grid(column=0, row=0)

window.mainloop()

