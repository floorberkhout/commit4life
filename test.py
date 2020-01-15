import os, sys
directory = os.path.dirname(os.path.realpath(__file__))
sys.path.append(os.path.join(directory, "code"))
sys.path.append(os.path.join(directory, "code", "classes"))
sys.path.append(os.path.join(directory, "code", "algoritmes"))


# importeer de gebruikte structuur
from board import Board
from random_algo import random_algo
from winning_row import winning_row

def main():
    
    log_file = "resultaten/testresults.csv"
    self.log = open(log_file, "w")
    self.log.truncate()
    header = "move count" + ',' + "time elapsed" + '\n'
    self.log.write(header)
    
    for iteration in range (5):
    
        board = Board("data/Rushhour9x9_5.csv")

        # move_count, time_elapsed = winning_row(board)
    
        move_count, time_elapsed = random_algo(board)

        log_row = request_car.name + ',' + str(request_move) + '\n'
        log.write(log_row)

if __name__ == "__main__":
    main()