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
<<<<<<< HEAD
    board = Board("data/Rushhour12x12_7.csv")
=======
<<<<<<< HEAD
    board = Board("data/Rushhour9x9_5.csv")
>>>>>>> 0fc4d73ce93a30ab48f71d61401be891c5d6b554

    """
    Selectors choose between all the algorithms and depth first and choose whether _memory_clearer = True or False
    """
    # algorithm = "random_algo"
    # algorithm = "improved_random"
<<<<<<< HEAD
    # algorithm = "breadth_first"
    algorithm = "depth_first"
    memory_clearer = False

    x = algorithm
=======
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
=======
    board = Board("data/Rushhour6x6_1.csv")


    solution, time_elapsed = improved_random(board)
    
    board.end_game(solution, time_elapsed)
 
 
 
 
 
    #
    # Runs algorithm
    # move_count, time_elapsed, nodes_list = depth_first(board)




    # Selectors choose between breadth and depth first and choose whether _memory_clearer = True or False
    
>>>>>>> 0fc4d73ce93a30ab48f71d61401be891c5d6b554
    
    if memory_clearer:
        algorithm = algorithm + "_memory_clearer"

    # Initializes the first node
    first_node_name = (0,)
    first_node = Node(board, first_node_name)
 
    # Setup and run the algorithm
    x_first_algorithm = X_first(first_node, memory_clearer, x) 
    
    if x == "depth_first" or x == "breadth_first":    
        solution, time_elapsed, nodes_dict = x_first_algorithm.run()
    
<<<<<<< HEAD
    elif x == "random_algo":
        solution, time_elapsed = random_algo(board)
    
    elif x == "improved_random":
        solution, time_elapsed = improved_random(board)
        
    board.end_game(solution, time_elapsed)

    # write the solution to a CSV file
    writer = CsvWriter(algorithm, board.name)
    writer.write_to_csv(time_elapsed, board.name, algorithm, solution)
=======
    # print(solution)
    # print("Move count:", move_count)
    # print("Time elapsed: ", time_elapsed)
>>>>>>> 7f46a9917aca824be549b78de23fd705bd87c9a5
    
    elif x == "improved_random":
        solution, time_elapsed = improved_random(board)

        
    board.end_game(move_count, time_elapsed)

    # write the solution to a CSV file
<<<<<<< HEAD
    writer = CsvWriter(algorithm, board.name)
    writer.write_to_csv(time_elapsed, board.name, algorithm, move_count, solution)
=======
    # writer = CsvWriter(algorithm, board.name)
#     writer.write_to_csv(time_elapsed, board.name, algorithm, move_count, solution)
>>>>>>> 7f46a9917aca824be549b78de23fd705bd87c9a5
>>>>>>> 0fc4d73ce93a30ab48f71d61401be891c5d6b554


    
if __name__ == "__main__":
    main()