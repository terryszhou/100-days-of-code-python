from tkinter import *
FONT = ("Arial", 24, "bold")

window = Tk()
window.title("My First GUI Program")
window.minsize(width=500, height=300)

# LABELS - - - - - - - - - - - - - - - - - -
my_label = Label(text="I am a label", font=FONT)
my_label.pack()

# TWO WAYS TO MANIPULATE THE KWARGS OF A PRE-CREATED COMPONENT
# my_label["text"] = "New Text"
# my_label.config(text="New Text")

# BUTTONS - - - - - - - - - - - - - - - - - -
def button_clicked():
    my_label["text"] = input.get()

button = Button(text="Click Me", command=button_clicked)
button.pack()

# ENTRY - - - - - - - - - - - - - - - - - -
input = Entry(width=10)
input.pack()

window.mainloop()