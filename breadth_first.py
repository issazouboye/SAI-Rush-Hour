import numpy as np 
import copy 
from board_v2 import Car, Board 
from collections import deque
from math import ceil 


class State: 

    def __init__(self, cars: set[Car], size: int):
        self.cars = cars
        self.size = size  
        self.board = None 
        self.create_board()          

    def create_board(self):
        board = [["0" for i in range(self.size)] for j in range(self.size)]
        self.board = np.array(board)

        # Place the cars on the board 
        for car in self.cars:
            if car.orientation == "H":
                for j in range(car.length):
                    self.board[car.row][car.column + j] = car.name 

            if car.orientation == "V":
                for i in range(car.length):
                    self.board[car.row + i][car.column] = car.name 
        
        return self.board     

    def get_next_configurations(self): 

        # List filled with sets of car objects 
        configurations = []    
     
        for car in self.cars:

            # Check for horizontal cars 
            if car.orientation == "H":

                # Check if you can move to the left 
                if car.is_movable("left", self.board):                     
                    car.move_left() 
                    configurations.append(copy.deepcopy(self.cars)) 
                    car.move_right()                 

                # Check if you can move to the right 
                if car.is_movable("right", self.board):                     
                    car.move_right() 
                    configurations.append(copy.deepcopy(self.cars)) 
                    car.move_left()                 

            # Check for vertical cars 
            if car.orientation == "V":

                # Check if you can move up 
                if car.is_movable("up", self.board):                    
                    car.move_up()                      
                    configurations.append(copy.deepcopy(self.cars)) 
                    car.move_down()                    

                # Check if you can move down 
                if car.is_movable("down", self.board):                    
                    car.move_down() 
                    configurations.append(copy.deepcopy(self.cars)) 
                    car.move_up()                    

        return configurations          

    def is_solved(self): 
        for car in self.cars:
            winning_column = self.size - 2 
            winning_row = ceil(self.size / 2) - 1 

            if car.name == "X" and car.column == winning_column and car.row == winning_row:
                return True 

        return False  
    
    def __hash__(self) -> int:
        return hash(self.__repr__())
    
    def __repr__(self) -> str:
        printable_board = np.array_str(self.board)

        return printable_board 

    def __eq__(self, other) -> bool:
        return isinstance(other, State) 


class BreadthFirst:

    def __init__(self, first_state: State, size):
        self.first_state = first_state
        self.size = size 
        self.steps = 0

        # Initialize a queue 
        self.boards_queue = deque()

        # Initialize a set to keep up the board states already visited 
        self.visited = set()        
        
        # Put first state in queue
        self.boards_queue.append(first_state)

        # Add first state to visited set 
        self.visited.add(first_state) 
    
    def run(self):

        while len(self.boards_queue) != 0 :
            for step in range(len(self.boards_queue)):

                # Pop new board 
                new_board = self.boards_queue.popleft()                

                # If board is solved return result
                if new_board.is_solved():
                    print(f"It took {self.steps} steps to solve this game") 
                    return new_board 

                # Add all possible next boards to queue, if they're not in visited set 
                else:
                    next_configurations = new_board.get_next_configurations()

                    for configuration in next_configurations:
                        next_board = State(configuration, self.size)

                        if next_board in self.visited:
                            pass                    
                        else:
                            self.boards_queue.append(next_board)
                            self.visited.add(next_board) 
            
            self.steps += 1


if __name__ == "__main__":

    initial_board = Board(6)
    initial_board.load_board("Rushhour6x6_1.csv") 
    initial_cars = initial_board.get_initial_cars()

    first_state = State(initial_cars, 6) 
    bf = BreadthFirst(first_state, 6) 
    print(bf.run())
    