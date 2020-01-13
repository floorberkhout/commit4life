import time
from board import Board

def Algoritme1(board):    
    game_won = False
    log_file = "resultaten/log.csv"
    log = open(log_file, "w")
    log.truncate()
    header = "car" + ',' + "move" + '\n'
    log.write(header)
    board.print_board()
    move_count = 0
    
    # Plays the game untill won
    while game_won == False:
        end_board = board.board[board.length-1][int(board.length/2-0.5)]
        if end_board != ".":
            
            
            
        
        
    # Get random car and move
            
        # request_car = random.choice(list(board.cars.values()))
#
        #request_move = random.choice([-1, 1])
    
        # move(board, request_car, request_move)
#         write_move(request_car, request_move, log)

        # Increases move count
        move_count += 1
    
        # check if the game has been won ( when the XX car is in front of the exit)
        if board.board[board.length-1][int(board.length/2-0.5)] == "X":
            time_elapsed = time.time() - start
            game_won = True
            
        # print the board one more time and tell the player he has won
        print("Congratulations you've won the game!")
        print("Move count: ", move_count)
        print("Time elapsed: ", time_elapsed)
        return move_count, time_elapsed