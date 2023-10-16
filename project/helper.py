import random
from project.classes.Surface import Surface

def isMobile(i:int, j:int, Z:int, grid:list[list[int]])->list[int]:
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

    return random.choice(c) if Ni>Z and len(c)>0 else []

    # if Ni > Z and len(c) > 0:
    #     random_pair = random.choice(c)
       
    #     #if it is true then only we will see the "c" storage array and if it is empty we cannot move else diffuse it in any of the pair
    # return random_pair