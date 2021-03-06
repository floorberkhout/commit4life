###############################################################
#   csvwriter.py
#   Provides Csvwriter class to save results of game Rush Hour
###############################################################

import csv

class CsvWriter(object):
    """
    Docstring for CsvWriter.
    """

    def __init__(self, algorithm, board):
        log_file = "results/logtest.csv"
        self.log = open("results/%s_%s" %(algorithm, board), "w")
        self.log.truncate()

    def write_to_csv(self, time, board, algorithm, solution):

        self.log.write(str(time) + '\n')
        self.log.write(board + '\n')
        self.log.write(algorithm + '\n')
        self.log.write(str(len(solution)) + '\n')
        self.log.write('\n')
        header = "car" + ',' + "move" + '\n'
        self.log.write(header)

        for step in solution:
            log_row = str(step[0]) + ',' + str(step[1]) + '\n'
            self.log.write(log_row)
