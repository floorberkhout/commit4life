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
        self.x = 0
        self.y = 0
        self.cars = {}
        self.board=[]
        
        # Function load_games returns game_data
        data = self.load_games(game)
    
        # Function car_objects returns dictionary of car objects
        dict_cars = self.car_objects(data)
    
        
        move_count = 0
        game_won = False

        
        # Plays the game untill won
        while game_won == False:
            
            # Prints board 
            self.print_board(dict_cars)
            
            randommove 
            
            # Moves chosen car
            self.move(dict_cars, request_car, request_move)

            # Increases move count
            move_count += 1
            print(move_count)
            
            
            # check if the game has been won ( when the XX car is in front of the exit)
            print(self.board[self.length-1][int(self.length/2-0.5)])
            if self.board[self.length-1][int(self.length/2-0.5)] == "X":
                game_won = True
                
        # print the board one more time and tell the player he has won
        self.print_board(dict_cars)
        print("Congratulations you've won the game!")
        
        # # Function load_games returns game_data
        # data = self.load_games(game)
        #
        # # Function car_objects returns dictionary of car objects
        # dict_cars = self.car_objects(data)
        #
        # # Function print_board visualizes board
        # self.print_board(dict_cars)
        #
        # # # Function ask_move asks for move if userinput is necessary and returns requested car and move
        # # self.requests = self.ask_move(dict_cars)
        #
        # # Function move moves the requested car
        # self.move(dict_cars)
        #
        # # Extra loop
        # self.print_board(dict_cars)

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
   
    def print_board(self, dict_cars):
        """ Prints board with cars """
        
        # Initialize the empty matrix
        for rows in range(self.length):
            row = ['.'] * self.length
            self.board.append(row)

        # Adds cars to board list
        for car in dict_cars.values():          
            self.x = car.coordinates[0]
            self.y = car.coordinates[1]
            
            # Saves coordinates of cars in list board
            if(car.orientation=="H"):
                for letter in range(car.length):
                    self.board[self.x+letter][self.y] = car.name

            else:
                for letter in range(car.length):
                    self.board[self.x][self.y-letter] = car.name
        
        # Prints content of the board and border 
        for dash in range(self.length + 2):
            print("_", end="")
        print("")
        
        for self.y in range(self.length):
            print("|", end="")
            
            for self.x in range(self.length):
                print(self.board[self.x][self.y], end="")
                
            if self.y != int(self.length/2-0.5):
                print("|", end="")
            print("")
        
        for dash in range(self.length+2):
            print("-", end="")
        print("")
        
    # def ask_move(self, dict_cars):
    #     while True:
    #         user_input = input("what move would you like to make? ([car], [move]): ")
    #         a = tuple(x for x in user_input.split(","))
    #
    #         request_car = a[0]
    #         request_move = int(a[1])
    #
    #         for car in dict_cars.values():
    #             if car.name is request_car:
    #                 status = "valid"
    #         if status is "valid":
    #             break
    #         # extra checkes????? and request_move > - self.length and request_move < self.length:
    #         print("invalid input")
    #     return request_car, request_move
    
    def move(self, dict_cars, request_car, request_move):
        """ function that allows a car to make a move """
        
        print("check if car ", request_car, "can make move ", request_move)

        # fetch the current possition of the car
        for car in dict_cars.values():
            if car.name == request_car:
                x = car.coordinates[0]
                y = car.coordinates[1]
                
                # check if the move would be valid TODO:
                if car.orientation == "H":

                    try:
                        for position in range(car.length):
                            if self.board[x+position+request_move][y] != "." and self.board[x+position+request_move][y] != car.name or x + position + request_move < 0:
                                print("invalid move")
                                return(0)
                    except IndexError:
                        print("invalid move")
                        return(0)
                    for position in range(car.length):
                        self.board[x+position][y] = "."
                    for position in range(car.length):
                        self.board[x+position+request_move][y] = car.name
                    car.coordinates[0] = int(x+request_move)

                else:
                    try:
                        for position in range(car.length):
                            if self.board[x][y-position+request_move] != "." and self.board[x][y-position+request_move] != car.name or y - position + request_move < 0:
                                print("invalid move")
                                return(0)
                    except IndexError:
                        print("invalid move")
                        return(0)
                    for position in range(car.length):
                        self.board[x][y-position] = "."
                    for position in range(car.length):
                        self.board[x][y-position+request_move] = car.name
                    car.coordinates[1] = int(y+request_move)

  