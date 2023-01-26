from __future__ import annotations
import numpy as np 
import copy 
# from board_v2 import Board 
from collections import deque
from math import ceil 
import heapq
import time
# from stateissa import State

class Board:

    def __init__(self, size: int):
        self.size = size        
        board = [["0" for i in range(self.size)] for j in range(self.size)]
        self.board = np.array(board)

        # Set with cars 
        self.cars = set()        
    
    def load_board(self, filename: str):  

        # Read the data
        with open(filename, 'r') as f:
            next(f) 

            for line in f:
                splits = line.strip().split(",")

                name = splits[0] 
                orientation = splits[1] 
                column = int(splits[2]) - 1
                row = int(splits[3]) - 1
                length = int(splits[4])  

                car = Car(name, orientation, column, row, length) 
                self.cars.add(car)                                  
        
        # Place the cars on the board 
        for car in self.cars:
            if car.orientation == "H":
                for j in range(car.length):
                    self.board[car.row][car.column + j] = car.name 

            if car.orientation == "V":
                for i in range(car.length):
                    self.board[car.row + i][car.column] = car.name 

        print("First board:")
        print(self.board)
        print() 

    def get_initial_cars(self):
        return self.cars 

    def get_initial_board(self):
        return self.board

class Car:

    def __init__(self, name, orientation, column, row, length):
        self.name = name 
        self.orientation = orientation 
        self.column = column 
        self.row = row 
        self.length = length 

    def is_movable(self, direction, board) -> bool:

        if self.orientation == "H":
            if direction == "left":
                if self.column - 1 >= 0 and board[self.row][self.column - 1] == "0":
                    return True 

            if direction == "right":
                if self.length == 2:
                    if self.column + 2 < len(board) and board[self.row][self.column + 2] == "0":
                        return True 

                if self.length == 3:
                    if self.column + 3 < len(board) and board[self.row][self.column + 3] == "0":
                        return True 

        if self.orientation == "V":
            if direction == "up":
                if self.row - 1 >= 0 and board[self.row - 1][self.column] == "0":
                    return True 

            if direction == "down":
                if self.length == 2:
                    if self.row + 2 < len(board) and board[self.row + 2][self.column] == "0":
                        return True

                if self.length == 3:
                    if self.row + 3 < len(board) and board[self.row + 3][self.column] == "0":
                        return True 

        return False     

    def move_left(self):

        moved_car = Car(self.name, self.orientation, self.column - 1, self.row, self.length) 

        return moved_car 

    def move_right(self):

        moved_car = Car(self.name, self.orientation, self.column + 1, self.row, self.length) 

        return moved_car 

    def move_up(self):

        moved_car = Car(self.name, self.orientation, self.column, self.row - 1, self.length) 

        return moved_car 

    def move_down(self):

        moved_car = Car(self.name, self.orientation, self.column, self.row + 1, self.length) 

        return moved_car 
    
    def __str__(self):
        return f"{self.name}, {self.column}, {self.row}"

    def __hash__(self) -> int:
        return hash(self.__str__())

    def __eq__(self, other) -> bool:
        return isinstance(other, Car)

class State: 

    def __init__(self, cars, size: int):
        self.cars = cars
        self.size = size  
        self.board = None 
        self.create_board()          

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
                    moved_car = car.move_left()  
                    new_cars = set(self.cars)                                   
                    new_cars.remove(car)
                    new_cars.add(moved_car)                    
                    configurations.append(new_cars)                                     

                # Check if you can move to the right 
                if car.is_movable("right", self.board):                     
                    moved_car = car.move_right() 
                    new_cars = set(self.cars)
                    new_cars.remove(car)
                    new_cars.add(moved_car)                   
                    configurations.append(new_cars)                 

            # Check for vertical cars 
            if car.orientation == "V":

                # Check if you can move up 
                if car.is_movable("up", self.board):                    
                    moved_car = car.move_up() 
                    new_cars = set(self.cars)
                    new_cars.remove(car)
                    new_cars.add(moved_car)                    
                    configurations.append(new_cars)                  

                # Check if you can move down 
                if car.is_movable("down", self.board):                    
                    moved_car = car.move_down() 
                    new_cars = set(self.cars)
                    new_cars.remove(car)
                    new_cars.add(moved_car)                  
                    configurations.append(new_cars)                  

        return configurations  

    def blockingcars(self):
        column = len(self.board) - 1
        numberofcars = 0
        while self.board[ceil(len(self.board) / 2) - 1][column] != "X":
            if self.board[ceil(len(self.board) / 2) - 1][column] != "0":
                numberofcars += 1
            column -= 1
        return numberofcars  

    def reddistance(self):
        column = 0
        distance = 0
        for i in range(len(self.board)-1):
            if self.board[ceil(len(self.board) / 2) - 1 ][i] == "X":
                distance = len(self.board) - 2 - i 
        return distance     

    def is_solved(self): 
        for car in self.cars:
            winning_column = self.size - 2 
            winning_row = ceil(self.size / 2) - 1 

            if car.name == "X" and car.column == winning_column and car.row == winning_row:
                return True 

        return False  
    
    def get_cars(self):
        return self.cars 
    
    def get_board(self):
        return self.board  
    
    def get_size(self):
        return self.size 
    
    def __hash__(self) -> int:
        return hash(self.__repr__())
    
    def __repr__(self) -> str:
        printable_board = np.array_str(self.board)

        return printable_board 

    def __eq__(self, other) -> bool:
        return isinstance(other, State) 
    
