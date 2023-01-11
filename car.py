import numpy as np 

class Car:

    def __init__(self, name, orientation, column, row, length):
        self.name = name 
        self.orientation = orientation 
        self.column = column 
        self.row = row 
        self.length = length 
        

    def move(self):

        if self.orientation == 'H':
            pass 
            