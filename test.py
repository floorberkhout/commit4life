
import os, sys
import time
import matplotlib.pyplot as plt
import itertools
import numpy as np
directory = os.path.dirname(os.path.realpath(__file__))
sys.path.append(os.path.join(directory, "code"))
sys.path.append(os.path.join(directory, "code", "classes"))
sys.path.append(os.path.join(directory, "code", "algoritmes"))


# importeer de gebruikte structuur
from board import Board
from random_algo import random_algo
from winning_row import winning_row

def main():
    
    test_results = {}
    move_counts = []
    time_elapses = []
    start = time.time()
    for iteration in range (100):
    
        board = Board("data/Rushhour9x9_5.csv")

        # move_count, time_elapsed = winning_row(board)
    
        move_count, time_elapsed = random_algo(board)
        
        test_results[iteration] = [move_count, time_elapsed]
    time_elapsed = time.time() - start
    time_elapsed = time_elapsed / 60
    print(f" Runtime of test: {time_elapsed}")
       
    # Gets min and max move count
    min_move_count = ((min(test_results.items(), key=lambda x: (x[1])[0]))[1])[0]
    max_move_count = ((max(test_results.items(), key=lambda x: (x[1])[0]))[1])[0]
    
    # Gets min and max time_elapsed
    min_time_elapsed = ((min(test_results.items(), key=lambda x: (x[1])[1]))[1])[1]
    max_time_elapsed = ((max(test_results.items(), key=lambda x: (x[1])[1]))[1])[1]
    
    for state in test_results.values():
        move_counts.append(state[0])
        time_elapses.append(state[1])
    
    
    print_results(min_move_count, max_move_count, min_time_elapsed, max_time_elapsed, move_counts, time_elapses)

def print_results(min_move_count, max_move_count, min_time_elapsed, max_time_elapsed, move_counts, time_elapses):
    
    plt.axis([0, int(max_move_count), 0, float(max_time_elapsed)])
    plt.plot(move_counts, time_elapses, '.')
    plt.ylabel('Runtimes in seconds')
    plt.xlabel('Amount moves')
    plt.show()
    
    
    
        
if __name__ == "__main__":
    main()

