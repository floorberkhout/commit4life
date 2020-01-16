import os, sys
directory = os.path.dirname(os.path.realpath(__file__))
sys.path.append(os.path.join(directory, "code"))
sys.path.append(os.path.join(directory, "code", "classes"))
sys.path.append(os.path.join(directory, "code", "algoritmes"))
import numpy as np

# importeer de gebruikte structuur
from board import Board
from random_algo import random_algo
from winning_row import winning_row
from improved_random import algoritme1


def main():

    board = Board("data/Rushhour6x6_1.csv")
    
    # random algo
    # move_count, time_elapsed = winning_row(board)
    

    #move_count, time_elapsed = random_algo(board)

    improved_random = algoritme1(board)




    # result = Winning_row(board)
    
    



if __name__ == "__main__":
    main()