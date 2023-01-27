"""
board.py

UVA Programming Lab

A program that loads the intial board from a csv file.

"""

from __future__ import annotations 
import numpy as np 
from .car import Car 
from typing import Set
import numpy.typing as npt

class Board:

    def __init__(self, size: int) -> None:
        self.size = size        
        board = [["0" for i in range(self.size)] for j in range(self.size)]
        self.board: npt.NDArray[np.str_] = np.array(board)

        # Set with cars 
        self.cars: Set[Car] = set()        
    
    def load_board(self, filename: str) -> None:  

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

        # print("First board:")
        # print(self.board)
        # print() 

    def get_initial_cars(self) -> Set[Car]:
        return self.cars 
    
    def get_initial_board(self) -> npt.NDArray[np.str_]:
        return self.board  

    def get_size(self) -> int:
        return self.size 