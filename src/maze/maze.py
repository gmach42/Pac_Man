from mazegenerator import MazeGenerator
from enum import IntFlag, Enum


class Border(IntFlag):
    """Represents the borders of a maze cell."""
    EMPTY = 0
    NORTH = 0b0001  # NORTH = 1
    EAST = 0b0010  # EAST = 2
    SOUTH = 0b0100  # SOUTH = 4
    WEST = 0b1000  # WEST = 8


class Direction(Enum):
    """N/E/S/W avec dx, dy et le bit de mur associé"""
    N = (0, -1, Border.NORTH)
    E = (1, 0, Border.EAST)
    S = (0, 1, Border.SOUTH)
    W = (-1, 0, Border.WEST)


class MazeError(Exception):

    def __init__(self, msg: str) -> None:
        super().__init__(f"MazeError:\n{msg}")


class Maze:

    def __init__(self, grid: list[list[int]]):
        self._grid = grid
        self.width = len(grid[0])
        self.height = len(grid)
        self.perfect: bool = False
        self.center = (self.width // 2, self.height // 2)
        self.corners = [(0, 0), (self.width - 1, 0), (0, self.height - 1),
                        (self.width - 1, self.height - 1)]

    def has_wall(self, x: int, y: int, d: Direction) -> bool:
        ...

    def is_open(self, x: int, y: int) -> bool:
        ...  # != 15

    def neighbors(self, x: int, y: int) -> list[tuple[int, int]]:
        ...


def build_maze(width: int, height: int, seed: int) -> Maze:
    try:
        gen = MazeGenerator(size=(width, height), perfect=False, seed=seed)
    except Exception as e:
        raise MazeError("An error happened while trying to create a maze of "
                        f"{width=}, {height=}:\n") from e
    return Maze(gen.maze)
