from mazegenerator import MazeGenerator


def generate_maze(width: int,
                  height: int,
                  seed: int = 42,
                  perfect: bool = False) -> MazeGenerator:
    return MazeGenerator(size=(width, height), seed=seed, perfect=perfect)
