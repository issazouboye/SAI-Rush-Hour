"""
Program: pruning.py

Course: Algoritmen en Heuristieken

Students: Issa Zouboye, Alex van Diepen, Shreyas Potdar

Description: This is a program that implements the branch
and bound algorithm to solve a rush hour game
"""

from __future__ import annotations
from ..classes.state import State
from typing import List


class Pruning:

    def __init__(self, cars_set: State, size: int) -> None:
        """
        A function that initializes the first state of the rush hour game
        and the required variables to properly keep track of the solved rush
        hour state such as the stack, set and dictionary.
        """

        # Stores the intial state of the rush hour configuration
        self.cars_set = cars_set

        # Stores the size of the board
        self.size = size

        # Dictionary to keep track of each state's depth level and previous state
        self.archive = {}
        self.archive[cars_set] = [0, 0]

        # Initializes a stack and includes the initial state in the stack
        self.stack = []
        self.stack.append(cars_set)

        # Initializes a set to keep up the board states already visuted
        self.visitedset = set()
        
        # Including the initial state in the set
        self.visitedset.add(cars_set)

        # Variable to keep track of the depth level of a solved rush hour state
        self.current_best: int = float('inf')
            
    def solve_board(self) -> int:
        """
        A function that implements the branch and bound algorithm which is
        similar to the depth first implementation however in this case there 
        is a constant check to see whether the depth level of a current board is
        smaller than its parent state. 
        """

        # Alrgorithm that runs until the stack is empty and returns the solution
        while (len(self.stack) != 0):
            new_state = self.stack.pop()
            
            # Checks if the board is solved, if so the current depth level of solution is updated
            if new_state.is_solved():
                self.current_best = self.archive[new_state][1]
    
            for potential_moves in new_state.get_next_configurations():
                # A new board state is created based on the potential configurations
                following_state = State(potential_moves, self.size)

                # Only if new state is not in the set or if its depth level exceeds the current solution, parameters are updated
                if following_state in self.visitedset or self.archive[new_state][1] >= self.current_best - 1:
                    pass
                else:
                    # Includes the new board state in the dictionary, with the its parent state and depth level as value           
                    self.archive[following_state] = [new_state, self.archive[new_state][1]+1]
                    
                    # New board put into the stack                   
                    self.visitedset.add(following_state)
                    
                    # New board put into the visited set
                    self.stack.append(following_state)

        return self.current_best

    def visited_states(self) -> int:
        """  
        Returns the the amount of visited states.
        """
        return len(self.visitedset)

