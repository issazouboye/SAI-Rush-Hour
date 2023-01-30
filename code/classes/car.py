"""
Program: car.py

Course: Algoritmen en Heuristieken

Students: Issa Zouboye, Alex van Diepen, Shreyas Potdar

Description: This is a program that implements the car class to
create car objects and saves its characteristics in the object. Furthermore
it checks if a car object is movable in a certain direction. 
"""


from __future__ import annotations 
import numpy as np 
import numpy.typing as npt


class Car:
    """
    A function that intializes the characteristics of a car into an object.
    """

    def __init__(self, name: str, orientation: str, column: int, row: int, length: int) -> None:
        self.name = name 
        self.orientation = orientation 
        self.column = column 
        self.row = row 
        self.length = length 

    def is_movable(self, direction: str, board: npt.NDArray[np.str_]) -> bool:
    """
    A function that returns a boolean to see if a car object can move.
    """
        # if the car's orientation is horizontal, it can only move left or right
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
        
        # if the car's orientation is vertical, it can only move up or down
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

    def move_left(self) -> Car:
        """
        A function that moves the car left.
        """
        # a new car object is created in the moved location of the old car
        moved_car = Car(self.name, self.orientation, self.column - 1, self.row, self.length) 

        return moved_car 

    def move_right(self) -> Car:
        """
        A function that moves the car right.
        """
        # a new car object is created in the moved location of the old car
        moved_car = Car(self.name, self.orientation, self.column + 1, self.row, self.length) 

        return moved_car 

    def move_up(self) -> Car:
        """
        A function that moves the car up.
        """
        # a new car object is created in the moved location of the old car
        moved_car = Car(self.name, self.orientation, self.column, self.row - 1, self.length) 

        return moved_car 

    def move_down(self) -> Car:
        """
        A function that moves the car down.
        """
        # a new car object is created in the moved location of the old car
        moved_car = Car(self.name, self.orientation, self.column, self.row + 1, self.length) 

        return moved_car 
    
    def __str__(self) -> str:
        return f"{self.name}, {self.column}, {self.row}"

    def __hash__(self) -> int:
        # each car object has a hash value
        return hash(self.__str__())

    def __eq__(self, other: object) -> bool:
        return isinstance(other, Car) 
   

            