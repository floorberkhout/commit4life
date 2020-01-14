import os, sys
directory = os.path.dirname(os.path.realpath(__file__))
sys.path.append(os.path.join(directory, "code"))
sys.path.append(os.path.join(directory, "code", "classes"))
sys.path.append(os.path.join(directory, "code", "algoritmes"))


# importeer de gebruikte structuur
from board import Board
from random_algo import random_algo
from winning_row import winning_row
<<<<<<< HEAD
from palomaalgoritme import algoritme1

=======
>>>>>>> 507d125bbeb9ecfb07cf0cedf74fbbcafdc20aab

def main():

    board = Board("data/Rushhour9x9_5.csv")
    
    # random algo
<<<<<<< HEAD
    move_count, time_elapsed = random_algo(board)
=======
    move_count, time_elapsed = winning_row(board)
<<<<<<< HEAD
    #move_count, time_elapsed = random_algo(board)
=======
>>>>>>> 507d125bbeb9ecfb07cf0cedf74fbbcafdc20aab
>>>>>>> 4ff221196506011a799007f463b3e7316547b19f
    
    board.print_board()
    
    board.end_game(move_count, time_elapsed)


<<<<<<< HEAD
=======
    # result = Winning_row(board)
    
    # palomaalg = Algoritme1(board)

<<<<<<< HEAD
=======

>>>>>>> 507d125bbeb9ecfb07cf0cedf74fbbcafdc20aab
>>>>>>> 4ff221196506011a799007f463b3e7316547b19f
if __name__ == "__main__":
    main()