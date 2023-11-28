from project.classes.Surface import Surface
from project.deposition import particle_deposition
from project.helper import check, get_random_coordinate, isMobile
from project.generate_graph import generate_surface_graph

row = int(input("Enter the number of rows: "))
col = int(input("Enter the number of columns: "))
theta_dep = int(input("Enter the value of theta_dep: "))
theta_max = int(input("Enter the theta_max: "))     # Max height
Z = int(input("Enter the value of Z: "))
tau = int(input("Enter the value of tau: "))
freq = int(input("Enter the value of saving freq: "))
# take tau_l_sq as input (as float) - round it off too

# creating an instance of "Surface" class as surface
surface = Surface(row, col, theta_dep, theta_max, Z)

# master counter here
master_counter = 0
while (check(theta_max, surface.get_max_height())):
    particle_deposition(surface)

    for _ in range(tau*row*col):  # tau_l_sq
        # increment the master counter
        master_counter += 1
        if (master_counter % freq == 0):
            generate_surface_graph(
                surface, f'surface-graph-at-{master_counter}')

        # take saving freq
        x, y = get_random_coordinate(row, col)
        xx, yy = isMobile(x, y, surface)
        # print(xx, yy)
        grid = surface.get_grid()
        if xx != -1:
            print(x, y)
            print(xx, yy)
            surface.print_grid()
            grid[x][y] -= 1
            grid[xx][yy] += 1
            surface.print_grid()

    # save the gird to an image - use numpy to convert the grid to an image
    # file name - should contain the master counter

surface.print_grid()

# print("Updated Average Height:", surface.get_average_height())
