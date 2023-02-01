"""
Program: get_visualization.py

Course: Algoritmen en Heuristieken

Students: Issa Zouboye, Alex van Diepen, Shreyas Potdar

Description: This is the program that keeps track of all of the steps 
             taken to to solve the rush hour puzzle and creates a visualization
             from it.
"""
from .visualize import visualize
from ..classes.state import State
from ..classes.board import Board
from ..algorithms.breadth_first import BreadthFirst
from typing import Optional, List



def backtrace(archive: dict, end_board: State) -> List[State]:
    """
    A function that shows keeps track of all of the steps taken for the depth first
    algorithm.
    """
    boardslist = [end_board]

    while boardslist[-1] != 0:
        boardslist.append(archive[boardslist[-1]])

    boardslist.pop()
    boardslist.reverse()
    boardslist

    return boardslist


if __name__ == "__main__":

    initial_board = Board(6)
    initial_board.load_board("data/Rushhour6x6_1.csv") 
    initial_cars = initial_board.get_initial_cars()

    first_state = State(initial_cars, 6) 
    bf = BreadthFirst(first_state, 6) 
    end_board = bf.run() 
    archive = bf.path
    stateslist = backtrace(archive, end_board)
    boardslist = []

    for i in stateslist:
        boardslist.append(i.board)

    visualize(boardslist, saveplot=True)
    