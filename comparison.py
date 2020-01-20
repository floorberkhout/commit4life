import os, sys
directory = os.path.dirname(os.path.realpath(__file__))
sys.path.append(os.path.join(directory, "code"))
sys.path.append(os.path.join(directory, "code", "classes"))
sys.path.append(os.path.join(directory, "code", "algoritmes"))
import numpy as np
import matplotlib.pyplot as plt

# importeer de gebruikte structuur
from board import Board
from random_algo import random_algo
from breath_first import breath_first
from depth_first import depth_first
from improved_random import algoritme1


def main():
    """ Runs Rush Hour game with the algorithm """
    
    move_count1, time_elapsed1, move_count2, time_elapsed2 = 0, 0, 0, 0
    
    for iteration in range(2):
        # Creates board
        board = Board("data/Rushhour6x6_1.csv")
    
        # Runs algorithm
        if iteration == 0:
            move_count1, time_elapsed1 = random_algo(board)
        
        if iteration == 1:
            move_count2, time_elapsed2, nodes_list = depth_first(board)
    
    print_results(move_count1, time_elapsed1, move_count2, time_elapsed2)

def print_results(move_count1, time_elapsed1, move_count2, time_elapsed2):
    """ Compares all the algorithms in a bar graph """
    
    # Plots content
    plt.plot(move_count1, time_elapsed1, '.', color='black')
    plt.plot(move_count2, time_elapsed2, "H")
    
    label1 = "{:.0f}, {:.2f}".format(move_count1, time_elapsed1)
    label2 = "{:.0f}, {:.2f}".format(move_count2, time_elapsed2)
    
    plt.annotate(label1, # this is the text
                     (move_count1, time_elapsed1), # this is the point to label
                     textcoords="offset points", # how to position the text
                     xytext=(-20,10), # distance from text to points (x,y)
                     ha='center') # horizontal alignment can be left, right or center
                     
    plt.annotate(label2, # this is the text
                     (move_count2, time_elapsed2), # this is the point to label
                     textcoords="offset points", # how to position the text
                     xytext=(20,-15), # distance from text to points (x,y)
                     ha='center') # horizontal alignment can be left, right or center
    
    # Plots labels
    plt.ylabel('Runtimes in minutes')
    plt.xlabel('Amount moves')
    plt.title('Compares algorithms by runtime and amount moves')
    plt.legend(('Random', 'Depth-first'),
               shadow=False, loc=(0.01, 0.75), handlelength=1.5, fontsize=9)
               
    plt.show()

if __name__ == "__main__":
    main()
