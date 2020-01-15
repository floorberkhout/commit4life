import random
import time


def random_algo(board):
    
    # Plays the game untill won
    while board.game_won  == False:
        
        # Get random car and move
        request_car = random.choice(list(board.cars.values()))
        
        request_move = random.choice([-1, 1]) 
        
        board.move(request_car, request_move)
        board.write_move(request_car, request_move, board.log)
        
        # check if the game has been won ( when the XX car is in front of the exit)
        if board.board[board.length-1][int(board.length/2-0.5)] == "X":
            time_elapsed = time.time() - board.start
            board.game_won = True
            
            return board.move_count, time_elapsed

