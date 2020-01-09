import random

def Random_move(board):
    
    move_count = 0
    game_won = False

    
    # Plays the game untill won
    while game_won == False:
        
        # Get random car and move
        request_car = random.choice(board.cars)
        print("This is the random car")
        print(request_car)
        print("This is the random car")
        request_move = random.choice([-1, 1]) 
        
        move(board, request_car, request_move)

        # Increases move count
        move_count += 1
        print(move_count)
        
        
        # check if the game has been won ( when the XX car is in front of the exit)
        winning_car = board.board[board.length-1][int(board.length/2-0.5)]
        if winning_car.name == "X":
            game_won = True
        print("hoi")
            
    # print the board one more time and tell the player he has won
    print(board.board)
    print("Congratulations you've won the game!")

def move(board, request_car, request_move):
    # Moves chosen car
    print("check if car ", request_car, "can make move ", request_move)

    # fetch the current possition of the car
    x = request_car.coordinates[0]
    y = request_car.coordinates[1]
    
    # check if the move would be valid TODO:
    if request_car.orientation == "H":

        try:
            for position in range(request_car.length):
                if board.board[x+position+request_move][y] != "." and board.board[x+position+request_move][y] != request_car.name or x + position + request_move < 0:
                    print("1: invalid move")
                    return 0
        except IndexError:
            print("invalid move")
            return 0
        for position in range(car.length):
            board.board[x+position][y] = "."
        for position in range(car.length):
            board.board[x+position+request_move][y] = request_car
        request_car.coordinates[0] = int(x+request_move)

    else:
        try:
            for position in range(request_car.length):
                if board.board[x][y-position+request_move] != "." and board.board[x][y-position+request_move] != request_car.name or y - position + request_move < 0:
                    print("invalid move")
                    return 0
        except IndexError:
            print("invalid move")
            return 0
        for position in range(request_car.length):
            board.board[x][y-position] = "."
        for position in range(request_car.length):
            board.board[x][y-position+request_move] = request_car
        request_car.coordinates[1] = int(y+request_move)


