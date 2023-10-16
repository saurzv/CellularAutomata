from project.classes.Surface import Surface
import random

row = 5  # Number of rows
col = 5  # Number of columns
theta_dep = 5  # Value of theta_dep
max_height = 10  # Max height
surface = Surface(row, col, theta_dep,max_height)   #creating an instance of "Surface" class as surface
average_height = 0

def particle_deposition(row_, col_, theta_dep_, average_height):

        num_of_particles = theta_dep_ * row_ * col_                        #number of particles to be distributed in the grid per iteration

        for _ in range(num_of_particles):                               #randomly guessing the (i,j)-coordinates and increasing the grid[i][j] by 1
            i = random.randint(0, row_ - 1)
            j = random.randint(0, col_ - 1)
            surface.grid[i][j] += 1

        
        print("Printing grid for testing:")                             # Print the updated grid and average height for each iteration
        for k in surface.grid:
            print(" ".join(map(str, k)))

        average_height = surface.set_total_particle()                                    #setting the total_particles which in turn sets the average_height
        print("Average Height:", surface.get_average_height())
        print("Total particle:", surface.get_total_particle())
        return avearge_height

average_height = particle_deposition(row, col, theta_dep, average_height)
print("Updated Average Height:", average_height)