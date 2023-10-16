class Surface:
    def __init__(self, row: int, col: int, theta_dep: int, max_height: int, average_height: int = 0, total_particle: int = 0) -> None:
        self.row = row  # get input from user
        self.col = col  # get input from user
        self.theta_dep = theta_dep  # input from user
        self._average_height = 0
        self._total_particle = 0
        self._max_height = max_height
        self._grid = [[0 for _ in range(col)] for _ in range(row)]

    def get_average_height(self) -> float:
        return self.get_total_particle() / (self.row * self.col)

    def set_total_particle(self) -> None:
        self.total_particle = self.get_total_particle() + (self.theta_dep*self.row*self.col)
        self.set_average_height()

    def get_total_particle(self) -> int:
        return self._total_particle
