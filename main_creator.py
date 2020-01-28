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
from boardcreator import BoardCreator
# from tree import tree

def main():
    """ Runs Rush Hour game with the algorithm """


    length = 6
    number_of_cars = 14
    new_board = BoardCreator(length, number_of_cars)

    # Creates board
    board = Board("data/Rushhour6x6_new.csv")

    # Runs algorithm
    # move_count, time_elapsed, nodes_list = depth_first(board)

    # Selectors choose between breath and deapth first and choose whether _memory_clearer = True or False
    algorithm = "breath_first"
    memory_clearer = False

    # prepare the selectors for the algorithm
    x = algorithm[:-6]
    if memory_clearer:
        algorithm = algorithm + "_memory_clearer"

    # Initializes the first node
    first_node_name = (0,)
    first_node = Node(board, first_node_name)

    # setup and run the algorithm
    x_first_algorithm = x_first(first_node, memory_clearer, x)
    # try:
    solution, time_elapsed, nodes_dict = x_first_algorithm.run()
    # except IndexError:
    #     reset()

    # Prints results
    time_elapsed = round(time_elapsed, 2)
    move_count = len(solution)
    print(solution)
    print("Move count:", move_count)
    print("Time elapsed: ", time_elapsed)

    # write the solution to a CSV file
    writer = CsvWriter(algorithm, board.name)
    writer.write_to_csv(time_elapsed, board.name, algorithm, move_count, solution)

def reset():
    main()

if __name__ == "__main__":
    main()
