from car import Car

class Board:
    
    def __init__(self, car_file):
        
        self.length = int(car_file[13])
        
        # Get car data
        self.cars = self.load_cars(car_file)
        
        # Create empty board
        self.board = self.create_board(car_file)
        
        # Fill empty board with cars
        self.fill_board()
    
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
                    self.board[x+letter][y] = car

            else:
                for letter in range(car.length):
                    self.board[x][y-letter] = car
                    
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
