import time
from board import Board

def algoritme1(board):      
    # Plays the game untill won
    while board.game_won == False:
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
                        print("yes")
                    else:
                        cars_to_move.append(car)
        

        
        horizontal_cars = []
        horizontal_cars_to_move = []  
        coordinates = []
        
        # Makes list of coordinates
        for coord in board.cars.values():
            coordinates.append(coord.coordinates)
        print(coordinates)
        
        moves = []
        
        for cars in board.cars.values():
            coordinates.append(cars.coordinates)
            x = cars.coordinates[0]
            y = cars.coordinates[1]
            length = cars.length
            if cars.orientation == 'H':           
                horizontal_cars.append(cars)
                requested_coordinate_1 = [(length + x + 1), y]
                print(requested_coordinate_1)
                requested_coordinate_2 = [(x - 1), y]
                print(requested_coordinate_2)
                if not requested_coordinate_1 or not requested_coordinate_2 in coordinates:
                    print(cars.name)
                    if (requested_coordinate_1[0] or requested_coordinate_2[0]) < length_board or (requested_coordinate_1[0] or requested_coordinate_2[0]) > 0:
                # if not requested_coordinate_1 in coordinates:
#                     print(requested_coordinate_1)
#                     input()
#                 if not requested_coordinate_2 in coordinates:
#                     print(requested_coordinate_2)
#                     input()
                        horizontal_cars_to_move.append(cars.name)
                        print(horizontal_cars_to_move)

                
                
                

                
        
             
                
                # for i in range (x + length, length_board):
#                     if board.board[i][y] == '.':
#                         moves.append(i - x - length + 1)
#                         print(moves)
#                     else:
#                         print("break")
#                         break
#                 for i in range(x -1, -1, -1):
#                     if board.board[i][y] == '.':
#                         print(board.board[i][y])
#                         moves.append(i - x)
#                         print(f"moves2 {moves}")
#                     else:
#                         print("break 2")
#                         break
#
#
#
#
#
#
                      
                   

            board.move_count += 1
    
        # check if the game has been won ( when the XX car is in front of the exit)
        if board.board[board.length-1][int(board.length/2-0.5)] == "X":
            time_elapsed = time.time() - start
            game_won = True
            
         
    return board.move_count, time_elapsed