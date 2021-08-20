from tkinter import *

# -------------------- CONSTANTS ------------------------ #
FONT = ("Arial", 14, "normal")

# -------------------- PASSWORD GENERATOR -------------------- #


# -------------------- SAVE PASSWORD -------------------- #


# -------------------- UI SETUP -------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=100, pady=100)

canvas = Canvas(width=200, height=200)
logo = PhotoImage(file="logo.png")
canvas.create_image(100,100, image=logo)
canvas.grid(column=1, row=0)

website_label = Label(text="Website:", font=FONT)
website_label.grid(column=0, row=1)

email_label = Label(text="Email/Username:", font=FONT)
email_label.grid(column=0, row=2)

password_label = Label(text="Password:", font=FONT)
password_label.grid(column=0, row=3)

website_entry = Entry(width=35, justify="center")
website_entry.grid(column=1, row=1, columnspan=2)

email_entry = Entry(width=35, justify="center")
email_entry.grid(column=1, row=2, columnspan=2)

password_entry = Entry(width=21, justify="center")
password_entry.grid(column=1, row=3)

password_button = Button(text="Generate Password", width=15, font=(("Arial", 10, "normal")))
password_button.grid(column=2, row=3)

add_button = Button(text="Add", width=32, justify="center")
add_button.grid(column=1, row=5, columnspan=2)

window.mainloop()
