import tkinter as tk
import random

countClick = 0
targetClicks = 0

def set_target_clicks():
    global targetClicks
    targetClicks = random.randint(1, 20)
    update_label()

def click_increase():
    global countClick
    countClick += 1
    update_label()
    check_game_status()

def click_decrease():
    global countClick
    if countClick > 0:
        countClick -= 1
    update_label()

def update_label():
    if countClick < 0:
        myLabel['text'] = f'Clicks: {countClick} (Negative)'
    else:
        myLabel['text'] = f'Clicks: {countClick}/{targetClicks}'

def check_game_status():
    if countClick == targetClicks:
        myLabel['text'] = 'Вітаю! Ти завершив етап'
        increaseBtn['state'] = 'disabled'
        decreaseBtn['state'] = 'disabled'

root = tk.Tk()
root.title('Clicker Game')
root.geometry('1500x500')
root.minsize(400, 300)
root.maxsize(800, 600)

myLabel = tk.Label(root, text='Clicks: 0/0', bg='#9feb34', fg='#3461eb', width=20, height=3, anchor='center', relief=tk.SOLID)
myLabel.pack(pady=20)

increaseBtn = tk.Button(root, text='Increase', bg='darkblue', fg='white', relief=tk.SOLID, command=click_increase)
increaseBtn.pack(side=tk.LEFT, padx=10)

decreaseBtn = tk.Button(root, text='Decrease', bg='darkred', fg='white', relief=tk.SOLID, command=click_decrease)
decreaseBtn.pack(side=tk.RIGHT, padx=10)

def click_increase2():
    global countClick2
    countClick2 += 1
    update_label()
    check_game_status()

def click_decrease2():
    global countClick2
    if countClick2 > 0:
        countClick2 -= 1
    update_label()

def update_label2():
     if countClick2 < 0:
        myLabel2['text'] = f'Clicks: {countClick2} (Negative)'
     else:
        myLabel2['text'] = f'Clicks: {countClick2}/{targetClicks}'

def check_game_status2():
        if countClick2 == targetClicks:
            myLabel2['text'] = 'Вітаю! Ти завершив етап'
            increaseBtn2['state'] = 'disabled'
            decreaseBtn2['state'] = 'disabled'


myLabel2 = tk.Label(root, text='Clicks: 0/0', bg='#9feb34', fg='#3461eb', width=20, height=3, anchor='center', relief=tk.SOLID)
myLabel2.pack(pady=20)

increaseBtn2 = tk.Button(root, text='Increase', bg='darkblue', fg='white', relief=tk.SOLID, command=click_increase)
increaseBtn2.pack(side=tk.LEFT, padx=10)

decreaseBtn2 = tk.Button(root, text='Decrease', bg='darkred', fg='white', relief=tk.SOLID, command=click_decrease)
decreaseBtn2.pack(side=tk.LEFT, padx=250)

set_target_clicks()

root.mainloop()

