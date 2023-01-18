from __future__ import annotations 
import numpy as np
# from car import Car
# import copy 
from math import ceil
import random  


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
        if self.orientation == "H":
            self.column -= 1 

    def move_right(self):
        if self.orientation == "H":
            self.column += 1

    def move_up(self):
        if self.orientation == "V":
            self.row -= 1 

    def move_down(self):
        if self.orientation == "V":
            self.row += 1  

    def __hash__(self) -> int:
        return hash((self.name, self.column, self.row))

    def __eq__(self, other) -> bool:
        return isinstance(other, Car) 
    

class Board:

    def __init__(self, size: int):
        self.size = size        
        board = [["0" for i in range(self.size)] for j in range(self.size)]
        self.board = np.array(board)

        # List with cars 
        self.cars = [] 
    
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
                self.cars.append(car)                   
        
        # Place the cars on the board 
        for car in self.cars:
            if car.orientation == "H":
                for j in range(car.length):
                    self.board[car.row][car.column + j] = car.name 

            if car.orientation == "V":
                for i in range(car.length):
                    self.board[car.row + i][car.column] = car.name 

        # print(self.board)
        # print() 

    def get_initial_cars(self):
        return self.cars  

    def get_initial_board(self):
        return self.board  

class Game:

    def __init__(self, cars, board):
        self.cars = cars 
        self.board = board      

    def get_updated_board(self, car, old_column, old_row, new_column, new_row):

        if car.orientation == "H":
            if car.length == "2":
                if j-1>=0 and self.board[i][j-1] == "0":
                    self.board[i][j-1] = self.board[i][j]
                    self.board[i][j+1] = "0"
                    
                elif j+1 < self.row and self.board[i][j+1] == "0":
                    self.board[i][j+1] = self.board[i][j]
                    self.board[i][j-1] = "0"
                    
            else:
                if j-1 >= 0 and self.board[i][j-1] == "0":
                    self.board[i][j-1] = self.board[i][j]
                    self.board[i][j+2] = "0"
                    
                elif j+1< self.row and self.board[i][j+1] == "0":
                    self.board[i][j+1] = self.board[i][j]
                    self.board[i][j-2] = "0"
                               
        else:
            if self.cars[self.board[i][j]].length == "2":
                # verticale move naar beneden
                if i+1< self.row and self.board[i + 1][j] == "0":
                    self.board[i + 1][j] = self.board[i][j]
                    self.board[i - 1][j] = "0"
                    
                elif i-1 >= 0 and self.board[i-1][j] == "0":
                    self.board[i-1][j] = self.board[i][j]
                    self.board[i+1][j] = "0"
                    
            else:
                if i-1 >= 0 and self.board[i-1][j] == "0":
                    self.board[i-1][j] = self.board[i][j]
                    self.board[i+2][j] = "0"
                    
                elif i+1< self.row and self.board[i+1][j] == "0":
                    self.board[i+1][j] = self.board[i][j]
                    self.board[i-2][j] = "0"
                              



        # new_board = [["0" for i in range(len(self.board))] for j in range(len(self.board))]
        # self.board = np.array(new_board)

        # # Place the cars on the board 
        # for car in new_cars:
        #     if car.orientation == "H":
        #         for j in range(car.length):
        #             self.board[car.row][car.column + j] = car.name 

        #     if car.orientation == "V":
        #         for i in range(car.length):
        #             self.board[car.row + i][car.column] = car.name 
        
        # return self.board      

    def is_solved(self): 
        for car in self.cars:
            winning_column = len(self.board) - 2 
            winning_row = ceil(len(self.board) / 2) - 1 

            if car.name == "X" and car.column == winning_column and car.row == winning_row:
                return True 

        return False 
    
    def get_cars(self):
        return self.cars 
    

class Random_solver_v2:

    def __init__(self, initial_cars, initial_board):
        self.initial_cars = initial_cars 
        self.initial_board = initial_board 
        self.steps = 0
        self.end_cars = None 
        self.end_board = None 

    def solve_board(self):     
        new_game = Game(self.initial_cars, self.initial_board)

        while True:
            cars = new_game.get_cars() 
            new_car = random.choice(cars) 

            if new_car.orientation == "H":
                direction = random.choice(["left", "right"])

                if direction == "left" and new_car.is_movable(direction, new_game.get_updated_board(cars)):
                    old_column = new_car.column 
                    old_row = new.car.row 

                    new_car.move_left()
                    new_column = new.car.column
                    new_row = new.car.row 

                    self.steps += 1

                elif direction == "right" and new_car.is_movable(direction, new_game.get_updated_board(cars)):
                    old_column = new_car.column 
                    old_row = new.car.row 

                    new_car.move_right()
                    new_column = new.car.column
                    new_row = new.car.row 

                    self.steps += 1 

            if new_car.orientation == "V":
                direction = random.choice(["up", "down"])

                if direction == "up" and new_car.is_movable(direction, new_game.get_updated_board(cars)):
                    old_column = new_car.column 
                    old_row = new.car.row 

                    new_car.move_up()
                    new_column = new.car.column
                    new_row = new.car.row 

                    self.steps += 1

                elif direction == "down" and new_car.is_movable(direction, new_game.get_updated_board(cars)):
                    old_column = new_car.column 
                    old_row = new.car.row 

                    new_car.move_down() 
                    new_column = new.car.column
                    new_row = new.car.row 

                    self.steps += 1

            new_game.get_updated_board(new_car, old_column, old_row, new_column, new_row)                  
             

            if new_game.is_solved():
                self.end_cars = cars 
                self.end_board = new_game.get_updated_board(cars)  
                print(f"It took {self.steps} steps to solve this game") 
                break 
        
    def step_count(self):
        return self.steps

    def get_end_board(self):
        return self.end_board 

    def get_end_cars(self):
        return self.end_cars 


if __name__ == "__main__":

    

    for i in range(10):    
        initial_board = Board(6)
        initial_board.load_board("Rushhour6x6_1.csv")

        initial_cars = initial_board.get_initial_cars() 
        initial_board = initial_board.get_initial_board()   

        random_solver = Random_solver_v2(initial_cars, initial_board) 
        random_solver.solve_board()

        end_cars = random_solver.get_end_cars()
        end_board = random_solver.get_end_board()

        # print(end_board)