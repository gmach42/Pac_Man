import json
import logging
import sys

from src.config import load_config, read_config_file
from src.maze import Maze, build_maze


def main() -> None:

    logging.basicConfig(
        level=logging.INFO,
        format="[%(levelname)s] %(name)s: %(message)s",
    )

    try:
        raw = read_config_file(sys.argv[1])
    except FileNotFoundError:
        print(f"Error: config file '{sys.argv[1]}' not found", file=sys.stderr)
        sys.exit(1)
    except json.JSONDecodeError as e:
        print(f"Error: invalid JSON line {e.lineno}: {e.msg}", file=sys.stderr)
        sys.exit(1)
    except (OSError, UnicodeDecodeError, ValueError) as e:
        print(f"Error: cannot read config: {e}", file=sys.stderr)
        sys.exit(1)
    config = load_config(raw)

    try:
        maze: Maze = build_maze(config)
    except Exception as e:
        print(e)


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"Error: unexpected {type(e).__name__}: {e}", file=sys.stderr)
        sys.exit(1)
