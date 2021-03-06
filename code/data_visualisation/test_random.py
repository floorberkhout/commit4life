##########################################################################
#   test_random.py
#   Let's you test the random algorithms in range(x) and plots a graph
##########################################################################

import os, sys
import time
import matplotlib.pyplot as plt
import itertools
import numpy as np
directory = os.path.dirname(os.path.realpath(__file__))
sys.path.append(os.path.join(directory, "code"))
sys.path.append(os.path.join(directory, "code", "classes"))
sys.path.append(os.path.join(directory, "code", "algorithms"))

from board import Board
from random_algo import random_algo
from improved_random import algoritme1

def main():
    """ Runs algorithm and creates the relevant information for the plot """
    
    test_results = {}
    move_counts = []
    time_elapses = []
    start = time.time()
    
    # Creates board and runs algorithm
    for iteration in range (100):  
        board = Board("data/Rushhour6x6_1.csv")
        move_count, time_elapsed = algoritme1(board)
        
        test_results[iteration] = [move_count, time_elapsed]
        
    time_elapsed = time.time() - start
    print(f" Runtime of test: {time_elapsed}")
       
    # Gets min and max move count
    min_move_count = ((min(test_results.items(), key=lambda x: (x[1])[0]))[1])[0]
    max_move_count = ((max(test_results.items(), key=lambda x: (x[1])[0]))[1])[0]
    
    # Gets min and max time_elapsed
    min_time_elapsed = ((min(test_results.items(), key=lambda x: (x[1])[1]))[1])[1]
    max_time_elapsed = ((max(test_results.items(), key=lambda x: (x[1])[1]))[1])[1]
    
    # Gets average move count and time_lapse
    for state in test_results.values():
        move_counts.append(state[0])
        time_elapses.append(state[1])
    
    average_move_count = sum(move_counts) / len(move_counts) 
    average_time_elapse = sum(time_elapses) / len(time_elapses) 
    
    # Prints reuslts in a graph
    print_results(min_move_count, max_move_count, min_time_elapsed, max_time_elapsed, move_counts, time_elapses, average_move_count, average_time_elapse)

def print_results(min_move_count, max_move_count, min_time_elapsed, max_time_elapsed, move_counts, time_elapses, average_move_count, average_time_elapse):
    """ Prints figure of 1000 runs Random Algorithm Rush Hour, average, lower bound and upper bound """
    
    # Creates axes
    plt.axis([0, (int(max_move_count)+ 50000), 0, (float(max_time_elapsed) + 1)])
    
    # Plots content
    plt.plot(move_counts, time_elapses, '.', color='black')
    plt.plot(average_move_count, average_time_elapse, "H")
    plt.plot(int(min_move_count), float(min_time_elapsed), "o")
    plt.plot(int(max_move_count), float(max_time_elapsed), "s")
    
    # Plots labels
    plt.ylabel('Runtimes in minutes')
    plt.xlabel('Amount moves')
    plt.title('Display of 100 runs Random Algorithm Rush Hour')
    plt.legend(('Runs', 'Average', 'Minimum', 'Maximum'),
               shadow=False, loc=(0.01, 0.75), handlelength=1.5, fontsize=9)
               
    plt.show()  
        
if __name__ == "__main__":
    main()

