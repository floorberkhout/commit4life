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
from randomize import randomize
from x_first import X_first
from improved_random import improved_random


def main():
    """ Runs every algorithm """
    
    move_count1, time_elapsed1, move_count2, time_elapsed2, move_count3, time_elapsed3, move_count4, time_elapsed4 = 0, 0, 0, 0, 0, 0, 0, 0
    
    for iteration in range(4):
    
        # Runs random algorithm
        if iteration == 0:
            test_results = {}
            move_counts = []
            time_elapses = []
            for iteration in range(100):
                board = Board("data/Rushhour6x6_2.csv")
                board.game_won = False
                move_count1, time_elapsed1 = randomize(board)
                move_count1 = len(move_count1)
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
            for iteration in range(100):
                board.game_won = False
                board = Board("data/Rushhour6x6_2.csv")
                move_count2, time_elapsed2 = improved_random(board) 
                move_count2 = len(move_count2)              
                test_results[iteration] = [move_count2, time_elapsed2]
                
    
            for state in test_results.values():
                move_counts.append(state[0])
                time_elapses.append(state[1])
    
            time_elapsed2 = sum(time_elapses) / len(time_elapses) 
            time_elapsed2 = round(time_elapsed2, 3)
            move_count2 = sum(move_counts) / len(move_counts)
        
        # Runs breadth-first
        if iteration == 2:
            board = Board("data/Rushhour6x6_2.csv")
            algorithm = "breadth_first"
            memory_clearer = True
    
            # # prepare the selectors for the algorithm
            x = algorithm
            if memory_clearer:
                algorithm = algorithm + "_memory_clearer"

            # Initializes the first node
            first_node_name = (0,)
            first_node = Node(board, first_node_name)

            # setup and run the algorithm
            x_first_algorithm = X_first(first_node, memory_clearer, x)
            solution, time_elapsed3, nodes_dict = x_first_algorithm.run()

            # Prints results
            time_elapsed3 = round(time_elapsed3, 3)
            move_count3 = len(solution)
        
        # Runs depth-first
        if iteration == 3:
            move_counts = []
            time_elapses = []
            for iteration in range(100):
                board.game_won = False
                board = Board("data/Rushhour6x6_2.csv")
                algorithm = "depth_first"
                memory_clearer = True
    
                # # prepare the selectors for the algorithm
                x = algorithm
                if memory_clearer:
                    algorithm = algorithm + "_memory_clearer"

                # Initializes the first node
                first_node_name = (0,)
                first_node = Node(board, first_node_name)

                # setup and run the algorithm
                x_first_algorithm = X_first(first_node, memory_clearer, x)
                move_count4, time_elapsed4, nodes_dict = x_first_algorithm.run()
                
                move_count4 = len(move_count4)              
                test_results[iteration] = [move_count4, time_elapsed4]
            

            for state in test_results.values():
                move_counts.append(state[0])
                time_elapses.append(state[1])

            time_elapsed4 = sum(time_elapses) / len(time_elapses) 
            time_elapsed4 = round(time_elapsed2, 3)
            move_count4 = sum(move_counts) / len(move_counts)
    print("Compare randomize, improved_random, breadth-first and depth-first on 6x6 2")
    print(f"Randomize average > move count: {move_count1}, time elapsed: {time_elapsed1}")
    print(f"Improved random average > move count: {move_count2}, time elapsed: {time_elapsed2}")
    print(f"breadth-first > move count: {move_count3}, time elapsed: {time_elapsed3}")
    print(f"depth-first > move count: {move_count4}, time elapsed: {time_elapsed4}")
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
    plt.title('Compares algorithms by runtime and amount moves, 6x6_2, takes average of 100x randoms and depth-first')
    plt.legend(('Random', 'Random advanced', 'Breadth_first', 'Depth_first'),
               shadow=False, loc=(0.01, 0.4), handlelength=1.5, fontsize=9)
               
    plt.show()

if __name__ == "__main__":
    main()
