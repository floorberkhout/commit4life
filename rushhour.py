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

        # phase 1: creates room objects for each set of data we just parsed
        i = 0
        for car_data in data:            
            # creates identifier
            i += 1
            id = i

            # creates the object with id, name, orientation, coordinates and length
            new_car = Car(id, car_data[0], car_data[1], car_data[2], car_data[3])
            self.cars[id] = new_car
            
        # # strip the strings
#         for string in self.cars[id]:
#             print(string.items)
#
        
    

        # phase 2: links rooms to each other
        for car in self.cars.values():
            print(car.name)

            # # creates identifier
#                id = int(room_data[0])

            # retrieves exisiting room object from dictionary
            car = self.cars[id]
            

            # # extracts the connection data
#                 connections = room_data[4:]

            # # adds connections to the room
#                 for connection in connections:
#                     direction, target_room_id = connection.split()
#
#                     room.add_connection(direction, target_room_id)
        return

 
if __name__ == "__main__":
    rushhour = Rushhour("games/Rushhour6x6_1.csv")
  