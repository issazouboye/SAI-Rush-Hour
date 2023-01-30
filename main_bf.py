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

if __name__ == "__main__":

    start = time.time()
    initial_board = Board(6)
    initial_board.load_board("data/Rushhour6x6_1.csv") 
    initial_cars = initial_board.get_initial_cars()

    first_state = State(initial_cars, 6) 
    bf = BlockingDistanceBestFirst(first_state, 6) 
    bf.run()
    print(len(bf.visited))

    print(time.time() - start)

    # with open('board1.csv', 'w') as f:
    #     writer = csv.writer(f)
    #     row = ["algorithm", "visited boards", "number of steps"]
    #     writer.writerow(row)
    #     algorithmlist = ["Random","BreadthFirst", "DepthFirst", "BlockingCars", "Distance", "Branch and Bound"]
    #     randomlist = []
    #     breadthfirstlist = []
    #     depthfirstlist = []
    #     blockingcarslist = []
    #     distancelist = []
    #     branchandboundlist = []
    
    #     first_state = State(initial_cars, 6) 
    #     bf = BlockingBestFirst(first_state, 6)
    #     random = Random_solver_v2(first_state)
    #     for i in range(3):
    #         newbf = copy.deepcopy(bf)
    #         newrandom = copy.deepcopy(random)
    #         newbf.run()
    #         newrandom.run()
    #         # randomlist.append(Random.visitedboards())
    #         breadthfirstlist.append(len(bf.visited))
    #         breadthfirstlist.append(bf.steps)
    #         randomlist.append(random.step_count())

        
        
        
    #     print(breadthfirstlist)
    #     print(randomlist)
    #     visitedboards = [5,6,7,8,9]
    #     steps = [1,2,3,4,5] 
    #     for i in range(5):
    #         rowvar = [algorithmlist[i],visitedboards[i], steps[i]]
    #         writer.writerow(rowvar)

