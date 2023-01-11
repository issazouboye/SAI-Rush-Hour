# class Board:
    
#     def __init__(self, size):
#         for i in range(size):

import numpy as np

class Board():
    def __init__(self, size):
        self.colomn = size
        self.row = size
    
    def load_board(self, filename):
        board = [["0" for i in range(self.colomn)] for j in range(self.row)]
        board = np.array(board)
        
        with open(filename, 'r') as f:
            variablearray = []
            for line in f:
                line = line.strip()
                variables = line.split(",")
                variablearray.append(variables)
            variablearray.pop(0)
        for i in variablearray:
            if i[1] == "H":
                board[int(i[3]) - 1][int(i[2]) - 1] = i[0]
                if i[4] == "2":
                    board[int(i[3]) - 1][[int(i[2])]] = i[0]
                if i[4] == "3":
                    board[int(i[3]) - 1][[int(i[2])]] = i[0]
                    board[int(i[3]) - 1][[int(i[2]) + 1]] = i[0]
            else:
                board[int(i[3]) - 1][int(i[2]) - 1]= i[0]
        print(board)

test =  Board(6)
print(test.load_board("Rushhour6x6_1.csv"))

