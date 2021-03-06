###############################################################
#   randomize_check_generated.py
#   Adapted randomize algorithm used to test random generated boards
###############################################################

import random
import time


def randomize_check_generated(board):
    """ Adapted randomize algorithm used to test random generated boards """
    solution = []

    counter = 0

    # Plays the game untill won
    while board.game_won == False:

        # Gets random car and move
        request_car = random.choice(list(board.cars.values()))
        request_move = random.choice([-1, 1])

        # Moves car and if moved adds step to solution
        moved = board.move(request_car, request_move)
        if moved is not 0:
            solution.append(", ".join([request_car.name, str(request_move)]))

        # Checks if another car prevents the winning car from getting out
        board.game_won, time_elapsed = board.check_win(board.start)

        counter += 1
        if counter > 100000:
            return False, False

    return solution, time_elapsed
