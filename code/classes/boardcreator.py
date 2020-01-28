import copy
import time
import sys
import csv
import random

class BoardCreator:
    def __init__(self, length, number_of_cars):
        self.length = length
        self.number_of_cars = number_of_cars

        self.log = open("data/%s%sx%s_%s.csv" %("Rushhour", self.length, self.length, "new"), "w")
        log_row = 'car' + ',' + ' orientation' + ',' + ' "x,y"' + ',' + ' length' + '\n'
        self.log.write(log_row)

        self.list_of_car_chars = "ABCDEFGHIJKLMNOPQRSTUVWYZ"
        self.create_board()
        self.fill_board()

    def fill_board(self):
        # place the X car # for now on the last node of the board
        x = 0
        y = int(self.length/2 - 0.5)
        car_length = 2
        car_orientation = 'H'
        car_char = 'X'
        self.place_car(car_char, x, y, car_length, car_orientation)
        self.write_row(car_char, x, y, car_length, car_orientation)
        reset_needed = False

        for car in range(self.number_of_cars):
            for i in range(1000):
                option = self.determine_spot()
                if option:
                    break
                if i == 999:
                    reset_needed = True
                    break
            if reset_needed == True:
                break
            self.place_car(self.list_of_car_chars[car], option[0], option[1], 2, option[2])
            self.write_row(self.list_of_car_chars[car], option[0], option[1], 2, option[2])

        if reset_needed == True:
            self.reset()

        self.log.close()

        self.print_board()


    def write_row(self, car_char, x, y, car_length, car_orientation):
        # A, H, "2,6", 2
        x = x + 1
        y = self.length - y
        xy = '"' + str(x) + ',' + str(y) + '"'
        xy = " " + xy
        car_orientation = " " + car_orientation
        car_length = " " + str(car_length)

        log_row = car_char + ',' + car_orientation + ',' + xy + ',' + car_length + '\n'
        self.log.write(log_row)

    def determine_spot(self):
        # define empty spots
        empty_spots = [(ix,iy) for ix, row in enumerate(self.board) for iy, i in enumerate(row) if i == '.']

        # choose a random empty spot
        empty_spot = random.choice(empty_spots)
        H = False
        V = False

        # see if length 2 is possible to put in both H and V if so place car random betwen H and V
        if empty_spot[0] < self.length - 1:
            if empty_spot[1] != int(self.length/2 - 0.5):
                if self.board[empty_spot[0] + 1][empty_spot[1]] == '.':
                    H = True
        if empty_spot[1] - 1 > -1:
            if self.board[empty_spot[0]][empty_spot[1] - 1] == '.':
                V = True

        # choose random between H and V if both possible
        if H == True & V == True:
            car_orientation = random.choice(['H', 'V'])
        elif H == True:
            car_orientation = 'H'
        elif V == True:
            car_orientation = 'V'
        else:
            return False

        # return the possible car location length and orientation
        return empty_spot[0], empty_spot[1], car_orientation

    def place_car(self, car_char, x, y, car_length, car_orientation):
        for position in range(car_length):
            if car_orientation == 'H':
                self.board[x + position][y] = car_char
            else:
                self.board[x][y - position] = car_char


    def create_board(self):
        """ Creates the empty board """

        self.board=[]

        for rows in range(self.length):
            row = ['.'] * self.length
            self.board.append(row)

    def reset(self):
        self.__init__(self.length, self.number_of_cars)

    def print_board(self):
        """ Prints the board """

        # Prints border
        print(' '"_", end="")
        for dash in range(self.length + int(self.length / 3)):
            print("___", end="")
        print("_", end="")
        print("")
        for y in range(self.length):
            print("|",' ', end="")

            # Prints content
            for x in range(self.length):
                if len(self.board[x][y]) == 1:
                    print(self.board[x][y], '  ', end="")
                else:
                    print(self.board[x][y], ' ', end="")
            if y != int(self.length/2-0.5):

                # Prints border
                print("|", end="")
            print("")
        print(' '"-", end="")
        for dash in range(self.length + int(self.length / 3)):
            print("---", end="")
        print("-", end="")
        print("")
