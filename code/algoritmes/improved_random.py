import random
import time
from board import Board

def improved_random(board):      
    
    length_board = board.length
    request_car = ""     
    request_move = ""
    
    board_archive = {str(board): [request_car, request_move]}
    solution = []
    

    # Plays the game untill won    
    while board.game_won == False:
        cars_move = set()
        cars_board = []
        horizontal_list = []   
        
        # Makes lists from all rows instead of columns and adds the list of columns to the same big list, cars_board
        for i in range(length_board):
            for col in board.board:
                horizontal_list.append(col[i])
                cars_board.append(col)
            cars_board.append(horizontal_list)
            horizontal_list = []

        for row_col in cars_board:
            check_car = []
            car = []    
            
            for letter in row_col:   
                if not letter in check_car or letter == ".":                   
                    # Appends all letters that are not double to a list
                    check_car.append(letter)
                else:                  
                    # Cars in row or column get saved in a list 
                    car.append(letter)
                        
            length_car_list = len(car)
            length_check_cars = len(check_car)
            
            # Checks for moveable cars
            while car != []:
                car_car = car[0]
                
                # Checks index of car to see where it is in the list
                index_car = check_car.index(car_car)
                car.remove(car_car)
            
                # If the car can not move, the loop goes on, otherwise, the car gets saved in another list
                if ((length_check_cars - 1 == index_car and check_car[index_car - 1] != ".") or (index_car == 0 and check_car[index_car + 1] != ".") or 
                                                            (check_car[index_car - 1] != "." and check_car[index_car + 1] != ".")):
                    continue
                else:
                    cars_move.add(car_car)        

               
        move_cars_objects = []
        
        last_car = request_car
        last_move = request_move

        # Seeks the objects from the corresponding moveable car
        for objects in board.cars.values():
            if objects.name in cars_move:
                move_cars_objects.append(objects)

        request_car = random.choice(list(move_cars_objects))
        request_move = random.choice([-1, 1])
        
               
        # Makes sure it doesn't reverse the last move
        if request_car == last_car:
            if request_move == last_move:
                last_one = list(board_archive.keys())[-1]
                board_archive.pop(last_one)
                     

        # If move creates new state of board (so no reversing of last move), perform move
        board.move(request_car, request_move)
        board_archive[str(board)] = [request_car.name, request_move]
            
            
                   
        # Checks if another car prevents the winning car from getting out
        board.game_won, time_elapsed = board.check_win(board.start)      
    
    for steps in board_archive.values():
        s = [str(i) for i in steps] 
        str_steps = ", ".join(s)
        solution.append(str_steps)
        
    return solution, time_elapsed