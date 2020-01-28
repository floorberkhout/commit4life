############################################
#   main.py
#   Implements the game of Rush Hour
############################################

directory = os.path.dirname(os.path.realpath(__file__))
sys.path.append(os.path.join(directory, "code"))
sys.path.append(os.path.join(directory, "code", "classes"))
sys.path.append(os.path.join(directory, "code", "algorithms"))
sys.path.append(os.path.join(directory, "code", "data_visualisation"))
import os, sys
import numpy as np

# Imports the used structure
from board import Board
from node import Node
from csvwriter import CsvWriter
from randomize import randomize
from improved_random import improved_random
from x_first import X_first


def main(algorithm, board_number):
    """ Runs Rush Hour game with the algorithm """

    # Creates board
    board = Board(f"data/Rushhour{sys.argv[2]}.csv")
    
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
    
    # Prints end board    
    board.print_board()
    
    # Prints the time that the algorithm runned and prints the amount of moves     
    board.end_game(solution, time_elapsed)

    # Writes the solution to a CSV file
    writer = CsvWriter(algorithm, board.name)
    writer.write_to_csv(time_elapsed, board.name, algorithm, solution)


    
if __name__ == "__main__":
    try:
        # Checks for the right input
        if sys.argv[1] != 'randomize' and sys.argv[1] != 'improved_random' and sys.argv[1] != 'breadth_first' and sys.argv[1] != 'depth_first':
            print("Wrong algorithm! Choose: randomize, improved_random, breadth_first, or depth_first.")
            sys.exit()
        
        if (sys.argv[2] != "6x6_1" and sys.argv[2] != "6x6_2" and sys.argv[2] != "6x6_3" and 
                    sys.argv[2] != "9x9_4" and sys.argv[2] != "9x9_5" and sys.argv[2] != "9x9_6" and sys.argv[2] != "12x12_7"):
            print("Board does not exist, choose '6x6_1' - '6x6_3', '9x9_4' - '9x9_6' or '12x12_7'")
            sys.exit()
        
        # Default mode is memory_clearer off, which means that he needs more memory to solve the board, 
        # but is faster than when memory is not saved          
        memory_clearer = False
        
        # Asks for memory clearer 
        if sys.argv[1] == 'breadth_first' or sys.argv[1] == 'depth_first':
            memory = input("Memory clearer on or off: ")
        
            if memory == "on":
                memory_clearer = True
        
        main(sys.argv[1], sys.argv[2])
    
    except IndexError:
        print("Choose one from the four algorithms: randomize, improved_random, breadth_first, or depth_first and choose a board.")