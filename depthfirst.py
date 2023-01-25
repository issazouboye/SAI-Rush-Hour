# Depth First Search Algorithm
from boardtest import *
from visualization import visualize
from car import Car
import copy 


class Board:

    def __init__(self, size: int):
        self.size = size        
        board = [["0" for i in range(self.size)] for j in range(self.size)]
        self.board = np.array(board)

        # Set with cars 
        self.cars = set()        
    
    def load_board(self, filename: str):  

        # Read the data
        with open(filename, 'r') as f:
            next(f) 

            for line in f:
                splits = line.strip().split(",")

                name = splits[0] 
                orientation = splits[1] 
                column = int(splits[2]) - 1
                row = int(splits[3]) - 1
                length = int(splits[4])  

                car = Car(name, orientation, column, row, length) 
                self.cars.add(car)                                  
        
        # Place the cars on the board 
        for car in self.cars:
            if car.orientation == "H":
                for j in range(car.length):
                    self.board[car.row][car.column + j] = car.name 

            if car.orientation == "V":
                for i in range(car.length):
                    self.board[car.row + i][car.column] = car.name 

        print("First board:")
        print(self.board)
        print() 
        # print(len(self.cars))

    def get_initial_cars(self):
        return self.cars 

    def get_initial_board(self):
        return self.board 
    
class State: 

    def __init__(self, cars, size: int):
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

class Depthfirst:
    def __init__(self, cars_set: State, size: int, max_height: int):
        self.cars_set = cars_set
        self.size = size
        self.steps = 0

        self.max_height = max_height

        self.archieve = {}
        self.archieve[cars_set] = [0, 0]


        # archieve = {}
        # archieve['Hello'] = ["o", 1]
        # print(archieve["Hello"][1] + 1)

        self.stack = []
        self.stack.append(cars_set)

        self.visitedset = set()
        self.visitedset.add(cars_set)


    def solve_board(self):

         while len(self.stack) != 0:
            new_state = self.stack.pop()
            self.steps += 1

            # if self.archieve[new_state][1] > self.max_height:


            if new_state.is_solved():
                print(f"It took {self.steps} steps to solve this game") 
                print("hello")
                print(self.archieve[new_state])
                return new_state 
            
            else:
                for potential_moves in new_state.get_next_configurations():
                    following_state = State(potential_moves, self.size)
                    
                    if following_state in self.visitedset:
                        pass

                    else:
                        self.archieve[following_state] = [new_state, self.archieve[new_state][1]+1]
                        self.stack.append(following_state)
                        self.visitedset.add(following_state)

    def backtrace(self, end_board):
        boardslist = [end_board]

        while boardslist[-1] != 0:
            boardslist.append(self.archieve[boardslist[-1]][0])

        boardslist.pop()
        boardslist.reverse()
        print((boardslist[-1]))

        return boardslist


    def get_end_board(self):
        return self.end_board 
    

                 
if __name__ == "__main__":
    initial_board = Board(6)
    initial_board.load_board("Rushhour6x6_1.csv")

    initial_cars = initial_board.get_initial_cars() 
    initial_board = initial_board.get_initial_board() 

    state_test = State(initial_cars, 6)
    df = Depthfirst(state_test, 6, 100)
    end_board = df.solve_board()
    df.backtrace(end_board)





                 


        

            

