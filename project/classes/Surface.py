class Surface:
    def __init__(self, row: int, col: int, theta_dep: int, theta_max: int, Z: int) -> None:
        self.row = row  # get input from user
        self.col = col  # get input from user
        self.theta_dep = theta_dep  # input from user
        self.theta_max = theta_max
        self.Z = Z
        self._max_height = 0

        self._average_height = 0
        self._total_particle = 0

        # initialize the grid
        self._grid = [[0 for _ in range(col)] for _ in range(row)]

    def get_average_height(self) -> float:
        return self.get_total_particle() / (self.row * self.col)

    def set_total_particle(self) -> None:
        print("Setting total particle")
        self._total_particle = self.get_total_particle() + (self.theta_dep*self.row*self.col)

    def get_total_particle(self) -> int:
        return self._total_particle

    def set_max_height(self, height: int) -> None:
        self._max_height = max(self._max_height, height)

    def get_max_height(self) -> int:
        return self._max_height

    def get_grid(self):
        return self._grid
