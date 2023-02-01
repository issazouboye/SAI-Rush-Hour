"""
Program: experiment.py

Course: Algoritmen en Heuristieken

Students: Issa Zouboye, Alex van Diepen, Shreyas Potdar

Description: This is a program that runs algorithms and heuristics 
on boards of choice
"""
import numpy as np
from ..classes.state import State
from ..classes.board import Board
from ..algorithms.randomise import Random_solver_v1
import csv


def get_data_board(filename, size):
    # Initialize board
    initial_board = Board(size)
    # Load board
    initial_board.load_board(filename)
    # Initialize cars
    initial_cars = initial_board.get_initial_cars()
    # Initialize first state
    initial_state = State(initial_cars, size) 
 
    # Solve the board
    data = Random_solver_v1(initial_state)
    end_state = data.run() 
    # Stores the end car locations
    end_cars = end_state.get_cars()  

    return initial_cars, end_cars 
                 
if __name__ == "__main__":

    # Store initial_cars and end_cars
    initial_cars, end_cars = get_data_board("data/Rushhour6x6_1.csv", 6)
    begincarlist = []
    for i in initial_cars:
        # If orientation is horizontal
        if i.orientation == "H":
            # Add column to list
            begincarlist.append(i.column)
        # If orientation is vertical
        if i.orientation == "V":
            # Add row to list
            begincarlist.append(i.row)
        
    endcarorientation = []
    for i in end_cars:
        # If orientation is horizontal
        if i.orientation == "H":
            # Add column to the list
            endcarorientation.append(i.column)
        # If orientation is vertical
        if i.orientation == "V":
            # Add row to the list
            endcarorientation.append(i.row)

    movement = []
    for i,j in zip(begincarlist, endcarorientation):
        # Add movement to the list
        movement.append(j-i)

    # Open csv file
    with open("output1.csv", 'w') as f:
        writer = csv.writer(f)
        # Adds header to csv file
        row = ["car", "move"]
        writer.writerow(row)

        # Adds car and move to csv file
        for i in range(len(begincarlist)):
            row = [end_cars[i].name, movement[i]]
            writer.writerow(row)


    


    
    

        


    


