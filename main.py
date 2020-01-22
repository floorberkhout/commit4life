import os, sys
directory = os.path.dirname(os.path.realpath(__file__))
sys.path.append(os.path.join(directory, "code"))
sys.path.append(os.path.join(directory, "code", "classes"))
sys.path.append(os.path.join(directory, "code", "algoritmes"))
import numpy as np

# importeer de gebruikte structuur
from board import Board
from csvwriter import CsvWriter
# from random_algo import random_algo
from winning_row import winning_row
from breath_first2 import breath_first
from depth_first import depth_first
from node import Node
from improved_random import algoritme1

def main():
    """ Runs Rush Hour game with the algorithm """

    # selectors
    algorithm = "breath_first"
    memory_clearer = True

    x = algorithm[:-6]
    if memory_clearer:
        algorithm = algorithm + "_memory_clearer"

    # Creates board
    board = Board("data/Rushhour6x6_2.csv")

    # Runs algorithm
    name = (0,)
    first_node = Node(board, name)



    x_first_algorithm = breath_first(first_node, memory_clearer, x)
    solution, time_elapsed = x_first_algorithm.run()
    time_elapsed = round(time_elapsed, 2)

    # Prints results
    move_count = len(solution)
    print(solution)
    print("Move count:", move_count)
    print("Time elapsed: ", time_elapsed)

    writer = CsvWriter(algorithm, board.name)
    writer.write_to_csv(time_elapsed, board.name, algorithm, move_count, solution)

if __name__ == "__main__":
    main()
