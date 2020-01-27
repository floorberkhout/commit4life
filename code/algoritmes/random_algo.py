import random
import time


def random_algo(board):
    solution = []
    
    # Plays the game untill won
    while board.game_won == False:
        # Get random car and move
        request_car = random.choice(list(board.cars.values()))
        
        request_move = random.choice([-1, 1]) 
        
<<<<<<< HEAD
        board.move(request_car, request_move)
        
        solution = board.move_count
=======
        moved = board.move(request_car, request_move)
        if moved is not 0:
            solution.append(", ".join([request_car.name, str(request_move)]))
>>>>>>> 7f46a9917aca824be549b78de23fd705bd87c9a5

        # Checks if another car prevents the winning car from getting out
        board.game_won, time_elapsed = board.check_win(board.start)
<<<<<<< HEAD

=======
        
>>>>>>> 7f46a9917aca824be549b78de23fd705bd87c9a5
    return solution, time_elapsed
