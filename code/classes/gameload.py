################################
#   rushhour.py
#   Prints boardgame rush hour
################################
from car import Car

class Gameload():
    """ Sets up the Rush Hour game """
    
    def __init__(self, game):
        """ Initializes the game """
        
        self.length = int(game[13])
        self.cars = {}
        
        # Function load_games returns game_data
        data = self.load_games(game)
    
        # Function car_objects returns dictionary of car objects
        dict_cars = self.car_objects(data)
    

    def load_games(self, filename):
        """ Loads game data from the given csv file """

        game_data = []

        # Loads from datafile
        with open(filename, "r") as f:
            
            for line in f:
                line = line.split()
                game_data.append(line)
            game_data.remove(game_data[0])                              
        return game_data
    
    def car_objects(self, data):
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
            car_coordinates[1] = abs(int(car_coordinates[1]) - self.length)          
            
            # Turns string length into int
            car_length = int(car_data[3])

            # Creates the object with id, name, orientation, coordinates and length
            new_car = Car(id, car_name, car_orientation, car_coordinates, car_length)
            self.cars[id] = new_car
        
        return self.cars

  