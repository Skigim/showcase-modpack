"""Where this pack and RSMM live, for the tools in tools/.

RSMM is found in this order:
    1. paths.toml at the pack root (copy paths.example.toml), key `rsmm`
    2. the RSMM_HOME environment variable
"""

from __future__ import annotations

import os
import tomllib
from pathlib import Path

PACK = Path(__file__).resolve().parent.parent
MODS = PACK / "mods"
PATHS_FILE = PACK / "paths.toml"


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
