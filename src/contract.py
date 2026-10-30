"""Shared contract between game logic and rendering.

Rules:
- logic (src/maze, src/models, src/highscores...) never imports pygame;
- rendering only reads the state below, it never mutates it;
- rendering -> logic: Command / TextInput only;
- logic -> rendering: AppView (read-only properties);
- time is passed explicitly: update(dt) with dt in seconds.

Main loop (pac-man.py):

    while app.running:
        for event in inputs.poll():   # rendering: pygame events -> Input
            app.handle(event)         # logic
        app.update(dt)                # logic
        renderer.draw(app)            # rendering

Coordinates: Pos = (x, y) in cells, x to the right, y downwards,
origin at the top-left corner. Pixel size is a rendering concern only.
"""

from collections.abc import Sequence, Set
from dataclasses import dataclass
from enum import Enum, IntFlag, auto
from typing import Protocol

Pos = tuple[int, int]


class Border(IntFlag):
    """Wall bits of a maze cell, as produced by mazegenerator."""

    EMPTY = 0
    NORTH = 0b0001
    EAST = 0b0010
    SOUTH = 0b0100
    WEST = 0b1000


class Direction(Enum):
    """N/E/S/W with dx, dy and the matching wall bit."""

    N = (0, -1, Border.NORTH)
    E = (1, 0, Border.EAST)
    S = (0, 1, Border.SOUTH)
    W = (-1, 0, Border.WEST)

    @property
    def dx(self) -> int:
        return self.value[0]

    @property
    def dy(self) -> int:
        return self.value[1]

    @property
    def wall(self) -> Border:
        return self.value[2]


class GhostState(Enum):
    CHASE = auto()
    FRIGHTENED = auto()
    EATEN = auto()  # back in its corner, waiting to respawn


class Scene(Enum):
    """Screen currently displayed. Name entry is part of GAME_OVER/VICTORY."""

    MENU = auto()
    HIGHSCORES = auto()
    INSTRUCTIONS = auto()
    PLAYING = auto()
    PAUSED = auto()
    GAME_OVER = auto()
    VICTORY = auto()


class Command(Enum):
    """Abstract inputs. UP/DOWN/LEFT/RIGHT also navigate menus."""

    UP = auto()
    DOWN = auto()
    LEFT = auto()
    RIGHT = auto()
    CONFIRM = auto()
    BACK = auto()
    PAUSE = auto()
    BACKSPACE = auto()
    CHEAT_TOGGLE = auto()
    CHEAT_SKIP_LEVEL = auto()
    CHEAT_FREEZE = auto()
    CHEAT_INVINCIBLE = auto()
    CHEAT_EXTRA_LIFE = auto()


@dataclass(frozen=True)
class TextInput:
    """One typed character, used for name entry. Filtered by the logic."""

    char: str


Input = Command | TextInput


class MazeView(Protocol):
    @property
    def width(self) -> int: ...

    @property
    def height(self) -> int: ...

    def has_wall(self, x: int, y: int, d: Direction) -> bool: ...

    def is_open(self, x: int, y: int) -> bool:
        """False for the closed cells of the '42' pattern."""
        ...


class EntityView(Protocol):
    """Drawn at (pos + direction * progress) * tile_size."""

    @property
    def pos(self) -> Pos:
        """Last cell reached."""
        ...

    @property
    def direction(self) -> Direction | None:
        """None when standing still."""
        ...

    @property
    def progress(self) -> float:
        """0..1, progress from pos towards the next cell."""
        ...


class GhostView(EntityView, Protocol):
    @property
    def index(self) -> int:
        """0..3, rendering picks the color/sprite from it."""
        ...

    @property
    def state(self) -> GhostState: ...

    @property
    def frightened_left(self) -> float:
        """Seconds left in FRIGHTENED state (for blinking), else 0."""
        ...


class LevelView(Protocol):
    @property
    def maze(self) -> MazeView: ...

    @property
    def player(self) -> EntityView: ...

    @property
    def ghosts(self) -> Sequence[GhostView]: ...

    @property
    def pacgums(self) -> Set[Pos]: ...

    @property
    def super_pacgums(self) -> Set[Pos]: ...

    @property
    def time_left(self) -> float:
        """Seconds left before the level time limit."""
        ...


class SessionView(Protocol):
    @property
    def score(self) -> int: ...

    @property
    def lives(self) -> int: ...

    @property
    def level_number(self) -> int:
        """1-based."""
        ...

    @property
    def level_count(self) -> int: ...

    @property
    def cheats_enabled(self) -> bool: ...

    @property
    def level(self) -> LevelView: ...


class AppView(Protocol):
    """Everything the renderer receives in draw()."""

    @property
    def running(self) -> bool: ...

    @property
    def scene(self) -> Scene: ...

    @property
    def menu_index(self) -> int:
        """Selected entry of the current menu (main or pause)."""
        ...

    @property
    def session(self) -> SessionView | None:
        """None outside of a game (main menu, highscores, instructions)."""
        ...

    @property
    def highscores(self) -> Sequence[tuple[str, int]]:
        """At most 10 (name, score), best first."""
        ...

    @property
    def name_buffer(self) -> str:
        """Name being typed on GAME_OVER/VICTORY."""
        ...
