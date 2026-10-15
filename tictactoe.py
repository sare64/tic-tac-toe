# **********************************************************
# *    Program: Tic Tac Toe - ISP                          *
# *    Date: January 25, 2022                              *
# *    Name: Sarah Crawford                                *
# *    Description: This program is a 2-player,            *
# *    best of 3, Tic Tac Toe game.                        *
# **********************************************************

# Import tkinter
from tkinter import *
from tkinter import messagebox

# Configure the window attributes and center it on screen
win = Tk()
win.configure(bg='light blue')
w_width = 430
w_height = 580
pos_right = int(win.winfo_screenwidth()/2 - w_width/2)
pos_down = int(win.winfo_screenheight()/2 - w_height/2)
win.geometry('+{}+{}'.format(pos_right, pos_down))
win.title('Tic Tac Toe')
win.resizable(False, False)

# Create the title label and position it on the window
lblTitle = Label(win, text='Tic Tac Toe', font="Verdana 25 bold", fg='thistle4', bg='azure2',
                 highlightthickness=2, highlightbackground='thistle3')
lblTitle.pack(ipadx=20, ipady=5, padx=50, pady=10)

# Initialize turn (True = X's turn, False = O's turn) and
# counters (turn, x_win, and o_win: all = 0)
x_turn = True
turn_counter = 0
x_win_counter = 0
o_win_counter = 0
tie_counter = 0

# Print welcome message, pointing the user to the help menu, to the console
print("==========================")
print("Welcome to Tic Tac Toe!\nFor help and/or rules:\n> help menu at the top.")
print("==========================\n\nX starts")


# Create the user-defined click function, which is activated when the player clicks on one of
# the tic-tac-toe buttons
#
# It responds to any of the tic-tac-toe buttons being clicked, alternates turns,
# and checks to see if a user won or the game was tied after each turn

