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



class Stack:
    
    def __init__(self) -> None:
        """
        post : creates an empty LIFO stack
        """
        self.depth_stack: List[Any] = []

    def push(self, car: Car) -> None:
        """
        post : places x on top of the stack
        """
        self.depth_stack.append(car)

    def remove_items(self):
        """pre : self.size O > 0
        post : removes and returns the top element of
        the stack
        """

        if len(self.depth_stack) > 0:
            return self.depth_stack.pop()


class Depthfirst:
    def __init__(self, cars_set, size):
        self.cars_set = cars_set
        self.size = size
        self.steps = 0
        self.visitedset = set()
        self.end_cars = None 
        self.end_board = None 

        self.stack = []
        self.stack.append(cars_set)
                
        # self.steps = float('inf')

        self.visitedset.add(cars_set)

    # def adding_configurations(self, board):
    #     new_step = self.stack.remove_items()
    #     self.visitedlist.add(new_step)

    def solve_board(self):
        while len(self.stack) != 0:
            new_state = self.stack.pop()
            self.steps += 1

            if new_state.is_solved():
                # self.end_cars = new_cars 
                # self.end_board = new_state
                print(f"It took {self.steps} steps to solve this game") 
                break 
            
            else:
                for potential_moves in new_state.get_next_configurations():
                    follwoing_state = State(potential_moves, self.size)
                    if follwoing_state in self.visitedset:
                        pass
                    
                    else:
                        self.stack.append(follwoing_state)
                        self.visitedset.add(follwoing_state)

    def get_end_board(self):
        return self.end_board 

    def get_end_cars(self):
        return self.end_cars 

                 
if __name__ == "__main__":
    initial_board = Board(6)
    initial_board.load_board("Rushhour6x6_1.csv")

    initial_cars = initial_board.get_initial_cars() 
    initial_board = initial_board.get_initial_board() 

    state_test = State(initial_cars, 6)
    df = Depthfirst(state_test, 6)
    print(df.solve_board())


    def solve_board(self):
        new_game = Game(self.initial_cars, self.initial_board)

        while True:
            configurations_list = new_game.get_next_configurations()
            for i in configurations_list:
                self.stack.push(i)

            new_step = self.stack.remove_items()
            updated_board = new_game.get_updated_board(new_step)
            new_game = Game(new_step, updated_board)
            
            if new_game.is_solved():
                self.end_cars = new_cars 
                self.end_board = updated_board 
                print(f"It took {steps} steps to solve this game") 
                break 

    def get_end_board(self):
        return self.end_board 

    def get_end_cars(self):
        return self.end_cars 

                 


        

            

