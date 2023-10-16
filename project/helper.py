import random
from project.classes.Surface import Surface


def isMobile(i: int, j: int, Z: int, surface: Surface) -> tuple[int, int]:
    grid = surface.get_grid()
    row = len(grid)
    col = len(grid[0])
    neighbors = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    # random_pair = []
    Ni = 0
    c = []

    for dx, dy in neighbors:
        ni, nj = (i + dx) % row, (j + dy) % col
        if grid[i][j] == grid[ni][nj]:
            Ni += 1
        elif grid[i][j] > grid[ni][nj]:
            c.append((ni, nj))

    return random.choice(c) if Ni > Z and len(c) > 0 else [-1, -1]

    # if Ni > Z and len(c) > 0:
    #     return random.choice(c)

    #     # if it is true then only we will see the "c" storage array and if it is empty we cannot move else diffuse it in any of the pair
    # return [-1, -1]


def check(theta_max: int, max_height: int) -> bool:
    return theta_max > max_height


def get_random_coordinate(row: int, col: int) -> tuple[int, int]:
    return random.randint(0, row - 1), random.randint(0, col - 1)