# It also contains more user-defined functions that execute when a player wins a round, and it has
# if statements that address a player winning the game or the game ending in a tie
def click(ind):
    global x_turn, turn_counter, x_win_counter, o_win_counter, tie_counter, state
    # If it's X's turn, change the button text to 'X', disable the button that was clicked,
    # set the turn to be O's, print whose turn is next to the console, and increase the turn counter by 1
    if x_turn:
        btnTTT[ind].config(text="X", font='Verdana 50', state='disabled', disabledforeground='azure3')
        state[ind] = "X"
        lblPX.config(bg='azure2')
        lblPO.config(bg='thistle')
        x_turn = False
        turn_counter += 1
        print("O's turn")
    # If it's O's turn, change the button text to 'O', disable the button that was clicked,
    # set the turn to be X's, print whose turn is next to the console, and increase the turn counter by 1
    else:
        btnTTT[ind].config(text="O", font='Verdana 50', state='disabled', disabledforeground='thistle3')
        state[ind] = "O"
        lblPX.config(bg='thistle')
        lblPO.config(bg='azure2')
        x_turn = True
        turn_counter += 1
        print("X's turn")

    # Define a function for when Player X wins a round that increases X's win counter by 1, updates the
    # scoreboard with their score, prints that they won a round to console, and soft resets the game
    def x_won_round():
        global x_win_counter
        x_win_counter += 1
        lblPXScore.config(text=str(x_win_counter) + '                                        ')
        print('X won a round\n')
        win.after(250, lambda: reset_board())

    # Define a function for when Player O wins a round that increases O's win counter by 1, updates the
    #     # scoreboard with their score, prints that they won a round to console, and soft resets the game
    def o_won_round():
        global o_win_counter
        o_win_counter += 1
        lblPOScore.config(text=str(o_win_counter) + '                                        ')
        print('O won a round\n')
        win.after(250, lambda: reset_board())

    # Check to see if Player X won
    # Vertically
    if state[0] == "X" and state[1] == "X" and state[2] == "X":
        x_won_round()
    elif state[3] == "X" and state[4] == "X" and state[5] == "X":
        x_won_round()
    elif state[6] == "X" and state[7] == "X" and state[8] == "X":
        x_won_round()
    # Horizontally
    elif state[0] == "X" and state[3] == "X" and state[6] == "X":
        x_won_round()
    elif state[1] == "X" and state[4] == "X" and state[7] == "X":
        x_won_round()
    elif state[2] == "X" and state[5] == "X" and state[8] == "X":
        x_won_round()
    # Diagonally
    elif state[0] == "X" and state[4] == "X" and state[8] == "X":
        x_won_round()
    elif state[2] == "X" and state[4] == "X" and state[6] == "X":
        x_won_round()

    # Check to see if Player O won
    # Vertically
    if state[0] == "O" and state[1] == "O" and state[2] == "O":
        o_won_round()
    elif state[3] == "O" and state[4] == "O" and state[5] == "O":
        o_won_round()
    elif state[6] == "O" and state[7] == "O" and state[8] == "O":
        o_won_round()
    # Horizontally
    elif state[0] == "O" and state[3] == "O" and state[6] == "O":
        o_won_round()
    elif state[1] == "O" and state[4] == "O" and state[7] == "O":
        o_won_round()
    elif state[2] == "O" and state[5] == "O" and state[8] == "O":
        o_won_round()
    # Diagonally
    elif state[0] == "O" and state[4] == "O" and state[8] == "O":
        o_won_round()
    elif state[2] == "O" and state[4] == "O" and state[6] == "O":
        o_won_round()

    # If Player X wins 3 times, they win the game. Print that they won to console and display a messagebox
    # that prompts the user to play again or exit the game. Hard reset if they select yes, exit if no
    if x_win_counter == 3:
        print("X won the game!")
        win.update()
        x_box = messagebox.askyesno("Player X Wins!", "X wins\nWould you like to play again?")
        if x_box:
            reset_game()
            x_win_counter = 0
            o_win_counter = 0
            tie_counter = 0
        else:
            exit()

    # If Player O wins 3 times, they win the game. Print that they won to console and display a messagebox
    # that prompts the user to play again or exit the game. Hard reset if they select yes, exit if no
    if o_win_counter == 3:
        print("O won the game!")
        win.update()
        o_box = messagebox.askyesno("Player O Wins!", "O wins\nWould you like to play again?")
        if o_box:
            reset_game()
            x_win_counter = 0
            o_win_counter = 0
            tie_counter = 0
        else:
            exit()

    # If the counter is 9, that means all the squares have been pressed and the result of the round is a tie
    # Update the tie counter and soft reset, and print that it was a tie to the console
    if turn_counter == 9:
        tie_counter += 1
        reset_board()
        print('Tied round\n')

    # If the players tie 3 times, the result of the game is a tie. Print that it wasa tie to console and
    # display a messagebox that prompts the user to play again or exit the game. Hard reset if they select
    # yes, exit if no
    if tie_counter == 3:
        print("Tied game!")
        win.update()
        tie_box = messagebox.askyesno("Tie!", "Tied game\nWould you like to play again?")
        if tie_box:
            reset_game()
            x_win_counter = 0
            o_win_counter = 0
            tie_counter = 0
        else:
            exit()


# Define a reset function that restores the board to its initial state, but doesn't reset the score
def reset_board():
    global x_turn, turn_counter, state
    for i in range(9):
        btnTTT[i].config(text='', state='normal')
        x_turn = True
        turn_counter = 0
    lblPX.config(bg='thistle')
    lblPO.config(bg='azure2')
    state = ['', '', '', '', '', '', '', '', '']


# Define a reset function that restores the entire game to its initial state
def reset_game():
    global x_win_counter, o_win_counter, tie_counter
    reset_board()
    x_win_counter = 0
    o_win_counter = 0
    tie_counter = 0
    lblPXScore.config(text='0                                        ')
    lblPOScore.config(text='0                                        ')
    print("\n==========================\n         New Game\n==========================\n\nX starts")


