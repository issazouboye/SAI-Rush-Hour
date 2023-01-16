
from board_v2 import *
import matplotlib.pyplot as plt

class Experiment:
    def __init__(self, runs):
        self.runs = runs
        self.step_list = []

    def experiment_list(self):
        for i in range(self.runs):
            initial_board = Board(6)
            initial_board.load_board("Rushhour6x6_1.csv")

            initial_cars = initial_board.get_initial_cars() 
            initial_board = initial_board.get_initial_board() 

            random_solver = Random_solver(initial_cars, initial_board) 
            random_solver.solve_board()
            
            self.step_list.append(random_solver.step_count())


    def plot(self):
        plt.hist(self.step_list, edgecolor='black')
        plt.xlabel('Amount of Steps')
        plt.ylabel('Frequencey')
        plt.savefig('Experiment.png')




if __name__ == "__main__":

    new_experiment = Experiment(100)
    new_experiment.experiment_list()
    new_experiment.plot()