# class State: 

#     def __init__(self, cars: set[Car], size: int):
#         self.cars = cars
#         self.size = size  
#         self.board = None 
#         self.create_board()  
#         self.counter = 0        

#     def create_board(self):
#         board = [["0" for i in range(self.size)] for j in range(self.size)]
#         self.board = np.array(board)

#         # Place the cars on the board 
#         for car in self.cars:
#             if car.orientation == "H":
#                 for j in range(car.length):
#                     self.board[car.row][car.column + j] = car.name 

#             if car.orientation == "V":
#                 for i in range(car.length):
#                     self.board[car.row + i][car.column] = car.name 
        
#         return self.board     

#     def get_next_configurations(self): 

#         # List filled with sets of car objects 
#         configurations = []    
     
#         for car in self.cars:

#             # Check for horizontal cars 
#             if car.orientation == "H":

#                 # Check if you can move to the left 
#                 if car.is_movable("left", self.board):                     
#                     car.move_left() 
#                     configurations.append(copy.deepcopy(self.cars)) 
#                     car.move_right()                 

#                 # Check if you can move to the right 
#                 if car.is_movable("right", self.board):                     
#                     car.move_right() 
#                     configurations.append(copy.deepcopy(self.cars)) 
#                     car.move_left()                 

#             # Check for vertical cars 
#             if car.orientation == "V":

#                 # Check if you can move up 
#                 if car.is_movable("up", self.board):                    
#                     car.move_up()                      
#                     configurations.append(copy.deepcopy(self.cars)) 
#                     car.move_down()                    

#                 # Check if you can move down 
#                 if car.is_movable("down", self.board):                    
#                     car.move_down() 
#                     configurations.append(copy.deepcopy(self.cars)) 
#                     car.move_up()                    

#         return configurations          

#     def is_solved(self): 
#         for car in self.cars:
#             winning_column = self.size - 2 
#             winning_row = ceil(self.size / 2) - 1 

#             if car.name == "X" and car.column == winning_column and car.row == winning_row:
#                 return True 

#         return False  

#     def blockingcars(self):
#         column = len(self.board) - 1
#         numberofcars = 0
#         while self.board[ceil(len(self.board) / 2) - 1 ][column] != "X":
#             if self.board[ceil(len(self.board) / 2) - 1 ][column] != "0":
#                 numberofcars += 1
#             column -= 1
#         return numberofcars

#     def __hash__(self) -> int:
#         return hash(self.__repr__())
    
#     def __repr__(self) -> str:
#         printable_board = np.array_str(self.board)

#         return printable_board 

#     def __eq__(self, other) -> bool:
#         return isinstance(other, State)


class BestFirst:

    def __init__(self, first_state: State, size):
        self.first_state = first_state
        self.first_score = first_state.blockingcars()
        self.size = size 
        self.steps = 0

        # Initialize a queue 
        self.boards_queue = []

        # Initialize a set to keep up the board states already visited 
        self.visited = set()        
        
        # Put first state in queue
        self.boards_queue.append((self.first_score, self.steps, self.first_state))
        heapq.heapify(self.boards_queue)

        # Add first state to visited set 
        self.visited.add(first_state) 
    
    def run(self):
        while len(self.boards_queue) != 0 :
            # Pop new board 
            blocks, steps, board = heapq.heappop(self.boards_queue)  
                         

            # If board is solved return result
            if board.is_solved():
                print(f"It took {steps} steps to solve this game") 
                return board 

            # Add all possible next boards to queue, if they're not in visited set 
            
            next_configurations = board.get_next_configurations()

            for configuration in next_configurations:
                next_board = State(configuration, self.size)
                blocks = next_board.blockingcars() + steps

                if next_board not in self.visited:
                                        
                    heapq.heappush(self.boards_queue, (blocks, steps + 1, next_board))
                    self.visited.add(next_board) 
            


if __name__ == "__main__":
    start = time.time()
    initial_board = Board(6)
    initial_board.load_board("Rushhour6x6_2.csv") 
    initial_cars = initial_board.get_initial_cars()

    first_state = State(initial_cars, 6) 
    bf = BestFirst(first_state, 6) 
    bf.run()
    print(time.time()- start)
    