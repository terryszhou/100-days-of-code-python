from tkinter import *
import string
import random

# -------------------- CONSTANTS -------------------- #
FONT = ("Arial", 14, "normal")
FONT_SMALL = ("Arial", 10, "normal")

# -------------------- PASSWORD GENERATOR -------------------- #
def generate_pass():
    random_list = [string.ascii_letters, string.digits, string.punctuation]
    random_pass = ""
    for _ in range(6):
        random_pass += random.choice(random.choice(random_list))
    print(random_pass)
    password_entry["text"] = random_pass

# -------------------- SAVE PASSWORD -------------------- #


# -------------------- UI SETUP -------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=100, pady=100)

LOGO = PhotoImage(file="logo.png")
canvas = Canvas(width=200, height=200)
canvas.create_image(100,100, image=LOGO)
canvas.grid(column=1, row=0)

website_label = Label(text="Website:", font=FONT)
email_label = Label(text="Email/Username:", font=FONT)
password_label = Label(text="Password:", font=FONT)
website_entry = Entry(width=35, justify="center")
password_entry = Label(width=21, justify="center", bg="#1e1e1e")
password_button = Button(text="Generate Password", width=15, font=FONT_SMALL, command=generate_pass)
add_button = Button(text="Add", width=32, justify="center")
email_entry = Entry(width=35, justify="center")

website_label.grid(column=0, row=1)
email_label.grid(column=0, row=2)
password_label.grid(column=0, row=3)
website_entry.grid(column=1, row=1, columnspan=2)
password_entry.grid(column=1, row=3)
password_button.grid(column=2, row=3)
add_button.grid(column=1, row=5, columnspan=2)
email_entry.grid(column=1, row=2, columnspan=2)

window.mainloop()