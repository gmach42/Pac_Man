from mazegenerator import MazeGenerator

from src.config import GameConfig
from src.contract import Direction


class MazeError(Exception):

    def __init__(self, msg: str) -> None:
        super().__init__(f"MazeError:\n{msg}")


class Maze:
    """Maze grid from mazegenerator.

    The grid is sorted line by line: a cell is read with self._grid[y][x],
    NOT self._grid[x][y]. Each cell stores its walls as bits
    (1=N, 2=E, 4=S, 8=W); 15 means a closed cell ("42" pattern).
    """

    def __init__(self, grid: list[list[int]]):
        self._grid: list[list[int]] = grid
        self.width: int = len(grid[0])
        self.height: int = len(grid)
        self.center: tuple[int, int] = (self.width // 2, self.height // 2)
        self.corners: list[tuple[int, int]] = [
            (0, 0),
            (self.width - 1, 0),
            (0, self.height - 1),
            (self.width - 1, self.height - 1),
        ]

    def has_wall(self, x: int, y: int, d: Direction) -> bool:
        """Check if when looking into a Direction d, a cell has a wall

        Returns True if there is a wall, or if the cell is out of the maze.
        """
        if not (0 <= x < self.width and 0 <= y < self.height):
            return True
        return (self._grid[y][x] & d.wall) != 0

    def is_open(self, x: int, y: int) -> bool:
        """Returns True if the cell is in the maze and is open != 15"""
        if not (0 <= x < self.width and 0 <= y < self.height):
            return False
        return self._grid[y][x] != 15

    def neighbors(self, x: int, y: int) -> list[tuple[int, int]]:
        """Returns a list of neighbors accessible for a given cell"""
        res: list[tuple[int, int]] = []
        if not self.is_open(x, y):
            return res
        for d in Direction:
            if not self.has_wall(x, y, d):
                res.append((x + d.dx, y + d.dy))
        return res


def build_maze(config: GameConfig) -> Maze:
    try:
        gen = MazeGenerator(size=(config.width, config.height),
                            perfect=False,
                            seed=config.seed)
    except Exception as e:
        raise MazeError("An error happened while trying to create a maze of "
                        f"{config.width=}, {config.height=}:\n") from e
    return Maze(gen.maze)
