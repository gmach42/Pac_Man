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
    """"N/E/S/W avec dx, dy et le bit de mur associé"""
    N = (0, -1, Border.NORTH)
    E = (1, 0, Border.EAST)
    S = (0, 1, Border.SOUTH)
    W = (-1, 0, Border.WEST)


class MazeError(Exception):

    def __init__(self, msg: str) -> None:
        super().__init__(f"MazeError:\n{msg}")


class Maze:

    def __init__(self, width: int, height: int, seed: int):
        self.width = width
        self.height = height
        self.seed = seed
        self.perfect: bool = False

    def build_maze(self) -> MazeGenerator:
        try:
            maze = MazeGenerator(size=(self.width, self.height),
                                 seed=self.seed,
                                 perfect=self.perfect)
        except Exception as e:
            raise MazeError(
                "An error happened while trying to create a maze of "
                f"{self.width=}, {self.height=}:\n{e}")
        return maze
