from mazegenerator import MazeGenerator
from enum import IntFlag, Enum


class Border(IntFlag):
    """Represents the borders of a maze cell."""
    EMPTY = 0
    NORTH = 0b0001  # NORTH = 1
    EAST = 0b0010  # EAST = 2
    SOUTH = 0b0100  # SOUTH = 4
    WEST = 0b1000  # WEST = 8


class MazeError(Exception):

    def __init__(self, msg: str) -> None:
        super().__init__(f"MazeError:\n{msg}")


class Maze:

    def __init__(self, width: int, height: int, seed: int):
        self.width = width
        self.height = height
        self.seed = seed
        self.perfect: bool = False
        self.center = (self.width // 2, self.height // 2)
        self.corners = [
            (0, 0),
            (self.width - 1, 0),
            (0, self.height - 1),
            (self.width - 1, self.height - 1)
        ]

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
