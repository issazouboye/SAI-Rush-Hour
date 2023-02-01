"""
Program: experiment.py

Course: Algoritmen en Heuristieken

Students: Issa Zouboye, Alex van Diepen, Shreyas Potdar

Description: This is a program that runs algorithms and heuristics 
on boards of choice
"""
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
    """
    Function that creates csv file for solutions for 
    multiple algorithms, creates histogram for random algorithm
    """

    # Initializes baord
    initial_board = Board(size)
    # Loads board
    initial_board.load_board(filename) 
    # Initializes cars
    initial_cars = initial_board.get_initial_cars()

    # Opens csv file
    with open(boardname, 'w') as f:
        writer = csv.writer(f)
        row = ["algorithm", "visited boards", "number of steps", "best solution"]
        # Adds row to csv file
        writer.writerow(row)
        algorithmlist = ["Random", "BreadthFirst", "BlockingBestFirst", "DistanceBestFirst", "BlockingDistanceBestFirst", "DepthFirst", "DepthFirstPruning"]
        randomlist = []
        # Creates first state
        first_state = State(initial_cars, size) 
        random = Random_solver_v2(first_state)
        for i in range(randomcount):
            # Runs random algorithm
            newrandom = copy.deepcopy(random)
            newrandom.run()
            randomlist.append(newrandom.step_count())
            
        # Runs breadthfirst algorithm
        bf = BreadthFirst(first_state, size)
        bf.run()
        # Runs blockingcars heuristic
        bc = BlockingBestFirst(first_state, size)
        bc.run()
        # Runs distance heuristic
        dc = DistanceBestFirst(first_state, size)
        dc.run()
        # Runs blockingdistance heuristic
        bdc = BlockingDistanceBestFirst(first_state, size)
        bdc.run()
        # Runs depthfirst algorithm
        df = Depthfirst(first_state, size)
        dfsteps = df.solve_board()
        # Runs depthfirst pruning algorithm
        pru = Pruning(first_state, size)
        prusteps = pru.solve_board

        # Sorts randomlist
        randomlist.sort()
        # Adds amount of visited board per algorithm
        visitedboards = [sum(randomlist)/randomcount, len(bf.visited), len(bc.visited), len(dc.visited), len(bdc.visited), df.visited_states(), pru.visited_states()]
        # Adds amount of steps per algorithm
        steps = [sum(randomlist)/randomcount, bf.steps, bc.steps, dc.steps, bdc.steps, df.solve_board(), pru.solve_board()] 
        # Adds smallest solution per algorithm
        bestvalue = [randomlist[0], bf.steps, bc.steps, dc.steps, bdc.steps, df.solve_board(), pru.solve_board()]
        # Adds results to csv file
        for i in range(7):
            rowvar = [algorithmlist[i],visitedboards[i], steps[i], bestvalue[i]]
            writer.writerow(rowvar)
       
        # Creates histogram for random algorithm
        bins=np.arange(0, 50000, 500)
        plt.hist(randomlist, color = "lightblue", edgecolor='black', bins = bins)
        plt.title('Rush Hour Board 1')
        plt.xlabel('Amount of Steps To Solve')
        plt.ylabel('Frequency')
        plt.savefig('Experiment_1000_board_1.png')

