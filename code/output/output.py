import numpy as np
from ..classes.state import State
from ..classes.board import Board
from ..algorithms.randomise import Random_solver_v1
import csv


def get_data_board(filename, size):
    initial_board = Board(size)
    initial_board.load_board(filename)
    initial_cars = initial_board.get_initial_cars()
    initial_state = State(initial_cars, size) 

    data = Random_solver_v1(initial_state)
    end_state = data.run() 
    end_cars = end_state.get_cars()  

    return initial_cars, end_cars 
                 
if __name__ == "__main__":

    initial_cars, end_cars = get_data_board("data/Rushhour6x6_1.csv", 6)
    begincarlist = []
    for i in initial_cars:
        if i.orientation == "H":
            begincarlist.append(i.column)
        if i.orientation == "V":
            begincarlist.append(i.row)
        
    endcarorientation = []
    for i in end_cars:
        if i.orientation == "H":
            endcarorientation.append(i.column)
        if i.orientation == "V":
            endcarorientation.append(i.row)

    movement = []
    for i,j in zip(begincarlist, endcarorientation):
        movement.append(j-i)

    with open("output1.csv", 'w') as f:
        writer = csv.writer(f)
        row = ["car", "move"]
        writer.writerow(row)

        for i in range(len(begincarlist)):
            row = [end_cars[i].name, movement[i]]
            writer.writerow(row)


    


    
    

        


    


