"""
Program: blockingbestfrist.py

Course: Algoritmen en Heuristieken

Students: Issa Zouboye, Alex van Diepen, Shreyas Potdar

Description: This is a algorithm that uses the number of blocking cars as a heuristic
to solve a rush hour game.
"""

from __future__ import annotations
from ..classes.state import State
from collections import deque
import heapq


class BlockingDistanceBestFirst:

    def __init__(self, first_state: State, size: int) -> None:
        """
        Takes an unsolved board with the size as arguments. Initializes a visited set, the amount of steps
        and a priority queue where the states that have the least amount of cars blocking the red car in 
        combination with the shortest distance of the red car to the exit will leave the queue first. 
        """
        # Stores first board
        self.first_state = first_state
        # Stores amount of blocking cars in first board
        self.first_score = first_state.blockingdistance()
        # Stores size of board
        self.size = size 
        # Stores amount of steps
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
        while len(self.boards_queue) != 0:
            # Pops and stores amount of blocking cars, steps and the board
            blockingdist, self.steps, board = heapq.heappop(self.boards_queue)  
                         
            # If board is solved return result
            if board.is_solved():                
                return board 

            # Add all possible next boards to queue, if they're not in visited set 
            
            next_configurations = board.get_next_configurations()

            for configuration in next_configurations:
                # Stores new board configuration
                next_board = State(configuration, self.size)
                # Stores amount of blocking cars and steps combined
                blockingdist = next_board.blockingdistance() + self.steps

                if next_board not in self.visited:
                    # Pushes the new board in a priority queue
                    heapq.heappush(self.boards_queue, (blockingdist, self.steps + 1, next_board))
                    # Puts new board in visited set
                    self.visited.add(next_board)             