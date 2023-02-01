"""
Program: distancebestfrist.py

Course: Algoritmen en Heuristieken

Students: Issa Zouboye, Alex van Diepen, Shreyas Potdar

Description: This is a algorithm that uses the number of blocking cars as a heuristic
to solve a rush hour game.
"""
from __future__ import annotations
import numpy as np 
import copy 
from ..classes.board import Board
from ..classes.state import State
from collections import deque
from math import ceil 
import heapq
import time


class DistanceBestFirst:

    def __init__(self, first_state: State, size: int) -> None:
        """
        Initializes the first board, a visited set, the amount of steps
        and a priority queue
        """
        # stores first board
        self.first_state = first_state
        # stores distance from red car to exit
        self.first_distance = first_state.reddistance()
        # stores size of board
        self.size = size
        # stores amount of steps 
        self.steps = 0

        # Initialize a queue 
        self.boards_queue = []

        # Initialize a set to keep up the board states already visited 
        self.visited = set()        
        
        # Put first state in queue
        self.boards_queue.append((self.first_distance, self.steps, self.first_state))
        heapq.heapify(self.boards_queue)

        # Add first state to visited set 
        self.visited.add(first_state) 
    
    def run(self) -> State:
        """
        Initializes the first board, a visited set, the amount of steps
        and a priority queue on distance from the exit for the red car
        """
        while len(self.boards_queue) != 0 :
            # Pops and stores distance red car to exit, steps and the board
            distance, self.steps, board = heapq.heappop(self.boards_queue)  
                         

            # If board is solved return result
            if board.is_solved():
                print(f"It took {self.steps} steps to solve this game") 
                return board 

            # Add all possible next boards to queue, if they're not in visited set 
            
            next_configurations = board.get_next_configurations()

            for configuration in next_configurations:
                # stores new board configuration
                next_board = State(configuration, self.size)
                # stores distance and steps combined
                distance = next_board.reddistance() + self.steps

                if next_board not in self.visited:
                    # pushes the new board in a priority queue
                    heapq.heappush(self.boards_queue, (distance, self.steps + 1, next_board))
                    # puts new board in visited set``
                    self.visited.add(next_board) 
            

