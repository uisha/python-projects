from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None
timer_state = True  # True: allow start button to be pressed. False: don't allow

# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    title_label.config(text="Timer", fg=GREEN)
    check_label.config(text="")
    global reps
    reps = 0

    start_button.config(state=NORMAL)
    restart_button.config(state=DISABLED)

# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    start_button.config(state=DISABLED)
    restart_button.config(state=NORMAL)
    global reps

    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    reps += 1
    if reps % 8 == 0:
        countdown(long_break_sec)
        title_label.config(text="Break", fg=RED)
    elif reps % 2 == 1:
        countdown(work_sec)
        title_label.config(text="Work", fg=GREEN)
    else:
        countdown(short_break_sec)
        title_label.config(text="Break", fg=PINK)



# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def countdown(count):

    count_min = math.floor(count / 60)
    count_sec = count % 60

    if count_min < 10:
        count_min = f"0{count_min}"
    elif count_min == 0:
        count_min = "00"

    if count_sec < 10:
        count_sec = f"0{count_sec}"
    elif count_sec == 0:
        count_sec = "00"

    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        global timer
        timer = window.after(1000, countdown, count-1)
    else:
        start_timer()
        # if reps % 2 == 0:
        #     check_label.config(text="✔"*int(reps/2))
        marks = ""
        work_sessions = math.floor(reps/2)
        for _ in range(work_sessions):
            marks += "✔"
            check_label.config(text=marks)



# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro App")
window.config(padx=100, pady=50, bg=YELLOW)

# Timer Label
title_label = Label(text="Timer", font=(FONT_NAME, 50), fg=GREEN, bg=YELLOW)
title_label.grid(column=1, row=0)

# Tomato Canvas
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(103, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)

# Start Button
start_button = Button(text="Start", highlightthickness=0, command=start_timer)
start_button.grid(column=0, row=2)

# Restart Button
restart_button = Button(text="Restart", highlightthickness=0, command=reset_timer, state=DISABLED)
restart_button.grid(column=2, row=2)

check_label = Label(fg=GREEN, bg=YELLOW)
check_label.grid(column=1, row=3)
window.mainloop()