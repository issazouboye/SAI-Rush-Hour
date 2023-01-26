from __future__ import annotations 
from board import Board 
from collections import deque
import time
from state import State 


class BreadthFirst:

    def __init__(self, first_state: State, size):
        self.first_state = first_state
        self.size = size 
        self.steps = 0

        # Initialize a queue 
        self.boards_queue = deque()

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
    
    def run(self):

        while len(self.boards_queue) != 0 :
            for depth in range(len(self.boards_queue)):

                # Pop new board 
                new_board = self.boards_queue.popleft()                

                # If board is solved return result
                if new_board.is_solved():
                    print(f"It took {self.steps} steps to solve this game") 
                    return new_board

                # Add all possible next boards to queue, if they're not in visited set       
                for configuration in new_board.get_next_configurations():
                    next_state = State(configuration, self.size)

                    if next_state not in self.visited:                    
                        self.boards_queue.append(next_state)
                        self.visited.add(next_state) 
                        self.path[next_state] = new_board 
            
            self.steps += 1


if __name__ == "__main__":

    start = time.time()

    initial_board = Board(6)
    initial_board.load_board("Rushhour6x6_1.csv") 
    initial_cars = initial_board.get_initial_cars()

    first_state = State(initial_cars, 6) 
    bf = BreadthFirst(first_state, 6) 
    bf.run()

    print(time.time() - start)
    