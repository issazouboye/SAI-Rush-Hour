"""
Program: blockingbestfrist.py

Course: Algoritmen en Heuristieken

Students: Issa Zouboye, Alex van Diepen, Shreyas Potdar

Description: This is a algorithm that uses the number of blocking cars as a heuristic
to solve a rush hour game.
"""
from __future__ import annotations
import numpy as np 
import copy 
from ..classes.state import State
from collections import deque
from math import ceil 
import heapq
import time
from typing import Optional


class BlockingBestFirst:

    def __init__(self, first_state: State, size: int) -> None:
        """
        Initializes the first board, a visited set, the amount of steps
        and a priority queue on number of cars that block the red car
        """
        # stores first board
        self.first_state = first_state
        # stores amount of blocking cars in first board
        self.first_score = first_state.blockingcars()
        # stores size of board
        self.size = size 
        # stores amount of steps
        self.steps = 0

        # Initialize a queue 
        self.boards_queue = []

        # Initialize a set to keep up the board states already visited 
        self.visited = set()        
        
        # Put first state in a priority queue
        self.boards_queue.append((self.first_score, self.steps, self.first_state))
        heapq.heapify(self.boards_queue)

        # Add first state to visited set 
        self.visited.add(first_state) 
    
    def run(self) -> State:
        """
        Makes the cars move using the blocking heuristic, 
        until winning board configuration is achieved
        """
        while len(self.boards_queue) != 0 :
            # Pops and stores amount of blocking cars, steps and the board
            blocks, self.steps, board = heapq.heappop(self.boards_queue)  
                         

            # If board is solved return result
            if board.is_solved():
                print(f"It took {self.steps} steps to solve this game") 
                return board 

            # Add all possible next boards to queue, if they're not in visited set 
            
            next_configurations = board.get_next_configurations()

            for configuration in next_configurations:
                # stores new board configuration
                next_board = State(configuration, self.size)
                # stores amount of blocking cars and steps combined
                blocks = next_board.blockingcars() + self.steps

                if next_board not in self.visited:
                    # pushes the new board in a priority queue
                    heapq.heappush(self.boards_queue, (blocks, self.steps + 1, next_board))
                    # puts new board in visited set
                    self.visited.add(next_board) 
            



    