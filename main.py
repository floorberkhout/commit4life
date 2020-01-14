import os, sys
directory = os.path.dirname(os.path.realpath(__file__))
sys.path.append(os.path.join(directory, "code"))
sys.path.append(os.path.join(directory, "code", "classes"))
sys.path.append(os.path.join(directory, "code", "algoritmes"))


# importeer de gebruikte structuur
from board import Board
<<<<<<< HEAD
from random_move import random_algo
from winning_row import Winning_row
from palomaalgoritme import Algoritme1
=======
from random_algo import random_algo
from winning_row import winning_row
from palomaalgoritme import algoritme1

>>>>>>> c2b8ca604fe6fc9b58c651e25e6bbc582d545126

def main():

    board = Board("data/Rushhour6x6_1.csv")
    
    # random algo
<<<<<<< HEAD
    move_count, time_elapsed = winning_row(board)
=======
    # move_count, time_elapsed = random_algo(board)
>>>>>>> c2b8ca604fe6fc9b58c651e25e6bbc582d545126
    
    board.print_board()
    
    board.end_game(move_count, time_elapsed)


    # result = Winning_row(board)
    
    # palomaalg = Algoritme1(board)

<<<<<<< HEAD

=======
>>>>>>> c2b8ca604fe6fc9b58c651e25e6bbc582d545126
if __name__ == "__main__":
    main()