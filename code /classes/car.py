############################################
#   car.py
#   Provides Car class for game Rush Hour
############################################


class Car(object):

    # Initializes a Car
    def __init__(self, id, name, orientation, coordinates, length):

        # Car properties
        self.id = id
        self.name = name
        self.orientation = orientation
        self.coordinates = coordinates
        self.length = length
        
        # Gets orientation of car
        def get_orientation(self, direction):
                return self.orientation