###############################################################
#   x_first.py
#   Runs either depth-first or breadth-first algorithm
###############################################################

import copy
import random
import time
import sys

class X_first:
    def __init__(self, first_node, memory_clearer, x):
        """ Initializes a node """

        # Creates the first node with name 0
        self.nodes = {first_node.name: first_node}
        self.start_node = first_node
        self.nodes_queue = [first_node.name]
        self.nodes_archive = {first_node.name: []}
        self.states = set()
        self.solved = False
        self.move_count = 0
        self.solution = []
        self.level = 0
        self.start_time = time.time()
        self.memory_clearer = memory_clearer
        self.x_first = x

    def get_next_node_name(self):
        """ Takes the next node from the queue in case of breadth first, fifo """

        if self.x_first == "depth_first":
            
            # Picks random node, instead of always the last node
            return self.nodes_queue.pop(random.randrange(len(self.nodes_queue)))
        else:
            return self.nodes_queue.pop(0)

    def build_children(self, current_node_name):
        """ Creates all possible child-states and adds them to the nodes_queue """

        if self.memory_clearer == False:
            
            # Retrieves the node
            current_node = self.nodes[current_node_name]
        else:
                 
            # Recreates the board state by performing the move history
            if current_node_name != (0,):
                current_node = copy.deepcopy(self.start_node)
                current_node.history = copy.deepcopy(self.nodes_archive[current_node_name])
                current_node.recreate(current_node_name)
            else:
                current_node = self.start_node

        child = 0

        # Creates the corresponding next nodes
        for movable_car in current_node.possible_moves:
            for request_move in current_node.possible_moves[movable_car]:
                new_node = copy.deepcopy(current_node)
                request_car = new_node.board.cars[movable_car]
                
                # Updates the new node
                new_node.update_node(child, request_car, request_move)
                self.printlevel(len(new_node.name))

                if not self.memory_clearer:
                    self.nodes[new_node.name] = new_node

                # Checks if node is a new state if so add to the nodes_queue and the set
                if str(new_node.board) not in self.states:
                    self.states.add(str(new_node.board))
                    self.nodes_queue.append(new_node.name)

                # Checks if the new node is a winnig state if so update the status to solved
                if new_node.board.check_win(0)[0]:
                    finish_node = copy.deepcopy(new_node)
                    request_car = finish_node.board.cars[finish_node.board.xcar]
                    request_move = finish_node.board.length - 2 - finish_node.board.cars[finish_node.board.xcar].coordinates[0]
                    finish_node.update_node(0, request_car, request_move)
                    finish_node.won = True
                    self.nodes[new_node.name] = new_node
                    self.solved = True
                    self.solution = copy.deepcopy(finish_node)
                    self.print_steps()
                    self.convert_car_id_to_char()
                    break
                child += 1

                # Writes the data to the nodes_archive
                self.nodes_archive[new_node.name] = new_node.history

                # Deletes the nodes to save memory if memory_clearer is on
                if self.memory_clearer:
                    del new_node

        if self.memory_clearer:
            del current_node

    def printlevel(self, level):
        """ Prints level so during tests the state of process is visible """
        
        if level > self.level:
            self.level = level
            print(str(level-1) + " levels deep")

    def print_steps(self):
        """ Prints the amount of levels that the algorithm is deep """
        
        board = copy.deepcopy(self.nodes[(0,)])
        for car_id, request_move in self.solution.history:
            request_car = board.board.cars[car_id]
            board.board.move(request_car, request_move)

    def convert_car_id_to_char(self):
        """ Converts car id to char to save memory """
        
        solution = []
        for car_id, request_move in self.solution.history:
            request_car = self.start_node.board.cars[car_id]
            solution.append([str(request_car), request_move])
        self.solution = solution

    def run(self):
        """ Runs the algorithm untill all possible states are visited """
        
        while self.solved == False:
            next_node_name = self.get_next_node_name()
            self.build_children(next_node_name)

        time_elapsed = time.time() -  self.start_time
        return self.solution, time_elapsed, self.nodes
