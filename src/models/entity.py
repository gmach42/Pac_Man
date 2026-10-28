from enum import Enum
from src.maze.maze import Border
from abc import ABC, abstractmethod


class Command(Enum):
    """Represents possible commands for an entity."""
    MOVE_NORTH = 1
    MOVE_EAST = 2
    MOVE_SOUTH = 3
    MOVE_WEST = 4
    PAUSE = 5
    CONFIRM = 6
    BACK = 7
    ACTIVATE_CHEAT = 8


class GhostState(Enum):
    CHASE = 1
    FRIGHTENED = 2
    EATEN = 3


class Entity(ABC):

    @abstractmethod
    def __init__(self, pos, dir, progress, state):
        self.pos = pos
        self.dir = dir
        self.progress = progress
        self.state = state


class Player(Entity):
    # pos, dir, progress, state
    pass


class Ghost(Entity):
    # pos, dir, progress, state
    pass


class Level:
    pass


class GameSession:
    # player, ghosts, level, score, lives
    pass
