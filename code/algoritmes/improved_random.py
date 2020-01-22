import random
import time
from board import Board

def algoritme1(board):      
    
    length_board = board.length
    request_car = ""     
    request_move = ""
    
    # Plays the game untill won    
    while board.game_won == False:
        cars_vertical = set()
        horizontal_board = []
        horizontal_list = []
        
        horizontal_cars_to_move = set()    
        
        # # Makes list from all rows instead of columns
 #        for i in range(length_board):
 #            for col in board.board:
 #                horizontal_list.append(col[i])
 #            horizontal_board.append(horizontal_list)
 #            horizontal_list = []
 #
 #        # Loops over the board with al the horizontal rows
 #        for row in horizontal_board:
 #            horizontal_car = []
 #            check_horizontal_car = []
 #            index_list = []
 #
 #            if "." in row:
 #                for i in range(length_board):
 #                    if not row[i] in check_horizontal_car or row[i] == ".":
 #                        check_horizontal_car.append(row[i])
 #                    else:
 #                        horizontal_car.append(row[i])

        for col in board.board:
            check_car = []
            vertical_car = []
            
            for letter in col:   
                if not letter in check_car or letter == ".":                   
                    # Appends all letters that are not double to a list
                    check_car.append(letter)
                else:                  
                    # Vertical cars get saved in a list 
                    vertical_car.append(letter)
                        
            length_car_list = len(vertical_car)
            length_check_cars = len(check_car)
            
            # Checks for moveable vertical cars
            while vertical_car != []:
                car = vertical_car[0]
                
                # Checks index of car to see where it is in the list
                index_car = check_car.index(car)
                vertical_car.remove(car)
            
                # If the car can not move, the loop goes on, otherwise, the car gets saved in another list
                if (length_check_cars - 1 == index_car and check_car[index_car - 1] != ".") or (index_car == 0 and check_car[index_car + 1] != ".") or (check_car[index_car - 1] != "." and check_car[index_car + 1] != "."):
                    continue
                else:
                    cars_vertical.add(car)        
        
        horizontal_cars_to_move = set()

        # Makes list from all rows instead of columns
        for i in range(length_board):
            for col in board.board:
                horizontal_list.append(col[i])
            horizontal_board.append(horizontal_list)
            horizontal_list = []

        # Loops over the board with al the horizontal rows
        for row in horizontal_board:
            horizontal_car = []
            check_horizontal_car = []
            index_list = []

            if "." in row:
                for i in range(length_board):
                    if not row[i] in check_horizontal_car or row[i] == ".":
                        check_horizontal_car.append(row[i])
                        if row[i] == ".":
                            index_list.append(i)
                    else:
                        horizontal_car.append(row[i])
            
                    for j in range(len(index_list)):
                        option_1 = int(index_list[j]) + 1
                        try:
                            if int(index_list[j]) - 1 >= 0:
                                option_2 = int(index_list[j]) - 1
                                
                                if row[option_2] in horizontal_car:
                                    horizontal_cars_to_move.add(row[option_2])
                            if row[option_1] in horizontal_car:
                                horizontal_cars_to_move.add(row[option_1])
                        except IndexError: 
                            continue
                            
        moveable_cars = cars_vertical.union(horizontal_cars_to_move)
        moveable_cars = list(moveable_cars)
        print(moveable_cars)
        board.print_board()
               
        move_cars_objects = []
        
        last_car = request_car
        last_move = request_move


        for objects in board.cars.values():
            if objects.name in moveable_cars:
                move_cars_objects.append(objects)

        make_move = "yes"
        request_car = random.choice(list(move_cars_objects))
        request_move = random.choice([-1, 1])
        
               
        # Makes sure it doesn't reverse the last move
        if request_car == last_car:
            if request_move != last_move:
                make_move = "no"

            else:
                board.move_count -= 1

        # If move creates new state of board (so no reversing of last move), perfom move
        if make_move == "yes":
            board.move(request_car, request_move)
            
        
        # Checks if another car prevents the winning car from getting out
        board.game_won, time_elapsed = board.check_win(board.start)
        print(board.game_won)

    return board.move_count, time_elapsed