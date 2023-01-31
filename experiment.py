from code.classes.board import Board
from code.classes.state import State
from code.algorithms.breadth_first import BreadthFirst 
from code.algorithms.blockingbestfirst import BlockingBestFirst
from code.algorithms.distancebestfirst import DistanceBestFirst
from code.algorithms.blockingdistancebestfirst import BlockingDistanceBestFirst
from code.algorithms.randomise import Random_solver_v2
from code.algorithms.depthfirst import Depthfirst
from code.algorithms.branch_and_bound import Branchandbound

import numpy as np 
import random 
import matplotlib.pyplot as plt
import time 
import csv 
import copy

def boardcsv():

    start = time.time()
    initial_board = Board(9)
    initial_board.load_board("data/Rushhour9x9_4.csv") 
    initial_cars = initial_board.get_initial_cars()

    # first_state = State(initial_cars, 6) 
    # bf = BlockingDistanceBestFirst(first_state, 6) 
    # bf.run()
    # print(len(bf.visited))

    print(time.time() - start)

    with open('boardscsv/board4.csv', 'w') as f:
        writer = csv.writer(f)
        row = ["algorithm", "visited boards", "number of steps", "best solution"]
        writer.writerow(row)
        algorithmlist = ["Random","BreadthFirst", "DepthFirst", "BlockingCars", "Distance", "Branch and Bound"]
        randomlist = []
        depthfirstlist = []
        blockingcarslist = []
        distancelist = []
        branchandboundlist = []

        # bf = BlockingBestFirst(first_state, 6)
        first_state = State(initial_cars, 9) 
        random = Random_solver_v2(first_state)
        for i in range(1000):
            
            newrandom = copy.deepcopy(random)
            newrandom.run()
            randomlist.append(newrandom.step_count())
            
        bf = BreadthFirst(first_state, 9)
        bf.run()
        bc = BlockingBestFirst(first_state, 9)
        bc.run()
        dc = DistanceBestFirst(first_state, 9)
        dc.run()

        df = Depthfirst(first_state, 9)
        dfsteps = df.solve_board()

        bab = Branchandbound(first_state, 9)
        babsteps = bab.solve_board_branch_bound()

        
        
        randomlist.sort()
        visitedboards = [sum(randomlist)/1000, len(bf.visited),df.visited_states(),len(bc.visited),len(dc.visited), bab.visited_states()]
        steps = [sum(randomlist)/1000,bf.steps,dfsteps,bc.steps,dc.steps, babsteps] 
        bestvalue = [randomlist[0], bf.steps, dfsteps, bc.steps, dc.steps, babsteps]
        for i in range(6):
            rowvar = [algorithmlist[i],visitedboards[i], steps[i], bestvalue[i]]
            writer.writerow(rowvar)
       
        bins=np.arange(0, 50000, 500)
        plt.hist(randomlist, color = "lightblue", edgecolor='black', bins = bins)
        plt.title('Amount of steps to solve 9x9 Rush Hour Board')
        plt.xlabel('Amount of Steps')
        plt.ylabel('Frequencey')
        plt.savefig('Experiment_10000_board_4.png')

boardcsv()