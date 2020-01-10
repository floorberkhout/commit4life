import os, sys
directory = os.path.dirname(os.path.realpath(__file__))
sys.path.append(os.path.join(directory, "code"))
sys.path.append(os.path.join(directory, "code", "classes"))
sys.path.append(os.path.join(directory, "code", "algoritmes"))


# importeer de gebruikte structuur
from board import Board
from random_move import Random_move

# from code.classes import car, board
# from code.algoritmes import random_move

def main():
    board = Board("data/Rushhour9x9_4.csv")
    
    result = Random_move(board)
    
    board.print_board()


    return

if __name__ == "__main__":
    main()