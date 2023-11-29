# Conway's Game of life implementation with cyclic boundary conditions.
# Author: Tiger Yotsawat
# Date: 29 May 2020

# The universe of the Game of Life is an infinite, two-dimensional orthogonal grid of square cells.
# Each cell is in one of two possible states, live or dead.
# Every cell interacts with its eight neighbours, which are the cells that are horizontally, vertically, or diagonally adjacent.

# Rules:
# Any live cell with two or three live neighbours survives.
# Any dead cell with three live neighbours becomes a live cell.
# All other live cells die in the next generation. Similarly, all other dead cells stay dead.

import numpy as np

def count_neighbours(state, coords):
    """ Counts the dead and alive neighbours of the given coordinate.
    Parameters:
    state (array): Current state of the grid.
    coords (int, int): Position of cell whose neighbours are to be returned.

    Returns:
    numAlive (int): Number of alive neighbours.
    """

    maxRow, maxCol = np.shape(state)
    row, col = coords
    if row >= maxRow or col >= maxCol:
        return -1
    count = 0
    increments = [-1, 0, 1]
    for i in increments:
        for j in increments:
            if (i != 0) or (j != 0):
                # Deal with wrap around values
                neighRow = (row + i) % maxRow
                neighCol = (col + j) % maxCol

                neighState = state[neighRow, neighCol]
                if neighState == 1:
                    count += 1
    return count

# Initialise empty grid
N = 10
grid = np.random.rand(N, N)
grid = np.around(grid)

print(grid)
coords = [(100, 100), (0, 0), (N-1, N-1), (3, 4), (0, N-1), (N-1, 0), (2, 2)]
for c in coords:
    print(c)
    print(count_neighbours(grid, c))