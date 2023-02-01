"""
Program: depthfirst.py

Course: Algoritmen en Heuristieken

Students: Issa Zouboye, Alex van Diepen, Shreyas Potdar

Description: This is a program that implements the depth-first
algorithm to solve a rush hour game
"""

from __future__ import annotations
from ..classes.state import State
from typing import List, Union


class Depthfirst:

    def __init__(self, cars_set: State, size: int) -> None:
        """       
        Takes an unsolved board with size as arguments. To solve the Rush Hour game,
        it makes use of a stack, a set to track the visited states and a dictionary if you want to backtrace 
        the taken path. 
        """

        # Stores the intial state of the rush hour configuration
        self.cars_set = cars_set

        # Stores the size of the board
        self.size = size

        # Dictionary to keep track of each state's depth level and previous state
        self.archive: dict[State, List[Union[State, 0], int]] = {}
        self.archive[cars_set] = [0, 0]

        # Initializes a stack and includes the initial state in the stack
        self.stack = []
        self.stack.append(cars_set)

        # Initializes a set to keep up the board states already visuted
        self.visitedset = set()
        
        # Including the initial state in the set
        self.visitedset.add(cars_set)

        # variable to keep track of the depth level of a solved rush hour state
        self.current_best: int = float('inf')

    def solve_board(self) -> State:
        """
        A function that implements the depth-first algorithm to find a solution
        to the rush hour game
        """

        # Alrgorithm that runs until the stack is empty or a solution is found
        while len(self.stack) != 0:
            # Removal of the top most board configuration from the stack
            new_state = self.stack.pop()

            # Checks if the board is solved, if so the result is returned
            if new_state.is_solved():
                return self.archive[new_state][1]   
            
            # If the board is not solved, all potential configurations are added to the stack
            for potential_moves in new_state.get_next_configurations():
                # A new board state is created based on the potential configurations
                following_state = State(potential_moves, self.size)

                if following_state not in self.visitedset:  
                    # Includes the new board state in the dictionary, with the its parent state and depth level as value           
                    self.archive[following_state] = [new_state, self.archive[new_state][1]+1]
                    
                    # New board put into the stack
                    self.stack.append(following_state)

                    # New board put into the visited set
                    self.visitedset.add(following_state)
   
    def backtrace(self, end_board: State) -> List[State]:
        """
        A function that shows keeps track of all of the steps taken for the depth first
        algorithm.
        """
        boardslist = [end_board]

        while boardslist[-1] != 0:
            boardslist.append(self.archive[boardslist[-1]][0])

        boardslist.pop()
        boardslist.reverse()

        return boardslist

    def visited_states(self) -> int:
        """  
        Returns the the amount of visited states.
        """
        return len(self.visitedset)       