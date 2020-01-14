import os, sys
directory = os.path.dirname(os.path.realpath(__file__))
sys.path.append(os.path.join(directory, "code"))
sys.path.append(os.path.join(directory, "code", "classes"))
sys.path.append(os.path.join(directory, "code", "algoritmes"))


# importeer de gebruikte structuur
from board import Board
<<<<<<< HEAD
from random_move import Random_move

from winning_row import Winning_row


def main():
    board = Board("data/Rushhour6x6_1.csv")
    
    result = Winning_row(board)

    # result = Random_move(board)


=======
from random_move import random_algo

from winning_row import Winning_row
from palomaalgoritme import Algoritme1


# from code.classes import car, board
# from code.algoritmes import random_move

def main():

    board = Board("data/Rushhour6x6_1.csv")
    
    # random algo
    move_count, time_elapsed = random_algo(board)
    
    board.print_board()
    board.end_game(move_count, time_elapsed)


    # result = Winning_row(board)
    
    # palomaalg = Algoritme1(board)

>>>>>>> 5ef47d070d3fde8d92aec0bf1657060f722c0f02


if __name__ == "__main__":
    main()