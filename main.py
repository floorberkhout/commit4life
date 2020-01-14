import os, sys
directory = os.path.dirname(os.path.realpath(__file__))
sys.path.append(os.path.join(directory, "code"))
sys.path.append(os.path.join(directory, "code", "classes"))
sys.path.append(os.path.join(directory, "code", "algoritmes"))


# importeer de gebruikte structuur
from board import Board
from random_move import Random_move

from winning_row import Winning_row


def main():
    board = Board("data/Rushhour6x6_1.csv")
    
    result = Winning_row(board)

    # result = Random_move(board)




if __name__ == "__main__":
    main()