from project.classes.Surface import Surface
from project.deposition import particle_deposition
from project.helper import check, get_random_coordinate, isMobile

row = int(input("Enter the number of rows: "))
col = int(input("Enter the number of columns: "))
theta_dep = int(input("Enter the value of theta_dep: "))
theta_max = int(input("Enter the theta_max: "))     # Max height
Z = int(input("Enter the value of Z: "))

# creating an instance of "Surface" class as surface
surface = Surface(row, col, theta_dep, theta_max, Z)

while (check(theta_max, surface.get_max_height())):
    particle_deposition(row, col, theta_dep, surface)

    for _ in range(5):
        x, y = get_random_coordinate(row, col)
        xx, yy = isMobile(x, y, Z, surface)
        print(xx, yy)
        grid = surface.get_grid()
        if xx != -1:
            grid[x][y] -= 1
            grid[xx][yy] += 1
            print(grid)


print(surface.get_grid())

# print("Updated Average Height:", surface.get_average_height())
