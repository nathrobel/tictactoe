from tkinter import *
import random


def next_game():
    pass


def check_win():
    pass

def empty_spaces():
    pass

def new_game():
    pass


players = ["x","o"]

player = random.choice(players)

buttons = [[0,0,0],
           [0,0,0],
           [0,0,0]]

window = Tk()
label = Label(text = player + " turn", font = ('consolas',40))
label.pack(side = "top")

reset_button = Button(text = "restart", font = ('consolas',20),command = new_game)
reset_button.pack(side = "top")

frame = Frame(window)
frame.pack()

for row in range(3):
    for column in range(3):
        buttons[row][column] = Button(frame,text = "",  font = ('consolas',40),width = 5,height = 2, command = lambda row=row, column= column: next_turn(row,column))
        buttons[row][column].grid(row=row,column=column)


window.mainloop()


