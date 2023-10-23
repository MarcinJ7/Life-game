# -*- coding: utf-8 -*-
"""
Created on Mon May 23 10:07:52 2022

Based on book: Python Playground: Geeky Projects for the Curious Programmer
"""

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation


# Define some patterns - for example: glider (szybowiec)
def glider_pattern(i, j, matrix):
    """
    This function generats well known pattern (glider) and
    allows to put it in desired location in our Game of Life
    board matrix.
    
    Parameters
    ----------
    i : int
        Number of matrix rows.
    j : int
        Number of matrix cols.
    matrix : Array of int32
        Game of Life matrix (board).

    Returns
    -------
    None.

    """
    # Define matrix with pattern
    glider_matrix = np.array([[0, 0, 255], 
                              [255, 0, 255], 
                              [0, 255, 255]]) 
    # Set flider in matrix
    matrix[i:i+glider_matrix.shape[0], j:j+glider_matrix.shape[0]] = glider_matrix

def updateFunction(frameNumber, img, matrix, N):
    """
    Updating game board with Game of Life rules.

    Parameters
    ----------
    frameNumber : int
        Number of frames.
    img : image.AxesImage
        Image (for plotting).
    matrix : Array of int32
        Game of Life matrix (board).
    N : int
        Matrix size.

    Returns
    -------
    img : image.AxesImage
        Updated image of board.

    """
    # Define states - on and off (255 or 0 in our matrix)
    on = 255
    off = 0
    
    # Copy matrix before calculations
    matrix_upd = matrix.copy()
    # Iterate through each point
    for i in range(N):
        for j in range(N):
            # Calculate 8-neighbours sum (boundaries, PacMan logic)
            sum_nghbs = int((matrix[i, (j-1)%N] + matrix[i, (j+1)%N] +
                             matrix[(i-1)%N, j] + matrix[(i+1)%N, j] +
                             matrix[(i-1)%N, (j+1)%N] + matrix[(i+1)%N, (j+1)%N] +
                             matrix[(i-1)%N, (j-1)%N] + matrix[(i+1)%N, (j-1)%N])/255)
            # Let's use our rules
            if(matrix[i, j] == on):
                # If less than 2 nghbs or more than 3 - cell dies
                if(sum_nghbs < 2 or sum_nghbs > 3):
                    matrix_upd[i, j] = off
            else:
                if(sum_nghbs == 3):
                    matrix_upd[i, j] = on
    img.set_data(matrix_upd)
    matrix[:] = matrix_upd[:]
    return img
   
def generateRadnomGameBoard(N):
    """
    Function allows to generate random Game of Life board matrix.

    Parameters
    ----------
    N : int
        Desired size of random Game of Life board matrix.

    Returns
    -------
    matrix : Array of int32
        Game of Life board matrix.

    """
    # Initialize simple random matrix
    matrix = np.random.choice([255, 0], size = (N, N), p = [0.2, 0.8])
    
    return matrix


# BEFORE RUN:
# Type in console: %matplotlib qt 
# To be able to watch Game of Life progress


# Create main matrix of size N
N = int(input('Provide desired N-size of Game of Life board matrix: '))

# Generate random matrix with desired size
matrix = generateRadnomGameBoard(N)

# Add glider example
glider_pattern(1, 1, matrix)

# Add refreshing interval
refreshing_int = 50

# Animation
fig, ax = plt.subplots()
img = ax.imshow(matrix, interpolation='nearest')
anim = animation.FuncAnimation(fig, updateFunction, fargs=(img, matrix, N, ), frames=10, interval=refreshing_int, save_count=50)
plt.show()
    

