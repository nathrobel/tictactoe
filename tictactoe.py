from tkinter import *
import random


def next_turn(row,column):
    '''Handle a player's move: place symbol, check winner/tie, and switch turns'''
    global player
    if buttons[row][column]['text'] == '' and check_winner() is False:
        if player == players[0]:
            buttons[row][column]["text"] = player
            if check_winner() is False:
                # if there is no winner swap players
                player = players[1]
                label.config(text = (players[1] + " turn"))
            elif check_winner() is True:
                label.config(text = (players[0] + " wins"))
            elif check_winner()  == "Tie":
                label.config(text = ("Tie!"))
        else:
            buttons[row][column]["text"] = player
            if check_winner() is False:
                # if there is no winner swap players
                player = players[0]
                label.config(text = (players[0] + " turn"))
            elif check_winner() is True:
                label.config(text = (players[1] + " wins"))
            elif check_winner()  == "Tie":
                label.config(text = ("Tie!"))


def check_winner():
    '''Return True if someone wins, Tie for draw, or False if game continues'''
    for row in range(3):
            if buttons[row][0]['text'] == buttons[row][1]['text'] == buttons[row][2]['text'] != "":
                buttons[row][0].config(highlightbackground = "green", highlightthickness=5)
                buttons[row][1].config(highlightbackground = "green", highlightthickness=5)
                buttons[row][2].config(highlightbackground = "green", highlightthickness=5)
                return True
            
    for column in range(3):
            if buttons[0][column]['text'] == buttons[1][column]['text'] == buttons[2][column]['text'] != "":
                buttons[0][column].config(highlightbackground = "green", highlightthickness=5)
                buttons[1][column].config(highlightbackground = "green", highlightthickness=5)
                buttons[2][column].config(highlightbackground = "green", highlightthickness=5)
                return True
    if buttons[0][0]['text'] == buttons[1][1]['text'] == buttons[2][2]['text'] != "":
        buttons[0][0].config(highlightbackground = "green", highlightthickness=5)
        buttons[1][1].config(highlightbackground = "green", highlightthickness=5)
        buttons[2][2].config(highlightbackground = "green", highlightthickness=5)
        return True
    if buttons[0][2]['text'] == buttons[1][1]['text'] == buttons[2][0]['text'] != "":
        buttons[0][2].config(highlightbackground = "green", highlightthickness=5)
        buttons[1][1].config(highlightbackground = "green", highlightthickness=5)
        buttons[2][0].config(highlightbackground = "green", highlightthickness=5)
        return True
    if empty_spaces() is False:
        for row in range(3):
            for column in range(3):
                buttons[row][column].config(highlightbackground = "yellow", highlightthickness=5)
        return "Tie"

    else:
        return False

    

def empty_spaces(): 
    '''Check if the board has empty spaces.'''
    num_spaces = 9

    for row in range(3):
        for column in range(3):
            if buttons[row][column]['text'] != "":
                num_spaces -=1
    if num_spaces == 0:
        return False
    else:
        return True


def new_game():
    '''Reset the board and start a new game'''
    global player

    player = random.choice(players)

    label.config(text = player + " turn")


    for row in range(3):
        for column in range(3):
            buttons[row][column].config(text ="",highlightbackground="#F0F0F0", highlightthickness=0 )


def end_game():
    '''Close the window'''
    window.destroy()





window = Tk()
window.title("Tic Tac Toe")

start_frame = Frame(window)
game_frame = Frame(window)

start_frame.pack()


players = ["x","o"]
player = random.choice(players)
buttons = [[0,0,0],
           [0,0,0],
           [0,0,0]]

def show_game_screen(mode):
    start_frame.pack_forget()
    game_frame.pack()
    new_game()


welcome_label = Label(start_frame, text="Welcome to Tic Tac Toe!", font=("consolas", 40))
welcome_label.pack(pady=40)

multiplayer_btn = Button(
    start_frame,
    text="Multiplayer",
    font=("consolas", 30),
    command=lambda: show_game_screen("multiplayer")
)
multiplayer_btn.pack(pady=20)

computer_btn = Button(
    start_frame,
    text="Vs Computer (coming soon)",
    font=("consolas", 20),
    state=DISABLED
)
computer_btn.pack(pady=10)




label = Label(game_frame,text = player + " turn", font = ('consolas',40))
label.pack(side = "top")

reset_button = Button(game_frame, text = "Restart", font = ('consolas',20),command = new_game)
end_game_button = Button(game_frame, text = "End Game", font = ('consolas',20),command = end_game)
reset_button.pack(side = "top")
end_game_button.pack(side = "top")



frame = Frame(game_frame)
frame.pack()
for row in range(3):
    for column in range(3):
        buttons[row][column]= Button(frame,text = "", font = ('consolas',40), width = 5, height = 2, command = lambda row = row, column = column: next_turn(row,column))
        buttons[row][column].grid(row=row,column = column)



window.mainloop()


