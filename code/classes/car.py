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
    Class that defines a car object for the Rush Hour game 

    Attributes: 
        name (str): name of the car 
        orientation (str): direction the car is positioned in (vertical or horizontal)
        column (int): column of car in the grid
        row (int): row of the car in the grid 
        length (int): length of the car (2 or 3)
    """

    def __init__(self, name: str, orientation: str, column: int, row: int, length: int) -> None:
        self.name = name 
        self.orientation = orientation 
        self.column = column 
        self.row = row 
        self.length = length 

    def is_movable(self, direction: str, board: npt.NDArray[np.str_]) -> bool:
        """
        A function that checks if a car object can be moved based on 
        its orientation and returns a boolean.
        """

        # If a car object is horizontally orientated, then it can only move left or right from the grid's perspective
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
        
        # If a car object is vertically orientated, then it can only move up or down from the grid's perspective
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
        A function that creates a new car object located in the new 
        location of current car that has moved to the left.
        """

        moved_car = Car(self.name, self.orientation, self.column - 1, self.row, self.length) 

        return moved_car 

    def move_right(self) -> Car:
        """
        A function that creates a new car object located in the new 
        location of the current car that has moved to the right.
        """

        moved_car = Car(self.name, self.orientation, self.column + 1, self.row, self.length) 

        return moved_car 

    def move_up(self) -> Car:
        """
        A function that creates a new car object located in the new 
        location of the current car that has moved up.
        """

        moved_car = Car(self.name, self.orientation, self.column, self.row - 1, self.length) 

        return moved_car 

    def move_down(self) -> Car:
        """
        A function that creates a new car object located in the new 
        location of the current car that has moved down.
        """

        moved_car = Car(self.name, self.orientation, self.column, self.row + 1, self.length) 

        return moved_car 
    
    def __str__(self) -> str:
        """
        A function that gives the string representation of the car objects.
        """
        return f"{self.name}, {self.column}, {self.row}"

    def __hash__(self) -> int:
        """
        A function that creates a hash value for each car object.
        """
        return hash(self.__str__())

    def __eq__(self, other: object) -> bool:
        """
        A function that enables you to compare whether two car objects are the same.
        """
        return isinstance(other, Car)             