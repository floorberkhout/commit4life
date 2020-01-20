import os, sys
import time
import matplotlib.pyplot as plt
import itertools
import numpy as np
import networkx as nx
import sklearn.datasets
from sklearn.datasets import load_iris

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
    
    
    iris = load_iris()

    # Model (can also use single decision tree)
    from sklearn.ensemble import RandomForestClassifier
    model = RandomForestClassifier(n_estimators=10)

    # Train
    model.fit(iris.data, iris.target)
    # Extract single tree
    estimator = model.estimators_[5]

    from sklearn.tree import export_graphviz
    # Export as dot file
    export_graphviz(estimator, out_file='tree.dot', 
                    feature_names = iris.feature_names,
                    class_names = iris.target_names,
                    rounded = True, proportion = False, 
                    precision = 2, filled = True)

    plt.plot(model)
    plt.show()
    
    
    # G = nx.Graph()
    # previous = ''
    # node_count = 0
    # axe = 0
    # for node in nodes_list:
    #     if node_count < 10:
    #         G.add_node(node, pos=(node_count, axe))
    #         G.add_edge(node, previous)
    #         previous = node
    #         node_count += 1
    #         axe += 1
    #
    # nx.draw(G)
    # plt.savefig("simple_path.png") # save as png
    # plt.show() # display
    
    
    # longest_node = max(len(node) for node in nodes_list)
    # sum_node = len(nodes_list)
    # half_sum = sum_node / 2
   

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


if __name__ == "__main__":
    main()
