from __future__ import annotations 
import numpy as np 


class Car:

    def __init__(self, name, orientation, column, row, length):
        self.name = name 
        self.orientation = orientation 
        self.column = column 
        self.row = row 
        self.length = length 

    def is_movable(self, direction, board) -> bool:

        if self.orientation == "H":
            if direction == "left":
                if self.column - 1 >= 0 and board[self.row][self.column - 1] == "0":
                    return True 

            if direction == "right":
                if self.length == 2:
                    if self.column + 2 < len(board) and board[self.row][self.column + 2] == "0":
                        return True 

                if self.length == 3:
                    if self.column + 3 < len(board) and board[self.row][self.column + 3] == "0":
                        return True 

        if self.orientation == "V":
            if direction == "up":
                if self.row - 1 >= 0 and board[self.row - 1][self.column] == "0":
                    return True 

            if direction == "down":
                if self.length == 2:
                    if self.row + 2 < len(board) and board[self.row + 2][self.column] == "0":
                        return True

                if self.length == 3:
                    if self.row + 3 < len(board) and board[self.row + 3][self.column] == "0":
                        return True 

        return False     

    def move_left(self):

        moved_car = Car(self.name, self.orientation, self.column - 1, self.row, self.length) 

        return moved_car 

    def move_right(self):

        moved_car = Car(self.name, self.orientation, self.column + 1, self.row, self.length) 

        return moved_car 

    def move_up(self):

        moved_car = Car(self.name, self.orientation, self.column, self.row - 1, self.length) 

        return moved_car 

    def move_down(self):

        moved_car = Car(self.name, self.orientation, self.column, self.row + 1, self.length) 

        return moved_car 
    
    def __str__(self):
        return f"{self.name}, {self.column}, {self.row}"

    def __hash__(self) -> int:
        return hash(self.__str__())

    def __eq__(self, other) -> bool:
        return isinstance(other, Car) 
   

            