import random
import time
from board import Board

def improved_random(board):      
    
    request_car = ""     
    request_move = ""
    count = 0
    
    board_archive = {count: str(board)}
    step_archive = {}
    

    # Plays the game untill won    
    while board.game_won == False:
        board.moveable_cars()
        
        # Function that gets the moveable cars        
        move_cars_objects = []
        
        last_car = request_car
        last_move = request_move

        # Seeks the objects from the corresponding moveable car
        for objects in board.cars.values():
            if objects.name in board.cars_move:
                move_cars_objects.append(objects)

        request_car = random.choice(list(move_cars_objects))
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
    board_duplicates = {current_board: [(k) for (k) in board_archive if board_archive[(k)] == current_board] for current_board in set(board_archive.values())}
    for board_name, counts in board_duplicates.items():
        for count in counts[1:]:
            del board_archive[count]
    for key, value in step_archive.items():
        if key in board_archive.keys():
                solution.append(value)

    return solution, time_elapsed

