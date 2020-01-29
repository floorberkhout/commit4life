###############################################################
#   creator.py
#   Algorithm that uses the class BoardCreator to create random boards and vaildates them
###############################################################

import os, sys
directory = os.path.dirname(os.path.realpath(__file__))
sys.path.append(os.path.join(directory, "code"))
sys.path.append(os.path.join(directory, "code", "classes"))
sys.path.append(os.path.join(directory, "code", "algorithms"))
sys.path.append(os.path.join(directory, "code", "data_visualisation"))
import numpy as np
import copy


# Imports the used structure
from board import Board
from node import Node
from randomize_check_generated import randomize_check_generated
from x_first import X_first
from board_visualisation import visualize_board
from boardcreator import BoardCreator

def main():
    """ Main program to create new boards """

    # declare the input variables
    length = 6
    number_of_cars = 14
    proper_length = 15

    # sets the boolean proper_board to false
    proper_board = False

    # name of the boards CSV file as created by BoardCreator
    file_name = "data/Rushhour" + str(length) + "x" + str(length) + "_new.csv"

    # Run the program untill a proper board has been established
    while proper_board == False:
        # Creates a new board
        new_board = BoardCreator(length, number_of_cars)
        print("new attempt")

        # Reads the newly created board
        board = Board(file_name)

        board2 = copy.deepcopy(board)

        # Check if a random algorithm can solve the newly created board
        solution, time_elapsed = randomize_check_generated(board)
        if solution == False:
            continue

        # If the new board was solved by randomize it's a valid board, then solve it breadth_first to see how many steps it takes
        first_node_name = (0,)
        first_node = Node(board2, first_node_name)
        x = "breadth_first"
        x_first_algorithm = X_first(first_node, True, x)
        solution, time_elapsed, nodes_dict, board = x_first_algorithm.run()

        # If the optimal solution is more than X save the board as a good option
        if len(solution) > proper_length:
            proper_board = True


    board.end_game(solution, time_elapsed)

    # Prints results
    time_elapsed = round(time_elapsed, 2)
    move_count = len(solution)
    print(solution)
    print("Move count:", move_count)
    print("Time elapsed: ", time_elapsed)

if __name__ == "__main__":
    main()
