"""Where this pack, RSMM and the game live, for every tool in tools/.

RSMM and the game are found in this order:
    1. paths.toml at the pack root (copy paths.example.toml), keys `rsmm` and `game`
    2. the RSMM_HOME and RSMM_GAME_DIR environment variables
    3. for the game only: the default Steam library
"""

from __future__ import annotations

import os
import sys
import tomllib
from pathlib import Path

PACK = Path(__file__).resolve().parent.parent
MODS = PACK / "mods"
PATHS_FILE = PACK / "paths.toml"
DEFAULT_GAME = Path(r"C:\Program Files (x86)\Steam\steamapps\common\Ravenswatch")


def _config() -> dict:
    try:
        return tomllib.loads(PATHS_FILE.read_text(encoding="utf-8"))
    except (OSError, tomllib.TOMLDecodeError):
        return {}


def rsmm_dir() -> Path | None:
    """The RSMM checkout (the folder holding the `rsmm` script), or None."""
    v = _config().get("rsmm") or os.environ.get("RSMM_HOME")
    p = Path(v) if v else None
    return p if p and (p / "rsmm").is_file() else None


def game_dir() -> Path:
    v = _config().get("game") or os.environ.get("RSMM_GAME_DIR")
    return Path(v) if v else DEFAULT_GAME


def apply_command() -> list[str]:
    """`rsmm apply` as an argv; raises with a fix when RSMM can't be found."""
    r = rsmm_dir()
    if r is None:
        raise FileNotFoundError(
            f"RSMM not found. Copy paths.example.toml to {PATHS_FILE.name} and set `rsmm` "
            f"to your RavenswatchModManager folder (or set RSMM_HOME).")
    return [sys.executable, str(r / "rsmm"), "apply"]
