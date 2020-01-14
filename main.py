import os, sys
directory = os.path.dirname(os.path.realpath(__file__))
sys.path.append(os.path.join(directory, "code"))
sys.path.append(os.path.join(directory, "code", "classes"))
sys.path.append(os.path.join(directory, "code", "algoritmes"))


# importeer de gebruikte structuur
from board import Board
from random_move import Random_move

from random_move_aanpassing import random_algo
from semiboard import Semiboard



from winning_row import Winning_row

from palomaalgoritme import Algoritme1



# from code.classes import car, board
# from code.algoritmes import random_move

def main():
    # board = Board("data/Rushhour6x6_1.csv")
    board = Semiboard("data/Rushhour6x6_1.csv")
    

    
    move_count, time_elapsed = random_algo(board)    
    board.print_board()
    board.end_game(move_count, time_elapsed) 

    # result = Random_move(board)


    return

if __name__ == "__main__":
    main()