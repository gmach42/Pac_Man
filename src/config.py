# TODO strip comments -> json -> validation/clamp -> GameConfig (dataclass)
import json
import logging
from dataclasses import asdict, dataclass, fields

logger = logging.getLogger(__name__)


@dataclass(frozen=True)
class Rule:
    kind: type
    low: float | None = None
    high: float | None = None


RULES: dict[str, Rule] = {
    "highscore_filename": Rule(str),
    "levels": Rule(int, 1, 99),
    "width": Rule(int, 10, 50),
    "height": Rule(int, 10, 50),
    "seed": Rule(int, 0, 2147483647),
    "level_max_time": Rule(int, 10, 600),
    "lives": Rule(int, 1, 99),
    # "player_speed": Rule(float, 1, 10),
    # "ghost_speed": Rule(float, 1, 10),
    # "frightened_duration": Rule(float, 1, 10),
    # "ghost_respawn_delay": Rule(float, 1, 10),
    "points_per_pacgum": Rule(int, 0, 10_000),
    "points_per_super_pacgum": Rule(int, 0, 10_000),
    "points_per_ghost": Rule(int, 0, 10_000),
}


@dataclass
class GameConfig:
    """Default Game Config"""

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
    # player_speed: float = 6.0

    # # Ghosts
    # ghost_speed: float = 5.0
    # frightened_duration: float = 7
    # ghost_respawn_delay: float = 5

    # Scoring
    points_per_pacgum: int = 10
    points_per_super_pacgum: int = 50
    points_per_ghost: int = 200


def test_rules_match_config() -> None:
    assert set(RULES) == {f.name for f in fields(GameConfig)}


def _check(key: str, value: object, rule: Rule, default: object) -> object:
    if (rule.kind is float and isinstance(value, int)
            and not isinstance(value, bool)):
        value = float(value)
    if isinstance(value, bool) or not isinstance(value, rule.kind):
        logger.warning("'%s': expected %s, got %r -> default %r", key,
                       rule.kind.__name__, value, default)
        return default
    if isinstance(value, (int, float)) and not isinstance(value, bool):
        if value < rule.low:
            logger.warning(
                "'%s'=%r below minimal value %r -> clamped",
                key,
                value,
                rule.low,
            )
            return rule.kind(rule.low)
        if value > rule.high:
            logger.warning(
                "'%s'=%r above maximal value %r -> clamped",
                key,
                value,
                rule.high,
            )
            return rule.kind(rule.high)
    if isinstance(value, str) and not value.strip():
        logger.warning("'%s' is empty -> default %r", key, default)
        return default
    return value


def read_config_file(path: str) -> dict[str, object]:
    """Read a JSON file where lines starting with '#' are comments."""
    with open(path, encoding="utf-8") as f:
        lines = ["\n" if line.lstrip().startswith("#") else line for line in f]
    data = json.loads("".join(lines))
    if not isinstance(data, dict):
        raise ValueError("top-level JSON value must be an object")
    return data


def load_config(data: dict[str, object]) -> GameConfig:
    defaults = asdict(GameConfig())
    values: dict[str, object] = {}
    for key, rule in RULES.items():
        if key not in data:
            logger.info("'%s' missing -> default %r", key, defaults[key])
            values[key] = defaults[key]
        else:
            values[key] = _check(key, data[key], rule, defaults[key])
    for key in data.keys() - RULES.keys():
        logger.warning("unknown key '%s' ignored", key)
    return GameConfig(**values)
