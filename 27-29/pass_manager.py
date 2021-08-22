from tkinter import *
from tkinter import messagebox
from string import *
from random import choice

# -------------------- CONSTANTS -------------------- #
FONT = ("Arial", 14, "normal")
FONT_SMALL = ("Arial", 10, "normal")

# -------------------- PASSWORD GENERATOR -------------------- #
def generate_pass():
    random_list = [ascii_letters, digits, punctuation]
    random_pass = ""
    for _ in range(12):
        random_pass += choice(choice(random_list))
    if password_entry.get() != None:
        password_entry.delete(0, END)
    password_entry.insert(END, random_pass)

# -------------------- SAVE PASSWORD -------------------- #
def save_pass():
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()

    if website == "":
        messagebox.showinfo(title="Website not found", message=f"Please enter a website.")
    elif password == "":
        messagebox.showinfo(title="Password} not found", message=f"Please enter a password.")
    else:
        is_okay = messagebox.askokcancel(title=website, message=f"These are the details entered: \nEmail: {email} \nPassword: {password} \nOkay to save?")
        if is_okay:
            with open("pass_manager.txt", mode="a") as file:
                file.write(f"{website} | {email} | {password}\n")
                website_entry.delete(0, END)
                password_entry.delete(0, END)

# -------------------- UI SETUP -------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=100, pady=100)

LOGO = PhotoImage(file="logo.png")
canvas = Canvas(width=200, height=200)
canvas.create_image(100,100, image=LOGO)
canvas.grid(column=1, row=0)

website_label = Label(text="Website:", font=FONT)
website_label.grid(column=0, row=1)
email_label = Label(text="Email/Username:", font=FONT)
email_label.grid(column=0, row=2)
password_label = Label(text="Password:", font=FONT)
password_label.grid(column=0, row=3)

website_entry = Entry(width=35, justify="center")
website_entry.focus()
website_entry.grid(column=1, row=1, columnspan=2)
email_entry = Entry(width=35, justify="center")
email_entry.insert(0, "terryszhou@gmail.com")
email_entry.grid(column=1, row=2, columnspan=2)
password_entry = Entry(width=21, justify="center", bg="#1e1e1e")
password_entry.grid(column=1, row=3)

password_button = Button(text="Generate Password",width=15, font=FONT_SMALL, command=generate_pass)
password_button.grid(column=2, row=3)
add_button = Button(text="Add", width=32, justify="center", command=save_pass)
add_button.grid(column=1, row=5, columnspan=2)

window.mainloop()