from project.classes.Surface import Surface
import random

row = 5  # Number of rows
col = 5  # Number of columns
theta_dep = 5  # Value of theta_dep
max_height = 10  # Max height
# creating an instance of "Surface" class as surface
surface = Surface(row, col, theta_dep, max_height)
average_height = 0


def particle_deposition(row_, col_, theta_dep_, average_height):

    # number of particles to be distributed in the grid per iteration
    num_of_particles = theta_dep_ * row_ * col_

    # randomly guessing the (i,j)-coordinates and increasing the grid[i][j] by 1
    for _ in range(num_of_particles):
        i = random.randint(0, row_ - 1)
        j = random.randint(0, col_ - 1)
        surface.grid[i][j] += 1

    # Print the updated grid and average height for each iteration
    print("Printing grid for testing:")
    for k in surface.grid:
        print(" ".join(map(str, k)))

    # setting the total_particles which in turn sets the average_height
    average_height = surface.set_total_particle()
    print("Average Height:", surface.get_average_height())
    print("Total particle:", surface.get_total_particle())
    return avearge_height


average_height = particle_deposition(row, col, theta_dep, average_height)
print("Updated Average Height:", average_height)
