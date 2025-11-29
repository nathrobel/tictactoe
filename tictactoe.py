from tkinter import *
import random


def next_turn(row,column,mode):
    '''Handle a player's move: place x/o, check winner/tie, and switch turns'''
    global player


    if mode == "multiplayer":
        grid = buttons
        current_label = label
    else:
        grid = buttons_sp
        current_label = sp_label

    if grid[row][column]['text'] == '' and check_winner(grid) is False:
        if player == players[0]:
            grid[row][column]["text"] = player
            if check_winner(grid) is False:
                # if there is no winner swap players
                player = players[1]
                current_label.config(text = (players[1] + " turn"))
            elif check_winner(grid) is True:
                current_label.config(text = (players[0] + " wins"))
            elif check_winner(grid)  == "Tie":
                current_label.config(text = ("Tie!"))
        else:
            grid[row][column]["text"] = player
            if check_winner(grid) is False:
                # if there is no winner swap players
                player = players[0]
                current_label.config(text = (players[0] + " turn"))
            elif check_winner(grid) is True:
                current_label.config(text = (players[1] + " wins"))
            elif check_winner(grid)  == "Tie":
                current_label.config(text = ("Tie!"))

def check_winner(grid):
    '''Return True if someone wins, Tie for draw, or False if game continues'''
    for row in range(3):
            if grid[row][0]['text'] == grid[row][1]['text'] == grid[row][2]['text'] != "":
                grid[row][0].config(highlightbackground = "green", highlightthickness=5)
                grid[row][1].config(highlightbackground = "green", highlightthickness=5)
                grid[row][2].config(highlightbackground = "green", highlightthickness=5)
                return True
            
    for column in range(3):
            if grid[0][column]['text'] == grid[1][column]['text'] == grid[2][column]['text'] != "":
                grid[0][column].config(highlightbackground = "green", highlightthickness=5)
                grid[1][column].config(highlightbackground = "green", highlightthickness=5)
                grid[2][column].config(highlightbackground = "green", highlightthickness=5)
                return True
    if grid[0][0]['text'] == grid[1][1]['text'] == grid[2][2]['text'] != "":
        grid[0][0].config(highlightbackground = "green", highlightthickness=5)
        grid[1][1].config(highlightbackground = "green", highlightthickness=5)
        grid[2][2].config(highlightbackground = "green", highlightthickness=5)
        return True
    if grid [0][2]['text'] == grid[1][1]['text'] == grid[2][0]['text'] != "":
        grid[0][2].config(highlightbackground = "green", highlightthickness=5)
        grid[1][1].config(highlightbackground = "green", highlightthickness=5)
        grid[2][0].config(highlightbackground = "green", highlightthickness=5)
        return True
    if empty_spaces(grid) is False:
        for row in range(3):
            for column in range(3):
                grid[row][column].config(highlightbackground = "yellow", highlightthickness=5)
        return "Tie"

    else:
        return False

    

def empty_spaces(grid): 
    '''Check if the board has empty spaces.'''
    num_spaces = 9

    for row in range(3):
        for column in range(3):
            if grid[row][column]['text'] != "":
                num_spaces -=1
    if num_spaces == 0:
        return False
    else:
        return True


def new_game(grid,current_label):
    '''Reset the board and start a new game'''
    global player

    player = random.choice(players)

    current_label.config(text = player + " turn")


    for row in range(3):
        for column in range(3):
            grid[row][column].config(text ="",highlightbackground="#F0F0F0", highlightthickness=0 )


def end_game():
    '''Close the window'''
    window.destroy()

def show_game_screen(mode):
    start_frame.pack_forget()
    if mode.lower() == "singleplayer":
        sp_game_frame.pack()
        new_game(buttons_sp,sp_label)
    elif mode.lower() == "multiplayer":
        mp_game_frame.pack()
        new_game(buttons,label)


# need some level functionality vs AI
# Level 1 is basic AI with basic heuristics
# if user wants to move to next level unlock level 2 button so they can progress they can restart on same level if they want
# Level 2 with A* search
# if user wants to move to next level unlock level 3 button so they can progress they can restart on same level if they want
# Level 3 with minmax alpha beta pruning

window = Tk()
window.title("Tic Tac Toe")

start_frame = Frame(window)
sp_game_frame = Frame(window)
mp_game_frame = Frame(window)

start_frame.pack()


players = ["x","o"]
player = random.choice(players)
buttons = [[0,0,0],
           [0,0,0],
           [0,0,0]]


# seperate grid logic for singleplayer
buttons_sp = [[0,0,0],
             [0,0,0],
             [0,0,0]]

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
    command=lambda: show_game_screen("singleplayer")
    
)
computer_btn.pack(pady=10)



# Multiplayer game frame 
label = Label(mp_game_frame,text = player + " turn", font = ('consolas',40))
label.pack(side = "top")

mp_reset_button = Button(mp_game_frame, text = "Restart", font = ('consolas',20),command = lambda: new_game(buttons,label))
mp_end_game_button = Button(mp_game_frame, text = "End Game", font = ('consolas',20),command = end_game)
mp_reset_button.pack(side = "top")
mp_end_game_button.pack(side = "top")



board_frame = Frame(mp_game_frame)
board_frame.pack()
for row in range(3):
    for column in range(3):
        buttons[row][column]= Button(board_frame,text = "", font = ('consolas',40), width = 5, height = 2, command = lambda row = row, column = column: next_turn(row,column,"multiplayer"))
        buttons[row][column].grid(row=row,column = column)

# Singleplayer game frame 
sp_label = Label(sp_game_frame,text = "vs Computer mode coming soon", font = ('consolas',40))
sp_label.pack(side = "top")

sp_reset_button = Button(sp_game_frame, text = "Restart", font = ('consolas', 20),command = lambda: new_game(buttons_sp,sp_label))
sp_end_game_button = Button(sp_game_frame, text = "End Game", font = ('consolas', 20),command = end_game)
sp_reset_button.pack(side = "top")
sp_end_game_button.pack(side = "top")

'''board_frame_sp = Frame(sp_game_frame)
board_frame_sp.pack()
for row in range(3):
    for column in range(3):
        buttons_sp[row][column]= Button(board_frame_sp,text = "", font = ('consolas', 40), width = 5, height = 2, command = lambda row = row, column = column: next_turn(row,column,"singleplayer"))
        buttons_sp[row][column].grid(row=row,column = column)'''

window.mainloop()


