from src.config import GameConfig
from src.contract import Direction
from src.maze.maze import Maze, build_maze

GRID = [[13, 7, 15]]

GRID_2D = [[9, 5, 3],
           [14, 15, 14]]


def test_has_wall() -> None:
    m = Maze(GRID)
    assert m.has_wall(0, 0, Direction.W)  # check wall west


def test_no_wall_between_first_two_cells() -> None:
    m = Maze(GRID)
    assert not m.has_wall(0, 0, Direction.E)  # check no wall east


def test_open() -> None:
    m = Maze(GRID)
    assert m.is_open(0, 0)  # check cell open east
    assert not m.is_open(-1, 0)  # check cell out of maze
    assert not m.is_open(2, 0)  # check full cell


def test_neighbors() -> None:
    m = Maze(GRID)
    assert m.neighbors(0, 0) == [(1, 0)]
    assert m.neighbors(1, 0) == [(0, 0)]
    assert not m.neighbors(2, 0)
    assert not m.neighbors(-1, 0)


def test_size() -> None:
    m = Maze(GRID_2D)
    assert m.width == 3
    assert m.height == 2


def test_wall_out_of_maze() -> None:
    m = Maze(GRID)
    assert m.has_wall(-1, 0, Direction.E)  # out of maze = wall
    assert m.has_wall(3, 0, Direction.W)
    assert m.has_wall(0, 1, Direction.N)


def test_wall_2d() -> None:
    m = Maze(GRID_2D)
    assert not m.has_wall(0, 0, Direction.S)  # vertical passage
    assert m.has_wall(1, 0, Direction.S)
    assert not m.has_wall(2, 1, Direction.N)
    assert m.has_wall(0, 1, Direction.E)


def test_neighbors_2d() -> None:
    m = Maze(GRID_2D)
    assert sorted(m.neighbors(0, 0)) == [(0, 1), (1, 0)]
    assert sorted(m.neighbors(1, 0)) == [(0, 0), (2, 0)]
    assert m.neighbors(0, 1) == [(0, 0)]
    assert m.neighbors(2, 1) == [(2, 0)]
    assert m.neighbors(1, 1) == []  # closed cell


def test_real_maze_size() -> None:
    config = GameConfig()
    m = build_maze(config)
    assert m.width == config.width
    assert m.height == config.height


def test_real_maze_neighbors_are_open() -> None:
    m = build_maze(GameConfig())
    for y in range(m.height):
        for x in range(m.width):
            for nx, ny in m.neighbors(x, y):
                assert m.is_open(nx, ny)
