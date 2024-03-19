import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d
from mpl_toolkits.mplot3d import Axes3D
import glob


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


def save_array(surface, name):
    grid = surface.get_grid()
    print(grid)
    print(surface.get_total_particle())
    # print(type(grid))
    # print('saving to file')
    grid.tofile(f'results/{name}.bin')
    # arr = np.fromfile(
    #     f'results/{name}.bin', dtype=np.int64).reshape((surface.row, surface.col))


def generate_surface_graph(surface, dirPath):
    """
    Generate a surface graph based on the given surface and name.

    Parameters:
    - surface: the surface object to generate the graph from.
    - name: the name of the graph.

    Returns:
    None
    """
    # arr = np.fromfile(
    #     f'results/{name}.bin', dtype=np.int64).reshape((surface.row, surface.col))

    cnt = 0
    std_dev = []
    for file in glob.glob(f'{dirPath}/*.bin'):
        arr = np.fromfile(file, dtype=np.int32).reshape((surface.row, surface.col))
        print(arr)
        std_dev.append(np.std(arr))
        # x, y = np.meshgrid(np.arange(arr.shape[1]), np.arange(arr.shape[0]))

        # x = x.flatten()
        # y = y.flatten()

        # z = np.zeros(arr.size)
        # dx = dy = 0.5
        # dz = arr.flatten()
        # fig = plt.figure()
        # ax = fig.add_subplot(111, projection='3d')
        # ax.bar3d(x, y, z, dx, dy, dz, zsort='average')
        # plt.savefig(f'graph/{cnt}.png')
        # cnt += 1

    print(std_dev)
    plt.plot(std_dev)
    plt.savefig(f'graph/roughness.png')

    # matrix = np.array(grid)
    # x = np.arange(0, matrix.shape[0], 1)
    # y = np.arange(0, matrix.shape[1], 1)

    # X, Y = np.meshgrid(x, y)

    # Z = get_value_at_coordinate(matrix, X, Y)

    # fig = plt.figure()
    # ax = plt.axes(projection='3d')
    # my_cmap = plt.get_cmap('hot')

    # surf = ax.plot_surface(X, Y, Z, cmap=my_cmap, edgecolor='none')

    # fig.colorbar(surf, ax=ax, shrink=0.5, aspect=5)

    # fig.savefig(f'graph/{name}.png')
