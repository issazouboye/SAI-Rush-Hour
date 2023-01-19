import numpy as np
from car import Car
import copy 
from math import ceil
import random  
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from board import visualize

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

    def get_next_configurations(self): 

        # List filled with lists of car objects 
        configurations = []         

        for car in self.cars:

            # Check for horizontal cars 
            if car.orientation == "H":

                # Check if you can move to the left 
                if car.is_movable("left", self.board):
                    new_cars = copy.copy(self.cars) 
                    new_car = copy.copy(car) 
                    new_car.move_left() 


                    # Remove old car from list and append the moved car to list 
                    new_cars.remove(car)
                    new_cars.append(new_car) 

                    # Add new list of cars to configurations list 
                    configurations.append(new_cars) 

                # Check if you can move to the right 
                if car.is_movable("right", self.board):
                    new_cars = copy.copy(self.cars) 
                    new_car = copy.copy(car) 
                    new_car.move_right() 

                    # Remove old car from list and append the moved car to list 
                    new_cars.remove(car)
                    new_cars.append(new_car) 

                    # Add new list of cars to configurations list 
                    configurations.append(new_cars)

            # Check for vertical cars 
            if car.orientation == "V":

                # Check if you can move up 
                if car.is_movable("up", self.board):
                    new_cars = copy.copy(self.cars) 
                    new_car = copy.copy(car) 
                    new_car.move_up() 


                    # Remove old car from list and append the moved car to list 
                    new_cars.remove(car)
                    new_cars.append(new_car) 

                    # Add new list of cars to configurations list 
                    configurations.append(new_cars) 

                # Check if you can move down 
                if car.is_movable("down", self.board):
                    new_cars = copy.copy(self.cars) 
                    new_car = copy.copy(car) 
                    new_car.move_down() 


                    # Remove old car from list and append the moved car to list 
                    new_cars.remove(car)
                    new_cars.append(new_car) 

                    # Add new list of cars to configurations list 
                    configurations.append(new_cars)

        return configurations 

    def get_updated_board(self, new_cars):
        new_board = [["0" for i in range(len(self.board))] for j in range(len(self.board))]
        self.board = np.array(new_board)

        # Place the cars on the board 
        for car in new_cars:
            if car.orientation == "H":
                for j in range(car.length):
                    self.board[car.row][car.column + j] = car.name 

            if car.orientation == "V":
                for i in range(car.length):
                    self.board[car.row + i][car.column] = car.name 
        
        return self.board      

    def is_solved(self): 
        for car in self.cars:
            winning_column = len(self.board) - 2 
            winning_row = ceil(len(self.board) / 2) - 1 

            if car.name == "X" and car.column == winning_column and car.row == winning_row:
                return True 

        return False     


class Random_solver:
    
    def __init__(self, initial_cars, initial_board):
        self.initial_cars = initial_cars 
        self.initial_board = initial_board 
        self.end_cars = None 
        self.end_board = None 
        self.listarray = [initial_board]
    
    def solve_board(self):
        new_game = Game(self.initial_cars, self.initial_board)          
        steps = 0 
        while True:        
            new_cars = random.choice(new_game.get_next_configurations())            
            updated_board = new_game.get_updated_board(new_cars) 
            # print(updated_board) 
            # print() 
            self.listarray.append(updated_board)
            new_game = Game(new_cars, updated_board)
            steps += 1 

            if new_game.is_solved():
                self.end_cars = new_cars 
                self.end_board = updated_board 
                print(f"It took {steps} steps to solve this game") 
                break 

    def get_end_board(self):
        return self.end_board 

    def get_end_cars(self):
        return self.end_cars 

               
if __name__ == "__main__":

    initial_board = Board(6)
    initial_board.load_board("Rushhour6x6_1.csv")

    initial_cars = initial_board.get_initial_cars() 
    initial_board = initial_board.get_initial_board() 

    random_solver = Random_solver(initial_cars, initial_board) 
    random_solver.solve_board()

    end_cars = random_solver.get_end_cars()
    end_board = random_solver.get_end_board()
        
    begincarlist = []
    for i in initial_cars:
        if i.orientation == "H":
            begincarlist.append(i.column)
        if i.orientation == "V":
            begincarlist.append(i.row)
        
    end_cars.sort(key=lambda x: x.name)
    endcarorientation = []
    for i in end_cars:
        if i.orientation == "H":
            endcarorientation.append(i.column)
        if i.orientation == "V":
            endcarorientation.append(i.row)

    movement = []
    for i,j in zip(begincarlist, endcarorientation):
        movement.append(j-i)
        
    print("Car Move")
    for i in range(len(begincarlist)):
        print(f"{end_cars[i].name}   ", end="")
        if movement[i] >= 0:
            print(f" {movement[i]}")
        else:
            print(movement[i])

    boardlist = random_solver.listarray
    visualize(boardlist, saveplot = True)


    
    

        


    


