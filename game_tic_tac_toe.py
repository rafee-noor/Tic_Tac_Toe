#---Global variables--

game_still_going = True
current_player = "X"
winner = None

#Board
board = [
         "-","-","-",
         "-","-","-",
         "-","-","-"
         ]

def display_board():
    print(board[0] + " |", board[1] + " |", board[2]  )
    print(board[3] + " |", board[4] + " |", board[5]  )
    print(board[6] + " |", board[7] + " |", board[8] )

def play_game():
    display_board()

    #Logic of the game
    while game_still_going:
        handle_turn(current_player)
        check_if_game_over()
        flip_player()

    #The Game has ended
    if winner == "X" or winner == "O":
        print(winner + " WON")
    elif winner == None :
        print(winner + "TIE")


def handle_turn(player):

    print(player + "'s turn")
    position = input("enter a value from 1-9 : ")

    #Trick part Replaceing the value
    valid = False
    while not valid:
        while position not in ["1", "2", "3", "4", "5", "6", "7", "8"]:
            position = input("Invalid input. Enter a value from 1-9 : ")

        if board[position] == "-":
            valid = True

        else:
            print("You can't go there")



    #user input is integer value, but list start from 0 index
    position = int(position) -1

    board[position] = player
    display_board()

def check_if_game_over():
    check_if_win()
    check_if_tie()

def check_if_win():

#for accessing global variable
    global winner

    #check rows
    row_win = check_rows()
    #check columns
    column_win= check_columns()
    #check diagonals
    diagonal_win= check_diagonals()

    if row_win:
        # There was a win
        winner = row_win

    elif column_win:
        # There was a win
        winner = column_win

    elif diagonal_win:
        # There was a win
        winner = diagonal_win

    else:
        #There was a tie
        winner = None
    return

def check_rows():

    # for accessing global variable
    global game_still_going

    #for checking the wining row values
    row_1= board[0] == board[1] == board[2] != "-" #using != "-" because three empty list will declare a win
    row_2 = board[3] == board[4] == board[5]!= "-"
    row_3 = board[6] == board[7] == board[8]!= "-"

    #If any rows match then flag that it will be a win!
    if row_1 or row_2 or row_3 :
        game_still_going = False

    #Checking who won X/O
    if row_1:
        return board[0]
    elif row_2:
        return board[3]
    elif row_3:
        return board[6]

    return

def check_columns():

    # for accessing global variable
    global game_still_going

    # for checking the wining row values
    column_1 = board[0] == board[3] == board[6] != "-"  # using != "-" because three empty list will declare a win
    column_2 = board[1] == board[4] == board[7] != "-"
    column_3 = board[2] == board[5] == board[8] != "-"

    # If any column match then flag that it will be a win!
    if column_1 or column_2 or column_3:
        game_still_going = False

    # Checking who won X/O
    if column_1:
        return board[0]
    elif column_2:
        return board[1]
    elif column_3:
        return board[2]

    return

def check_diagonals():
    # for accessing global variable
    global game_still_going

    # for checking the wining row values
    diagonal_1 = board[0] == board[4] == board[8] != "-"  # using != "-" because three empty list will declare a win
    diagonal_2 = board[2] == board[4] == board[6] != "-"

    # If any diagonal match then flag that it will be a win!
    if diagonal_1 or diagonal_2 :
        game_still_going = False

    # Checking who won X/O
    if diagonal_1:
        return board[0]
    elif diagonal_2:
        return board[2]


    return

def check_if_tie():
    global game_still_going
    if "-" not in board:
        game_still_going = False
    return
def flip_player():

    global current_player

    if current_player == "X":
        current_player = "O"
    elif current_player == "O":
        current_player = "X"
    return
play_game()