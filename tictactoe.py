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



window.mainloop()


