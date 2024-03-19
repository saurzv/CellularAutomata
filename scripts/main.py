from project.classes.Surface import Surface
from project.deposition import particle_deposition
from project.helper import check, get_random_coordinate, isMobile
from project.generate_graph import generate_surface_graph, save_array
import cProfile
import pstats
import numpy as np
import matplotlib.pyplot as plt

surface = Surface()


def start():
    surface.get_input()

    row = surface.row
    col = surface.col
    # theta_dep = surface.theta_dep
    theta_max = surface.theta_max
    freq = surface.freq
    # Z = surface.Z
    tau = surface.tau

    test_arr = []


    master_counter = 0
    while (check(theta_max, surface.get_max_height())):
        particle_deposition(surface)
        grid = surface.get_grid()
        print(grid)


        test_arr.append(np.std(grid))

        
        # yahi pe save karna hai bin file ko
        save_array(surface, f'surface-at-{master_counter}')

        for _ in range(int(tau*row*col)):  # tau_l_sq
            # increment the master counter
            master_counter += 1
            # if (master_counter % freq == 0):
            #     generate_surface_graph(
            #         surface, f'surface-graph-at-{master_counter}')

            # take saving freq
            x, y = get_random_coordinate(row, col)
            xx, yy = isMobile(x, y, surface)
            # print(xx, yy)
            # grid = surface.get_grid()
            if xx != -1:
                # print(x, y)
                # print(xx, yy)
                # surface.print_grid()
                grid[x][y] -= 1
                grid[xx][yy] += 1
                # surface.print_grid()

        surface.grid = grid
    print(test_arr)
    plt.plot(test_arr)
    plt.savefig(f'graph/roughness.png')


if __name__ == "__main__":
    with cProfile.Profile() as pr:
        start()
        # generate_surface_graph(surface, 'results/')

    results = pstats.Stats(pr)
    results.sort_stats(pstats.SortKey.TIME)
    results.print_stats()
