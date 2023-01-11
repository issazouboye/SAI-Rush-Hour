# class Board:
    
#     def __init__(self, size):
#         for i in range(size):

import numpy as np

class Board():
    def __init__(self, size: int):
        self.colomn = size
        self.row = size
        board = [["0" for i in range(self.colomn)] for j in range(self.row)]
        self.board = np.array(board)
    
    def load_board(self, filename: str):  

        with open(filename, 'r') as f:
            variablearray = []
            for line in f:
                line = line.strip()
                variables = line.split(",")
                variablearray.append(variables)
            variablearray.pop(0)
        for i in variablearray:
            if i[1] == "H":
                self.board[int(i[3]) - 1][int(i[2]) - 1] = i[0]
                if i[4] == "2":
                    self.board[int(i[3]) - 1][int(i[2])] = i[0]
                if i[4] == "3":
                    self.board[int(i[3]) - 1][int(i[2])] = i[0]
                    self.board[int(i[3]) - 1][int(i[2]) + 1] = i[0]
            else:
                self.board[int(i[3]) - 1][int(i[2]) - 1]= i[0]
                if i[4] == "2":
                    self.board[int(i[3])][int(i[2]) - 1] = i[0]
                if i[4] == "3":
                    self.board[int(i[3])][int(i[2]) - 1] = i[0]
                    self.board[int(i[3]) + 1][int(i[2]) - 1] = i[0]
        print(self.board)
    
    def move(self):




test =  Board(6)
test.load_board("Rushhour6x6_1.csv")
# print(test.load_board("Rushhour6x6_1.csv"))


