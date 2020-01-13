import os, sys
directory = os.path.dirname(os.path.realpath(__file__))
sys.path.append(os.path.join(directory, "code"))
sys.path.append(os.path.join(directory, "code", "classes"))
sys.path.append(os.path.join(directory, "code", "algoritmes"))


# importeer de gebruikte structuur
from board import Board
from random_move import Random_move
<<<<<<< HEAD
from winning_row import Winning_row
from palomaalgoritme import Algoritme1
=======

from winning_row import Winning_row

from palomaalgoritme import Algoritme1

>>>>>>> 5eb296986aff62d5a983bb45894d10dc8cce6833

# from code.classes import car, board
# from code.algoritmes import random_move

def main():
    board = Board("data/Rushhour6x6_1.csv")
<<<<<<< HEAD
    
    # palomaalg = Algoritme1(board)
    
    # result = Winning_row(board)
=======

    
    palomaalg = Algoritme1(board)

    
    # result = Random_move(board)
>>>>>>> 5eb296986aff62d5a983bb45894d10dc8cce6833
    
    result = Random_move(board)


    return

if __name__ == "__main__":
    main()