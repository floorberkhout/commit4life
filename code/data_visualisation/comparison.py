##########################################################################
#   test_random.py
#   Generates a graph with results from all the algorithms
##########################################################################

import os, sys
import numpy as np
import matplotlib.pyplot as plt

directory = os.path.dirname(os.path.realpath(__file__))
sys.path.append(os.path.join(directory, "code"))
sys.path.append(os.path.join(directory, "code", "classes"))
sys.path.append(os.path.join(directory, "code", "algorithms"))

from board import Board
from node import Node
from random_algo import random_algo
from x_first import x_first
from improved_random import algoritme1


def main():
    """ Runs every algorithm """
    
    move_count1, time_elapsed1, move_count2, time_elapsed2, move_count3, time_elapsed3, move_count4, time_elapsed4 = 0, 0, 0, 0, 0, 0, 0, 0
    
    for iteration in range(4):
        # Creates board
        board = Board("data/Rushhour6x6_1.csv")
    
        # Runs random algorithm
        if iteration == 0:
            test_results = {}
            move_counts = []
            time_elapses = []
            for iteration in range(1000):
                board = Board("data/Rushhour6x6_1.csv")
                board.game_won = False
                move_count1, time_elapsed1 = random_algo(board)
                test_results[iteration] = [move_count1, time_elapsed1]
             
            for state in test_results.values():
                move_counts.append(state[0])
                time_elapses.append(state[1])
        
            time_elapsed1 = sum(time_elapses) / len(time_elapses) 
            time_elapsed1 = round(time_elapsed1, 3)
            move_count1 = sum(move_counts) / len(move_counts) 
        
        # Runs advanced random algorithm
        if iteration == 1:
            move_counts = []
            time_elapses = []
            for iteration in range(1000):
                board.game_won = False
                board = Board("data/Rushhour6x6_1.csv")
                move_count2, time_elapsed2 = algoritme1(board)               
                test_results[iteration] = [move_count2, time_elapsed2]
                
    
            for state in test_results.values():
                move_counts.append(state[0])
                time_elapses.append(state[1])
    
            time_elapsed2 = sum(time_elapses) / len(time_elapses) 
            time_elapsed2 = round(time_elapsed2, 3)
            move_count2 = sum(move_counts) / len(move_counts)
        
        # Runs breadth-first
        if iteration == 2:
    
            algorithm = "breath_first"
            memory_clearer = True
    
            # # prepare the selectors for the algorithm
            x = algorithm[:-6]
            if memory_clearer:
                algorithm = algorithm + "_memory_clearer"

            # Initializes the first node
            first_node_name = (0,)
            first_node = Node(board, first_node_name)

            # setup and run the algorithm
            x_first_algorithm = x_first(first_node, memory_clearer, x)
            solution, time_elapsed3, nodes_dict = x_first_algorithm.run()

            # Prints results
            time_elapsed3 = round(time_elapsed3, 3)
            move_count3 = len(solution)
        
        # Runs depth-first
        if iteration == 3:
    
            algorithm = "depth_first"
            memory_clearer = True
    
            # # prepare the selectors for the algorithm
            x = algorithm[:-6]
            if memory_clearer:
                algorithm = algorithm + "_memory_clearer"

            # Initializes the first node
            first_node_name = (0,)
            first_node = Node(board, first_node_name)

            # setup and run the algorithm
            x_first_algorithm = x_first(first_node, memory_clearer, x)
            solution, time_elapsed, nodes_dict = x_first_algorithm.run()

            # Prints results
            time_elapsed4 = round(time_elapsed, 3)
            move_count4 = len(solution)

    print_results(move_count1, time_elapsed1, move_count2, time_elapsed2, move_count3, time_elapsed3, move_count4, time_elapsed4)

def print_results(move_count1, time_elapsed1, move_count2, time_elapsed2, move_count3, time_elapsed3, move_count4, time_elapsed4):
    """ Compares all the algorithms in a bar graph """
    
    # Plots content
    plt.plot(time_elapsed1, move_count1, '.', color='black')
    plt.plot(time_elapsed2, move_count2, "H")
    plt.plot(time_elapsed3, move_count3, "*")
    plt.plot(time_elapsed4, move_count4, "D")
    
    label1 = "{:.3f}, {:.0f}".format(time_elapsed1, move_count1)
    label2 = "{:.3f}, {:.0f}".format(time_elapsed2, move_count2)
    label3 = "{:.3f}, {:.0f}".format(time_elapsed3, move_count3)
    label4 = "{:.3f}, {:.0f}".format(time_elapsed4, move_count4)
    
    plt.annotate(label1, # this is the text
                     (time_elapsed1, move_count1), # this is the point to label
                     textcoords="offset points", # how to position the text
                     xytext=(-20, -15), # distance from text to points (x,y)
                     ha='center') # horizontal alignment can be left, right or center
                     
    plt.annotate(label2, # this is the text
                     (time_elapsed2, move_count2), # this is the point to label
                     textcoords="offset points", # how to position the text
                     xytext=(-20, 6), # distance from text to points (x,y)
                     ha='center') # horizontal alignment can be left, right or center
    
    plt.annotate(label3, # this is the text
                     (time_elapsed3, move_count3), # this is the point to label
                     textcoords="offset points", # how to position the text
                     xytext=(20, -10), # distance from text to points (x,y)
                     ha='center') # horizontal alignment can be left, right or center
    plt.annotate(label4, # this is the text
                     (time_elapsed4, move_count4), # this is the point to label
                     textcoords="offset points", # how to position the text
                     xytext=(20, 6), # distance from text to points (x,y)
                     ha='center') # horizontal alignment can be left, right or center
    
    # Plots labels
    plt.ylabel('Amount moves')
    plt.xlabel('Runtimes in seconds')
    plt.title('Compares algorithms by runtime and amount moves, 6x6_1')
    plt.legend(('Random', 'Random advanced', 'Breadth_first', 'Depth_first'),
               shadow=False, loc=(0.01, 0.4), handlelength=1.5, fontsize=9)
               
    plt.show()

if __name__ == "__main__":
    main()
