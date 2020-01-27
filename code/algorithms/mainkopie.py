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
from random_algo import random_algo
from winning_row import winning_row
from x_first import X_first
from improved_random import improved_random
from board_visualisation import visualize_board
from board_visualisation import visualize_board



def main():
    """ Runs Rush Hour game with the algorithm """

    # # Creates board
    board = Board("data/Rushhour6x6_1.csv")

    """
    Selectors choose between all the algorithms and depth first and choose whether _memory_clearer = True or False
    """
    # algorithm = "random_algo"
    # algorithm = "improved_random"
#     algorithm = "breadth_first"
    algorithm = "depth_first"
    memory_clearer = True

    x = algorithm
    
    if memory_clearer:
        algorithm = algorithm + "_memory_clearer"

    # Initializes the first node
    first_node_name = (0,)
    first_node = Node(board, first_node_name)
 
    # Setup and run the algorithm
    x_first_algorithm = X_first(first_node, memory_clearer, x) 
    
    if x == "depth_first" or x == "breadth_first":    
        solution, time_elapsed, nodes_dict = x_first_algorithm.run()
    
    elif x == "random_algo":
        solution, time_elapsed = random_algo(board)
    
    elif x == "improved_random":
        solution, time_elapsed = improved_random(board)
        
    board.end_game(move_count, time_elapsed)

    # write the solution to a CSV file
    writer = CsvWriter(algorithm, board.name)
    writer.write_to_csv(time_elapsed, board.name, algorithm, move_count, solution)


    
if __name__ == "__main__":
    main()