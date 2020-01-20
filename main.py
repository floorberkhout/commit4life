import os, sys
directory = os.path.dirname(os.path.realpath(__file__))
sys.path.append(os.path.join(directory, "code"))
sys.path.append(os.path.join(directory, "code", "classes"))
sys.path.append(os.path.join(directory, "code", "algoritmes"))
import numpy as np

# importeer de gebruikte structuur
from board import Board
<<<<<<< HEAD
from random_algo import random_algo
from breath_first import breath_first
from depth_first import depth_first
=======
# from random_algo import random_algo
from winning_row import winning_row
from breath_first2 import breath_first
from depth_first import depth_first
from node import Node
>>>>>>> 45962deee4ca2cb3ee5ca27aa5c675b719d7d17d
from improved_random import algoritme1


def main():
    """ Runs Rush Hour game with the algorithm """

    # Creates board
<<<<<<< HEAD
    board = Board("data/Rushhour6x6_1.csv")
    
    # Runs algorithm
    # move_count, time_elapsed = depth_first(board)
    move_count, time_elapsed, nodes_list = depth_first(board)
=======
    board = Board("data/Rushhour9x9_4.csv")

    # Runs algorithm
    name = (0,)
    first_node = Node(board, name)

    breath_first_algorithm = breath_first(first_node)
    solution = breath_first_algorithm.run()
>>>>>>> 45962deee4ca2cb3ee5ca27aa5c675b719d7d17d

    # Prints results
    print(len(solution.history))
    print(solution.history)

if __name__ == "__main__":
    main()
