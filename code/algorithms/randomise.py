"""
Program: randomise.py
Course: Algoritmen en Heuristieken
Students: Issa Zouboye, Alex van Diepen, Shreyas Potdar
Description: This is a program that implements two differently implemented
random algorthms to solved the rush hour game
"""
from __future__ import annotations 
import numpy as np 
import random 
from ..classes.car import Car 
from ..classes.board import Board 
from ..classes.state import State 
from math import ceil 
import numpy.typing as npt



class Random_solver_v1:
    
    def __init__(self, initial_state: State) -> None:
        self.initial_state = initial_state        
        self.steps = 0                        
    
    def run(self) -> State:                 

        new_state = self.initial_state 
        size = self.initial_state.get_size()

        while True:        
            new_configuration = random.choice(new_state.get_next_configurations())    
            new_state = State(new_configuration, size)     
            self.steps += 1 

            if new_state.is_solved():                
                print(f"It took {self.steps} steps to solve this game") 
                return new_state 
   
    def step_count(self) -> int:
        return self.steps     
    


class Random_solver_v2:

    def __init__(self, initial_state: State) -> None:
        self.initial_state = initial_state
        self.cars = initial_state.get_cars()
        self.board = initial_state.get_board()
        self.steps = 0      

    def run(self) -> None:   

        while True:             
            new_car = random.choice(list(self.cars))           
            old_column = new_car.column
            old_row = new_car.row   
            move_made = False          

            if new_car.orientation == "H":
                direction = random.choice(["left", "right"])

                if direction == "left" and new_car.is_movable(direction, self.board):
                    moved_car = new_car.move_left()                                                         
                    self.cars.remove(new_car)
                    self.cars.add(moved_car)                                             
                    self.steps += 1
                    move_made = True 

                elif direction == "right" and new_car.is_movable(direction, self.board):
                    moved_car = new_car.move_right()                                                         
                    self.cars.remove(new_car)
                    self.cars.add(moved_car)                                             
                    self.steps += 1 
                    move_made = True

            if new_car.orientation == "V":
                direction = random.choice(["up", "down"])

                if direction == "up" and new_car.is_movable(direction, self.board):
                    moved_car = new_car.move_up()                                                         
                    self.cars.remove(new_car)
                    self.cars.add(moved_car)                                             
                    self.steps += 1
                    move_made = True 

                elif direction == "down" and new_car.is_movable(direction, self.board):
                    moved_car = new_car.move_down()                                                         
                    self.cars.remove(new_car)
                    self.cars.add(moved_car)                                             
                    self.steps += 1
                    move_made = True 

            if move_made:                
                self.board = self.get_updated_board(moved_car, old_column, old_row)                                                 

            if self.is_solved():                 
                print(f"It took {self.steps} steps to solve this game") 
                break

    def get_updated_board(self, moved_car: Car, old_column: int, old_row: int) -> npt.NDArray[np.str_]:

        new_column = moved_car.column
        new_row = moved_car.row       

        if moved_car.orientation == "H":
            if moved_car.length == 2:

                # Case car moved to the right 
                if new_column > old_column:
                    self.board[old_row][old_column] = "0" 
                    self.board[old_row][old_column + 2] = moved_car.name                     

                # Case if car moved to the left 
                elif new_column < old_column:
                    self.board[old_row][new_column + 2] = "0"
                    self.board[old_row][new_column] = moved_car.name 

            if moved_car.length == 3:

                # Case car moved to the right 
                if new_column > old_column:
                    self.board[old_row][old_column] = "0" 
                    self.board[old_row][old_column + 3] = moved_car.name 

                # Case car moved to the left 
                elif new_column < old_column:
                    self.board[old_row][new_column + 3] = "0"
                    self.board[old_row][new_column] = moved_car.name 

        if moved_car.orientation == "V":
            if moved_car.length == 2:

                # Case car moved down
                if new_row > old_row:
                    self.board[old_row][old_column] = "0" 
                    self.board[old_row + 2][old_column] = moved_car.name 

                # Case if car moved up
                elif new_row < old_row:
                    self.board[new_row + 2][old_column] = "0"
                    self.board[new_row][old_column] = moved_car.name 

            if moved_car.length == 3:

                # Case car moved down
                if new_row > old_row:
                    self.board[old_row][old_column] = "0" 
                    self.board[old_row + 2][old_column] = moved_car.name 

                # Case if car moved up
                elif new_row < old_row:
                    self.board[new_row + 2][old_column] = "0"
                    self.board[new_row][old_column] = moved_car.name    

        return self.board  

    def is_solved(self) -> bool: 
        
        for car in self.cars:
            winning_column = len(self.board) - 2 
            winning_row = ceil(len(self.board) / 2) - 1 
            if car.name == "X" and car.column == winning_column and car.row == winning_row:
                return True 

        return False                
        
    def step_count(self) -> int:
        return self.steps 
                 
