import os, sys
directory = os.path.dirname(os.path.realpath(__file__))
sys.path.append(os.path.join(directory, "code"))
sys.path.append(os.path.join(directory, "code", "classes"))
sys.path.append(os.path.join(directory, "code", "algoritmes"))
sys.path.append(os.path.join(directory, "code", "data_visualisation"))
import numpy as np

# importeer de gebruikte structuur
from board import Board
from random_algo import random_algo
from breath_first2 import breath_first
from depth_first import depth_first
from improved_random import algoritme1
from tree import tree


def main():
    """ Runs Rush Hour game with the algorithm """

    # Creates board
    board = Board("data/Rushhour6x6_1.csv")
    
    # Runs algorithm
    # move_count, time_elapsed, nodes_list = depth_first(board)

    move_count, time_elapsed = algoritme1(board)

    # Prints results
    board.print_board()
    board.end_game(move_count, time_elapsed)
    
    # tree_depth = tree(nodes_list)
    # tree_breadth = tree(nodes)


if __name__ == "__main__":
    main()
