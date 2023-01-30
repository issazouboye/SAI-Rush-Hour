from code.classes.board import Board
from code.classes.state import State
from code.algorithms.breadth_first import BreadthFirst 
from code.algorithms.blockingbestfirst import BlockingBestFirst
from code.algorithms.distancebestfirst import DistanceBestFirst
from code.algorithms.blockingdistancebestfirst import BlockingDistanceBestFirst
from code.algorithms.randomise import Random_solver_v2


import time 
import csv 
import copy

def boardcsv():

    start = time.time()
    initial_board = Board(6)
    initial_board.load_board("data/Rushhour6x6_1.csv") 
    initial_cars = initial_board.get_initial_cars()

    # first_state = State(initial_cars, 6) 
    # bf = BlockingDistanceBestFirst(first_state, 6) 
    # bf.run()
    # print(len(bf.visited))

    print(time.time() - start)

    with open('boardscsv/board1.csv', 'w') as f:
        writer = csv.writer(f)
        row = ["algorithm", "visited boards", "number of steps", "best solution"]
        writer.writerow(row)
        algorithmlist = ["Random","BreadthFirst", "DepthFirst", "BlockingCars", "Distance", "Branch and Bound"]
        randomlist = []
        breadthfirstlist = []
        depthfirstlist = []
        blockingcarslist = []
        distancelist = []
        branchandboundlist = []

        # bf = BlockingBestFirst(first_state, 6)
        first_state = State(initial_cars, 6) 
        random = Random_solver_v2(first_state)
        for i in range(10):
            
            newrandom = copy.deepcopy(random)
            newrandom.run()
            randomlist.append(newrandom.step_count())
            

        
        
        randomlist.sort()
        visitedboards = [sum(randomlist)/10,6,7,8,9]
        steps = [sum(randomlist)/10,2,3,4,5] 
        bestvalue = [randomlist[0], 2, 3, 4, 5]
        for i in range(5):
            rowvar = [algorithmlist[i],visitedboards[i], steps[i], bestvalue[i]]
            writer.writerow(rowvar)

boardcsv()