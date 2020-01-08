import csv

with open('data/Rushhour6x6_1.csv', newline='') as csvfile:
    cars = list(csv.reader(csvfile))

# dimensions of the board
n=6

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
            x =+ 1
        if (y+1)/n != 0.5:
            print("|", end="")
        print("")
        y =+ 1
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
        print("invalid input")
    move(request_car, request_move)

# ask user for a move
def move(request_car, request_move):
    """ funcation that allows a car to make a move """
    print("check if car ", request_car, "can make move ", request_move)



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
                        if board[x+position+request_move][y] != "." and board[x+position+request_move][y] != car_char and x+postion+request_move < 0:
                            print("invalid move")
                            return(0)
                except IndexError:
                    print("invalid move")
                    return(0)
                for position in range(car_length):
                    board[x+position][y] = "."
                for position in range(car_length):
                    board[x+position+request_move][y] = car_char
                car[2] = x+request_move
            else:
                try:
                    for position in range(car_length):
                        if board[x][y-position+request_move] != "." and board[x][y-position+request_move] != car_char:
                            print(position)
                            print(x, y, request_move)
                            print("invalid move")
                            return(0)
                except IndexError:
                    print("invalid move")
                    return(0)
                for position in range(car_length):
                    board[x][y-position] = "."
                for position in range(car_length):
                    board[x][y-position+request_move] = car_char
                car[3] = y+request_move

        # todo fix out of bounds going round?

# set game_won boolean to false
game_won = False

# play the game untill won
while game_won == False:
    printboard()
    print(cars[13])
    ask_move()
    print(board[n-1][int(n/2-0.5)])
    if board[n-1][int(n/2-0.5)] == "X":
        game_won = True

printboard()
print("Congratulations you've won the game!")

    # check if the game has been won ( when the XX car is in front of the exit)