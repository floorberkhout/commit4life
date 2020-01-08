################################
#   rushhour.py
#   Prints boardgame rush hour
################################
from car import Car


class Rushhour():
    
    def __init__(self, game):
        data = self.load_games(game)
        self.cars = {}
        self.car_objects(data)

        return 

    def load_games(self, filename):

        # list for returning
        games_data = []

        # load from datafile
        with open(filename, "r") as f:
            game_data = []
            
            for line in f:
                line = line.split()
                game_data.append(line)
            game_data.remove(game_data[0])                              
        return game_data
    
    """ loads rooms from filename in two-step process """
    def car_objects(self, data):

        # creates car objects for each set of data
        i = 0
        for car_data in data:            
            
            # creates identifier
            i += 1
            id = i

            # creates the object with id, name, orientation, coordinates and length
            new_car = Car(id, car_data[0], car_data[1], car_data[2], car_data[3])
            self.cars[id] = new_car
        
            
        for car in self.cars.values():
            # name of car
            car_name = car.name
            car_name = car_name.strip(',')
            print(car_name)
            print(car.orientation)
            print(car.coordinates)
            print(car.length)

        return

 
if __name__ == "__main__":
    rushhour = Rushhour("data/Rushhour6x6_1.csv")
  