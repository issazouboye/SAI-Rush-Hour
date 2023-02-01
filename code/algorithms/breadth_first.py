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
import time
from typing import Optional, List, Deque



class BreadthFirst:
    """
    A function that initializes the first state of the rush hour game
    and the required variables to properly keep track of the solved rush
    hour state such as the queue, set and dictionary.
    """

    def __init__(self, first_state: State, size: int) -> None:
        self.first_state = first_state
        
        # stores the size of the board
        self.size = size 

        # a variable to keep track of all the steps taken
        self.steps = 0

        # Initialize a queue 
        self.boards_queue: Deque[State] = deque()

        # Initialize a set to keep up the board states already visited 
        self.visited = set()  

        # Initialize a dictionary for path 
        self.path = {}    
        
        # Put first state in queue
        self.boards_queue.append(first_state)

        # Add first state to visited set 
        self.visited.add(first_state) 

        # Add first state to path dictionary  
        self.path[first_state] = 0 
    
    def run(self) -> Optional[State]:
        """
        A function that initializes the first state of the rush hour game
        and the required variables to properly keep track of the solved rush
        hour state such as the stack, set and dictionary.
        """

        # alrgorithm that runs until the stack is empty or a solution is found
        while len(self.boards_queue) != 0 :
            for depth in range(len(self.boards_queue)):

                # Pop new board 
                new_board = self.boards_queue.popleft()                

                # If board is solved return result
                if new_board.is_solved():
                    # print(f"It took {self.steps} steps to solve this game") 
                    return new_board

                # Add all possible next boards to queue, if they're not in visited set       
                for configuration in new_board.get_next_configurations():
                    next_state = State(configuration, self.size)

                    if next_state not in self.visited:     
                        # next board put into the queue
                        self.boards_queue.append(next_state)

                        # next board put into the visited set
                        self.visited.add(next_state) 
                        
                        # includes the next board state in the dictionary, with the its parent state as value           
                        self.path[next_state] = new_board 
            
            self.steps += 1



    