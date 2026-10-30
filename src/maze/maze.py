from mazegenerator import MazeGenerator

from src.config import GameConfig
from src.contract import Direction


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
        self.corners = [
            (0, 0),
            (self.width - 1, 0),
            (0, self.height - 1),
            (self.width - 1, self.height - 1),
        ]

    def has_wall(self, x: int, y: int, d: Direction) -> bool: ...

    def is_open(self, x: int, y: int) -> bool: ...  # != 15

    def neighbors(self, x: int, y: int) -> list[tuple[int, int]]: ...


def build_maze(config: GameConfig) -> Maze:
    try:
        gen = MazeGenerator(
            size=(config.width, config.height), perfect=False, seed=config.seed
        )
    except Exception as e:
        raise MazeError(
            "An error happened while trying to create a maze of "
            f"{config.width=}, {config.height=}:\n"
        ) from e
    return Maze(gen.maze)