# Create messageboxes that are executed when the user clicks on the
# drop-down help menu, which informs the player of how to play the game
#
# How to Play messagebox
def htp_menu():
    messagebox.showinfo("How to Play", "Tic Tac Toe is a 2-player, best of 3 game where players take turns marking "
                                       "empty squares until one wins or all the squares are marked.\n\nLeft click on a "
                                       "square to mark it. To start over, click on the reset button. To stop the "
                                       "game and close the application, click on the exit button.\n\n"
                                       "**Player X always goes first.**")


# Objective messagebox
def o_menu():
    messagebox.showinfo("Objective", "To win a round, you must mark 3 adjacent squares, either vertically, "
                                     "horizontally, or diagonally, before your opponent.\n\nTo win the game, "
                                     "you must win 3 rounds. If 3 rounds are tied, the game will result in a tie.")


# Create a frame to hold the list of tic-tac-toe buttons
tttFrame = Frame(win, bg='azure2', highlightthickness=2, highlightbackground='thistle3')
tttFrame.pack()

# Create the list of indexed buttons (tic-tac-toe buttons)
btnTTT = list()
state = ['', '', '', '', '', '', '', '', '']
i = 0
for row in range(3):
    for col in range(3):
        btnTTT.append(Button(tttFrame, text="", height=1, width=1,
                             fg='thistle', font="Verdana 50", relief='groove',
                             command=lambda c=i: click(c)))
        btnTTT[i].grid(row=row, column=col, sticky="news", padx=15, pady=10, ipadx=15, ipady=15)
        i = i + 1

# Create the main frame, which will hold the other frames
mainFrame = Frame(win, bg='azure2', highlightthickness=2, highlightbackground='thistle3')
mainFrame.pack(padx=10, pady=10)

# Create the score frame, which will hold the scoreboard
scoreFrame = Frame(mainFrame, bg='azure2')
scoreFrame.grid(row=0, column=0, pady=10)

# Create the scoreboard, which will hold the players' labels and scores
scoreboard = LabelFrame(scoreFrame, bg='azure2', fg='thistle4', text='Score', font='Verdana 15 bold', labelanchor='nw')
scoreboard.pack(padx=15)

# Create the player labels (displays whose turn it is)
lblPX = Label(scoreboard, bg='thistle', text="Player X:")
lblPX.grid(row=0, column=0, pady=5, padx=5)
lblPO = Label(scoreboard, bg='azure2', text="Player O:")
lblPO.grid(row=1, column=0, pady=5, padx=5)

# Create the player scores (keeps track of each player's points)
lblPXScore = Label(scoreboard, bg='white', text='0                                        ', relief='sunken')
lblPXScore.grid(row=0, column=1, padx=5)
lblPOScore = Label(scoreboard, bg='white', text='0                                        ', relief='sunken')
lblPOScore.grid(row=1, column=1, padx=5)

# Create the button frame, which will hold the reset and exit buttons
buttonFrame = Frame(mainFrame, bg='azure2')
buttonFrame.grid(row=0, column=1)

# Create the reset button (hard resets the game)
btnReset = Button(buttonFrame, text="Reset", font='Verdana 15', fg='thistle4', command=reset_game)
btnReset.grid(row=0, column=0, padx=15, pady=5, ipady=4, ipadx=3)

# Create the exit button (exits the game)
btnExit = Button(buttonFrame, text='Exit', font='Verdana 15', fg='thistle4', command=exit)
btnExit.grid(row=1, column=0, padx=15, pady=5, ipady=3, ipadx=9)

# Create the help drop-down menu (Contains 'How to Play' and 'Objective')
menu = Menu(win)
win.config(menu=menu)
help_menu = Menu(menu, tearoff=False)
menu.add_cascade(label="Help", menu=help_menu)
help_menu.add_command(label="How to play", command=htp_menu)
help_menu.add_command(label="Objective", command=o_menu)

win.mainloop()