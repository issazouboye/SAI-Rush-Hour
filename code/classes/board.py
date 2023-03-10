"""
Program: board.py

Course: Algoritmen en Heuristieken

Students: Issa Zouboye, Alex van Diepen, Shreyas Potdar

Description: This is a program that utilizes a data file to
load the initial configuration of the rush hour game.
"""

from __future__ import annotations 
import numpy as np 
from .car import Car
from typing import List
import numpy.typing as npt


class Board:

    def __init__(self, size: int) -> None:
        """
        A function that initializes an np array to create a board
        for the initial rush hour configuration. 
        """
        self.size = size        
        board = [["0" for i in range(self.size)] for j in range(self.size)]
        self.board: npt.NDArray[np.str_] = np.array(board)

        # List with cars 
        self.cars: List[Car] = []       
    
    def load_board(self, filename: str) -> None:  
        """
        A function that loads data from a csv file and creates
        Car objects and places the cars on the board.
        """
        # Reads the data
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
 
    def get_initial_cars(self) -> List[Car]:
        """
        A function that returns the list of car objects with stored
        characteristics from the csv file. 
        """
        return self.cars 
    
    def get_initial_board(self) -> npt.NDArray[np.str_]:
        """
        A function that returns the intial rush hour board.
        """
        return self.board  

    def get_size(self) -> int:
        """
        A function that returns the size of the intial rush hour 
        board
        """
        return self.size 