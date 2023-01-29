import numpy as np 
import copy 
from collections import deque
from math import ceil 
from visualize import visualize
from state import State
from board import Board


class BreadthFirstPath:

    def __init__(self, first_state: State, size):
        self.first_state = first_state
        self.size = size 
        self.steps = 0
        self.archive = {}

        # Initialize a queue 
        self.boards_queue = deque()

        # Initialize a set to keep up the board states already visited 
        self.visited = set()        
        
        # Put first state in queue
        self.boards_queue.append(first_state)

        # Add first state to visited set 
        self.visited.add(first_state) 
    
    def run(self):

        self.archive[first_state] = 0
        while len(self.boards_queue) != 0 :
            for depth in range(len(self.boards_queue)):

                # Pop new board 
                new_board = self.boards_queue.popleft()                

                # If board is solved return result
                if new_board.is_solved():
                    print(f"It took {self.steps} steps to solve this game") 
                    return new_board, self.archive

                # Add all possible next boards to queue, if they're not in visited set 
                
                next_configurations = new_board.get_next_configurations()

                for configuration in next_configurations:
                    next_board = State(configuration, self.size)

                    if next_board not in self.visited:                   
                        self.archive[next_board] = new_board
                        self.boards_queue.append(next_board)
                        self.visited.add(next_board) 
            
            self.steps += 1

def backtrace(archive, end_board):
    boardslist = [end_board]

    while boardslist[-1] != 0:
        boardslist.append(archive[boardslist[-1]])

    boardslist.pop()
    boardslist.reverse()
    boardslist

    return boardslist


if __name__ == "__main__":

    initial_board = Board(6)
    initial_board.load_board("Rushhour6x6_1.csv") 
    initial_cars = initial_board.get_initial_cars()

    first_state = State(initial_cars, 6) 
    bf = BreadthFirstPath(first_state, 6) 
    end_board, archive = bf.run() 
    stateslist = backtrace(archive, end_board)
    boardslist = []
    for i in stateslist:
        boardslist.append(i.board)
    visualize(boardslist, saveplot=True)
    