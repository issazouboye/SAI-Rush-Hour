from __future__ import annotations 
import numpy as np
from car import Car
import copy 
from math import ceil
import random  
  

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

    def get_updated_board(self, new_car: Car, old_column, old_row):

        new_column = new_car.column
        new_row = new_car.row

        if new_car.orientation == "H":
            if new_car.length == 2:

                # Case car moved to the right 
                if new_column > old_column:
                    self.board[old_row][old_column] = "0" 
                    self.board[old_row][old_column + 2] = new_car.name 

                # Case if car moved to the left 
                elif new_column < old_column:
                    self.board[old_row][new_column + 2] = "0"
                    self.board[old_row][new_column] = new_car.name 

            if new_car.length == 3:

                # Case car moved to the right 
                if new_column > old_column:
                    self.board[old_row][old_column] = "0" 
                    self.board[old_row][old_column + 3] = new_car.name 

                # Case car moved to the left 
                elif new_column < old_column:
                    self.board[old_row][new_column + 3] = "0"
                    self.board[old_row][new_column] = new_car.name 

        if new_car.orientation == "V":
            if new_car.length == 2:

                # Case car moved down
                if new_row > old_row:
                    self.board[old_row][old_column] = "0" 
                    self.board[old_row + 2][old_column] = new_car.name 

                # Case if car moved up
                elif new_row < old_row:
                    self.board[new_row + 2][old_column] = "0"
                    self.board[new_row][old_column] = new_car.name 

            if new_car.length == 3:

                # Case car moved down
                if new_row > old_row:
                    self.board[old_row][old_column] = "0" 
                    self.board[old_row + 2][old_column] = new_car.name 

                # Case if car moved up
                elif new_row < old_row:
                    self.board[new_row + 2][old_column] = "0"
                    self.board[new_row][old_column] = new_car.name    

        return self.board                                                         

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
        self.boards = []

    def solve_board(self):     
        new_game = Game(self.initial_cars, self.initial_board)
        cars = new_game.get_cars()
        board = self.initial_board 
        self.boards.append(board)

        while True:             
            new_car = random.choice(cars) 
            old_column = new_car.column
            old_row = new_car.row            

            if new_car.orientation == "H":
                direction = random.choice(["left", "right"])

                if direction == "left" and new_car.is_movable(direction, board):
                    new_car.move_left()                 
                    self.steps += 1

                elif direction == "right" and new_car.is_movable(direction, board):
                    new_car.move_right()                  
                    self.steps += 1 

            if new_car.orientation == "V":
                direction = random.choice(["up", "down"])

                if direction == "up" and new_car.is_movable(direction, board):
                    new_car.move_up()               
                    self.steps += 1

                elif direction == "down" and new_car.is_movable(direction, board):
                    new_car.move_down()                   
                    self.steps += 1

            board = new_game.get_updated_board(new_car, old_column, old_row)  
            self.boards.append(board)                      

            if new_game.is_solved():
                self.end_cars = cars 
                self.end_board = board   
                print(f"It took {self.steps} steps to solve this game") 
                break 
        
    def step_count(self):
        return self.steps

    def get_end_board(self):
        return self.end_board 

    def get_end_cars(self):
        return self.end_cars 
    
    def get_list_boards(self):
        return self.boards 


if __name__ == "__main__":

    smallest_steps = 100000

    initial_board = Board(6)
    initial_board.load_board("Rushhour6x6_1.csv")     

    initial_cars = initial_board.get_initial_cars() 
    initial_board = initial_board.get_initial_board()      

    master_random_solver = Random_solver_v2(initial_cars, initial_board)  
 
    for i in range(100):     

        random_solver = copy.deepcopy(master_random_solver)
        random_solver.solve_board()

        end_cars = random_solver.get_end_cars()
        end_board = random_solver.get_end_board()

        steps = random_solver.step_count()

        if steps < smallest_steps:
            smallest_steps = steps                          

    print()
    print(f"The smallest number of steps is: {smallest_steps}") 

