import os, sys
directory = os.path.dirname(os.path.realpath(__file__))
sys.path.append(os.path.join(directory, "code"))
sys.path.append(os.path.join(directory, "code", "classes"))
sys.path.append(os.path.join(directory, "code", "algoritmes"))
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import colors

# importeer de gebruikte structuur
from board import Board

def create_init(board, my_board, cars):
    """ Creates a numpy board """
    
    count = 2
    for i in range(len(board.board)):
        for n in range(len(board.board)):
            if board.board[n][i] == '.':
                my_board[i][n] = 0
                cars[board.board[n][i]] = 0
            elif board.board[n][i] == "X":
                my_board[i][n] = 1
                cars[board.board[n][i]] = 1
            else:
                if board.board[n][i] in cars:
                    my_board[i][n] = cars[board.board[n][i]]
                else:
                    my_board[i][n] = count
                    cars[board.board[n][i]] = count
                    count += 1
    return my_board

def create_numpy(board, my_board, cars):
    """ Creates a numpy board """
    
    count = 2
    for i in range(len(board.board)):
        for n in range(len(board.board)):
            my_board[i][n] = cars[board.board[n][i]]
    return my_board

def visualize_board(steps):
    """ Animates rush hour game 6x6_1 """
    count = 0
    cars = {}
    cmap = colors.ListedColormap(['white', 'red', 'green', 'blue', 'pink', 'orange', 'black','purple', 'brown', 'beige', 'yellow', 'turquoise', 'coral', 'grey'])
    
    # Creates board object
    board = Board("data/Rushhour6x6_1.csv")
    
    # Creates begin state
    my_board = np.zeros((board.length, board.length))
    my_board = create_init(board, my_board, cars)
    
    # Creates state created by each step
    for step in steps:
        for car in board.cars.values():
            if car.name == step[0]:
                request_car = car
                board.move(request_car, step[1])
                my_board = create_numpy(board, my_board, cars)
                
        # Visualizes numpy list
        fig = plt.gcf()
        im = plt.imshow(my_board, cmap=cmap, animated=True)
    
        # Saves visualisation
        plt.savefig(fname=f'screenshots/6x6_1_depth/{count}Rush_hour6x6_1', dpi=150)
    
        count += 1
        
    

    