import time
from board import Board

def algoritme1(board):    
    
    # Plays the game untill won
    while board.game_won == False:
        for col in board.board:
            print(col)
            for car in col:
                if car != ".":
                    print(type(car))
  
            board.move_count += 1
    
        # check if the game has been won ( when the XX car is in front of the exit)
        if board.board[board.length-1][int(board.length/2-0.5)] == "X":
            time_elapsed = time.time() - start
            game_won = True
            
         
    return board.move_count, time_elapsed