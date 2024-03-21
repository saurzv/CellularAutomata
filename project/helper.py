import random
from project.classes.config import surface


def isMobile(i: int, j: int) -> tuple[int, int]:
    """
    Generate the function comment for the given function body in a markdown code block with the correct language syntax.

    Parameters:
    i (int): The first integer parameter.
    j (int): The second integer parameter.
    surface (Surface): The surface object.

    Returns:
    tuple[int, int]: A tuple containing two integers representing the result of the function.
    """
    row = surface.row
    col = surface.col
    neighbors = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    Ni = 0
    choices = [((i+dx) % row, (j+dy) % col) for dx, dy in neighbors if surface.grid[i]
               [j] > surface.grid[(i+dx) % row][(j+dy) % col]]

    # for dx, dy in neighbors:
    #     ni, nj = (i + dx) % row, (j + dy) % col
    #     if surface.grid[i][j] == surface.grid[ni][nj]:
    #         Ni += 1
    #         if Ni >= surface.Z:
    #             return [-1, -1]
    #     elif surface.grid[i][j] > surface.grid[ni][nj]:
    #         choices.append((ni, nj))

    # Z = surface.Z
    # return random.choice(choices) if (Ni < Z and len(choices) > 0) else [-1, -1]

    for ni, nj in choices:
        if surface.grid[i][j] == surface.grid[ni][nj]:
            Ni += 1
            if Ni >= surface.Z:
                return [-1, -1]

    return random.choice(choices) if len(choices) > 0 else [-1, -1]


def check(theta_max: int, max_height: int) -> bool:
    """
    Check if theta_max is greater than max_height.

    Args:
        theta_max (int): The maximum theta value.
        max_height (int): The maximum height value.

    Returns:
        bool: True if theta_max is greater than max_height, False otherwise.
    """
    return theta_max > max_height


def get_random_coordinate(row: int, col: int) -> tuple[int, int]:
    """
    Get a random coordinate within the given row and column range.

    :param row: An integer representing the number of rows.
    :param col: An integer representing the number of columns.
    :return: A tuple of two integers representing the random coordinate.
    """
    return random.randint(0, row - 1), random.randint(0, col - 1)

# write function to calc std deviation of 2d np array
# make graph of roughness vs no iterations (time)
