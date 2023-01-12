import numpy as np
from car import Car

class Board():
    def __init__(self, size: int):
        self.colomn = size
        self.row = size
        board = [["0" for i in range(self.colomn)] for j in range(self.row)]
        self.board = np.array(board)
        self.cars = {}
    
    def load_board(self, filename: str):  

        with open(filename, 'r') as f:
            variablearray = []
            for line in f:
                line = line.strip()
                variables = line.split(",")
                car = Car(variables[0], variables[1], variables[2], variables[3], variables[4])
                self.cars[variables[0]] = car
                variablearray.append(variables)
            variablearray.pop(0)
            self.cars.pop("car")
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
        for i in range(len(self.board)):
            for j in range(len(self.board)):
                if self.board[i][j] != "0":
                    if self.cars[self.board[i][j]].orientation == "H":
                        if self.cars[self.board[i][j]].length == "2":
                            if j-1>=0 and self.board[i][j-1] == "0":
                                self.board[i][j-1] = self.board[i][j]
                                self.board[i][j+1] = "0"
                            elif j+2 < self.row and self.board[i][j+2] == "0":
                                self.board[i][j+2] = self.board[i][j]
                                self.board[i][j] = "0"
                        else:
                            if j-1 >= 0 and self.board[i][j-1] == "0":
                                self.board[i][j-1] = self.board[i][j]
                                self.board[i][j+2] = "0"
                            elif j+3< self.row and self.board[i][j+3] == "0":
                                print("hello")
                                print(i)
                                print(j)
                                print(self.board[i][j])
                                self.board[i][j+3] = self.board[i][j]
                                self.board[i][j] = "0"
                    else:
                        if self.cars[self.board[i][j]].length == "2":
                            # verticale move naar beneden
                            if i+1< self.row and self.board[i + 1][j] == "0":
                                self.board[i + 1][j] = self.board[i][j]
                                self.board[i - 1][j] = "0"
                            elif i-1 >= 0 and self.board[i-1][j] == "0":
                                self.board[i-1][j] = self.board[i][j]
                                self.board[i+1][j] = "0"
                                print(self.board)
                        else:
                            if i-1 >= 0 and self.board[i-1][j] == "0":
                                self.board[i-1][j] = self.board[i][j]
                                self.board[i+2][j] = "0"
                            elif i+3< self.row and self.board[i+3][j] == "0":
                                self.board[i+3][j] = self.board[i][j]
                                self.board[i][j] = "0"

        print(self.board)










test =  Board(6)
test.load_board("Rushhour6x6_1.csv")
for i in range(2):
    test.move()
# print(test.load_board("Rushhour6x6_1.csv"))


