import random

board = [' ' for _ in range(9)]

def print_board(board):
    print(f" {board[0]} | {board[1]} | {board[2]} ")
    print("---|---|---")
    print(f" {board[3]} | {board[4]} | {board[5]} ")
    print("---|---|---")
    print(f" {board[6]} | {board[7]} | {board[8]} ")


print_board(board)
def player_move(board, player):
    while True:
        
            position = int(input(f"Player {player}, enter your move (0-8): "))
            if position < 0 or position > 8:
                print("Invalid position! Choose a number from 0 to 8.")
            elif board[position] != ' ':
                print("That position is already taken. Try another one.")
            else:
                board[position] = player
                break
def comp_move(board,player):
     while True:
          num=random.randint(0,8)
          if board[num]!=' ':
             print("That position is already taken. Try another one.")
          else:
               board[num]=player
               break  

while True:
     player_move(board, 'X')
     comp_move(board,'O')
     print_board(board)