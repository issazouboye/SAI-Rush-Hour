import numpy as np 

class Car:

    def __init__(self, name, orientation, column, row, length):
        self.name = name 
        self.orientation = orientation 
        self.column = column 
        self.row = row 
        self.length = length 
        

    def __repr__(self) -> str:
        return f"{self.orientation}{self.column}{self.row}{self.length}"

            