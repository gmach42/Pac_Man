from src.maze import Maze, build_maze
from src.config import load_config


def main() -> None:
    config = load_config('config.json')
    maze: Maze = build_maze(config)
    print(maze._grid)


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(e)
