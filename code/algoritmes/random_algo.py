import random
import time


def random_algo(board):
    
    # Plays the game untill won
    while board.game_won  == False:
        
        # Get random car and move
        request_car = random.choice(list(board.cars.values()))
        
        request_move = random.choice([-1, 1]) 
        
        board.move(request_car, request_move)

        # board.write_move(request_car, request_move, board.log)
 
        # Checks if another car prevents the winning car from getting out
        board.game_won, time_elapsed = board.check_win(board.start)

    return board.move_count, time_elapsed
