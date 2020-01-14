import random
import time


def winning_row(board):
    
    # Plays the game untill won
    while board.game_won == False:
        
        # Creates archive for last move
        last_car = board.request_car
        last_move = board.request_move

        # Get random car and move
        board.request_car = random.choice(list(board.cars.values()))
        
        board.request_move = random.choice([-1, 1]) 

        # Makes sure it doesn't reverse the last move
        if board.request_car == last_car:
            if board.request_move != last_move:
                board.make_move = "no"  
            else:
                board.move_count -= 1
                
        # If move creates new state of board (so no reversing of last move), perfom move    
        if board.make_move == "yes":
            board.move(board.request_car, board.request_move)
            board.write_move(board.request_car, board.request_move, board.log)

            # Increases move count
            board.move_count += 1
        
        # check if the game has been won ( when the XX car is in front of the exit)
        if board.board[board.length-1][int(board.length/2-0.5)] == "X":
            time_elapsed = time.time() - start
            game_won = True

    return move_count, time_elapsed
