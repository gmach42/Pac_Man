import json
import logging
import sys

from src.config import load_config, read_config_file

USAGE = "usage: python3 pac-man.py <config.json>"


def die(message: str) -> None:
    """Print an error on stderr and exit with status 1."""
    print(f"Error: {message}", file=sys.stderr)
    sys.exit(1)


def main() -> None:

    logging.basicConfig(
        level=logging.INFO,
        format="[%(levelname)s] %(name)s: %(message)s",
    )

    if len(sys.argv) != 2:
        die(f"expected 1 argument, got {len(sys.argv) - 1}\n{USAGE}")
    path = sys.argv[1]

    try:
        raw = read_config_file(path)
    except FileNotFoundError:
        die(f"config file '{path}' not found")
    except IsADirectoryError:
        die(f"'{path}' is a directory, not a config file")
    except PermissionError:
        die(f"permission denied when reading '{path}'")
    except json.JSONDecodeError as e:
        die(f"'{path}' line {e.lineno}, column {e.colno}: {e.msg}")
    except UnicodeDecodeError:
        die(f"'{path}' is not a text file")
    except (OSError, ValueError) as e:
        die(f"cannot read '{path}': {e}")
    config = load_config(raw)


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        sys.exit(130)
    except Exception as e:
        print(f"Error: unexpected {type(e).__name__}: {e}", file=sys.stderr)
        sys.exit(1)
