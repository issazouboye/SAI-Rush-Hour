from board_random import *
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import colors as c
import matplotlib.animation as animation
from typing import List

def visualize(grid_values:List[np.ndarray], showplot:bool=True, saveplot:bool=False,
              filename:str='simulation_alex', 
              ):
    
    # colors:List[str]=['white', 'green', 'green', 'blue','red']

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
    grid_values = np.vectorize(lambda x: ord(x) - ord('A'))(grid_values[:10])
    print(grid_values[0])

    float_dict = { 
    '0': 0.0,   
    'X': 1.0,
    'A': 2.0,
    'B': 3.0,
    'C': 4.0,
    'D': 5.0,
    'E': 6.0,
    'F': 7.0,
    'G': 8.0,
    'H': 9.0,
    'I': 10.0,
    'J': 11.0,
    'K': 12.0,
    'L': 13.0,    
    }

    converted_series = series.map(float_dict).copy()

    # Map each float to a specific color
    color_dict = {
        0.0: 'white',
        1.0: 'red',
        2.0: 'blue',
        3.0: 'green',
        4.0: 'yellow',
        5.0: 'turquoise',
        6.0: 'orange',
        7.0: 'pink',
        8.0: 'brown',
        9.0: 'purple',
        10.0: 'limegreen',
        11.0: 'darkblue',
        12.0: 'dark'
    }

    # Create a cmap from a color list
    color_list = list(converted_series.map(color_dict))
    custom_cmap = c.ListedColormap(color_list, name="custom_cmap")    

    # Set up figure and colors
    fig = plt.figure(figsize=(8,8))
    # cmap = c.ListedColormap(colors)  

    # Plot frames
    ims = [[plt.imshow(grid, vmin=0, vmax=len(custom_cmap), cmap=custom_cmap, animated=True)] for grid in grid_values]

    plt.axis('off')
    plt.tight_layout()

    ani = animation.ArtistAnimation(fig, ims, interval=50, blit=True, repeat_delay=1000)

    if saveplot:
        ani.save(filename + '.gif', writer=animation.PillowWriter(fps=10))

    if showplot:
        plt.show()


if __name__ == "__main__":  
    
    initial_board = Board(6)
    initial_board.load_board("Rushhour6x6_1.csv")     

    initial_cars = initial_board.get_initial_cars() 
    initial_board = initial_board.get_initial_board()   
    print(initial_board)      

    random_solver = Random_solver_v2(initial_cars, initial_board)       
    random_solver.solve_board()      

    steps = random_solver.step_count()                  
    print(f"The number of steps is: {steps}")
    print()

    boards = random_solver.get_list_boards()     

    visualize(boards, saveplot = True)

