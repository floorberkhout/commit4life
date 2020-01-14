import os, sys
directory = os.path.dirname(os.path.realpath(__file__))
sys.path.append(os.path.join(directory, "code"))
sys.path.append(os.path.join(directory, "code", "classes"))
sys.path.append(os.path.join(directory, "code", "algoritmes"))


# importeer de gebruikte structuur
from board import Board
from random_move import Random_move
from winning_row import Winning_row
from palomaalgoritme import Algoritme1

# from code.classes import car, board
# from code.algoritmes import random_move

def main():
    board = Board("data/Rushhour6x6_1.csv")
    
    result = Winning_row(board)
    
    # palomaalg = Algoritme1(board)

<<<<<<< HEAD
    # result = Random_move(board)
=======
<<<<<<< HEAD
    result = Random_move(board)
=======
<<<<<<< HEAD
    result = Random_move(board)
=======
    # result = Random_move(board)
>>>>>>> f65bacffd5f01d8d6f3f6e272a81ea37b793b637
>>>>>>> b01a7fe877ad7782a1caabae9473b3d049fc376d
>>>>>>> 87819b4b681d16d57c92b6cefaf83c6d567c18d5



if __name__ == "__main__":
    main()