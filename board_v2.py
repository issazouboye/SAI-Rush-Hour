import numpy as np
from car import Car


class Board():
    def __init__(self, size: int):
        self.colomn = size
        self.row = size
        board = [["0" for i in range(self.colomn)] for j in range(self.row)]
        self.board = np.array(board)

        # List with cars 
        self.cars_list = [] 
    
    def load_board(self, filename: str):  

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
                self.cars_list.append(car) 
                    
            print(self.cars_list) 

        # Place the cars on the board 
        for car in self.cars_list:
            if car.orientation == "H":
                for j in range(car.length):
                    self.board[car.row][car.column + j] = car.name 

            if car.orientation == "V":
                for i in range(car.length):
                    self.board[car.row + i][car.column] = car.name 

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


if __name__ == "__main__":


    test =  Board(9)
    test.load_board("Rushhour9x9_4.csv")


    # for i in range(2):
    #     test.move()
    # print(test.load_board("Rushhour6x6_1.csv"))


