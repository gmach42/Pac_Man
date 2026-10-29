import logging
import json
import pytest

from src.config import RULES, GameConfig, load_config, read_config_file
from dataclasses import fields
from pathlib import Path

# === TEST load_config ===


def test_empty_dict_gives_defaults() -> None:
    assert load_config({}) == GameConfig()


@pytest.mark.parametrize(
    ("key", "value", "expected"),
    [
        ("width", 21, 21),  # valid
        ("width", -5, 10),  # too small -> clamp
        ("width", 999, 50),  # too big -> clamp
        ("width", "big", 15),  # wrong type -> défaut
        ("lives", True, 3),  # bool refused -> défaut
        # ("player_speed", 6, 6.0),  # int accepted for float
        ("highscore_filename", 5, "highscores.json"),
        ("highscore_filename", "  ", "highscores.json"),
    ],
)
def test_single_value(key: str, value: object, expected: object) -> None:
    config = load_config({key: value})
    assert getattr(config, key) == expected


def test_unknown_key_is_ignored_and_logged(
    caplog: pytest.LogCaptureFixture, ) -> None:
    with caplog.at_level(logging.WARNING):
        config = load_config({"favorite_color": "yellow"})
    assert config == GameConfig()
    assert "favorite_color" in caplog.text


def test_invalid_value_is_logged(caplog: pytest.LogCaptureFixture) -> None:
    with caplog.at_level(logging.WARNING):
        load_config({"width": "big"})
    assert "width" in caplog.text


def test_rules_match_config() -> None:
    assert set(RULES) == {f.name for f in fields(GameConfig)}


# === TEST read_config_file ===


def test_comments_are_ignored(tmp_path: Path) -> None:
    f = tmp_path / "c.json"
    f.write_text('# comment\n{\n  # inner\n  "width": 21\n}\n')
    assert read_config_file(str(f)) == {"width": 21}


@pytest.mark.parametrize(
    ("content", "error"),
    [
        ("", json.JSONDecodeError),
        ('{"width": 15\n"height": 15}', json.JSONDecodeError),
        ("[1, 2]", ValueError),
    ],
)
def test_bad_files_raise(tmp_path: Path, content: str,
                         error: type[Exception]) -> None:
    f = tmp_path / "c.json"
    f.write_text(content)
    with pytest.raises(error):
        read_config_file(str(f))


def test_missing_file_raises() -> None:
    with pytest.raises(FileNotFoundError):
        read_config_file("does_not_exist.json")
