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


def init_board(board, my_board, request_car, request_move):
    """ Initialize the board with starting positions """
    
    count = 1
    global cars 
    cars = {}
    for car in board.cars.values():
        y = car.coordinates[0] 
        x = car.coordinates[1]       
        move = 0
        if car.name == request_car:
            move = request_move
        # Saves coordinates of cars in list board
        if(car.orientation=="V"):
            for letter in range(car.length):
                my_board[[x-letter+move], [y]] = count 
                cars[car.name] = count
                print(my_board)
        else:
            for letter in range(car.length):
                my_board[[x], [y+letter+move]] = count
                cars[car.name] = count
        count += 1

    return my_board

def update_board(my_board):
    """ Update the board based on the game rules, each call to update_board is one turn """
    old_board = my_board.copy()
    
    return my_board

def main():
    """ Animates rush hour game 6x6_1 """
    request_car = ""
    request_move = 0
    count = 0
    cmap = colors.ListedColormap(['white', 'grey', 'green', 'blue', 'pink', 'orange', 'black','purple', 'brown', 'beige', 'yellow', 'turquoise', 'coral', 'red'])
    
    # Creates board
    board = Board("data/Rushhour6x6_1.csv")
    
    # Input variables for the board
    boardsize = board.length               
    
    my_board = np.zeros((boardsize,boardsize))
    
    for i in range(2):
        print(my_board)
        my_board = init_board(board, my_board, request_car, request_move)
        print(my_board)
        request_car = "A"
        request_move = -1
        
        fig = plt.gcf()
        im = plt.imshow(my_board, cmap=cmap, animated=True)              

        plt.savefig(fname=f'{count}game_of_life', dpi=150)
        count += 1
        
    

if __name__ == "__main__":
    main()
    