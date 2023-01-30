from code.classes.board import Board
from code.classes.state import State
from code.algorithms.breadth_first import BreadthFirst 
from code.algorithms.blockingbestfirst import BlockingBestFirst
from code.algorithms.distancebestfirst import DistanceBestFirst
from code.algorithms.blockingdistancebestfirst import BlockingDistanceBestFirst
from code.algorithms.randomise import Random_solver_v2
from code.algorithms.depthfirst import Depthfirst
from code.algorithms.branch_and_bound import Branchandbound


import time 
import csv 
import copy

if __name__ == "__main__":

    start = time.time()
    initial_board = Board(6)
    initial_board.load_board("data/Rushhour6x6_1.csv") 
    initial_cars = initial_board.get_initial_cars()

    first_state = State(initial_cars, 6) 
    df = Depthfirst(first_state, 6) 

    bab = Branchandbound(first_state, 6)

    print(df.solve_board())
    print((df.visited_states()))
    
    print(bab.solve_board_branch_bound())
    print((bab.visited_states()))

    

    print(time.time() - start)


