from code.classes.board import Board
from code.classes.board_generator import RandomBoard
from code.classes.state import State
from code.algorithms.randomise import Random_solver_v1, Random_solver_v2
from code.algorithms.breadth_first import BreadthFirst 
from code.algorithms.depthfirst import Depthfirst
from code.algorithms.pruning import Pruning
from code.algorithms.blockingbestfirst import BlockingBestFirst
from code.algorithms.distancebestfirst import DistanceBestFirst
from code.algorithms.blockingdistancebestfirst import BlockingDistanceBestFirst
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
        
        if board_number >= 1 and board_number <= 8:
            print()

            if board_number <= 3:
                size = 6 
            elif board_number >= 4 and board_number <= 6:
                size = 9 
            elif board_number == 7:
                size = 12 
            else:
                while True:
                     size = int(input("Choose board size of 6, 9, or 12 for randomly generated board: "))

                     if size == 6 or size == 9 or size == 12:
                         print()
                         break 

            return board_number, size 
        

def choose_algorithm(): 
    """  
    Ask the user with which algorithm he wants to solve the board 
    """

    print("There are several algorithms to solve this board:")
    print("Random: 1")
    print("Breadthfirst: 2")
    print("Depthfirst: 3")
    print("Depthfirst pruning: 4")
    print("Blocking best first (heuristic): 5")
    print("Distance best first (heuristic): 6")
    print("Blocking distance best first (heuristic): 7")
    print()

    while True:
        algorithm = int(input("Choose algorithm (1-7): "))

        if algorithm >= 1 and algorithm <= 7:
            print()

            return algorithm  


def get_initial_state(board_number, size):
    """ 
    Gets the initial state of the board
    """

    assert board_number >= 1 and board_number <= 8 

    if board_number == 8:
        initial_board = RandomBoard(size)
        initial_cars = initial_board.get_initial_cars()   
        initial_state = State(initial_cars, size)
        print("Randomly generated board:") 
        print(initial_state.get_board())
        print()
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
    assert algorithm >= 1 and algorithm <= 7 

    if algorithm == 1:
        if size == 6:    
            start = time.time() 
            random_solver = Random_solver_v2(initial_state)
            random_solver.run()
            print(f"It took {random_solver.steps} steps to solve this game")                                
            print(f"Solving this board took {time.time() - start} seconds")
        else:
            start = time.time() 
            random_solver = Random_solver_v1(initial_state)
            random_solver.run() 
            print(f"It took {random_solver.steps} steps to solve this game")                               
            print(f"Solving this board took {time.time() - start} seconds")

    
    elif algorithm == 3: 
        start = time.time() 
        df = Depthfirst(initial_state, size) 
        print(f"It took {df.solve_board()} steps to solve this game")
        print(f"There were {df.visited_states()} states visited")
        print(f"Solving this board took {time.time() - start} seconds") 

    elif algorithm == 4: 
        start = time.time() 
        data = Pruning(initial_state, size) 
        data.solve_board()
        print(f"It took {data.solve_board()} steps to solve this game")
        print(f"There were {data.visited_states()} states visited")
        print(f"Solving this board took {time.time() - start} seconds") 

    else: 
        if algorithm == 2:  
            start = time.time() 
            data = BreadthFirst(initial_state, size) 
            data.run()        

        elif algorithm == 5:
            start = time.time() 
            data = BlockingBestFirst(initial_state, size) 
            data.run()

        elif algorithm == 6:
            start = time.time() 
            data = DistanceBestFirst(initial_state, size) 
            data.run()         
        else:
            start = time.time() 
            data = BlockingDistanceBestFirst(initial_state, size) 
            data.run()
            
        print(f"It took {data.steps} steps to solve this game") 
        print(f"There were {len(data.visited)} states visited")
        print(f"Solving this board took {time.time() - start} seconds")
    

if __name__ == "__main__":
    board_number, size = get_gameboard()
    algorithm = choose_algorithm()
    initial_state = get_initial_state(board_number, size)

    solve_board(initial_state, algorithm, size)

