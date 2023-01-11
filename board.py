# class Board:
    
#     def __init__(self, size):
#         for i in range(size):

import numpy as np

class Board():
    def __init__(self, size):
        self.colomn = size
        self.row = size
    
    def load_board(filename):
        
            


with open("Rushhour6x6_1.csv", 'r') as f:
    variablearray = []
    for line in f:
        line = line.strip()
        variables = line.split(",")
        variablearray.append(variables)
    variablearray.pop(0)
    print(variablearray)


