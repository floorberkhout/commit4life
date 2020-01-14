from car import Car
import time

class Semiboard:
    
    def __init__(self, car_file):
        
        self.length = int(car_file[13])
        
        # Get car data
        self.cars = self.load_cars(car_file)
        
        # Create empty board
        self.board = self.create_board(car_file)
        
        # Fill empty board with cars
        self.fill_board()
        
        self.start_algo()
        
    
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
        
        return cars                         

    def create_board(self, car_file):
    
        board=[]
        
        # Initialize the empty matrix
        for rows in range(self.length):
            row = ['.'] * self.length
            board.append(row)
        
        return board
        
    
    def fill_board(self):
        
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
        """ prints the board"""
        
        for dash in range(self.length+2):
            print("_", end="")
        print("")
        for y in range(self.length):
            print("|", end="")
            for x in range(self.length):
                print(self.board[x][y], end="")
            if y != int(self.length/2-0.5):
                print("|", end="")
            print("")
        for dash in range(self.length+2):
            print("-", end="")
        print("")
    
    def start_algo(self):
    
        self.move_count = 0
        self.game_won = False
        self.start = time.time()
        log_file = "resultaten/log.csv"
        self.log = open(log_file, "w")
        self.log.truncate()
        header = "car" + ',' + "move" + '\n'
        self.log.write(header)
        
        
    def move(self, request_car, request_move):

        # fetch the current possition of the car
        x = request_car.coordinates[0]
        y = request_car.coordinates[1]
    
        # check if the move would be valid TODO:
        if request_car.orientation == "H":
            try:
                for position in range(request_car.length):
                    if self.board[x+position+request_move][y] != "." and self.board[x+position+request_move][y] != request_car.name or x + position + request_move < 0:
                        return 0
            except IndexError:
                return 0
            for position in range(request_car.length):
                self.board[x+position][y] = "."
            for position in range(request_car.length):
                self.board[x+position+request_move][y] = request_car.name
            request_car.coordinates[0] = int(x+request_move)
        
        else:
            try:
                for position in range(request_car.length):
                    if self.board[x][y-position+request_move] != "." and self.board[x][y-position+request_move] != request_car.name or y - position + request_move < 0:
                        return 0
            except IndexError:
                return 0
            for position in range(request_car.length):
                self.board[x][y-position] = "."
            for position in range(request_car.length):
                self.board[x][y-position+request_move] = request_car.name
            request_car.coordinates[1] = int(y+request_move)
    

    # write a move to the log
    def write_move(self, request_car, request_move, log):
        log_row = request_car.name + ',' + str(request_move) + '\n'
        log.write(log_row)
        
    def end_game(self, move_count, time_elapsed): 
         # print the board one more time and tell the player he has won
        print("Congratulations you've won the game!")
        print("Move count: ", self.move_count)
        print("Time elapsed: ", time_elapsed)
    
    
    
    
