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
from randomize import randomize
from improved_random import improved_random
from x_first import X_first
from board_visualisation import visualize_board
from boardcreator import BoardCreator

def main():
    """ Runs Rush Hour game with the algorithm """

    proper_board = False

    while proper_board == False:
        # creates a new board
        length = 9
        number_of_cars = 25
        new_board = BoardCreator(length, number_of_cars)
        print("new attempt")

        # Reads the newly created board
        board = Board("data/Rushhour9x9_new.csv")

        board2 = copy.deepcopy(board)

        # Check if a random algorithm can solve the newly created board
        solution, time_elapsed = randomize(board)
        if solution == False:
            continue


        # If the new board can be solved random, determine the optimal solution breath_first

        # Initializes the first node
        first_node_name = (0,)
        first_node = Node(board2, first_node_name)
        x = "breadth_first"

        x_first_algorithm = X_first(first_node, True, x)
        solution, time_elapsed, nodes_dict = x_first_algorithm.run()

        # if the optimal solution is more than X save the board as a good option
        if len(solution) > 15:
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
