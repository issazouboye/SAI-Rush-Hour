import numpy as np
from ..classes.state import State
from ..classes.board import Board
from ..algorithms.randomise import Random_solver_v1


def get_data_board1():
    initial_board = Board(6)
    initial_board.load_board("data/Rushhour6x6_1.csv")
    initial_cars = initial_board.get_initial_cars()
    initial_state = State(initial_cars, 6) 

    data = Random_solver_v1(initial_state, 6)
    end_state = data.run() 
    end_cars = end_state.get_cars()  

    return initial_cars, end_cars 


def get_data_board2():
    initial_board = Board(6)
    initial_board.load_board("data/Rushhour6x6_2.csv")
    initial_cars = initial_board.get_initial_cars()
    initial_state = State(initial_cars, 6) 

    data = Random_solver_v1(initial_state, 6)
    end_state = data.run() 
    end_cars = end_state.get_cars()  

    return initial_cars, end_cars 


def get_data_board3():
    initial_board = Board(6)
    initial_board.load_board("data/Rushhour6x6_3.csv")
    initial_cars = initial_board.get_initial_cars()
    initial_state = State(initial_cars, 6) 

    data = Random_solver_v1(initial_state, 6)
    end_state = data.run() 
    end_cars = end_state.get_cars()  

    return initial_cars, end_cars 


def get_data_board4():
    initial_board = Board(9)
    initial_board.load_board("data/Rushhour9x9_4.csv")
    initial_cars = initial_board.get_initial_cars()
    initial_state = State(initial_cars, 9) 

    data = Random_solver_v1(initial_state, 9)
    end_state = data.run() 
    end_cars = end_state.get_cars()  

    return initial_cars, end_cars 


def get_data_board5():
    initial_board = Board(9)
    initial_board.load_board("data/Rushhour9x9_5.csv")
    initial_cars = initial_board.get_initial_cars()
    initial_state = State(initial_cars, 9) 

    data = Random_solver_v1(initial_state, 9)
    end_state = data.run() 
    end_cars = end_state.get_cars()  

    return initial_cars, end_cars 


def get_data_board6():
    initial_board = Board(9)
    initial_board.load_board("data/Rushhour9x9_6.csv")
    initial_cars = initial_board.get_initial_cars()
    initial_state = State(initial_cars, 9) 

    data = Random_solver_v1(initial_state, 9)
    end_state = data.run() 
    end_cars = end_state.get_cars()  

    return initial_cars, end_cars 


def get_data_board7():
    initial_board = Board(9)
    initial_board.load_board("data/Rushhour12x12_7.csv")
    initial_cars = initial_board.get_initial_cars()
    initial_state = State(initial_cars, 12) 

    data = Random_solver_v1(initial_state, 12)
    end_state = data.run() 
    end_cars = end_state.get_cars()  

    return initial_cars, end_cars 

                 
if __name__ == "__main__":

    
        
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
    


    
    

        


    


