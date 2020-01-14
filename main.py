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

from palomaalgoritme import Algoritme1


from winning_row import Winning_row

from palomaalgoritme import Algoritme1


>>>>>>> f65bacffd5f01d8d6f3f6e272a81ea37b793b637

# from code.classes import car, board
# from code.algoritmes import random_move

def main():
    board = Board("data/Rushhour6x6_1.csv")
<<<<<<< HEAD
    
    # result = Winning_row(board)
=======
>>>>>>> f65bacffd5f01d8d6f3f6e272a81ea37b793b637

    
    # palomaalg = Algoritme1(board)

<<<<<<< HEAD
    result = Random_move(board)
=======
    # result = Random_move(board)
>>>>>>> f65bacffd5f01d8d6f3f6e272a81ea37b793b637


    return

if __name__ == "__main__":
    main()