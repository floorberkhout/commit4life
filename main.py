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
<<<<<<< HEAD
from randomize import randomize
=======
from random_algo import random_algo
>>>>>>> c2986556ef86ada66f20856450e989f5e12c114a
from x_first import X_first
from improved_random import improved_random
from board_visualisation import visualize_board



def main():
    """ Runs Rush Hour game with the algorithm """

<<<<<<< HEAD
    # # Creates board
    board = Board("data/Rushhour6x6_1.csv")

    # Choose between all the algorithms and depth first and choose whether _memory_clearer = True or False 
    
    algorithm = "randomize"
=======
    # Creates board
    board = Board("data/Rushhour6x6_1.csv")


    # Choose between all the algorithms and depth first and choose whether _memory_clearer = True or False 
    
    algorithm = "random_algo"
>>>>>>> c2986556ef86ada66f20856450e989f5e12c114a
    # algorithm = "improved_random"
    # algorithm = "breadth_first"
    # algorithm = "depth_first"
    
    memory_clearer = False

    x = algorithm
    if memory_clearer:
        algorithm = algorithm + "_memory_clearer"

    # Initializes the first node
    first_node_name = (0,)
    first_node = Node(board, first_node_name)
 
    # Sets and runs the algorithm
    x_first_algorithm = X_first(first_node, memory_clearer, x) 
    
    if x == "depth_first" or x == "breadth_first":    
        solution, time_elapsed, nodes_dict = x_first_algorithm.run()
    
    elif x == "randomize":
        solution, time_elapsed = randomize(board)
    
    elif x == "improved_random":
        solution, time_elapsed = improved_random(board)
        
    board.end_game(solution, time_elapsed)

    # Writes the solution to a CSV file
    writer = CsvWriter(algorithm, board.name)
    writer.write_to_csv(time_elapsed, board.name, algorithm, solution)


    
if __name__ == "__main__":
    main()