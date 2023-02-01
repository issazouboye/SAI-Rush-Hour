"""
Program: randomise.py

Course: Algoritmen en Heuristieken

Students: Issa Zouboye, Alex van Diepen, Shreyas Potdar

Description: This is a program that implements two different implemented
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
        """ 
        Takes an unsolved board as argument and randomly solves it 
        """        
        self.initial_state = initial_state    
        # Store steps    
        self.steps = 0                        
    
    def run(self) -> State:
        """  
        Runs the random solver 
        """                 
        # Store state
        new_state = self.initial_state 
        # Store size
        size = self.initial_state.get_size()

        while True:       
            # Choose random new board configuration 
            new_configuration = random.choice(new_state.get_next_configurations())    
            new_state = State(new_configuration, size)    
            # Count step 
            self.steps += 1 

            if new_state.is_solved(): 
                # Returns winning board             
                return new_state 
   
    def step_count(self) -> int:
        """ 
        Returns amount of steps
        """     
        return self.steps     
    

class Random_solver_v2:

    def __init__(self, initial_state: State) -> None:
        """  
        Takes an unsolved board as argument and randomly solves it 
        """
        
        # Store first state
        self.initial_state = initial_state
        # Store car objects
        self.cars = set(initial_state.get_cars())
        # Store board
        self.board = initial_state.get_board()
        # Store steps
        self.steps = 0      

    def run(self) -> None:  
        """  
        Runs the random solver 
        """    

        while True:     
            # Choose random car        
            new_car = random.choice(list(self.cars))   
            # Store new column        
            old_column = new_car.column
            # Store new row
            old_row = new_car.row   
            # Initialize move_made
            move_made = False          

            # If orientation is horizontal
            if new_car.orientation == "H":
                # Choose random direction
                direction = random.choice(["left", "right"])

                # If the car can move left
                if direction == "left" and new_car.is_movable(direction, self.board):
                    # Moves the car left
                    moved_car = new_car.move_left() 
                    # Remove old car location                                                        
                    self.cars.remove(new_car)
                    # Add new car location
                    self.cars.add(moved_car) 
                    # Count step                                            
                    self.steps += 1
                    move_made = True 
 
                # If the car can move right
                elif direction == "right" and new_car.is_movable(direction, self.board):
                    # Moves the car right
                    moved_car = new_car.move_right()
                    # Remove old car location                                                         
                    self.cars.remove(new_car)
                    # Add new car location
                    self.cars.add(moved_car)  
                    # Count step                                         
                    self.steps += 1 
                    move_made = True

            # If the car orientation is vertical
            if new_car.orientation == "V":
                # Choose random direction
                direction = random.choice(["up", "down"])

                # If the car can move up
                if direction == "up" and new_car.is_movable(direction, self.board):
                    # Moves the car up
                    moved_car = new_car.move_up() 
                    # Remove old car location                                                         
                    self.cars.remove(new_car)
                    # Add new car location
                    self.cars.add(moved_car) 
                    # Count step                                              
                    self.steps += 1
                    move_made = True 

                # If the car can move down
                elif direction == "down" and new_car.is_movable(direction, self.board):
                    # Moves the car down
                    moved_car = new_car.move_down()   
                    # Remove old location                                                      
                    self.cars.remove(new_car)
                    # Add new location
                    self.cars.add(moved_car) 
                    # Count step                                            
                    self.steps += 1
                    move_made = True 

            if move_made:  
                # Stores new board configuration              
                self.board = self.get_updated_board(moved_car, old_column, old_row)                                                 

            if self.is_solved():          
                break

    def get_updated_board(self, moved_car: Car, old_column: int, old_row: int) -> npt.NDArray[np.str_]:
        """   
        Function that updates the board based on the moved car and the old coordinates of the moved car 
        """
 
        # Stores column
        new_column = moved_car.column
        # Stores row
        new_row = moved_car.row       

        # If the cars orientation is horizontal
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

        # If the cars orientation is vertical
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
        """  
        Checks if the board is solved 
        """
        
        # For every car object in the set of cars
        for car in self.cars:
            # Stores winning column in board
            winning_column = len(self.board) - 2 
            # Stores winning row in board
            winning_row = ceil(len(self.board) / 2) - 1 
            # If the red car is at the exit
            if car.name == "X" and car.column == winning_column and car.row == winning_row:
                return True 

        return False                
        
    def step_count(self) -> int:   
        """ 
        Returns amount of steps
        """         
        return self.steps 
                 
