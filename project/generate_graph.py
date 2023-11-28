import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d
from mpl_toolkits.mplot3d import Axes3D


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


def generate_surface_graph(surface, name):
    """
    Generate a surface graph based on the given surface and name.

    Parameters:
    - surface: the surface object to generate the graph from.
    - name: the name of the graph.

    Returns:
    None
    """
    grid = surface.get_grid()
    matrix = np.array(grid)
    x = np.arange(0, matrix.shape[0], 1)
    y = np.arange(0, matrix.shape[1], 1)

    X, Y = np.meshgrid(x, y)

    Z = get_value_at_coordinate(matrix, X, Y)

    fig = plt.figure()
    ax = plt.axes(projection='3d')
    my_cmap = plt.get_cmap('hot')

    surf = ax.plot_surface(X, Y, Z, cmap=my_cmap, edgecolor='none')

    fig.colorbar(surf, ax=ax, shrink=0.5, aspect=5)

    fig.savefig(f'graph/{name}.png')
