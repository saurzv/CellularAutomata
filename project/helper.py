import random
from project.classes.Surface import Surface


def isMobile(i: int, j: int, surface: Surface) -> tuple[int, int]:
    grid = surface.get_grid()
    row = len(grid)
    col = len(grid[0])
    neighbors = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    Ni = 0
    choices = []

    for dx, dy in neighbors:
        ni, nj = (i + dx) % row, (j + dy) % col
        if grid[i][j] == grid[ni][nj]:
            Ni += 1
        elif grid[i][j] > grid[ni][nj]:
            choices.append((ni, nj))

    Z = surface.Z
    return random.choice(choices) if (Ni < Z and len(choices) > 0) else [-1, -1]


def check(theta_max: int, max_height: int) -> bool:
    return theta_max > max_height


def get_random_coordinate(row: int, col: int) -> tuple[int, int]:
    return random.randint(0, row - 1), random.randint(0, col - 1)
