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
reps = 1
timer = None

# ---------------------------- TIMER RESET ------------------------------- #


def reset_timer():
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    tit.config(text="Timer")
    label.config(text="")
    global reps
    reps = 1


# ---------------------------- TIMER MECHANISM ------------------------------- # 


def start_timer():
    work_sec = WORK_MIN * 60
    short_break = SHORT_BREAK_MIN*60
    long_break = LONG_BREAK_MIN*60
    global reps
    if reps % 8 == 0:
        count_down(long_break)
        reps += 1
        tit.config(text="LONG BREAK")
    elif reps % 2 == 0:
        count_down(short_break)
        tit.config(text="SHORT BREAK")
        reps += 1
    else:
        count_down(work_sec)
        tit.config(text="WORK ASSHOLE!!!")
        reps += 1


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #


def count_down(count):
    count_min = math.floor(count/60)
    count_sec = count % 60
    if len(str(count_sec)) == 1:
        count_sec = f"0{count_sec}"
    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    elif count < 0:
        if tit.cget("text") == "WORK ASSHOLE!!!":
            txt = label.cget("text") + "✓"
            label.configure(text=txt)
        elif tit.cget("text") == "LONG BREAK":
            label.configure(text="")

        start_timer()


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro Timer")
window.config(padx=50, pady=50, bg=YELLOW)

tit = Label(text="Timer", font=(FONT_NAME, 40, "bold"))
tit.config(fg=GREEN, bg=YELLOW)
tit.grid(column=1, row=0)

canvas = Canvas(height=224, width=200, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 113, text="00:00", font=(FONT_NAME, 20, "bold"), fill="white")
canvas.grid(column=1, row=1)

label = Label(text="")
label.config(fg=GREEN, bg=YELLOW, padx=10, pady=10)
label.grid(column=1, row=2)

reset = Button(text="Reset", fg=PINK, command=reset_timer)
reset.grid(column=2, row=2)

start = Button(text="Start", fg=PINK, command=start_timer)
start.grid(column=0, row=2)

window.mainloop()
