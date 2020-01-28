#####################################################
#   board.py
#   Implements board with cars for game Rush Hour.
#####################################################

from car import Car
import time
import numpy as np

class Board:

    def __init__(self, car_file):
        """ Initializes the game of Rush Hour """

        # Gets width and hide of board from file name
        length = [car_file[13]]
        if car_file[14].isdigit() == True:
            length.append(car_file[14])
        self.length = int(''.join(length))

        # Get car data
        self.cars = self.load_cars(car_file)

        # Create empty board
        self.board = self.create_board(car_file)

        # Fill empty board with cars
        self.fill_board()

        # gives the board a name tag
        self.name = car_file[5:-4]
        print(self.name)

        # Variables that are required for all the algorithms
        self.start_algo()
        
        # Function to get all moveable cars
        self.moveable_cars()
        
    
    def load_cars(self, car_file):
        """ Loads car data from the given csv file """

        game_data = []

        # Loads from datafile
        with open(car_file, "r") as f:

            for line in f:
                line = line.split()
                game_data.append(line)
            game_data.remove(game_data[0])

        # Creates car objects for each set of data
        i = 0
        cars = {}

        for car_data in game_data:

            # Creates identifier
            i += 1
            id = i

            # Strips name from car_data
            car_name = car_data[0].strip(',')

            # Strips name from car_data
            car_orientation = car_data[1].strip(',')

            # Strips coordinates from car_data
            car_coordinates = car_data[2].strip(',')
            car_coordinates = car_coordinates.strip('""')
            car_coordinates = car_coordinates.split(',')
            car_coordinates[0] = int(car_coordinates[0]) - 1
            car_coordinates[1] = abs(int(car_coordinates[1]) - self.length)

            # Turns string length into int
            car_length = int(car_data[3])

            # Creates the object with id, name, orientation, coordinates and length
            new_car = Car(id, car_name, car_orientation, car_coordinates, car_length)
            cars[id] = new_car

            if car_name == 'X':
                self.xcar = id
        return cars

    
    def create_board(self, car_file):
        """ Creates the empty board """

        board=[]
        for rows in range(self.length):
            row = ['.'] * self.length
            board.append(row)

        return board


    def fill_board(self):
        """ Fills the empty board with cars """

        # Adds cars to board list
        for car in self.cars.values():
            x = car.coordinates[0]
            y = car.coordinates[1]

            # Saves coordinates of cars in list board
            if(car.orientation=="H"):
                for letter in range(car.length):
                    self.board[x+letter][y] = car.name
            else:
                for letter in range(car.length):
                    self.board[x][y-letter] = car.name

    
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

    
    def check_win (self, start):
        """ Checks if no car prevents the winning car from getting out, thus: winning """

        length = self.length
        board = self.board
        game_won = False
        winning_row = []
        time_elapsed = 0
        step_count = 0

        # Checks for winning car and then after if there are other cars on the same row
        for spot in range(len(board)):
            if board[spot][int(length/2-0.5)] != "." and board[spot][int(length/2-0.5)] == "X":
                for target in (range(len(board)))[(spot + 2):]:
                    if board[target][int(length/2-0.5)] != ".":
                        return game_won, time_elapsed
                time_elapsed = time.time() - start
                game_won = True
                step_count += 1
                return game_won, time_elapsed

    
    def start_algo(self):
        """ Initializes variables requiered for every algorithm """

        self.request_car = ""
        self.request_move = 0
        self.move_count = 0
        self.game_won = False
        self.start = time.time()

    
    def move(self, request_car, request_move):
        """ Moves car on the board """

        # Fetches the current possition of the car
        x = request_car.coordinates[0]
        y = request_car.coordinates[1]

        # Checks if the move would be valid
        if request_car.orientation == "H":
            try:
                for position in range(request_car.length):

                    # Checks if the move is valid
                    if self.board[x+position+request_move][y] != "." and self.board[x+position+request_move][y] != request_car.name or x + position + request_move < 0:
                        return 0
            except IndexError:
                return 0

            # Changes coordinates of the car to perform the move if it appears valid
            for position in range(request_car.length):
                self.board[x+position][y] = "."
            for position in range(request_car.length):
                self.board[x+position+request_move][y] = request_car.name
            request_car.coordinates[0] = int(x+request_move)

        else:
            try:
                for position in range(request_car.length):

                    # Checks if the move is valid
                    if self.board[x][y-position+request_move] != "." and self.board[x][y-position+request_move] != request_car.name or y - position + request_move < 0:
                        return 0
            except IndexError:
                return 0

            # Changes coordinates of the car to perform the move if it appears valid
            for position in range(request_car.length):
                self.board[x][y-position] = "."
            for position in range(request_car.length):
                self.board[x][y-position+request_move] = request_car.name
            request_car.coordinates[1] = int(y+request_move)
        return self.board
        
    
    def moveable_cars(self):
        """ Finds moveable cars """
        
        self.cars_move = set()
        cars_board = []
        horizontal_list = []   
        
        # Makes lists from all rows instead of columns and adds the list of columns to the same big list, cars_board
        for i in range(self.length):
            for col in self.board:
                horizontal_list.append(col[i])
                cars_board.append(col)
            cars_board.append(horizontal_list)
            horizontal_list = []

        for row_col in cars_board:
            check_car = []
            car = []    
            
            for letter in row_col:   
                if not letter in check_car or letter == ".":                   
                    
                    # Appends all letters that are not double to a list
                    check_car.append(letter)
                else:                  
                    
                    # Cars in row or column get saved in a list 
                    car.append(letter)
                        
            length_car_list = len(car)
            length_check_cars = len(check_car)
            
            # Checks for moveable cars
            while car != []:
                car_car = car[0]
                
                # Checks index of car to see where it is in the list
                index_car = check_car.index(car_car)
                car.remove(car_car)
            
                # If the car can not move, the loop goes on, otherwise, the car gets saved in another list
                if ((length_check_cars - 1 == index_car and check_car[index_car - 1] != ".") or (index_car == 0 and check_car[index_car + 1] != ".") or 
                    (check_car[index_car - 1] != "." and check_car[index_car + 1] != ".")):
                    continue
                else:
                    self.cars_move.add(car_car)               
        return self.cars_move
    
    
    def get_car_objects(self):
        """ Seeks the objects from the corresponding moveable car """
        
        # Objects of moveable cars
        self.move_cars_objects = []                     
        
        for objects in self.cars.values():
            if objects.name in self.cars_move:
                self.move_cars_objects.append(objects)        
        return self.move_cars_objects

    
    def write_move(self, request_car, request_move, log):
        """ Writes every move to a csv file """

        log_row = request_car.name + ',' + str(request_move) + '\n'
        log.write(log_row)

    
    def end_game(self, solution, time_elapsed):
        """ Prints end state """

        print("Congratulations you've won the game!")
        print("Move count: ", len(solution))
        print("Time elapsed: ", round(time_elapsed, 2))


    def __str__(self):
        str = ""
        for y in range(self.length):
            for x in range(self.length):
                str = str + self.board[x][y]
        return str
