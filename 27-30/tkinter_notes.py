from tkinter import *
FONT = ("Arial", 24, "bold")

window = Tk()
window.title("My First GUI Program")
window.minsize(width=500, height=300)

# LABELS - - - - - - - - - - - - - - - - - -
my_label = Label(text="I am a label", font=FONT)

# LAYOUT MANAGERS - - - - - - - - - - - - - - - - - -
my_label.pack() # <-- approximate placement, takes side arg
my_label.place(x=0,y=0) # <-- exact placement, takes integers as coordinates
my_label.grid(column=1, row=1) # <-- placement by grid rows and columns; incompatible with pack

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

# TEXT - - - - - - - - - - - - - - - - - -
text = Text(height=5, width=30)
#Puts cursor in textbox.
text.focus()
#Adds some text to begin with.
text.insert(END, "Example of multi-line text entry.")
#Get's current value in textbox at line 1, character 0
print(text.get("1.0", END))
text.pack()

# SPINBOX - - - - - - - - - - - - - - - - - -
def spinbox_used():
    #gets the current value in spinbox.
    print(spinbox.get())
spinbox = Spinbox(from_=0, to=10, width=5, command=spinbox_used)
spinbox.pack()

# SCALE - - - - - - - - - - - - - - - - - -
#Called with current scale value.
def scale_used(value):
    print(value)
scale = Scale(from_=0, to=100, command=scale_used)
scale.pack()

# CHECK BUTTON - - - - - - - - - - - - - - - - - -
def checkbutton_used():
    #Prints 1 if On button checked, otherwise 0.
    print(checked_state.get())
#variable to hold on to checked state, 0 is off, 1 is on.
checked_state = IntVar()
checkbutton = Checkbutton(text="Is On?", variable=checked_state, command=checkbutton_used)
checked_state.get()
checkbutton.pack()

# RADIO BUTTON - - - - - - - - - - - - - - - - - -
def radio_used():
    print(radio_state.get())
#Variable to hold on to which radio button value is checked.
radio_state = IntVar()
radiobutton1 = Radiobutton(text="Option1", value=1, variable=radio_state, command=radio_used)
radiobutton2 = Radiobutton(text="Option2", value=2, variable=radio_state, command=radio_used)
radiobutton1.pack()
radiobutton2.pack()


# LISTBOX - - - - - - - - - - - - - - - - - -
def listbox_used(event):
    # Gets current selection from listbox
    print(listbox.get(listbox.curselection()))

listbox = Listbox(height=4)
fruits = ["Apple", "Pear", "Orange", "Banana"]
for item in fruits:
    listbox.insert(fruits.index(item), item)
listbox.bind("<<ListboxSelect>>", listbox_used)
listbox.pack()

window.mainloop()