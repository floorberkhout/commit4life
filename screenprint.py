import csv

with open('games/Rushhour6x6_1.csv', newline='') as csvfile:
    cars = list(csv.reader(csvfile))

# dimensions of the board
n=6

board=[]

# initialize the matrix with dots
for rows in range(n):
    row = ['.'] * n
    board.append(row)

# read in the cars
itercars = iter(cars)
next(itercars)
for car in itercars:
    x = int(car[2][-1])-1
    y = int(car[3][0])-1
    car_char = car[0]
    char_length = int(car[4])

    if(car[1]=="H"):
        for letter in range(char_length):
            board[x-letter][y] = car_char
    else:
        for letter in range(char_length):
            board[x][y-letter] = car_char

print("cars loaded")

print("")

# prints the board
for dash in range(n+2):
    print("_", end="")
print("")
for i in range(n):
    print("|", end="")
    for j in range(n):
        print(board[i][j], end="")
        j =+ 1
    if (i+1)/n != 0.5:
        print("|", end="")
    print("")
    i =+ 1
for dash in range(n+2):
    print("-", end="")
print("")
