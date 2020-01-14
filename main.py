import os, sys
directory = os.path.dirname(os.path.realpath(__file__))
sys.path.append(os.path.join(directory, "code"))
sys.path.append(os.path.join(directory, "code", "classes"))
sys.path.append(os.path.join(directory, "code", "algoritmes"))


# importeer de gebruikte structuur
from board import Board
from random_move import random_algo
from winning_row import Winning_row
from palomaalgoritme import Algoritme1

def main():

    board = Board("data/Rushhour6x6_1.csv")
    
    # random algo
    move_count, time_elapsed = winning_row(board)
    
    board.print_board()
    
    board.end_game(move_count, time_elapsed)


    # result = Winning_row(board)
    
    # palomaalg = Algoritme1(board)


if __name__ == "__main__":
    main()