import random
from project.classes.Surface import Surface


def particle_deposition(row_: int, col_: int, theta_dep_: int, surface: Surface) -> None:

    # number of particles to be distributed in the grid per iteration
    surface.set_total_particle()
    num_of_particles = theta_dep_ * row_ * col_
    grid = surface.get_grid()

    # randomly guessing the (i,j)-coordinates and increasing the grid[i][j] by 1
    for _ in range(num_of_particles):
        i = random.randint(0, row_ - 1)
        j = random.randint(0, col_ - 1)
        grid[i][j] += 1
        surface.set_max_height(grid[i][j])

    # print(grid)
    # Print the updated grid and average height for each iteration
    # print("Printing grid for testing:")
    # for k in surface.grid:
    #     print(" ".join(map(str, k)))

    # setting the total_particles which in turn sets the average_height
    print("Average Height:", surface.get_average_height())
    print("Total particle:", surface.get_total_particle())
