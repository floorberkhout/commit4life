import os, sys
directory = os.path.dirname(os.path.realpath(__file__))
sys.path.append(os.path.join(directory, "code"))
sys.path.append(os.path.join(directory, "code", "classes"))
sys.path.append(os.path.join(directory, "code", "algoritmes"))
import numpy as np

# importeer de gebruikte structuur
from board import Board
from random_algo import random_algo
from winning_row import winning_row
from breath_first import breath_first
from depth_first import depth_first

from improved_random import algoritme1


def main():
    """ Runs Rush Hour game with the algorithm """
    
    # Creates board
    board = Board("data/Rushhour6x6_1.csv")
   
    board.print_board()
    # Runs algorithm
    # move_count, time_elapsed = depth_first(board)
    move_count, time_elapsed = random_algo(board)


    # Prints results
    board.print_board()
    board.end_game(move_count, time_elapsed)

if __name__ == "__main__":
    main()
