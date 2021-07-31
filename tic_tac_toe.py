import numpy as np

board = np.array([['_', '_', '_'], ['_', '_', '_'], ['_', '_', '_']])

player1_symbol = 'X'
player2_symbol = 'O'

def check_rows(symbol):
    #parsing row wise
    for r in range(3):
        count = 0
        for c in range(3):
            if board[r][c] == symbol:
                count += 1
        if count == 3:
            return True


def check_columns(symbol):
    #parsing column wise
    for c in range(3):
        count = 0
        for r in range(3):
            if board[r][c] == symbol:
                count += 1
        if count == 3:
            return True


def check_diagonals(symbol):
    if (board[0][0] == symbol and board[1][1] == symbol and board[2][2] == symbol) or (board[0][2] == symbol and board[1][1] == symbol and board[2][0] == symbol):
        return True


def won(symbol):
    return check_rows(symbol) or check_columns(symbol) or check_diagonals(symbol)


def place(symbol):
    print(np.matrix(board))     #display the list into rows and columns format
    while 1:
        row = int(input('\nRow 1 || Row 2 || Row 3 ? '))
        column = int(input('Column 1 || Column 2 || Column 3 ? '))
        #valid or invalid
        if row > 0 and row < 4 and column > 0 and column < 4 and board[row-1][column-1] == '_':
            break
        else:
            print("Invalid input! Enter again. ")
    board[row-1][column-1] = symbol




def play():
    player1 = str(input("Player 1: Enter your name --> "))
    player2 = str(input("Player 2: Enter your name --> "))
    for turn in range(9):
        #even turns for player1, odd turns for player2
        #player1
        if turn % 2 == 0:
            print('\nPlayer 1: put X: ')
            place(player1_symbol)
            if won(player1_symbol):
                print(player1, 'You Won!')

                break
        else:
            #player2
            print('Player 2: put O: ')
            place(player2_symbol)
            if won(player2_symbol):
                print(player2, 'You Won!')
                break

    if not(won(player1_symbol)) and not(won(player2_symbol)):
        print("Draw! ")





print("\t\t--TIC TAC TOE GAME --\n")
#calling the play function
play()

