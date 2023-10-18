class Surface:
    def __init__(self, row: int, col: int, theta_dep: int, theta_max: int, Z: int) -> None:
        # input from user
        self.row = row
        self.col = col
        self.theta_dep = theta_dep
        self.theta_max = theta_max
        self.Z = Z

        # additional properties
        self._max_height = 0
        self._average_height = 0
        self._total_particle = 0

        # initialize the grid
        self._grid = [[0 for _ in range(col)] for _ in range(row)]

    def get_average_height(self) -> float:
        return self.get_total_particle() / (self.row * self.col)

    def set_total_particle(self) -> None:
        self._total_particle = self.get_total_particle() + (self.theta_dep *
                                                            self.row * self.col)

    def get_total_particle(self) -> int:
        return self._total_particle

    def set_max_height(self, height: int) -> None:
        self._max_height = max(self._max_height, height)

    def get_max_height(self) -> int:
        return self._max_height

    def get_grid(self) -> list[list[int]]:
        return self._grid

    def print_grid(self) -> None:
        for row in self._grid:
            print(row)
        print()
