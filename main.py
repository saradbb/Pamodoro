from tkinter import *
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
CHECK_MARK = "✓"
time = 0
DEFAULT_TIME = "25:00"
round_count = 0
play = False

def reset():
    """
    Changes all the values back to normal and pauses the execution
    :return:
    """
    global time,round_count,play
    round_count = 0
    time = 1500
    canvas.itemconfig(timer_text,text = DEFAULT_TIME)
    label.config(text = "Timer")
    check_label.config(text = "")
    start_button.wait_variable(start_button)
    play = False

def start():
    """
    When the start button in clicked, run the next round
    :return:
    """

    next_round()



# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #

def time_format():
    """
    Converts time in second into displayable format.
    :return:
    """
    global time
    min = (time//60)
    min_str = str(min)
    if min < 10:
        min_str = f"0{min}"     #To ensure minute is 2 digit everytime
    sec = (time %60)
    sec_str = str(sec)
    if sec < 10:                 #To ensure second is 2 digit everytime
        sec_str = f"0{sec}"
    return min_str +":"+sec_str


def next_round():
    """
    The function that does most of operation
    :return:
    """
    global round_count,time

    round_count += 1
    regular_time = [1,3,5,7]     #Starts with work time, break, work time.......
    short_break = [2,4,6]
    long_break = [8]        #one long break at the end of 4 work sessions

    if round_count in regular_time:          #During the work time
        label.config(text = "Work", fg = GREEN)
        time = 1500

    elif round_count in short_break:    #During the short break
        label.config(text = "Break", fg = PINK)
        str_val = CHECK_MARK * (round_count // 2)
        check_label.config(text = str_val)
        time = 300

    elif round_count == 8:             #During the long break
        label.config(text = "Break", fg = RED)
        time = 1200
    else:               #Once the long break ends
        reset()
    count_down(canvas,timer_text)   #Recursive function to run the timer







def count_down(canvas,timer_text):
    """
    Recursive function  to run the timer
    :param canvas:
    :param timer_text:
    :return:
    """
    #Recursive funtion
    global time,play

    canvas.itemconfig(timer_text, text=time_format())   #Change the time on display
    if (time == 0 ):
        next_round()
    time -= 1
    window.after(1000,count_down,canvas,timer_text)


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()

window.config(padx = 100, pady= 40, bg = YELLOW)
window.title("Pomodoro")
canvas = Canvas(width = 200,height=224,bg = YELLOW, highlightthickness = 0)


label = Label(text = "Timer", fg = GREEN, bg=YELLOW, font = (FONT_NAME,40,"bold"))
label.config(pady = 15)
label.grid(column = 3,row = 1)


tomato_image = PhotoImage(file = "tomato.png")
canvas.create_image(100,112,image = tomato_image)
timer_text = canvas.create_text(110,112,text=DEFAULT_TIME, fill = "white",font = (FONT_NAME,35,"bold"))
canvas.grid(column = 3,row = 3)


reset_button = Button(text="Reset", command = reset)
start_button = Button(text = "Start", command = start)
reset_button.grid(column = 4,row = 5)
start_button.grid(column = 2, row = 5)


check_label = Label(text = "", bg = YELLOW, fg = GREEN, font = (FONT_NAME,18,"bold"))

check_label.grid(column = 3, row = 5)





window.mainloop()