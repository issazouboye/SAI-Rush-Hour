from code.classes.board import Board
from code.classes.state import State
from code.algorithms.breadth_first import BreadthFirst 
from code.algorithms.blockingbestfirst import BlockingBestFirst
from code.algorithms.distancebestfirst import DistanceBestFirst
from code.algorithms.blockingdistancebestfirst import BlockingDistanceBestFirst
from code.algorithms.randomise import Random_solver_v2, Random_solver_v1
from code.algorithms.depthfirst import Depthfirst
from code.algorithms.pruning import Pruning

import numpy as np 
import random 
import matplotlib.pyplot as plt
import time 
import csv 
import copy

def boardcsv(filename, boardname, size, randomcount):

    start = time.time()
    initial_board = Board(size)
    initial_board.load_board(filename) 
    initial_cars = initial_board.get_initial_cars()
    print(time.time() - start)

    with open(boardname, 'w') as f:
        writer = csv.writer(f)
        row = ["algorithm", "visited boards", "number of steps", "best solution"]
        writer.writerow(row)
        algorithmlist = ["Random", "BreadthFirst", "BlockingBestFirst", "DistanceBestFirst", "BlockingDistanceBestFirst", "DepthFirst", "DepthFirstPruning"]
        randomlist = []
        first_state = State(initial_cars, size) 
        random = Random_solver_v2(first_state)
        for i in range(randomcount):
            
            newrandom = copy.deepcopy(random)
            newrandom.run()
            randomlist.append(newrandom.step_count())
            
        bf = BreadthFirst(first_state, size)
        bf.run()
        bc = BlockingBestFirst(first_state, size)
        bc.run()
        dc = DistanceBestFirst(first_state, size)
        dc.run()
        bdc = BlockingDistanceBestFirst(first_state, size)
        bdc.run()

        df = Depthfirst(first_state, size)
        dfsteps = df.solve_board()

        pru = Pruning(first_state, size)
        prusteps = pru.solve_board

        
        
        randomlist.sort()
        visitedboards = [sum(randomlist)/randomcount, len(bf.visited), len(bc.visited), len(dc.visited), len(bdc.visited), df.visited_states(), pru.visited_states()]
        steps = [sum(randomlist)/randomcount, bf.steps, bc.steps, dc.steps, bdc.steps, df.solve_board(), pru.solve_board()] 
        bestvalue = [randomlist[0], bf.steps, bc.steps, dc.steps, bdc.steps, df.solve_board(), pru.solve_board()]
        for i in range(7):
            rowvar = [algorithmlist[i],visitedboards[i], steps[i], bestvalue[i]]
            writer.writerow(rowvar)
       
        bins=np.arange(0, 50000, 500)
        plt.hist(randomlist, color = "lightblue", edgecolor='black', bins = bins)
        plt.title('Rush Hour Board 1')
        plt.xlabel('Amount of Steps To Solve')
        plt.ylabel('Frequency')
        plt.savefig('Experiment_1000_board_1.png')

boardcsv("data/Rushhour6x6_1.csv", "boardscsv/board1.csv", 6, 1000)