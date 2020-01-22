import os, sys
directory = os.path.dirname(os.path.realpath(__file__))
sys.path.append(os.path.join(directory, "code"))
sys.path.append(os.path.join(directory, "code", "classes"))
sys.path.append(os.path.join(directory, "code", "algoritmes"))
sys.path.append(os.path.join(directory, "code", "data_visualisation"))
import numpy as np

# importeer de gebruikte structuur
from board import Board
from node import Node
from csvwriter import CsvWriter
# from random_algo import random_algo
from winning_row import winning_row
from x_first import x_first
from depth_first import depth_first
from improved_random import algoritme1
# from tree import tree

def main():
    """ Runs Rush Hour game with the algorithm """

    # Creates board
    board = Board("data/Rushhour6x6_2.csv")

    # Runs algorithm
    # move_count, time_elapsed, nodes_list = depth_first(board)

    # Selectors choose between breath and deapth first and choose whether _memory_clearer = True or False
    algorithm = "breath_first"
    memory_clearer = True

    # prepare the selectors for the algorithm
    x = algorithm[:-6]
    if memory_clearer:
        algorithm = algorithm + "_memory_clearer"

<<<<<<< HEAD
    x_first_algorithm = breath_first(first_node, memory_clearer, x)
    solution, time_elapsed = x_first_algorithm.run()
=======
    # Initializes the first node
    first_node_name = (0,)
    first_node = Node(board, first_node_name)

    # setup and run the algorithm
    x_first_algorithm = x_first(first_node, memory_clearer, x)
    solution, time_elapsed, nodes_dict = x_first_algorithm.run()

    # Prints results
>>>>>>> e9d7de2c8138621745b9fd053c1e1881f5dd8f53
    time_elapsed = round(time_elapsed, 2)
    move_count = len(solution)
    print(solution)
    print("Move count:", move_count)
    print("Time elapsed: ", time_elapsed)

    # write the solution to a CSV file
    writer = CsvWriter(algorithm, board.name)
    writer.write_to_csv(time_elapsed, board.name, algorithm, move_count, solution)

if __name__ == "__main__":
    main()
