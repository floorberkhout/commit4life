#################################################################################################################
#   node.py
#   Makes nodes for two algorithms, breadth first and depth first, in order to remember the states of the board.
#################################################################################################################

import copy

class Node():
    def __init__(self, board, name):
        self.name = name
        self.board = copy.deepcopy(board)
        self.new = True
        self.possible_moves = {}
        self.determine_possible_moves()
        self.history = []
        self.won = False

    def update_node(self, child, request_car, request_move):
        """ Functions get called to update the new node """
        
        self.board.move(request_car, request_move)
        self.determine_possible_moves()
        self.update_history(request_car.id, request_move)
        self.update_name(child)

    def determine_possible_moves(self):
        """ Returns a dict of all possible moves from the board """
        
        possible_moves = {}
        
        # Identifies all possible moves
        for option_car in list(self.board.cars.values()):
            option = self.possible_moves_car(option_car)
            if option:
                possible_moves[option_car.id] = option
        self.possible_moves = possible_moves

    def possible_moves_car(self, request_car):
        """ Gets the possible moves from the given car """
        
        n = self.board.length
        moves = []

        # Fetches the car details
        car_orientation = request_car.orientation
        x = request_car.coordinates[0]
        y = request_car.coordinates[1]
        length = request_car.length

        # Determine moves for horizontal cars
        if car_orientation == 'H':
            for i in range (x + length, n):
                if self.board.board[i][y] == '.':
                    moves.append(i - x - length + 1)
                else:
                    break
            for i in range(x -1, -1, -1):
                if self.board.board[i][y] == '.':
                    moves.append(i - x)
                else:
                    break
        
        # Determine moves for vertical cars
        else:
            for i in range (y - length, -1, -1):
                if self.board.board[x][i] == '.':
                    moves.append(i - y + length - 1)
                else:
                    break
            for i in range(y + 1, n):
                if self.board.board[x][i] == '.':
                    moves.append(i - y)
                else:
                    break
        return moves

    
    def update_history(self, request_car, request_move):
        """ Adds a move to the move history """
        
        self.history.append([request_car, request_move])


    def update_name(self, child):
        """ New name gets another name: self.name """
        
        new_name = list(self.name)
        new_name.append(child)
        self.name = tuple(new_name)

  
    def recreate(self, name):
        """ If memory clearer in on, he reads the steps to recreate the board by performing all the steps in the history """
        
        for step in self.history:
            request_car = self.board.cars[step[0]]
            request_move = step[1]
            self.board.move(request_car, request_move)
        self.determine_possible_moves()
        self.name = tuple(name)

