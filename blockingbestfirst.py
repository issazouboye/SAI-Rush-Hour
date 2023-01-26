from __future__ import annotations
import numpy as np 
import copy 
from board import Board
from collections import deque
from math import ceil 
import heapq
import time
from state import State

class BlockingBestFirst:

    def __init__(self, first_state: State, size):
        self.first_state = first_state
        self.first_score = first_state.blockingcars()
        self.size = size 
        self.steps = 0

        # Initialize a queue 
        self.boards_queue = []

        # Initialize a set to keep up the board states already visited 
        self.visited = set()        
        
        # Put first state in queue
        self.boards_queue.append((self.first_score, self.steps, self.first_state))
        heapq.heapify(self.boards_queue)

        # Add first state to visited set 
        self.visited.add(first_state) 
    
    def run(self):
        while len(self.boards_queue) != 0 :
            # Pop new board 
            blocks, steps, board = heapq.heappop(self.boards_queue)  
                         

            # If board is solved return result
            if board.is_solved():
                print(f"It took {steps} steps to solve this game") 
                return board 

            # Add all possible next boards to queue, if they're not in visited set 
            
            next_configurations = board.get_next_configurations()

            for configuration in next_configurations:
                next_board = State(configuration, self.size)
                blocks = next_board.blockingcars() + steps

                if next_board not in self.visited:
                                        
                    heapq.heappush(self.boards_queue, (blocks, steps + 1, next_board))
                    self.visited.add(next_board) 
            


if __name__ == "__main__":
    start = time.time()
    initial_board = Board(6)
    initial_board.load_board("Rushhour6x6_2.csv") 
    initial_cars = initial_board.get_initial_cars()

    first_state = State(initial_cars, 6) 
    bf = BlockingBestFirst(first_state, 6) 
    bf.run()
    print(time.time()- start)
    