import random

print("1) Do you want to play with the computer?")
print("2) Do you want to play with another player?")
game_version = input("1 or 2: ")


def board_xo(board, num, xo):
    return board.replace(num, xo)


def with_computer():
    flag = True
    board = "|1|2|3|\n|4|5|6|\n|7|8|9|"  
    ml = ['1', '2', '3', '4', '5', '6', '7', '8', '9']  
    
    while flag:
        print(board)

        if len(ml) % 2 != 0:  
            xo = 'X'
            print("Your turn")
            num = input('Enter the number: ')
            ml.remove(num)
            board = board_xo(board, num, xo)

        else:
            xo = 'O'
            print("Computer's turn")
            num = random.choice(ml)
            ml.remove(num) 
            board = board_xo(board, num, xo)
        

        if winner(board):
            print(board)
            print(winner(board))
            flag = False 

        else:
            flag = True  


def with_another_player():
    flag = True
    board = "|1|2|3|\n|4|5|6|\n|7|8|9|" 
    ml = ['1', '2', '3', '4', '5', '6', '7', '8', '9']  
    
    while flag:
        print(board)
        if len(ml) % 2 != 0: 
            xo = 'X'
            print("Player X")
            num = input('Enter the number: ')
            ml.remove(num)
            board = board_xo(board, num, xo)
        else:
            xo = 'O'
            print("Player O")
            num = input('Enter the number: ')
            ml.remove(num) 
            board = board_xo(board, num, xo)
        

        if winner(board):
            print(board)
            print(winner(board))
            flag = False 
        else:
            flag = True  
    

def winner(board):
    if board[1] == 'X' and board[3] == 'X' and board[5] == 'X':
        return 'X WIN'
    if board[9] == 'X' and board[11] == 'X' and board[13] == 'X':
        return 'X WIN'
    if board[17] == 'X' and board[19] == 'X' and board[21] == 'X':
        return 'X WIN'
    if board[1] == 'X' and board[9] == 'X' and board[17] == 'X':
        return 'X WIN'
    if board[3] == 'X' and board[11] == 'X' and board[19] == 'X':
        return 'X WIN'
    if board[5] == 'X' and board[13] == 'X' and board[21] == 'X':
        return 'X WIN'
    if board[1] == 'X' and board[11] == 'X' and board[21] == 'X':
        return 'X WIN'
    if board[5] == 'X' and board[11] == 'X' and board[17] == 'X':
        return 'X WIN'


    if board[1] == 'O' and board[3] == 'O' and board[5] == 'O':
        return 'O WIN'
    if board[9] == 'O' and board[11] == 'O' and board[13] == 'O':
        return 'O WIN'
    if board[17] == 'O' and board[19] == 'O' and board[21] == 'O':
        return 'O WIN'
    if board[1] == 'O' and board[9] == 'O' and board[17] == 'O':
        return 'O WIN'
    if board[3] == 'O' and board[11] == 'O' and board[19] == 'O':
        return 'O WIN'
    if board[5] == 'O' and board[13] == 'O' and board[21] == 'O':
        return 'O WIN'
    if board[1] == 'O' and board[11] == 'O' and board[21] == 'O':
        return 'O WIN'
    if board[5] == 'O' and board[11] == 'O' and board[17] == 'O':
        return 'O WIN'
    
    
    if "1" not in board and "2" not in board and "3" not in board and "4" not in board and "5" not in board and "6" not in board and "7" not in board and "8" not in board and "9" not in board:
        return "Draw"


if game_version == '1':
    with_computer()
elif game_version == '2':
    with_another_player()