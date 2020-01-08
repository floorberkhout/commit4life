################################
#   rushhour.py
#   Prints boardgame rush hour
################################
from car import Car

class Rushhour():
    """ Sets up the Rush Hour game """
    
    def __init__(self, game):
        """ Initializes the game """
        
        n = int(game[13])
        
        data = self.load_games(game)
        
        self.cars = {}
        
        dict_cars = self.car_objects(data, n)
        
        self.print_board(dict_cars, n)
        
        

    def load_games(self, filename):
        """ Loads game data from the given csv file """

        games_data = []

        # Loads from datafile
        with open(filename, "r") as f:
            game_data = []
            
            for line in f:
                line = line.split()
                game_data.append(line)
            game_data.remove(game_data[0])                              
        return game_data
    
    def car_objects(self, data, length_game):
        """ Creates car objects from game data """

        # Creates car objects for each set of data
        i = 0
        for car_data in data:            
            
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
            car_coordinates[1] = abs(int(car_coordinates[1]) - length_game)          
            car_coordinates = tuple(car_coordinates)
            
            # Turns string length into int
            car_length = int(car_data[3])

            # Creates the object with id, name, orientation, coordinates and length
            new_car = Car(id, car_name, car_orientation, car_coordinates, car_length)
            self.cars[id] = new_car
        
        return self.cars
   
    def print_board(self, dict_cars, length_game):
        """ Prints board with cars """
        
        board=[]
        
        # Initialize the empty matrix
        for rows in range(length_game):
            row = ['.'] * length_game
            board.append(row)

        # Adds cars to board list
        for car in dict_cars.values():          
            x = car.coordinates[0]
            y = car.coordinates[1]
            
            # Saves coordinates of cars in list board
            if(car.orientation=="H"):
                for letter in range(car.length):
                    board[x+letter][y] = car.name

            else:
                for letter in range(car.length):
                    board[x][y-letter] = car.name
        
        # Prints content of the board and border 
        for dash in range(length_game+2):
            print("_", end="")
        print("")
        for y in range(length_game):
            print("|", end="")
            for x in range(length_game):
                print(board[x][y], end="")
            if y != int(length_game/2-0.5):
                print("|", end="")
            print("")
        for dash in range(length_game+2):
            print("-", end="")
        print("")
  