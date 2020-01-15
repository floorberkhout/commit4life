import time
from board import Board

def algoritme1(board):    
    
    # Plays the game untill won
    while board.game_won == False:
        cars_to_move = []
        horizontal_list = []
        print(board.board)
        input()
        for col in board.board:
            check_car = []
            vertical_car = []        
            for letter in col:
                print(letter)
                if letter == col[0]:
                    horizontal_list.append(letter)
                    print(f" horizontal {horizontal_list}")
                if not letter in check_car or letter == ".":
                    
                    # appends all letters that are not double to a list
                    check_car.append(letter)
                    print(check_car)
                    input()
                else:
                    car = letter
                    
                    # vertical cars get saved in a list 
                    vertical_car.append(car)
                    print(vertical_car)
                    input()
            if vertical_car != []:
                length_car_list = len(vertical_car)
                length_check_cars = len(check_car)
                while vertical_car != []:
                    car = vertical_car[0]
                    print(car)
                    
                    # checks index of car to see where it is in the list
                    index_car = check_car.index(car)
                    vertical_car.remove(car)
                    print(vertical_car)
                    print(index_car)                    
                    print(length_check_cars)
                    
                    # if the car can not move, the loop goes on, oterwise, the car gets saved in another list
                    if (length_check_cars - 1 == index_car and check_car[index_car - 1] != ".") or (index_car == 0 and check_car[index_car + 1] != ".") or (check_car[index_car - 1] != "." and check_car[index_car + 1] != "."):
                        print("yes")
                    else:
                        cars_to_move.append(car) 
                        
                    
                    
                    
                    
                      
                   

            board.move_count += 1
    
        # check if the game has been won ( when the XX car is in front of the exit)
        if board.board[board.length-1][int(board.length/2-0.5)] == "X":
            time_elapsed = time.time() - start
            game_won = True
            
         
    return board.move_count, time_elapsed