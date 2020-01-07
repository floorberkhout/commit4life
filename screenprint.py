import csv

with open('games/Rushhour6x6_1.csv', newline='') as csvfile:
    cars = list(csv.reader(csvfile))

# dimensions of the board
n=6

board=[]
car_list = []

# initialize the matrix with dots
for rows in range(n):
    row = ['.'] * n
    board.append(row)

# read in the cars
itercars = iter(cars)
next(itercars)
for car in itercars:

    y = abs(int(car[3][0]) - n)

    x = int(car[2][-1]) - 1

    car_char = car[0]
    char_length = int(car[4])

    # create a list with all the cars in the play
    car_list.append(car_char)

    if(car[1]==" H"):
        for letter in range(char_length):
            board[x+letter][y] = car_char

    else:
        for letter in range(char_length):
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

printboard()

def ask_move():
    while True:
        user_input = input("what move would you like to make? ([car], [move]): ")
        a = tuple(x for x in user_input.split(","))
        car = a[0]
        request = int(a[1])
        if car in car_list and request > - 5 and request < 5:
            break
        print("invalid input")
    move(car, request)

# ask user for a move
def move(car, request):
    """ funcation that allows a car to make a move """
    print("check if car ", car, "can make move ", request)

    # check if the move would be valid


    # perform the move

ask_move()
