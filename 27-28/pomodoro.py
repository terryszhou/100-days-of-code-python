from tkinter import *
from math import floor

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT = ("Courier", 35, "bold")
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20

# ---------------------------- TIMER RESET ------------------------------- # 

# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    count_down(5 * 60)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
    count_min = floor(count/60)
    count_sec = count % 60
    if count_sec == 0 or count_sec < 10:
        count_sec = f"0{count_sec}"
    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        window.after(1000, count_down, count - 1)

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100,112, image=tomato_img)
timer_text = canvas.create_text(100,135, text="00.00", fill="white", font=FONT)
canvas.pack()

timer_label = Label(text="Timer", font=FONT, fg=GREEN, bg=YELLOW)
timer_label.place(x=45, y=-40)

start_btn = Button(text="START", highlightbackground=YELLOW, fg=PINK, command=start_timer)
start_btn.place(x=-60, y=230)

reset_btn = Button(text="STOP", highlightbackground=YELLOW, fg=PINK)
reset_btn.place(x=200, y=230)

check_marks = Label(text="✓", fg=GREEN, bg=YELLOW)
check_marks.place(x=90, y=230)

window.mainloop()