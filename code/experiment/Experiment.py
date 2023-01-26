
from board_random import *
import matplotlib.pyplot as plt

class Experiment:
    def __init__(self, runs):
        self.runs = runs
        self.step_list = []

    def experiment_list(self):

        smallest_steps = 100000

        initial_board = Board(6)
        initial_board.load_board("Rushhour6x6_1.csv")     

        initial_cars = initial_board.get_initial_cars() 
        initial_board = initial_board.get_initial_board()  

        master_random_solver = Random_solver_v2(initial_cars, initial_board)  
    
        for i in range(self.runs):     

            random_solver = copy.deepcopy(master_random_solver)
            random_solver.solve_board()

            end_cars = random_solver.get_end_cars()
            end_board = random_solver.get_end_board()
            steps = random_solver.step_count()

            self.step_list.append(steps)

            if steps < smallest_steps:
                smallest_steps = steps                          

        print()
        print(f"The smallest number of steps is: {smallest_steps}") 



    def plot(self):
        bins=np.arange(0, 100000, 1000)
        plt.hist(self.step_list, edgecolor='black', bins = bins)
        plt.title('Aantal Stappen om Rush Hour op te lossen')
        plt.xlabel('Amount of Steps')
        plt.ylabel('Frequencey')
        plt.savefig('Experiment_10000_runs.png')

if __name__ == "__main__":

    new_experiment = Experiment(10000)
    new_experiment.experiment_list()
    new_experiment.plot()
