from tkinter import *
from tkinter import messagebox
from string import *
from random import choice
import pyperclip
import json

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
    pyperclip.copy(random_pass)
    password_entry.insert(END, random_pass)

# -------------------- SAVE PASSWORD -------------------- #
def save_pass():
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()
    new_data = {
        website: {
            "email": email,
            "password": password,
        }
    }

    if website == "":
        messagebox.showinfo(title="Website not found", message=f"Please enter a website.")
    elif password == "":
        messagebox.showinfo(title="Password not found", message=f"Please enter a password.")
    else:
        try: 
            with open("pass_manager.json", "r") as data_file:
                data = json.load(data_file)
        except FileNotFoundError:
            with open("pass_manager.json", "w") as data_file:
                json.dump(new_data, data_file, indent=4)
        else:
            data.update(new_data)
            with open("pass_manager.json", "w") as data_file:
                json.dump(data, data_file, indent=4)
        finally:
            website_entry.delete(0, END)
            password_entry.delete(0, END)
# -------------------- SAVE PASSWORD -------------------- #
def find_password():
    website = website_entry.get()
    try:
        with open("pass_manager.json", "r") as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showinfo(title="Error", message="No Data File Found")
    else:
        if website in data:
            messagebox.showinfo(title=website, message=f'Email: {data[website]["email"]}\nPassword: {data[website]["password"]}')
        else:
            messagebox.showinfo(title=website, message=f"No details for {website} exist.")

# -------------------- UI SETUP -------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=100, pady=100)

LOGO = PhotoImage(file="logo.png")
canvas = Canvas(width=200, height=200)
canvas.create_image(100,100, image=LOGO)
canvas.grid(column=1, row=0)

website_label = Label(text="Website:")
website_label.grid(column=0, row=1)
email_label = Label(text="Email/Username:")
email_label.grid(column=0, row=2)
password_label = Label(text="Password:")
password_label.grid(column=0, row=3)

website_entry = Entry(width=21)
website_entry.grid(column=1, row=1)
website_entry.focus()
email_entry = Entry(width=38)
email_entry.insert(0, "terryszhou@gmail.com")
email_entry.grid(column=1, row=2, columnspan=2)
password_entry = Entry(width=21, bg="#1e1e1e")
password_entry.grid(column=1, row=3)

search_button = Button(text="Search", width=13, command=find_password)
search_button.grid(column=2, row=1)
password_button = Button(text="Generate Password", command=generate_pass)
password_button.grid(column=2, row=3)
add_button = Button(text="Add", width=36, command=save_pass)
add_button.grid(column=1, row=4, columnspan=2)

window.mainloop()