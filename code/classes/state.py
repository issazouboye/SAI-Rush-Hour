from __future__ import annotations
import numpy as np
from math import ceil
from .car import Car
from .board import Board
from typing import Set, List
import numpy.typing as npt
import copy

class State:

    def __init__(self, cars: dict[Car], size: int) -> None:
        self.cars = cars
        self.size = size
        board = [["0" for i in range(self.size)] for j in range(self.size)]
        self.board: npt.NDArray[np.str_] = np.array(board)
        self.create_board()

    def create_board(self) -> npt.NDArray[np.str_]:

        # Place the cars on the board
        for car in self.cars:
            if car.orientation == "H":
                for j in range(car.length):
                    self.board[car.row][car.column + j] = car.name

            if car.orientation == "V":
                for i in range(car.length):
                    self.board[car.row + i][car.column] = car.name

        return self.board

    def get_next_configurations(self) -> List[dict[Car]]:

        # List filled with sets of car objects
        configurations = []

        for index, car in enumerate(self.cars):

            # Check for horizontal cars
            if car.orientation == "H":

                # Check if you can move to the left
                if car.is_movable("left", self.board):
                    moved_car = car.move_left()
                    new_cars = list(self.cars)
                    new_cars[index] = moved_car                    
                    configurations.append(new_cars)

                # Check if you can move to the right
                if car.is_movable("right", self.board):
                    moved_car = car.move_right()
                    new_cars = list(self.cars)
                    new_cars[index] = moved_car                   
                    configurations.append(new_cars)

            # Check for vertical cars
            if car.orientation == "V":

                # Check if you can move up
                if car.is_movable("up", self.board):
                    moved_car = car.move_up()
                    new_cars = list(self.cars)
                    new_cars[index] = moved_car                   
                    configurations.append(new_cars)

                # Check if you can move down
                if car.is_movable("down", self.board):
                    moved_car = car.move_down()
                    new_cars = list(self.cars)
                    new_cars[index] = moved_car                    
                    configurations.append(new_cars)

        return configurations
    
    def blockingcars(self) -> int:
        column = len(self.board) - 1
        numberofcars = 0
        while self.board[ceil(len(self.board) / 2) - 1 ][column] != "X":
            if self.board[ceil(len(self.board) / 2) - 1 ][column] != "0":
                numberofcars += 1
            column -= 1
        return numberofcars 

    def reddistance(self) -> int:
        column = 0
        distance = 0
        for i in range(len(self.board)-1):
            if self.board[ceil(len(self.board) / 2) - 1 ][i] == "X":
                distance = len(self.board) - 2 - i 
        return distance  

    def blockingdistance(self) -> int:
        return (self.blockingcars() + self.reddistance())      

    def is_solved(self) -> bool:
        for car in self.cars:
            winning_column = self.size - 2
            winning_row = ceil(self.size / 2) - 1

            if car.name == "X" and car.column == winning_column and car.row == winning_row:
                return True

        return False

    def get_cars(self) -> Set[Car]:
        return self.cars

    def get_board(self) -> npt.NDArray[np.str_]:
        return self.board

    def get_size(self) -> int:
        return self.size

    def __hash__(self) -> int:
        return hash(self.__repr__())

    def __repr__(self) -> str:
        printable_board = np.array_str(self.board)

        return printable_board

    def __eq__(self, other: object) -> bool:
        return isinstance(other, State)
