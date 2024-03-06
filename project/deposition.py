from project.classes.Surface import Surface
from project.helper import get_random_coordinate


def particle_deposition(surface: Surface) -> None:
    """
    Distributes particles on a surface grid using a random deposition algorithm.

    Parameters:
        surface (Surface): The surface object representing the grid.

    Returns:
        None
    """
    row = surface.row
    col = surface.col
    theta_dep = surface.theta_dep

    # number of particles to be distributed in the grid per iteration
    surface.set_total_particle()
    num_of_particles = int(theta_dep * row * col)
    grid = surface.get_grid()

    # randomly guessing the (i,j)-coordinates and increasing the grid[i][j] by 1
    for _ in range(num_of_particles):
        # i = random.randint(0, row - 1)
        # j = random.randint(0, col - 1)
        i, j = get_random_coordinate(row, col)
        grid[i][j] += 1
        surface.set_max_height(grid[i][j])

    surface.grid = grid
