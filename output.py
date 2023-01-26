import numpy as np
# from car import Car
import copy 
from math import ceil
import random  
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from visualize import visualize



                 
if __name__ == "__main__":

    initial_board = Board(6)
    initial_board.load_board("Rushhour6x6_1.csv")

    initial_cars = initial_board.get_initial_cars() 
    initial_board = initial_board.get_initial_board() 

    random_solver = Random_solver(initial_cars, initial_board) 
    random_solver.solve_board()

    end_cars = random_solver.get_end_cars()
    end_board = random_solver.get_end_board()
        
    begincarlist = []
    for i in initial_cars:
        if i.orientation == "H":
            begincarlist.append(i.column)
        if i.orientation == "V":
            begincarlist.append(i.row)
        
    end_cars.sort(key=lambda x: x.name)
    endcarorientation = []
    for i in end_cars:
        if i.orientation == "H":
            endcarorientation.append(i.column)
        if i.orientation == "V":
            endcarorientation.append(i.row)

    movement = []
    for i,j in zip(begincarlist, endcarorientation):
        movement.append(j-i)
        
    print("Car Move")
    for i in range(len(begincarlist)):
        print(f"{end_cars[i].name}   ", end="")
        if movement[i] >= 0:
            print(f" {movement[i]}")
        else:
            print(movement[i])

    boardlist = random_solver.listarray
    visualize(boardlist, saveplot = True)


    
    

        


    


