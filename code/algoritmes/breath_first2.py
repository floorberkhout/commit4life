import copy

class breath_first:
    def __init__(self, first_node):

        # create the firt node with name 0

        self.nodes = {first_node.name: first_node}
        self.nodes_queue = [first_node.name]
        self.states = set()
        self.solved = False
        self.move_count = 0
        self.solution = []
        self.level = 0


    def get_next_node_name(self):
        """
        Method that takes the next node from the queue in case of breath first fifo
        """
        return self.nodes_queue.pop(0)

    def build_children(self, current_node_name):
        """
        Creates all possible child-states and adds them to the nodes_queue
        """
        # Retrieve the node
        current_node = self.nodes[current_node_name]

        child = 0
        # Create the corresponding next nodes
        for movable_car in current_node.possible_moves:
            for request_move in current_node.possible_moves[movable_car]:
                new_node = copy.deepcopy(current_node)
                request_car = new_node.board.cars[movable_car]
                # update the new node
                new_node.update_node(child, request_car, request_move)
                self.printlevel(len(new_node.name))
                self.nodes[new_node.name] = new_node

                # check if node is a new state if so add to the nodes_queue and the set
                if str(new_node.board) not in self.states:
                    self.states.add(str(new_node.board))
                    self.nodes_queue.append(new_node.name)

                # check if the new node is a winnig state if so updat the status to solved
                if new_node.board.check_win(0)[0]:
                    self.solved = True
                    self.solution = copy.deepcopy(new_node)
                    self.print_steps()
                    print("congrats you won")
                    break
                child += 1

    def printlevel(self, level):
        if level > self.level:
            self.level = level
            print(str(level-1) + " levels deep")

    def print_steps(self):
        board = copy.deepcopy(self.nodes[(0,)])
        board.board.print_board()
        for car_id, request_move in self.solution.history:
            request_car = board.board.cars[car_id]
            board.board.move(request_car, request_move)
            print(request_car, request_move)
            board.board.print_board()
            print("-------")

    def run(self):
        """
        Runs the algorithm untill all possible states are visited.
        """
        while self.solved == False:
            next_node_name = self.get_next_node_name()
            self.build_children(next_node_name)

        return self.solution
