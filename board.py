from car import Car
from board_random import *
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import colors as c
import matplotlib.animation as animation
from typing import List


def visualize(grid_values:List[np.ndarray], showplot:bool=True, saveplot:bool=False,
              filename:str='simulation_animation', colors:List[str]=['red', 'black', 'green']):
    """
    Animates the Cellular automata simulation result.

    Args:
        grid_values (List[np.ndarray]): a list of the grids (numpy 2d-arrays) generated during the simulation
        showplot (bool, optional): show the visualization. Defaults to True.
        saveplot (bool, optional): saves the visualization as a gif. Defaults to False.
        filename (str, optional): filename used to save animation. Defaults to 'simulation_animation'.
        colors (List[str], optional): colors used in animation. Length of list must correspond with number of
                                      unique values in grid (i.e. the number of unique states).
                                      Defaults to ['black', 'green', 'red'].
    """
    grid_values = np.vectorize(lambda x: ord(x) - ord('A'))(grid_values[:5])
    print(grid_values)

    # Set up figure and colors
    fig = plt.figure(figsize=(8,8))
    cmap = c.ListedColormap(colors)
    
    # (ord(car_character) - ord('A')) % 3

    # Plot frames
    ims = [[plt.imshow(grid, vmin=0, vmax=len(colors), cmap=cmap, animated=True)] for grid in grid_values]

    plt.axis('off')
    plt.tight_layout()

    ani = animation.ArtistAnimation(fig, ims, interval=50, blit=True, repeat_delay=1000)

    if saveplot:
        ani.save(filename + '.gif', writer=animation.PillowWriter(fps=10))

    if showplot:
        plt.show()

if __name__ == "__main__":
  
    smallest_steps = 100000

    initial_board = Board(6)
    initial_board.load_board("Rushhour6x6_1.csv")     

    initial_cars = initial_board.get_initial_cars() 
    initial_board = initial_board.get_initial_board()         

    master_random_solver = Random_solver_v2(initial_cars, initial_board)  
 
    for i in range(1):     

        random_solver = copy.deepcopy(master_random_solver)
        random_solver.solve_board()

        # end_cars = random_solver.get_end_cars()
        # end_board = random_solver.get_end_board()        

        steps = random_solver.step_count()

        if steps < smallest_steps:
            smallest_steps = steps                          

    print()
    print(f"The smallest number of steps is: {smallest_steps}")

    boards = random_solver.get_list_boards()
    print(boards)

    # visualize(boards, saveplot = True)



