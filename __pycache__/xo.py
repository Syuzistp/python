# #XO GAME
# def board_xo(board, num, xo):
#     return board.replace(num, xo)




# def xo_game():
#     list = [1,2,3,4,5,6,7,8,9]
#     flag = True
#     board = "|1|2|3|\n|4|5|6|\n|7|8|9|"
#     while flag:
#         print(board)
#         xo = input('Enter X or O: ').upper()
#         num = input('Enter the number: ')
#         board = board_xo(board, num, xo)
#         if check_input(num, list):
#             board = board_xo(board, num, xo) 
#         if winner(board)=='X WIN' or winner(board)== 'O WIN':
#             print(winner(board))
#             flag = False 
#         else:
#             flag = True

# def check_input(number, list):
#     if number in list:
#         list.remove(number)
#         return True
#     return False
    

# def winner(board):
#     if board[1] == 'X' and board[3] == 'X' and board[5] == 'X':
#         return 'X WIN'
#     if board[9] == 'X' and board[11] == 'X' and board[13] == 'X':
#         return 'X WIN'
#     if board[17] == 'X' and board[19] == 'X' and board[21] == 'X':
#         return 'X WIN'
#     if board[1] == 'X' and board[9] == 'X' and board[17] == 'X':
#         return 'X WIN'
#     if board[3] == 'X' and board[11] == 'X' and board[19] == 'X':
#         return 'X WIN'
#     if board[5] == 'X' and board[13] == 'X' and board[21] == 'X':
#         return 'X WIN'
#     if board[1] == 'X' and board[11] == 'X' and board[21] == 'X':
#         return 'X WIN'
#     if board[5] == 'X' and board[11] == 'X' and board[17] == 'X':
#         return 'X WIN'


#     if board[1] == 'O' and board[3] == 'O' and board[5] == 'O':
#         return 'O WIN'
#     if board[9] == 'O' and board[11] == 'O' and board[13] == 'O':
#         return 'O WIN'
#     if board[17] == 'O' and board[19] == 'O' and board[21] == 'O':
#         return 'O WIN'
#     if board[1] == 'O' and board[9] == 'O' and board[17] == 'O':
#         return 'O WIN'
#     if board[3] == 'O' and board[11] == 'O' and board[19] == 'O':
#         return 'O WIN'
#     if board[5] == 'O' and board[13] == 'O' and board[21] == 'O':
#         return 'O WIN'
#     if board[1] == 'O' and board[11] == 'O' and board[21] == 'O':
#         return 'O WIN'
#     if board[5] == 'O' and board[11] == 'O' and board[17] == 'O':
#         return 'O WIN'
#     elif "1" or "2" or "3" or "4" or "5" or "6" or "7" or "8" or "9" not in board:
#         return "Draw"
# xo_game()