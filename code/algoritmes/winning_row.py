import random
import time
import csv


def Winning_row(board):
    
    move_count = 0
    game_won = False
    winning_row = []
    start = time.time()
    log_file = "resultaten/log.csv"
    log = open(log_file, "w")
    log.truncate()
    header = "car" + ',' + "move" + '\n'
    log.write(header)
    
    # Plays the game untill won
    while game_won == False:
        
        # Get random car and move
        request_car = random.choice(list(board.cars.values()))
        
        request_move = random.choice([-1, 1]) 
        
        move(board, request_car, request_move)
        write_move(request_car, request_move, log)

        # Increases move count
        move_count += 1
        
        # Checks if another car prevents the winning car from getting out
        for spot in range(len(board.board)):
            winning_row.append(board.board[spot][int(board.length/2-0.5)])

        for car in winning_row:
            if car != "." and car.name == "X":
                print(car.coordinates)
                for spot in winning_row[(car.coordinates[0] + car.length):]:
                    if spot != ".":
                        break
                    time_elapsed = time.time() - start
                    game_won == True

    # print the board one more time and tell the player he has won
    board.print_board()
    print("Congratulations you've won the game!")
    print("Move count: ", move_count)
    print("Time elapsed: ", time_elapsed)
    return move_count, time_elapsed

def move(board, request_car, request_move):

    # fetch the current possition of the car
    x = request_car.coordinates[0]
    y = request_car.coordinates[1]
    
    # check if the move would be valid TODO:
    if request_car.orientation == "H":
        try:
            for position in range(request_car.length):
                if board.board[x+position+request_move][y] != "." and board.board[x+position+request_move][y] != request_car.name or x + position + request_move < 0:
                    return 0
        except IndexError:
            return 0
        for position in range(request_car.length):
            board.board[x+position][y] = "."
        for position in range(request_car.length):
            board.board[x+position+request_move][y] = request_car.name
        request_car.coordinates[0] = int(x+request_move)
        board.print_board()
        
    else:
        try:
            for position in range(request_car.length):
                if board.board[x][y-position+request_move] != "." and board.board[x][y-position+request_move] != request_car.name or y - position + request_move < 0:
                    return 0
        except IndexError:
            return 0
        for position in range(request_car.length):
            board.board[x][y-position] = "."
        for position in range(request_car.length):
            board.board[x][y-position+request_move] = request_car.name
        request_car.coordinates[1] = int(y+request_move)
        board.print_board()

# write a move to the log
def write_move(request_car, request_move, log):
    log_row = request_car.name + ',' + str(request_move) + '\n'
    log.write(log_row)    