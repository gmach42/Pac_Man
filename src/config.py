# TODO strip comments -> json -> validation/clamp -> GameConfig (dataclass)
from dataclasses import dataclass


@dataclass
class GameConfig:
    width: int
    height: int
    seed: int
    perfect: bool = False
