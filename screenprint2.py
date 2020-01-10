import csv
import random
import time

with open('data/Rushhour6x6_1.csv', newline='') as csvfile:
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
    x = int(car[2][-1]) - 1
    car[2] = x

    car_char = car[0]
    car_orientation = car[1][-1]
    car[1] = car_orientation
    car_length = int(car[4])
    car[4] = car_length

    # create a list with all the cars in the play
    car_list.append(car_char)

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

def fetch_car_data(request_car):
    itercars = iter(cars)
    next(itercars)
    for car in itercars:
        if car[0] == request_car:
            return car
    return(1)


# ask user for a move
def move(request_car, request_move):
    """ function that allows a car to make a move """
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




def random_move():
    request_car = random.choice(car_list)
    request_move = random.choice([-1, 1])
    return(request_car, request_move)

# write a move to the log
def write_move(request_car, request_move):
    global log
    log_row = request_car + ',' + str(request_move) + '\n'
    log.write(log_row)



def determine_moves(request_car):
    moves = []
    print(request_car)
    # fetch the car details
    request_car = fetch_car_data(request_car)
    car_orientation = request_car[1]
    x = request_car[2]
    y = request_car[3]
    length = request_car[4]

    # determine moves
    if car_orientation == 'H':
        print('h')
        for i in range (x + length, n):
            print(i)
            if board[i][y] == '.':
                print(i)
                print(i-x)
                moves.append(i - x - length + 1)
            else:
                break
        for i in range(x -1, -1, -1):
            print(i)
            if board[i][y] == '.':
                print(i)
                print(i-x)
                moves.append(i - x)
            else:
                break
    else:
        for i in range (y - length, -1, -1):
            if board[x][i] == '.':
                moves.append(i - y)
            else:
                break
        for i in range(y , n, -1):
            if board[i][y] == '.':
                moves.append(i - y - length + 1)
            else:
                break
    print(moves)
    return moves


# nodes algorithm
def node_algorithm():
    global nodes

# 1. Take the node highest up the tree




# 2. Identify all possible moves
# 3. Create the corresponding nodes
# 4. Compare the new nodes with nodes earlier up the tree
# 5. Check if the game is won
# 6. Shut of nodes that represent a board state that was achieved before


# sort of init
move_count = 0
start = time.time()
log_file = "log.csv"
log = open(log_file, "w")
log.truncate()
header = "car" + ',' + "move" + '\n'
log.write(header)

# set game_won boolean to false
game_won = False

nodes = {}

nodes[0] = {}
nodes[0]['board'] = board
nodes[0]['won'] = False
nodes[0]['new'] = False
nodes[0]['moves'] = []

print(nodes[0])
print(nodes[0]['moves'])

# check if the game has been won ( when the XX car is in front of the exit)
def check_if_won():
    if board[n-1][int(n/2-0.5)] == "X":
        return True
    return False





request_car = random_move()[0]
request_move = random_move()[1]
determine_moves('A')


# # play the game untill won
# while game_won == False:
#     # printboard()
#     request_car = random_move()[0]
#     request_move = random_move()[1]
#     determine_moves(request_car)
#     move(request_car, request_move)
#     # write_move(request_car, request_move)
#
#     move_count += 1
#
#
#     if check_if_won():
#         time_elapsed = time.time() - start
#         game_won = True

# print the board one more time and tell the player he has won
printboard()
print("Congratulations you've won the game!")
print("Move count: ", move_count)
print("Time elapsed: ", time_elapsed)
