import random
import time

def get_request(board, winning_row):
    
    for spot in winning_row[::-1]:
        if spot != ".":
            for car in board.cars.values():
                if car.name == spot:
                    print(spot, car.name)
                    request_car = car
                    return request_car

def winning_row(board):
    request_car = board.request_car
    request_move = board.request_move
    move_count = board.move_count
    log = board.log
    cars = board.cars.values()
    length = board.length
    start = board.start
    game_won = board.game_won
    list_board = board.board
    
    # Plays the game untill won
    while game_won == False:
        
        make_move = "yes"
        winning_row = []
        
        # Creates archive for last move
        last_car = request_car
        last_move = request_move


        for spot in range(len(list_board)):
            winning_row.append(list_board[spot][int(length/2-0.5)])
        
        request_car = get_request(board, winning_row)                           

        # Makes sure it doesn't reverse the last move
        if request_car == last_car:
            if request_move != last_move:
                make_move = "no" 

            else:
                move_count -= 1
               
        # If move creates new state of board (so no reversing of last move), perfom move    
        if make_move == "yes":
            board.move(request_car, request_move)
            board.write_move(request_car, request_move, log)

            # Increases move count
            move_count += 1

        # check if the game has been won ( when the XX car is in front of the exit)
        board.game_won, time_elapsed = board.check_win(board.start)
            
    return move_count, time_elapsed

