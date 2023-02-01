# SAI-Rush-Hour

Authors: Issa Zouboye, Alex van Diepen, Shreyas Potdar

Updated: 01/02/2023

<img src = "https://github.com/issazouboye/SAI-Rush-Hour/blob/main/simulation_animation.gif" width = "200"/>

## Summary
The main goal of this project is to investigate and apply a variety of algorithms and heuristics to solve the Rush Hour puzzle. The Rush Hour puzzle is solved when the ‘red’ car passes through the exit and this is only possible by moving all of the car’s blocking its path. A given car has either a vertical or horizontal orientation and the car can only move forwards or backwards into an empty space. Thus, we have implemented a mixture of different algorithms and heuristics to identify the best way possible to solve this Rush Hour puzzle. 


## Requirements 
The python version that was used for this project is: Python 3.8.10. The requirements.txt file consists of all of the packages that are required to run the code successfully. This can be done by typing in the following command:

```
pip install -r requirements.txt
```

## How to function the code

Follow the instructions to run the different algorithms for your preffered board.
```
python3 main.py
```

Use the following command to get the visualization of the solved first board using the breadth first algorithm.
```
python3 -m code.visualisation.get_visualization 
```


## Repository Summary
This repository contains 4 main folders. The following tables gives a summary of all the different files:

**Main**:
| File          | Summary           |
| ------------- |:-------------:|
| main.py|This file asks the user which board they want to solve, and with which algorithm. 
| experiment.py    | A file that generates data to evaluate the performance of each algorithm and heuristic for a given initial configuration of the puzzle.
|Plots Folder| Includes histograms of the performance of the random algorithm for the different configurations of the puzzle.
|Boardscsv folder | Includes the results of the different experiments conducted, with the number on the file name indicating the results of that particular initial configuration. 


**Algorithms:**
| File          | Code Summary                     |
| ------------- |:-----------------------:|
| blockingbestfirst.py |A heuristic that gives priority to the state with the least amount of cars that block the red car.|
| blockingdistancebestfirst.py | A heuristic that gives priority to the car’s blocking the exit to move first.|
| breadth_first.py| An algorithm that looks through all nodes at the current depth level to find a solution before moving onto the next one|
|depthfirst.py  |An algorithm that starts from the node and goes as far down a given path to find a solution.|
|distancebestfirst.py|A heuristic that gives priority to the state with the smallest distance of the red car to the exit.|
|pruning.py| An algorithm that looks for a solution that is better than the initial depth first solution to solve the puzzle.|
|randomise.py| An algorithm that makes a random move at each node to solve the puzzle.|
|Data folder| A folder with different initial configurations of the Rush Hour puzzle.|

**Classes**:
| File          | Summary           |
| ------------- |:-------------:|
|board_generator.py|              Generates a random configuration of the Rush Hour puzzle|
|car.py|A class that stores characteristics of a car object such as its orientation and location.|
|state.py| A class that creates the board with the given list of cars and gives you the possibility to get the next configurations/states of the board.|

**Visualization**:
| File          | Summary           |
| ------------- |:-------------:|
|Visualization Folder            | Creates a GIF of the different movements taken to solve the puzzle. Inspiration of code from the forest fire assignment.|



## Acknowledgements:
* Programming Minor at UVA
* Paper used as inspiration: https://www.human-competitive.org/sites/default/files/sipper-rush-paper.pdf


