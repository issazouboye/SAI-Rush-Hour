"""
Program: breadth_first.py

Course: Algoritmen en Heuristieken

Students: Issa Zouboye, Alex van Diepen, Shreyas Potdar

Description: This is a program that implements the breadth-first
algorithm to solve a rush hour game
"""

from __future__ import annotations 
from ..classes.state import State 
from collections import deque
from typing import List, Deque


class BreadthFirst:    

    def __init__(self, first_state: State, size: int) -> None:
        """
        Takes an unsolved board with size as arguments. To solve the Rush Hour game,
        it makes use of a queue, a set to track the visited states and a dictionary if you want to backtrace 
        the taken path (e.g. for visualization purposes).   
        """

        self.first_state = first_state
        
        # Stores the size of the board
        self.size = size 

        # A variable to keep track of all the steps taken
        self.steps = 0

        # Initialize a queue 
        self.boards_queue: Deque[State] = deque()

        # Initialize a set to keep up the board states already visited 
        self.visited = set()  

        # Initialize a dictionary for path 
        self.path: dict[State, State] = {}    
        
        # Put first state in queue
        self.boards_queue.append(first_state)

        # Add first state to visited set 
        self.visited.add(first_state) 

        # Add first state to path dictionary  
        self.path[first_state] = 0 
    
    def run(self) -> State:
        """
        A function that initializes the first state of the rush hour game
        and the required variables to properly keep track of the solved rush
        hour state such as the stack, set and dictionary.
        """

        # Algorithm that runs until the stack is empty or a solution is found
        while len(self.boards_queue) != 0:
            for depth in range(len(self.boards_queue)):

                # Pop new board 
                new_board = self.boards_queue.popleft()                

                # If board is solved return result
                if new_board.is_solved():                    
                    return new_board

                # Add all possible next boards to queue, if they're not in visited set       
                for configuration in new_board.get_next_configurations():
                    next_state = State(configuration, self.size)

                    if next_state not in self.visited:     
                        # Next board put into the queue
                        self.boards_queue.append(next_state)

                        # Next board put into the visited set
                        self.visited.add(next_state) 
                        
                        # Includes the next board state in the dictionary, with the its parent state as value           
                        self.path[next_state] = new_board 
            
            self.steps += 1  