import os, sys
import time
import matplotlib.pyplot as plt
import itertools
import numpy as np
import networkx as nx

directory = os.path.dirname(os.path.realpath(__file__))
sys.path.append(os.path.join(directory, "code"))
sys.path.append(os.path.join(directory, "code", "classes"))
sys.path.append(os.path.join(directory, "code", "algoritmes"))

# importeer de gebruikte structuur
from board import Board
from random_algo import random_algo
from winning_row import winning_row
from breath_first import breath_first
from depth_first import depth_first

# def main():
#
#     board = Board("data/Rushhour6x6_3.csv")
#
#     # move_count, time_elapsed = winning_row(board)
#
#     move_count, time_elapsed = breath_first(board)
#
#     board.print_board()


def main():
    """ Runs Rush Hour game with the algorithm """
    
    # Creates board
    board = Board("data/Rushhour6x6_1.csv")
   
    # Runs algorithm
    move_count, time_elapsed, nodes_list = depth_first(board)

    # Prints results
    board.print_board()
    board.end_game(move_count, time_elapsed)
    
    
    print_results(nodes_list)
    
    

def print_results(nodes_list):
    """ Prints figure of 1000 runs Random Algorithm Rush Hour, average, lower bound and upper bound """

    G = nx.Graph()
    previous = ''
    for node in nodes_list:
        G.add_node(node)
        G.add_edge(node, previous)
        previous = node

    nx.draw(G)
    plt.savefig("simple_path.png") # save as png
    plt.show() # display
    
    
    # longest_node = max(len(node) for node in nodes_list)
    # sum_node = len(nodes_list)
    # half_sum = sum_node / 2
    

    # girls_grades = [89, 90, 70, 89, 100, 80, 90, 100, 80, 34]
    # boys_grades = [30, 29, 49, 48, 100, 48, 38, 45, 20, 30]
    # grades_range = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
    # fig=plt.figure()
    # ax=fig.add_axes([0,0,1,1])
    # ax.plot(grades_range, girls_grades, 'o', color='r')
    # ax.plot(grades_range, boys_grades, 'o', color='b')
    # ax.set_xlabel('Grades Range')
    # ax.set_ylabel('Grades Scored')
    # ax.set_title('scatter plot')
    # plt.show()
    
   

    # x = np.linspace(-half_sum, half_sum)
    # y = np.linspace(0, longest_node)
    #
    # node_count = 0
    # for node in nodes_list:
    #     if node_count < 100:
    #         for state in node:
    #             plt.plot(node_count, len(node), '.', color='black')
    #     node_count += 1
    #
    # plt.show()
    
    
    
    
    
    
    #
    # # Creates axes
    # plt.axis([0, (int(max_move_count)+ 50000), 0, (float(max_time_elapsed) + 1)])
    #
    # # Plots content
    # plt.plot(move_counts, time_elapses, '.', color='black')
    # plt.plot(average_move_count, average_time_elapse, "H")
    # plt.plot(int(min_move_count), float(min_time_elapsed), "o")
    # plt.plot(int(max_move_count), float(max_time_elapsed), "s")
    #
    # # Plots labels
    # plt.ylabel('Runtimes in seconds')
    # plt.xlabel('Amount moves')
    # plt.title('Display of 1000 runs Random Algorithm Rush Hour')
    # plt.legend(('Runs', 'Average', 'Minimum', 'Maximum'),
    #            shadow=False, loc=(0.01, 0.75), handlelength=1.5, fontsize=9)
    #
    # plt.show()

if __name__ == "__main__":
    main()
