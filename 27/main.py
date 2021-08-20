import tkinter
FONT = ("Arial", 24, "bold")

window = tkinter.Tk()
window.title("My First GUI Program")
window.minsize(width=500, height=300)

my_label = tkinter.Label(text="I am a label", font=FONT)
my_label.pack()

window.mainloop()