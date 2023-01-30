"""
Program: depthfirst.py

Course: Algoritmen en Heuristieken

Students: Issa Zouboye, Alex van Diepen, Shreyas Potdar

Description: This is a program that implements the depth-first
algorithm to solve a rush hour game
"""
from __future__ import annotations

import sys
sys.path.append("..")
# from visualize import visualize
from ..classes.state import State
from ..classes.board import Board 
from typing import Optional, List


class Depthfirst:
    def __init__(self, cars_set: State, size: int) -> None:
        """
        A function that initializes the first state of the rush hour game
        and the required variables to properly keep track of the solved rush
        hour state such as the stack, set and dictionary.
        """

        # stores the intial state of the rush hour configuration
        self.cars_set = cars_set

        # stores the size of the board
        self.size = size

        # dictionary to keep track of each state's depth level and previous state
        self.archieve = {}
        self.archieve[cars_set] = [0, 0]

        # initializes a stack and includes the initial state in the stack
        self.stack = []
        self.stack.append(cars_set)

        # initializes a set to keep up the board states already visuted
        self.visitedset = set()
        
        #including the initial state in the set
        self.visitedset.add(cars_set)

        # variable to keep track of the depth level of a solved rush hour state
        self.current_best: int = float('inf')
        

    def solve_board(self) -> State:
        """
        A function that implements the depth-first algorithm to find a solution
        to the rush hour game
        """

        # alrgorithm that runs until the stack is empty or a solution is found
        while len(self.stack) != 0:
            # Removal of the top most board configuration from the stack
            new_state = self.stack.pop()

            # checks if the board is solved, if so the result is returned
            if new_state.is_solved():
                # print(f"It took {self.steps} steps to solve this game") 
                # print("hello")
                # print(self.archieve[new_state])

                return self.archieve[new_state][1]   
            
            # if the board is not solved, all potential configurations are added to the stack
            for potential_moves in new_state.get_next_configurations():
                # a new board state is created based on the potential configurations
                following_state = State(potential_moves, self.size)
                

                if following_state not in self.visitedset:  
                    # includes the new board state in the dictionary, with the its parent state and depth level as value           
                    self.archieve[following_state] = [new_state, self.archieve[new_state][1]+1]
                    
                    # new board put into the stack
                    self.stack.append(following_state)

                    # new board put into the visited set
                    self.visitedset.add(following_state)

   
    def backtrace(self, end_board: State) -> List[State]:
        boardslist = [end_board]

        while boardslist[-1] != 0:
            boardslist.append(self.archieve[boardslist[-1]][0])

        boardslist.pop()
        boardslist.reverse()
        print((boardslist[-1]))

        return boardslist


    def visited_states(self) -> int:
        return len(self.visitedset) 
    

                 
if __name__ == "__main__":
    initial_board = board.Board(6)
    initial_board.load_board("data\Rushhour6x6_1.csv")

    initial_cars = initial_board.get_initial_cars() 
    initial_board = initial_board.get_initial_board() 

    state_test = State(initial_cars, 6)
    df = Depthfirst(state_test, 6, 100)
    end_board = df.solve_board()
    df.backtrace(end_board)





                 


        

            

