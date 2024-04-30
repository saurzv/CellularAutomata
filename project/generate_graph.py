import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d
from mpl_toolkits.mplot3d import Axes3D
import glob
from project.helper import load_grid
from project.classes.config import surface


def get_value_at_coordinate(matrix, x, y):
    """
    Get the value at the given coordinate in the matrix.

    Parameters:
        matrix (list): The input matrix.
        x (int): The x-coordinate.
        y (int): The y-coordinate.

    Returns:
        The value at the given coordinate.
    """
    return matrix[x, y]


def generate_surface_graph(dirPath):
    file_path = glob.glob(f'{dirPath}/*.npy')
    cnt = 0
    for file in file_path:
        grid = load_grid(file)
        fig = plt.figure()
        x, y = np.meshgrid(np.arange(grid.shape[1]), np.arange(grid.shape[0]))

        x = x.flatten()
        y = y.flatten()

        z = np.zeros(grid.size)
        dx = dy = 0.5
        dz = grid.flatten()
        fig = plt.figure()
        ax = fig.add_subplot(111, projection='3d')
        ax.bar3d(x, y, z, dx, dy, dz, zsort='average')
        ax.set_zlim(0, surface.theta_max)
        plt.savefig(f'image/{cnt}.png')
        plt.close('all')
        cnt += 1


def generate_graph(cnt, grid):
    fig = plt.figure()
    x, y = np.meshgrid(np.arange(grid.shape[1]), np.arange(grid.shape[0]))

    x = x.flatten()
    y = y.flatten()

    z = np.zeros(grid.size)
    dx = dy = 0.5
    dz = grid.flatten()
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.bar3d(x, y, z, dx, dy, dz, zsort='average')
    ax.set_zlim(0, surface.theta_max)
    plt.savefig(f'graph/{cnt}.png')
    plt.close('all')
