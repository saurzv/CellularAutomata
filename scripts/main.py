from project.classes.config import surface, roughness_array
from project.deposition import particle_deposition
from project.helper import check, get_random_coordinate, isMobile, save_grid, save_csv
from project.generate_graph import generate_surface_graph, generate_graph
import cProfile
import pstats
import numpy as np
import matplotlib.pyplot as plt
import time
import os
import asyncio

strt = time.time()


def start():
    row = surface.row
    col = surface.col
    # theta_dep = surface.theta_dep
    theta_max = surface.theta_max
    freq = surface.freq
    # Z = surface.Z
    tau = surface.tau
    name = surface.get_name()

    master_counter = 0
    while (check(theta_max, surface.get_max_height())):
        particle_deposition()
        roughness_array.append(np.std(surface.grid))

        # asyncio.run(save_grid(surface.grid))
        # generate_graph(master_counter, surface.grid)

        for _ in range(int(tau*row*col)):  # tau_l_sq
            # increment the master counter
            master_counter += 1
            # if (master_counter % freq == 0):
            #     generate_surface_graph(
            #         surface, f'surface-graph-at-{master_counter}')

            # take saving freq
            x, y = get_random_coordinate(row, col)
            xx, yy = isMobile(x, y)
            # print(xx, yy)
            # grid = surface.get_grid()
            if xx != -1:
                # print(x, y)
                # print(xx, yy)
                # surface.print_grid()
                surface.grid[x][y] -= 1
                surface.grid[xx][yy] += 1
                # surface.print_grid()

    plt.plot(roughness_array)
    if os.path.exists('graph') == False:
        os.mkdir('graph')
    plt.savefig(f'graph/{name}-{strt}.png')
    save_csv(roughness_array)


if __name__ == "__main__":
    with cProfile.Profile() as pr:
        start()
        # generate_surface_graph('grids')

    results = pstats.Stats(pr)
    if os.path.exists('results') == False:
        os.mkdir('results')

    name = surface.get_name()
    results.dump_stats(f'results/{name}-{strt}.prof')
