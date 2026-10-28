# TODO strip comments -> json -> validation/clamp -> GameConfig (dataclass)
from dataclasses import dataclass


@dataclass
class GameConfig:
    # Highscores
    highscore_filename: str = "highscores.json"

    # Maze
    levels: int = 10
    width: int = 15
    height: int = 15
    seed: int = 42
    level_max_time: int = 90

    # Player
    lives: int = 3

    # Scoring
    points_per_pacgum: int = 10
    points_per_super_pacgum: int = 50
    points_per_ghost: int = 200


def load_config(config: dict) -> GameConfig:
    pass
