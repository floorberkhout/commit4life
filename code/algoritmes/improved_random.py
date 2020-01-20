import time
from board import Board

def algoritme1(board):      
    # Plays the game untill won
    while board.game_won == False:
        moveable_cars = []
        cars_to_move = []
        board.print_board()
        horizontal_board = []
        horizontal_list = []
        for col in board.board:
            length_board = len(col)
    
        for i in range(length_board):    
            for col in board.board:
                horizontal_list.append(col[i])
            horizontal_board.append(horizontal_list)
            horizontal_list = []
      
        for col in board.board:
            check_car = []
            vertical_car = []
            
            for letter in col:   
                if not letter in check_car or letter == ".":                   
                    # appends all letters that are not double to a list
                    check_car.append(letter)
                else:
                    car = letter                   
                    # vertical cars get saved in a list 
                    vertical_car.append(car)
            
            if vertical_car != []:
                length_car_list = len(vertical_car)
                length_check_cars = len(check_car)
                while vertical_car != []:
                    car = vertical_car[0]
                
                    # checks index of car to see where it is in the list
                    index_car = check_car.index(car)
                    vertical_car.remove(car)
                
                    # if the car can not move, the loop goes on, oterwise, the car gets saved in another list
                    if (length_check_cars - 1 == index_car and check_car[index_car - 1] != ".") or (index_car == 0 and check_car[index_car + 1] != ".") or (check_car[index_car - 1] != "." and check_car[index_car + 1] != "."):
                        break
                    else:
                        cars_to_move.append(car)
                        moveable_cars_vert = set(cars_to_move)
                        moveable_cars.append(moveable_cars_vert)
        
        horizontal_cars_to_move = []    
        for row in horizontal_board:
            horizontal_car = []
            check_horizontal_car = []
            index_list = []
            length_row = len(row)
            if "." in row:            
                for i in range(length_row):                      
                    # if not horizontal_letter in check_horizontal_car or horizontal_letter == ".":
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
                                    horizontal_cars_to_move.append(row[option_2])
                            if row[option_1] in horizontal_car:
                                horizontal_cars_to_move.append(row[option_1])
                            moveable_cars_h = set(horizontal_cars_to_move)
                        except IndexError: 
                            continue
        
        moveable_cars.append(moveable_cars_h)
        print(moveable_cars)
       
        # check if the game has been won ( when the XX car is in front of the exit)
        if board.board[board.length-1][int(board.length/2-0.5)] == "X":
            time_elapsed = time.time() - start
            game_won = True
            
         
    return board.move_count, time_elapsed