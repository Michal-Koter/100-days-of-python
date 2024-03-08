import math
from tkinter import *

PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
check_icon = "✔"
timer = None

def reset_timer():
    window.after_cancel(timer)

    global reps
    reps = 0
    check_marks.config(text="")
    timer_label.config(text="Timer")
    canvas.itemconfig(timer_text, text="00:00")


def start_timer():
    global reps
    reps += 1

    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    if reps % 8 == 0:
        countdown(long_break_sec)
        timer_label.config(text="Break", fg=RED)
    elif reps % 2 == 0:
        countdown(short_break_sec)
        timer_label.config(text="Break", fg=PINK)
    else:
        countdown(work_sec)
        timer_label.config(text="Work", fg=GREEN)


def countdown(count):
    minutes = math.floor(count / 60)
    seconds = count % 60
    canvas.itemconfig(timer_text, text=f"{minutes:02d}:{seconds:02d}")

    if count <= 0:
        new_text = check_icon * math.floor((reps+1) / 2)
        check_marks.config(text=new_text)
        start_timer()
        return None

    global timer
    timer = window.after(1000, countdown, count-1)


window = Tk()
window.title("Pomodoro App")
window.config(padx=100, pady=50)
window.config(background=YELLOW)
window.geometry("525x450")

timer_label = Label(text="Timer", font=(FONT_NAME, 50, "bold"), bg=YELLOW, fg=GREEN)
timer_label.grid(row=0, column=1)

canvas = Canvas(width=205, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(row=1, column=1)

start_btn = Button(text="Start", font=(FONT_NAME, 14), highlightthickness=0, command=start_timer)
start_btn.grid(row=2, column=0)

reset_btn = Button(text="Reset", font=(FONT_NAME, 14), highlightthickness=0, command=reset_timer)
reset_btn.grid(row=2, column=3)

check_marks = Label(font=(FONT_NAME, 14, "bold"), bg=YELLOW, fg=GREEN)
check_marks.grid(row=3, column=1)

window.mainloop()