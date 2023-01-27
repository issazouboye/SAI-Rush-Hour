from math import ceil
import numpy as np
import copy
from car import Car

class State: 

    def __init__(self, cars: set[Car], size: int):
        self.cars = cars
        self.size = size  
        self.board = None 
        self.create_board()  
        self.counter = 0        

    def create_board(self):
        board = [["0" for i in range(self.size)] for j in range(self.size)]
        self.board = np.array(board)

        # Place the cars on the board 
        for car in self.cars:
            if car.orientation == "H":
                for j in range(car.length):
                    self.board[car.row][car.column + j] = car.name 

            if car.orientation == "V":
                for i in range(car.length):
                    self.board[car.row + i][car.column] = car.name 
        
        return self.board     

    def get_next_configurations(self): 

        # List filled with sets of car objects 
        configurations = []    
     
        for car in self.cars:

            # Check for horizontal cars 
            if car.orientation == "H":

                # Check if you can move to the left 
                if car.is_movable("left", self.board):                     
                    car.move_left() 
                    configurations.append(copy.deepcopy(self.cars)) 
                    car.move_right()                 

                # Check if you can move to the right 
                if car.is_movable("right", self.board):                     
                    car.move_right() 
                    configurations.append(copy.deepcopy(self.cars)) 
                    car.move_left()                 

            # Check for vertical cars 
            if car.orientation == "V":

                # Check if you can move up 
                if car.is_movable("up", self.board):                    
                    car.move_up()                      
                    configurations.append(copy.deepcopy(self.cars)) 
                    car.move_down()                    

                # Check if you can move down 
                if car.is_movable("down", self.board):                    
                    car.move_down() 
                    configurations.append(copy.deepcopy(self.cars)) 
                    car.move_up()                    

        return configurations          

    def is_solved(self): 
        for car in self.cars:
            winning_column = self.size - 2 
            winning_row = ceil(self.size / 2) - 1 

            if car.name == "X" and car.column == winning_column and car.row == winning_row:
                return True 

        return False  

    def blockingcars(self):
        for i in range(len(self.board) - 1):
                if self.board[ceil(len(self.board) / 2) - 1 ][i] != "0" and self.board[ceil(len(self.board) / 2) - 1 ][i] != "X":
                    self.counter += 1

        return (self.board, self.counter)

    def __hash__(self) -> int:
        return hash(self.__repr__())
    
    def __repr__(self) -> str:
        printable_board = np.array_str(self.board)

        return printable_board 

    def __eq__(self, other) -> bool:
        return isinstance(other, State)

# class Blockingheuristic:
    
#     def __init__(self, board):
#         self.board =  board
#         self.counter = 0

#     def blockingcars(self):
#         for i in range(len(self.board) - 1):
#                 if self.board[ceil(len(self.board) / 2) - 1 ][i] != "0" and self.board[ceil(len(self.board) / 2) - 1 ][i] != "X":
#                     self.counter += 1

#         return self.counter

