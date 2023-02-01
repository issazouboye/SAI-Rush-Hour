from code.classes.board import Board
from code.classes.state import State
from code.algorithms.breadth_first import BreadthFirst 
from code.algorithms.blockingbestfirst import BlockingBestFirst
from code.algorithms.distancebestfirst import DistanceBestFirst
from code.algorithms.blockingdistancebestfirst import BlockingDistanceBestFirst
from code.algorithms.randomise import Random_solver_v1, Random_solver_v2
from code.algorithms.depthfirst import Depthfirst
from code.algorithms.branch_and_bound import Branchandbound
import time 


def get_gameboard():
    """
    Asks the user which board he wants to solve
    """

    print("There are 7 given boards to solve. Board 1-3 are of size 6x6, board 4-6 are of size 9x9 and")
    print("board 7 is of size 12x12.")
    print()

    while True:
        board_number = int(input("Choose which board (1-7) you want to solve or choose a randomly generated board (press 8): "))
        size = 0 
        
        if board_number >= 1 and board_number <= 8:
            print()

            if board_number <= 3:
                size = 6 
            elif board_number >= 4 and board_number <= 6:
                size = 9 
            else:
                size = 12 

            return board_number, size 
        

def choose_algorithm(): 
    """  
    Ask the user with which algorithm he wants to solve the board 
    """

    print("There are several algorithms to solve this board:")
    print("Random: 1")
    print("Breadthfirst: 2")
    print("Depthfirst: 3")
    print("Blocking best first (heuristic): 4")
    print("Distance best first (heuristic): 5")
    print("Blocking distance best first (heuristic): 6")
    print()

    while True:
        algorithm = int(input("Choose algorithm (1-6): "))

        if algorithm >= 1 and algorithm <= 6:
            print()

            return algorithm  


def get_initial_state(board_number, size):
    """ 
    Gets the initial state of the board
    """

    assert board_number >= 1 and board_number <= 8 

    if board_number == 8:
        pass 
    else:
        initial_board = Board(size)
        initial_board.load_board(f"data/Rushhour{size}x{size}_{board_number}.csv")     
        initial_cars = initial_board.get_initial_cars()   
        initial_state = State(initial_cars, size)

        return initial_state 


def solve_board(initial_state: State, algorithm, size):
    """ 
    Solves the board 
    """
    assert algorithm >= 1 and algorithm <= 6 

    if algorithm == 1:
        if size == 6:    
            start = time.time() 
            random_solver = Random_solver_v2(initial_state)
            random_solver.run()                               
            print(f"Solving this board took {time.time() - start} seconds")
        else:
            start = time.time() 
            random_solver = Random_solver_v1(initial_state)
            random_solver.run()                               
            print(f"Solving this board took {time.time() - start} seconds")

    elif algorithm == 2:  
        start = time.time() 
        bf = BreadthFirst(initial_state, size) 
        bf.run()
        print(f"There were {len(bf.visited)} states visited")
        print(f"Solving this board took {time.time() - start} seconds")

    elif algorithm == 3: 
        start = time.time() 
        df = Depthfirst(initial_state, size) 
        print(df.solve_board())
        print(f"There were {df.visited_states()} states visited")
        print()
        print(f"Solving this board took {time.time() - start} seconds") 

    elif algorithm == 4:
        start = time.time() 
        blocking = BlockingBestFirst(initial_state, size) 
        blocking.run()
        print(f"There were {len(blocking.visited)} states visited")
        print(f"Solving this board took {time.time() - start} seconds")

    elif algorithm == 5:
        start = time.time() 
        distance = DistanceBestFirst(initial_state, size) 
        distance.run()
        print(f"There were {len(distance.visited)} states visited")
        print(f"Solving this board took {time.time() - start} seconds")

    else:
        start = time.time() 
        blockingdistance = DistanceBestFirst(initial_state, size) 
        blockingdistance.run()
        print(f"There were {len(blockingdistance.visited)} states visited")
        print(f"Solving this board took {time.time() - start} seconds")
 

if __name__ == "__main__":
    board_number, size = get_gameboard()
    algorithm = choose_algorithm()
    initial_state = get_initial_state(board_number, size)

    solve_board(initial_state, algorithm, size)

