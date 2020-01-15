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


def main():

    board = Board("data/Rushhour6x6_1.csv")
    
    # random algo
    # move_count, time_elapsed = winning_row(board)
    

    #move_count, time_elapsed = random_algo(board)
=======

def main():

    board = Board("data/Rushhour9x9_5.csv")

    # move_count, time_elapsed = winning_row(board)
    
    move_count, time_elapsed = random_algo(board)
>>>>>>> 686932d3dc35b8b78d0188bb7fe54d2ca421c606

    board.print_board()
    
    # board.end_game(move_count, time_elapsed)

<<<<<<< HEAD

    # result = Winning_row(board)
    
    palomaalg = algoritme1(board)



=======
>>>>>>> 686932d3dc35b8b78d0188bb7fe54d2ca421c606
if __name__ == "__main__":
    main()