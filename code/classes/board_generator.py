from __future__ import annotations 
from car import Car 
from board import Board 
from state import State 
from breadth_first import BreadthFirst 
from math import ceil 
import time
import random
from string import ascii_uppercase
import numpy as np 
import numpy.typing as npt


class RandomBoard:

    def __init__(self, size: int) -> None:        
        self.size = size        
        self.cars = set() 
        board = [["0" for i in range(self.size)] for j in range(self.size)]
        self.board: npt.NDArray[np.str_] = np.array(board)
        self.generate_board()        

    
    def generate_board(self):

        # Create list of car names 
        list_letters = list(ascii_uppercase)
        list_letters.remove("X")
        list_double_letters = ["A"+letter for letter in ascii_uppercase] 
        names_list = list_letters + list_double_letters        
      
        # Place the red car on the board in the middel of the board, but not at the exit position        
        red_car_col = random.randint(0, self.size - 3) 
        red_car_row = ceil(self.size / 2) - 1          

        for i in range(2):    
            self.board[red_car_row][red_car_col + i] = "X"

        red_car = Car("X", "H", red_car_col, red_car_row, 2) 
        self.cars.add(red_car)         

        # If the red car is placed almost at the winning position, make sure to place a blocking car 
        if red_car_col == self.size - 3:
            car_name = names_list.pop(0)                         
            car_col = self.size - 1 
            car_row = ceil(self.size / 2) - 1 
            orientation = "V" 
            car_length = random.choice([2,3])
            new_car = Car(car_name, orientation, car_col, car_row, car_length)
            self.cars.add(new_car)

            for i in range(car_length):
                self.board[car_row + i][car_col] = car_name         
    
        # Initialize counter for number of attempts to place a car on the board 
        attempts = 0
        max_attempts = random.randint(5, 20)

        # randomly place vehicles on the board
        while len(names_list) > 0: 
            car_placed = False

            orientation = random.choice(["H", "V"])
            car_length = random.choice([2, 2, 2, 3, 3])

            if orientation == "H":
                col = random.randint(0, self.size - car_length)
                row = random.randint(0, self.size - 1)

                if self.car_fits(orientation, col, row, car_length):
                    car_name = names_list.pop(0)
                    new_car = Car(car_name, orientation, col, row, car_length)  
                    self.cars.add(new_car)                  
                    self.place_car(new_car)
                    car_placed = True                                    
            
            if orientation == "V":
                col = random.randint(0, self.size - 1)
                row = random.randint(0, self.size - car_length)

                if self.car_fits(orientation, col, row, car_length):                    
                    car_name = names_list.pop(0)
                    new_car = Car(car_name, orientation, col, row, car_length)  
                    self.cars.add(new_car)                  
                    self.place_car(new_car)
                    car_placed = True                    
            
            if car_placed == False:
                attempts += 1 

            # Try to attempt at most 20 times to place a car, if unsuccesful stop placing cars 
            if attempts > max_attempts:
                break         

    def car_fits(self, orientation, col, row, car_length):

        if orientation == "H":
            for j in range(car_length):
                if self.board[row][col + j] != "0":
                    return False
        
        if orientation == "V":
            for i in range(car_length):
                if self.board[row + i][col] != "0":
                    return False
        
        return True
    
    def place_car(self, car: Car):

        if car.orientation == "H":
            for j in range(car.length):
                self.board[car.row][car.column + j] = car.name

        if car.orientation == "V":
            for i in range(car.length):
                self.board[car.row + i][car.column] = car.name

        return self.board 
    
    def get_initial_cars(self):
        return self.cars 
    
    def get_initial_board(self):
        return self.board  

    def get_size(self):
        return self.size 
    

if __name__ == "__main__":

    start = time.time()
    
    random_board = RandomBoard(6)
    print(random_board.get_initial_board())
    print()

    initial_cars = random_board.get_initial_cars() 
    print(f"Number of placed cars is {len(initial_cars)}")
    print()

    first_state = State(initial_cars, 6) 
    bf = BreadthFirst(first_state, 6) 
    end_state = bf.run()
    print(end_state.get_board())
    print(f"There were {len(bf.visited)} states visited")

    print(time.time() - start)
 
