from code.classes.board import Board
from code.classes.state import State
from code.algorithms.breadth_first import BreadthFirst 
from code.algorithms.blockingbestfirst import BlockingBestFirst
from code.algorithms.randomise import Random_solver_v2


import time 
import csv 
import copy

if __name__ == "__main__":

    start = time.time()
    initial_board = Board(6)
    initial_board.load_board("data/Rushhour6x6_1.csv") 
    initial_cars = initial_board.get_initial_cars()

    # first_state = State(initial_cars, 6) 
    # bf = BreadthFirst(first_state, 6) 
    # bf.run()

    print(time.time() - start)

    with open('board1.csv', 'w') as f:
        writer = csv.writer(f)
        row = ["algorithm", "visited boards", "number of steps"]
        writer.writerow(row)
        algorithmlist = ["Random","BreadthFirst", "DepthFirst", "BlockingCars", "Distance", "Branch and Bound"]
        randomlist = []
        breadthfirstlist = []
        depthfirstlist = []
        blockingcarslist = []
        distancelist = []
        branchandboundlist = []
        
        for i in range(10):
            first_state = State(initial_cars, 6) 
            bf = BlockingBestFirst(first_state, 6) 
            random = Random_solver_v2(first_state)
            bf.run()
            random.run()
            # randomlist.append(Random.visitedboards())
            breadthfirstlist.append(len(bf.visited))
            breadthfirstlist.append(bf.steps)
            randomlist.append(Random_solver_v2.step_count)

        
        
        
        print(BreadthFirstlist)
        visitedboards = [5,6,7,8,9]
        steps = [1,2,3,4,5] 
        for i in range(5):
            rowvar = [algorithmlist[i],visitedboards[i], steps[i]]
            writer.writerow(rowvar)

