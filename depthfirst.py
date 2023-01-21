# Depth First Search Algorithm
from boardtest import *
from visualization import visualize

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

    def get_initial_cars(self):
        return self.cars 

    def get_initial_board(self):
        return self.board 
    

class Game:

    def __init__(self, cars, board):
        self.cars = cars 
        self.board = board 

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

    def get_updated_board(self, new_cars):
        new_board = [["0" for i in range(len(self.board))] for j in range(len(self.board))]
        self.board = np.array(new_board)

        # Place the cars on the board 
        for car in new_cars:
            if car.orientation == "H":
                for j in range(car.length):
                    self.board[car.row][car.column + j] = car.name 

            if car.orientation == "V":
                for i in range(car.length):
                    self.board[car.row + i][car.column] = car.name 
        
        return self.board      

    def is_solved(self): 
        for car in self.cars:
            winning_column = len(self.board) - 2 
            winning_row = ceil(len(self.board) / 2) - 1 

            if car.name == "X" and car.column == winning_column and car.row == winning_row:
                return True 

        return False     


class Deppthfirst_Stack:
    
    def __init__(self) -> None:
        """
        post : creates an empty LIFO stack
        """
        self.depth_stack: List[Any] = []
        self.visited = False


    def push(self, car: Car) -> None:
        """
        post : places x on top of the stack
        """
        self.depth_stack.append(car)

    def remove_items(self) -> Any:
        """pre : self.size O > 0
        post : removes and returns the top element of
        the stack
        """
        if len(self.depth_stack) > 0:
            return self.depth_stack.pop()


class Deppthfirst:
    def __init__(self, initial_cars, initial_board):
        self.initial_cars = initial_cars
        self.initial_board = copy.deepcopy(initial_board)
        self.stack = Deppthfirst_Stack()

        self.end_cars = None 
        self.end_board = None 
        
        self.steps = float('inf')

        self.visitedset = set()

    # def adding_configurations(self, board):
    #     new_step = self.stack.remove_items()
    #     self.visitedlist.add(new_step)

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

                 
if __name__ == "__main__":


        

            

