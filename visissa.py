from car import Car
from board_random import *
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import colors as c
import matplotlib.animation as animation
from typing import List


def visualize(grid_values:List[np.ndarray], showplot:bool=True, saveplot:bool=False,
              filename:str='simulation_animation', colors:List[str]=["white","indigo","maroon", "lightblue","black","lavender", "darkgreen","darkblue", "lightseagreen", "tomato", "darkorange", "yellowgreen", "chocolate", "orange", "purple","teal", "sienna", "pink", "olive", "yellow","blue","green", "gold", "silver", "brown",'red']):
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
    grid_values = np.vectorize(lambda x: ord(x) - ord('A'))(grid_values[:])
    print(grid_values)
    print(len(colors))

    # Set up figure and colors
    fig = plt.figure(figsize=(8,8))
    cmap = c.ListedColormap(colors)
    
    # (ord(car_character) - ord('A')) % 3

    # Plot frames
    ims = [[plt.imshow(grid, vmin=-2, vmax=23, cmap=cmap, animated=True)] for grid in grid_values]

    plt.axis('off')
    plt.tight_layout()

    ani = animation.ArtistAnimation(fig, ims, interval=50, blit=True, repeat_delay=1000)

    if saveplot:
        ani.save(filename + '.gif', writer=animation.PillowWriter(fps=10))

    if showplot:
        plt.show()



