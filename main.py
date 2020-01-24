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
from x_first import x_first
# from depth_first import depth_first
from improved_random import algoritme1
<<<<<<< HEAD

from board_visualisation import visualize_board
=======
from board_visualisation import visualize_board
from tree import tree


>>>>>>> a22b4b605ba1d71c039dd74ec07c34260df9e7d6

def main():
    """ Runs Rush Hour game with the algorithm """

    # # Creates board
    board = Board("data/Rushhour6x6_1.csv")

<<<<<<< HEAD
    move_count, time_elapsed = random_algo(board)
=======
    # Runs algorithm
    # move_count, time_elapsed, nodes_list = depth_first(board)

    # Selectors choose between breadth and depth first and choose whether _memory_clearer = True or False
    algorithm = "depth_first"
    memory_clearer = True


    
 

    # move_count, time_elapsed = algoritme1(board)
    # move_count, time_elapsed = random_algo(board)

    # Prints results
    # board.print_board()
#     board.end_game(move_count, time_elapsed)


    # Prepare the selectors for the algorithm
    x = algorithm[:-6]
    if memory_clearer:
        algorithm = algorithm + "_memory_clearer"

    # Initializes the first node
    first_node_name = (0,)
    first_node = Node(board, first_node_name)

    # setup and run the algorithm
    x_first_algorithm = x_first(first_node, memory_clearer, x)
    solution, time_elapsed, nodes_dict = x_first_algorithm.run()
    move_count = len(solution)
>>>>>>> a22b4b605ba1d71c039dd74ec07c34260df9e7d6

#     # visualize_board(solution)
#
    board.end_game(move_count, time_elapsed)
<<<<<<< HEAD
    
   
   
   
   
   
    
    # # input
    # board = Board("data/Rushhour6x6_1.csv")
    # algorithm = "breath_first"
    # memory_clearer = True
    #
    # # # prepare the selectors for the algorithm
    # x = algorithm[:-6]
    # if memory_clearer:
    #     algorithm = algorithm + "_memory_clearer"
    #
    # # Initializes the first node
    # first_node_name = (0,)
    # first_node = Node(board, first_node_name)
    #
    # # setup and run the algorithm
    # x_first_algorithm = x_first(first_node, memory_clearer, x)
    # solution, time_elapsed, nodes_dict = x_first_algorithm.run()
    #
    # # Prints results
    # time_elapsed = round(time_elapsed, 2)
    # move_count = len(solution)
    # print(solution)
    # print("Move count:", move_count)
    # print("Time elapsed: ", time_elapsed)
    
    # De-comment to generate images that visualize every step taken to win the game
    # visualize_board(solution)

=======
#
#
#     tree_depth = tree(nodes_dict)
#
    

    # write the solution to a CSV file
    # writer = CsvWriter(algorithm, board.name)
#     writer.write_to_csv(time_elapsed, board.name, algorithm, move_count, solution)
>>>>>>> a22b4b605ba1d71c039dd74ec07c34260df9e7d6

    
if __name__ == "__main__":
    main()
