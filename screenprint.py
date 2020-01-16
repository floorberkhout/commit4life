import csv
import random
import time

with open('data/Rushhour6x6_2.csv', newline='') as csvfile:
    cars = list(csv.reader(csvfile))

# dimensions of the board
n=6
log = ""

board=[]
car_list = []

# initialize the matrix with dots
for rows in range(n):
    row = ['.'] * n
    board.append(row)

# read in the cars and clean the cars data
itercars = iter(cars)
next(itercars)
for car in itercars:

    y = abs(int(car[3][0]) - n)
    car[3] = y
    print(f" y: {y}")
    x = int(car[2][-1]) - 1
    car[2] = x
    print(x)

    car_char = car[0]
    car_orientation = car[1][-1]
    car[1] = car_orientation
    car_length = int(car[4])
    car[4] = car_length

    # create a list with all the cars in the play
    car_list.append(car_char)

    # saves coordinates of length car
    if(car_orientation=="H"):
        for letter in range(car_length):
            board[x+letter][y] = car_char

    else:
        for letter in range(car_length):
            board[x][y-letter] = car_char

print("cars loaded")
print(car_list)
print("")

def printboard():
    """ prints the board"""
    for dash in range(n+2):
        print("_", end="")
    print("")
    for y in range(n):
        print("|", end="")
        for x in range(n):
            print(board[x][y], end="")
        if y != int(n/2-0.5):
            print("|", end="")
        print("")
    for dash in range(n+2):
        print("-", end="")
    print("")

def ask_move():
    while True:
        user_input = input("what move would you like to make? ([car], [move]): ")
        a = tuple(x for x in user_input.split(","))
        request_car = a[0]
        request_move = int(a[1])
        if request_car in car_list and request_move > - n and request_move < n:
            break
        # print("invalid input")
    move(request_car, request_move)

# ask user for a move
def move(request_car, request_move):
    """ funcation that allows a car to make a move """
    # print("check if car ", request_car, "can make move ", request_move)

    # fetch the current possition of the car
    itercars = iter(cars)
    next(itercars)
    for car in itercars:
        if car[0] == request_car:
            car_length = car[4]
            car_char = car[0]
            y = car[3]
            x = car[2]

            # check if the move would be valid
            if car[1] == "H":
                try:
                    for position in range(car_length):
                        if board[x+position+request_move][y] != "." and board[x+position+request_move][y] != car_char or x + position + request_move < 0:
                            # print("invalid move")
                            return(0)
                except IndexError:
                    # print("invalid move")
                    return(0)
                for position in range(car_length):
                    board[x+position][y] = "."
                for position in range(car_length):
                    board[x+position+request_move][y] = car_char
                car[2] = x+request_move
            else:
                try:
                    for position in range(car_length):
                        if board[x][y-position+request_move] != "." and board[x][y-position+request_move] != car_char or y - position + request_move < 0:
                            # print("invalid move")
                            return(0)
                except IndexError:
                    # print("invalid move")
                    return(0)
                for position in range(car_length):
                    board[x][y-position] = "."
                for position in range(car_length):
                    board[x][y-position+request_move] = car_char
                car[3] = y+request_move


# set game_won boolean to false
game_won = False

def random_move():
    request_car = random.choice(car_list)
    request_move = random.choice([-1, 1])
    return(request_car, request_move)

# write a move to the log
def write_move(request_car, request_move):
    global log
    log_row = request_car + ',' + str(request_move) + '\n'
    log.write(log_row)

# sort of init
move_count = 0
start = time.time()
log_file = "log.csv"
log = open(log_file, "w")
log.truncate()
header = "car" + ',' + "move" + '\n'
log.write(header)

# play the game untill won
while game_won == False:
    printboard()
    # request_car = random_move()[0]
    # request_move = random_move()[1]
    # move(request_car, request_move)
    ask_move()
    # write_move(request_car, request_move)

    move_count += 1

    # check if the game has been won ( when the XX car is in front of the exit)
    if board[n-1][int(n/2-0.5)] == "X":
        time_elapsed = time.time() - start
        game_won = True

# print the board one more time and tell the player he has won
printboard()
print("Congratulations you've won the game!")
print("Move count: ", move_count)
print("Time elapsed: ", time_elapsed)
