"""
Program: board_generator.py

Course: Algoritmen en Heuristieken

Students: Issa Zouboye, Alex van Diepen, Shreyas Potdar

Description: This is a algorithm that generates a random rush hour puzzle.
"""

from __future__ import annotations 
from ..classes.car import Car
from math import ceil 
import random
from string import ascii_uppercase
import numpy as np 
import numpy.typing as npt


class RandomBoard:

    def __init__(self, size: int) -> None:        
        self.size = size        
        self.cars: list = [] 
        board = [["0" for i in range(self.size)] for j in range(self.size)]
        self.board: npt.NDArray[np.str_] = np.array(board)
        self.generate_board()        

    
    def generate_board(self):
        """  
        A function that places random cars on the board. If a car fits, a car object will be created and added in 
        the cars list. 
        """

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
        self.cars.append(red_car)         

        # If the red car is placed almost at the winning position, make sure to place a blocking car 
        if red_car_col == self.size - 3:
            car_name = names_list.pop(0)                         
            car_col = self.size - 1 
            car_row = ceil(self.size / 2) - 1 
            orientation = "V" 
            car_length = random.choice([2,3])
            new_car = Car(car_name, orientation, car_col, car_row, car_length)
            self.cars.append(new_car)

            for i in range(car_length):
                self.board[car_row + i][car_col] = car_name         
    
        # Initialize counter for number of attempts to place a car on the board 
        attempts = 0
        max_attempts = random.randint(5, 20)

        # randomly place vehicles on the board
        while len(names_list) > 0: 
            car_placed = False

            orientation = random.choice(["H", "V"])
            car_length = random.choice([2, 2, 2, 2, 3])

            if orientation == "H":
                col = random.randint(0, self.size - car_length)
                row = random.randint(0, self.size - 1)

                if self.car_fits(orientation, col, row, car_length):
                    car_name = names_list.pop(0)
                    new_car = Car(car_name, orientation, col, row, car_length)  
                    self.cars.append(new_car)                  
                    self.place_car(new_car)
                    car_placed = True 
                    attempts = 0                                   
            
            if orientation == "V":
                col = random.randint(0, self.size - 1)
                row = random.randint(0, self.size - car_length)

                if self.car_fits(orientation, col, row, car_length):                    
                    car_name = names_list.pop(0)
                    new_car = Car(car_name, orientation, col, row, car_length)  
                    self.cars.append(new_car)                  
                    self.place_car(new_car)
                    car_placed = True 
                    attempts = 0                   
            
            if car_placed == False:
                attempts += 1 

            # Try to attempt at most 20 times to place a car, if unsuccesful stop placing cars 
            if attempts > max_attempts:
                break         

    def car_fits(self, orientation, col, row, car_length):
        """ 
        A function that checks if a car can be placed on the board 
        """

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
        """  
        A function that places a Car object on the board
        """

        if car.orientation == "H":
            for j in range(car.length):
                self.board[car.row][car.column + j] = car.name

        if car.orientation == "V":
            for i in range(car.length):
                self.board[car.row + i][car.column] = car.name

        return self.board 
    
    def get_initial_cars(self):
        """
        A function that returns the list of car objects with stored
        characteristics from the csv file. 
        """
        return self.cars 
    
    def get_initial_board(self):
        """
        A function that returns the intial rush hour board.
        """
        return self.board  

    def get_size(self):
        """
        A function that returns the size of the intial rush hour 
        board
        """
        return self.size 
    


 
