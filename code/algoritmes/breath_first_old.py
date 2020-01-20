import random
import time
import copy
# from board import Board

# nodes algorithm
def node_algorithm(nodes, nodes_queue):

    # 1. Take the node highest up the tree (this is the node first in the queue and than also pop it from the queue)
    node = nodes_queue.pop(0)
    print(len(node))
    board = copy.deepcopy(nodes[node]['board'])

    # 2. Identify all possible moves
    for option_car in list(board.cars.values()):
        option = determine_moves(board, option_car)
        if option:
            nodes[node]['possible_moves'][option_car.id] = option

    child = 0
    # 3. Create the corresponding nodes
    for movable_car in nodes[node]['possible_moves']:
        for request_move in nodes[node]['possible_moves'][movable_car]:
            # read the board state from the previous node
            board = copy.deepcopy(nodes[node]['board'])
            # perform moves

            # get the car object from the board based on the letter
            request_car = board.cars[movable_car]
            # board.print_board()
            # print(request_car, request_move)
            status = board.move(request_car, request_move)
            if status == 0:
                print("invalid move!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
                board.print_board()

            # determine the index for the new node and create a tuple
            new_node = list(node)
            new_node.append(child)
            new_node = tuple(new_node)

            # # write outcome to new nodes
            nodes[new_node] = {}
            nodes[new_node]['board'] = board

            nodes[new_node]['state'] = str(board)
            nodes[new_node]['won'] = False
            nodes[new_node]['new'] = True
            nodes[new_node]['solved'] = False
            nodes[new_node]['possible_moves'] = {}
            nodes[new_node]['history'] = copy.deepcopy(nodes[node]['history'])
            nodes[new_node]['history'].append([movable_car, request_move])
            child += 1

            # add the new node to the queue
            nodes_queue.append(new_node)

            # 4. Compare the new nodes with nodes earlier up the tree
            for check_node in nodes:
                # if nodes[check_node]['board'] == nodes[new_node]['board'] and check_node != new_node and nodes[check_node]['new'] == True:
                if nodes[check_node]['state'] == nodes[new_node]['state'] and check_node != new_node and nodes[check_node]['new'] == True:
                    # print(nodes[new_node]['board'])
                    # print(nodes[new_node]['history'])
                    nodes[new_node]['new'] = False
                    # 6. Shut of nodes that represent a board state that was achieved before
                    # print(nodes_queue)
                    # print(new_node)
                    nodes_queue.remove(new_node)

            # 5. Check if the game is won
            if board.check_win(board.start)[0]:
                print("Game won")
                board = copy.deepcopy(nodes[0,]['board'])
                move_count = 0
                print(board)
                for car_id, request_move in nodes[new_node]['history']:
                    request_car = board.cars[car_id]
                    board.move(request_car, request_move)
                    print(request_car, request_move)
                    board.print_board()
                    move_count += 1
                    print("-------")

                print(nodes[new_node]['history'])
                nodes[new_node]['new'] = True
                return(1)

    #set the current node to solved
    nodes[node]['solved'] = True

    return(nodes, nodes_queue)

def determine_moves(board, request_car):
    n = board.length
    moves = []
    # fetch the car details
    car_orientation = request_car.orientation
    x = request_car.coordinates[0]
    y = request_car.coordinates[1]
    length = request_car.length

    # determine moves
    if car_orientation == 'H':
        for i in range (x + length, n):
            if board.board[i][y] == '.':
                moves.append(i - x - length + 1)
            else:
                break
        for i in range(x -1, -1, -1):
            if board.board[i][y] == '.':
                moves.append(i - x)
            else:
                break
    else:
        for i in range (y - length, -1, -1):
            if board.board[x][i] == '.':
                moves.append(i - y + length - 1)
            else:
                break
        for i in range(y + 1, n):
            if board.board[x][i] == '.':
                moves.append(i - y)
            else:
                break
    return moves




def breath_first(board):
    # init
    nodes_queue = []

    nodes = {}
    new_node = (0,)
    first_node = new_node
    nodes_queue.append(new_node)

    nodes[new_node] = {}
    nodes[new_node]['board'] = copy.deepcopy(board)
    nodes[new_node]['state'] = str(board)
    nodes[new_node]['won'] = False
    nodes[new_node]['new'] = True
    nodes[new_node]['solved'] = False
    nodes[new_node]['possible_moves'] = {}
    nodes[new_node]['history'] = []
    print("hallo")
    print(board)
    # Plays the game untill won
    while board.game_won  == False:

        # Get a car and move it
        nodes, nodes_queue = node_algorithm(nodes, nodes_queue)

        # Checks if another car prevents the winning car from getting out
        board.game_won, time_elapsed = board.check_win(board.start)


    return board.move_count, time_elapsed
