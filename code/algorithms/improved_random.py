############################################
#   improved_random.py
#   Makes a random improved algorithm
############################################

import random
import time
from board import Board
from node import Node

def improved_random(board):      
    count = 0
    board_archive = {count: str(board)}
    step_archive = {}
    
    # Plays the game untill won    
    while board.game_won == False:
        # Function that gets the moveable cars        
        move_cars_objects = []

        # Seeks the objects from the corresponding moveable car
        for objects in board.cars.values():
            if objects.name in board.cars_move:
                move_cars_objects.append(objects)
        # Function that gets the moveable cars          
        board.moveable_cars()
        
        # Function that seeks the objects from the corresponding moveable car
        board.get_car_objects()

        request_car = random.choice(list(board.move_cars_objects))
        
        request_move = random.choice([-1, 1])

        # If move creates new state of board (so no reversing of last move), perform move
        moved = board.move(request_car, request_move)
        if moved is not 0:
            count += 1
            board_archive[count] = str(board)
            step_archive[count] = [request_car, request_move]        
                   
        # Checks if another car prevents the winning car from getting out
        board.game_won, time_elapsed = board.check_win(board.start)

    # https://stackoverflow.com/questions/52508696/check-if-repeating-key-or-value-exists-in-python-dictionary
    solution = []
    
    # Checks how many keys contain the same board state by creating a set of the board_archive dictionary 
    # and checking how many times every unique board from the set appears in the dictionary and with which key
    board_duplicates = {current_board: [(k) for (k) in board_archive if board_archive[(k)] == current_board] for current_board in set(board_archive.values())}
    
    # Deletes the duplicated boards from the archive but never the one that appeared first
    for board_name, counts in board_duplicates.items():
        for count in counts[1:]:
            del board_archive[count]
    
    # Adds the steps to solution that correspond with the boards that are left after deleting the duplicated boards
    for key, value in step_archive.items():
        if key in board_archive.keys():
                solution.append(value)

    return solution, time_elapsed

