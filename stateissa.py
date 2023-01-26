from __future__ import annotations 
import numpy as np 
from math import ceil
from carissa import Car
from breadth_first import Board



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
        while self.board[ceil(len(self.board) / 2) - 1 ][column] != "X":
            if self.board[ceil(len(self.board) / 2) - 1 ][column] != "0":
                numberofcars += 1
            column -= 1
        return numberofcars       

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
    

if __name__ == "__main__":

    initial_board = Board(6)
    initial_board.load_board("Rushhour6x6_1.csv") 
    initial_cars = initial_board.get_initial_cars()

    first_state = State(initial_cars, 6) 
    next_configurations = first_state.get_next_configurations() 
   
    for configuration in next_configurations:
        next_state = State(configuration, 6)
        print(next_state.get_board())
        print()

        

    
