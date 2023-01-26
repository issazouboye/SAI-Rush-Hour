# Depth First Search Algorithm
from __future__ import annotations
# from visualize import visualize
from ..classes.car import Car
from ..classes.board import Board
from ..classes.state import State
import copy 


class Depthfirst:
    def __init__(self, cars_set: State, size: int, max_height: int):
        self.cars_set = cars_set
        self.size = size

        self.max_height = max_height

        self.archieve = {}
        self.archieve[cars_set] = [0, 0]

        self.stack = []
        self.stack.append(cars_set)

        self.visitedset = set()
        self.visitedset.add(cars_set)

        self.current_best = float('inf')
        

    def solve_board(self):

         while len(self.stack) != 0:
            new_state = self.stack.pop()

            # if self.archieve[new_state][1] > self.max_height:
            if new_state.is_solved():
                print(f"It took {self.steps} steps to solve this game") 
                print("hello")
                print(self.archieve[new_state])
                return new_state 
            
            else:
                for potential_moves in new_state.get_next_configurations():
                    following_state = State(potential_moves, self.size)
                    
                    if following_state in self.visitedset:
                        pass

                    else:
                        self.archieve[following_state] = [new_state, self.archieve[new_state][1]+1]
                        self.stack.append(following_state)
                        self.visitedset.add(following_state)

    def solve_board_branch_bound(self):

        while (len(self.stack) != 0):
            new_state = self.stack.pop()
            # self.steps += 1
            # while self.archieve[new_state][1] < self.max_height:

            if new_state.is_solved():
                # print(self.archieve[new_state][0])
                self.current_best = self.archieve[new_state][1]
                # print(self.current_best)
                # return new_state
                # # if current_best < 100:
                # #     return new_state 
            
            else:
                for potential_moves in new_state.get_next_configurations():
                    following_state = State(potential_moves, self.size)

                    if following_state in self.visitedset or self.archieve[new_state][1] >= self.current_best - 1:
                        pass

                    else:
                        self.archieve[following_state] = [new_state, self.archieve[new_state][1]+1]
                        self.visitedset.add(following_state)
                        self.stack.append(following_state)
            # new_state = self.stack.pop()
        print(self.current_best)
        return self.current_best

    def backtrace(self, end_board):
        boardslist = [end_board]

        while boardslist[-1] != 0:
            boardslist.append(self.archieve[boardslist[-1]][0])

        boardslist.pop()
        boardslist.reverse()
        print((boardslist[-1]))

        return boardslist


    def get_end_board(self):
        return self.end_board 
    

                 
if __name__ == "__main__":
    initial_board = Board(6)
    initial_board.load_board("Rushhour6x6_1.csv")

    initial_cars = initial_board.get_initial_cars() 
    initial_board = initial_board.get_initial_board() 

    state_test = State(initial_cars, 6)
    df = Depthfirst(state_test, 6, 100)
    end_board = df.solve_board()
    df.backtrace(end_board)





                 


        

            

