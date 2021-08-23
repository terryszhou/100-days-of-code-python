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
reps = 0
timer = None

# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    global reps
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    title_label["text"] = "Timer"
    reps = 0
    check_marks["text"] = ""

# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps
    reps += 1

    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    if reps in (1, 3, 5, 7):
        count_down(work_sec)
        title_label.config(text="WORK!", fg=GREEN)
    elif reps in (2, 4, 6):
        count_down(short_break_sec)
        title_label.config(text="BREAK!", fg=PINK)
    elif reps == 8:
        count_down(long_break_sec)
        title_label.config(text="BREAK!", fg=RED)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
    global reps
    count_min = floor(count/60)
    if count_min < 10:
        count_min = f"0{count_min}"
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"
    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        if reps % 2 == 0:
            check_marks["text"] += "✓"

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100,112, image=tomato_img)
timer_text = canvas.create_text(100,135, text="00.00", fill="white", font=FONT)
canvas.pack()

title_label = Label(text="Timer", font=FONT, fg=GREEN, bg=YELLOW)
title_label.place(x=45, y=-40)

start_btn = Button(text="START", highlightbackground=YELLOW, fg=PINK, command=start_timer)
start_btn.place(x=-60, y=230)

reset_btn = Button(text="RESET", highlightbackground=YELLOW, fg=PINK, command=reset_timer)
reset_btn.place(x=200, y=230)

check_marks = Label(fg=GREEN, bg=YELLOW)
check_marks.place(x=80, y=230)

window.mainloop()