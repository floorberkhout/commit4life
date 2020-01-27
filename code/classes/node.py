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
        self.board.move(request_car, request_move)
        self.determine_possible_moves()
        self.update_history(request_car.id, request_move)
        self.update_name(child)

    def determine_possible_moves(self):
        """
        Returns a dict of all possible moves from the board
        """
        possible_moves={}
        # 2. Identify all possible moves
        for option_car in list(self.board.cars.values()):
            option = self.possible_moves_car(option_car)
            if option:
                possible_moves[option_car.id] = option
        self.possible_moves = possible_moves

    def possible_moves_car(self, request_car):
        n = self.board.length
        moves = []
        # fetch the car details
        car_orientation = request_car.orientation
        x = request_car.coordinates[0]
        y = request_car.coordinates[1]
        length = request_car.length

        # determine moves
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
        self.history.append([request_car, request_move])

    def get_string_value(self):
        return print(board)

    def update_name(self, child):
        new_name = list(self.name)
        new_name.append(child)
        self.name = tuple(new_name)

    def set_name(self, name):
        self.name = tuple(name)

    def recreate(self, name):
        for step in self.history:
            request_car = self.board.cars[step[0]]
            request_move = step[1]
            self.board.move(request_car, request_move)
        self.determine_possible_moves()
        self.set_name(name)

    def __repr__(self):
        """
        Make sure that the object is printed properly if it is in a list/dict.
<<<<<<< HEAD

        """    
=======
        """    

>>>>>>> c2986556ef86ada66f20856450e989f5e12c114a
        return self.name
