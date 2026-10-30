"""Hardcoded AppView so rendering can be built before the game logic.

Delete once the real App exists. mypy checks it matches src/contract.py.
"""

from dataclasses import dataclass, field

from src.contract import (
    AppView,
    Border,
    Direction,
    GhostState,
    Pos,
    Scene,
)

WIDTH = 10
HEIGHT = 8
# (x, y) cells with a wall on their east side, to get some corridors
_EAST_WALLS = {(2, 1), (2, 2), (6, 4), (6, 5), (4, 6)}


def _make_grid() -> list[list[int]]:
    grid = [[0] * WIDTH for _ in range(HEIGHT)]
    for x in range(WIDTH):
        grid[0][x] |= Border.NORTH
        grid[HEIGHT - 1][x] |= Border.SOUTH
    for y in range(HEIGHT):
        grid[y][0] |= Border.WEST
        grid[y][WIDTH - 1] |= Border.EAST
    for x, y in _EAST_WALLS:
        grid[y][x] |= Border.EAST
        grid[y][x + 1] |= Border.WEST
    grid[3][4] = grid[3][5] = 15  # closed cells, like the "42" pattern
    return grid


@dataclass(frozen=True)
class FakeMaze:
    grid: list[list[int]] = field(default_factory=_make_grid)
    width: int = WIDTH
    height: int = HEIGHT

    def has_wall(self, x: int, y: int, d: Direction) -> bool:
        return bool(self.grid[y][x] & d.wall)

    def is_open(self, x: int, y: int) -> bool:
        return self.grid[y][x] != 15


@dataclass(frozen=True)
class FakePlayer:
    pos: Pos = (4, 4)
    direction: Direction | None = Direction.E
    progress: float = 0.5


@dataclass(frozen=True)
class FakeGhost:
    index: int
    pos: Pos
    state: GhostState
    direction: Direction | None = Direction.N
    progress: float = 0.0
    frightened_left: float = 0.0


@dataclass(frozen=True)
class FakeLevel:
    maze: FakeMaze = field(default_factory=FakeMaze)
    player: FakePlayer = field(default_factory=FakePlayer)
    ghosts: list[FakeGhost] = field(default_factory=lambda: [
        FakeGhost(0, (1, 1), GhostState.CHASE),
        FakeGhost(1, (8, 1), GhostState.FRIGHTENED, frightened_left=3.0),
        FakeGhost(2, (1, 6), GhostState.EATEN),
        FakeGhost(3, (8, 6), GhostState.CHASE, Direction.W, 0.3),
    ])
    pacgums: frozenset[Pos] = frozenset(
        (x, y) for x in range(1, WIDTH - 1) for y in (2, 5)
    )
    super_pacgums: frozenset[Pos] = frozenset(
        {(0, 0), (WIDTH - 1, 0), (0, HEIGHT - 1), (WIDTH - 1, HEIGHT - 1)}
    )
    time_left: float = 72.5


@dataclass(frozen=True)
class FakeSession:
    score: int = 1230
    lives: int = 2
    level_number: int = 3
    level_count: int = 10
    cheats_enabled: bool = False
    level: FakeLevel = field(default_factory=FakeLevel)


@dataclass(frozen=True)
class FakeApp:
    scene: Scene = Scene.PLAYING
    running: bool = True
    menu_index: int = 0
    session: FakeSession | None = field(default_factory=FakeSession)
    highscores: list[tuple[str, int]] = field(default_factory=lambda: [
        ("lucpelle", 4200), ("gmach", 4100), ("marvin", 42),
    ])
    name_buffer: str = ""


def make_fake_app(scene: Scene = Scene.PLAYING) -> AppView:
    """Return a fake state for the given scene."""
    return FakeApp(scene=scene)
