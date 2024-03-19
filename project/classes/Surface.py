import numpy as np


class Surface:
    _grid = [[]]
    grid = np.array(_grid, dtype=int)

    def __init__(self, row: int, col: int, theta_dep: float, theta_max: int, Z: int, tau: float, freq: int) -> None:
        """
        Initializes an instance of the class Surface

        Args:
            row (int): The number of rows in the grid.
            col (int): The number of columns in the grid.
            theta_dep (int): The depth of the grid.
            theta_max (int): The maximum theta value.
            Z (int): The Z value.

        Returns:
            None

        Raises:
            None
        """
        # input from user
        self.row = row
        self.col = col
        self.theta_dep = theta_dep
        self.theta_max = theta_max
        self.Z = Z
        self.tau = tau
        self.freq = freq
        self._total_particle = 0
        self._max_height = 0
        self.grid = np.zeros((self.row, self.col), dtype=int)

    def get_average_height(self) -> float:
        """
        Calculates and returns the average height of a particle in the grid.

        Returns:
            float: The average height of a particle in the grid.
        """
        return self.get_total_particle() / (self.row * self.col)

    def set_total_particle(self) -> None:
        """
        Set the total number of particles.

        This function calculates the total number of particles based on the current
        value of `total_particle` and the values of `theta_dep`, `row`, and `col`.
        The calculated value is then assigned to the `total_particle` attribute.

        Parameters:
        - None

        Returns:
        - None
        """
        self._total_particle = self.get_total_particle() + 1*(self.theta_dep *
                                                              self.row * self.col)

    def get_total_particle(self) -> int:
        """
        Return the total number of particles.

        :return: An integer representing the total number of particles.
        """
        return self._total_particle

    def set_max_height(self, height: int) -> None:
        """
        Set the maximum height of the object.

        Args:
            height (int): The height to set as the maximum height.

        Returns:
            None: This function does not return anything.
        """
        self._max_height = max(self._max_height, height)

    def get_max_height(self) -> int:
        """
        Return the maximum height of the object.

        :return: An integer representing the maximum height.
        """
        return self._max_height

    def print_grid(self) -> None:
        """
        Print the grid.

        This function iterates over each row in the grid and prints it.

        Parameters:
            None

        Returns:
            None
        """
        for row in self.grid:
            print(row)
        print()
