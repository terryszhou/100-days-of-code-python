from tkinter import *
FONT = ("Arial", 18, "normal")

window = Tk()
window.title("Mile to Km Converter")
window.minsize(width=300, height=150)

is_equal = Label(text="is equal to", font=FONT) 
is_equal.grid(column=0,row=1, padx=30)

input = Entry(width=10, justify="center")
input.insert(END, 0)
input.grid(column=1, row=0, pady=10)

miles = Label(text="Miles", font=FONT)
miles.grid(column=2, row=0, padx=30)

answer = Label(text=0, font=FONT)
answer.grid(column=1, row=1)

km = Label(text="Km", font=FONT)
km.grid(column=2, row=1)

def convert():
    result = float(input.get())*1.609
    answer["text"] = f"{result:.2f}"

calculate = Button(text="Calculate", command=convert)
calculate.grid(column=1, row=2, pady=10)

window.mainloop()
