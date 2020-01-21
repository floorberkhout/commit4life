import os, sys
directory = os.path.dirname(os.path.realpath(__file__))
sys.path.append(os.path.join(directory, "code"))
sys.path.append(os.path.join(directory, "code", "classes"))
sys.path.append(os.path.join(directory, "code", "algoritmes"))
import numpy as np
import random

import time
from IPython import display
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib import colors

# importeer de gebruikte structuur
from board import Board
from random_algo import random_algo
from breath_first2 import breath_first
from depth_first import depth_first
from improved_random import algoritme1

def create_numpy(board, my_board):
    """ Creates a numpy board """
    
    for i in range(len(board.board)):
        for n in range(len(board.board)):
            if board.board[n][i] == ".":
                my_board[[i], [n]] = 0
            elif board.board[n][i] == "X":
                my_board[[i], [n]] = 2
            else:
                my_board[[i], [n]] = 1
    return my_board


def visualize_board(steps):
    """ Animates rush hour game 6x6_1 """
    count = 0
    cmap = colors.ListedColormap(['white', 'grey', 'green', 'blue', 'pink', 'orange', 'black','purple', 'brown', 'beige', 'yellow', 'turquoise', 'coral', 'red'])
    
    # Creates board
    board = Board("data/Rushhour6x6_1.csv")
    
    # Creates numpy board
    my_board = np.zeros((board.length, board.length))
    my_board = create_numpy(board, my_board)
    
    for step in steps:
        for car in board.cars.values():
            if car.name == step[0]:
                request_car = car
                board.move(request_car, step[1])
                my_board = create_numpy(board, my_board)
        
        fig = plt.gcf()
        im = plt.imshow(my_board, cmap=cmap, animated=True)              

        plt.savefig(fname=f'{count}game_of_life', dpi=150)
    
        count += 1
        
    

if __name__ == "__main__":
    steps = [["A", -1], ["B", -1]]
    visualize_board(steps)
    