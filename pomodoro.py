from tkinter import *

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
BLUE = "#73A9AD"
YELLOW = "#F5F0BB"
DARK_BLUE = "#242F9B"
LIGHT_BLUE = "#DBDFFD"

FONT_NAME = "Courier"
SHORT_BREAK_MIN = 2
LONG_BREAK_MIN = 10
reps = 0
work_sessions = 0
timer = '0'
set_time = 0


def reset():
    global reps, work_sessions
    window.after_cancel(timer)
    timer_label.config(text="Timer", bg=YELLOW, fg=BLUE, font=(FONT_NAME, 40, 'bold'))
    canvas.itemconfig(timer_text, text="00:00")
    check_label.config(text="")
    reps = 0
    work_sessions = 0


def set_timer():
    global set_time

    set_time = scale.get()
    canvas.itemconfig(timer_text, text=f"{set_time}:00")



def start_timer():
    global reps, work_sessions
    reps += 1
    if reps < 9:
        work = set_time * 60
        short_break = SHORT_BREAK_MIN * 60
        long_break = LONG_BREAK_MIN * 60

        window.attributes('-topmost', 1)
        if reps % 8 == 0:
            timer_label.config(text="Break", bg=YELLOW, fg=RED)
            count_down(long_break)
        elif reps % 2 == 0:
            timer_label.config(text="Break", bg=YELLOW, fg=PINK)
            count_down(short_break)
        else:
            work_sessions += 1
            timer_label.config(text="Study", bg=YELLOW, fg=BLUE)
            count_down(work)
        window.attributes('-topmost', 0)

    else:
        window.after_cancel(timer)
        timer_label.config(text="Timer", bg=YELLOW, fg=BLUE, font=(FONT_NAME, 40, 'bold'))
        canvas.itemconfig(timer_text, text="00:00")
        check_label.config(text="")
        reps = 0
        work_sessions = 0


def count_down(count):
    global work_sessions, reps, timer
    count_min = count // 60
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"
    if count_min < 10:
        count_min = f"0{count_min}"
    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        timer = window.after(1000, count_down, count-1)
    else:
        if reps % 2 != 0:
            check_label.config(text="✔"*work_sessions)

        start_timer()


window = Tk()
window.title("Pomodoro")
window.config(pady=50, padx=100, bg=YELLOW)
tomato_img = PhotoImage(file="tomato.png")
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, 'bold'))
canvas.grid(column=1, row=1)


timer_label = Label(text="Timer", bg=YELLOW, fg=BLUE, font=(FONT_NAME, 40, 'bold'))
timer_label.grid(column=1, row=0)

time_start = Button(text="Start", command=start_timer, bg=LIGHT_BLUE, fg=DARK_BLUE, highlightthickness=0,
                    font=(FONT_NAME, 10, 'bold'))
time_start.grid(column=0, row=2)

time_reset = Button(text="Reset", bg=LIGHT_BLUE, fg=DARK_BLUE, highlightthickness=0, font=(FONT_NAME, 10, 'bold'),
                    command=reset)
time_reset.grid(column=2, row=2)

check_label = Label(bg=YELLOW, fg=BLUE)
check_label.grid(column=1, row=4)


scale = Scale(from_=20, to=60, sliderlength=5, bg=YELLOW, highlightthickness=0, orient=HORIZONTAL,
              resolution=5)
scale.grid(column=1, row=2)

timer_button = Button(text="Set", command=set_timer, bg=LIGHT_BLUE, fg=DARK_BLUE, highlightthickness=0,
                      font=(FONT_NAME, 10, 'bold'))
timer_button.config(padx=10, pady=10)
timer_button.grid(column=1, row=3)


window.mainloop()
