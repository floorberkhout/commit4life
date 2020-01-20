import os, sys
directory = os.path.dirname(os.path.realpath(__file__))
sys.path.append(os.path.join(directory, "code"))
sys.path.append(os.path.join(directory, "code", "classes"))
sys.path.append(os.path.join(directory, "code", "algoritmes"))
import numpy as np

# importeer de gebruikte structuur
from board import Board
# from random_algo import random_algo
from winning_row import winning_row
from breath_first2 import breath_first
from depth_first import depth_first
from node import Node


def main():
    """ Runs Rush Hour game with the algorithm """

    # Creates board
    board = Board("data/Rushhour9x9_4.csv")

    # Runs algorithm
    name = (0,)
    first_node = Node(board, name)

    breath_first_algorithm = breath_first(first_node)
    solution = breath_first_algorithm.run()

    # Prints results
    print(len(solution.history))
    print(solution.history)

if __name__ == "__main__":
    main()
