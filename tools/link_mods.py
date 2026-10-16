"""Make RSMM see this pack's mods: one directory junction per mod in RSMM's mods/.

    python tools/link_mods.py           link every mod under mods/
    python tools/link_mods.py --unlink  remove those links (the mods here are untouched)

A junction needs no admin rights. RSMM then builds, applies and packs the mods
in place, so edits here are what the game gets. An existing real folder of the
same name in RSMM's mods/ is never touched: move it aside and run this again.
"""

from __future__ import annotations

import os
import subprocess
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import paths  # noqa: E402


def points_here(link: Path, target: Path) -> bool:
    return os.path.realpath(link) == os.path.realpath(target)


def main(argv: list[str]) -> int:
    rsmm = paths.rsmm_dir()
    if rsmm is None:
        print(f"RSMM not found. Copy paths.example.toml to paths.toml and set `rsmm` "
              f"(or set RSMM_HOME).")
        return 2
    dest = rsmm / "mods"
    dest.mkdir(exist_ok=True)
    unlink = "--unlink" in argv
    bad = 0
    for mod in sorted(p for p in paths.MODS.iterdir() if (p / "manifest.toml").is_file()):
        link = dest / mod.name
        linked = link.is_junction() or link.is_symlink()
        if unlink:
            if linked and points_here(link, mod):
                os.rmdir(link)          # removes the junction only, never its contents
                print(f"unlinked  {mod.name}")
            continue
        if linked and points_here(link, mod):
            print(f"ok        {mod.name}")
        elif link.exists() or linked:
            print(f"SKIPPED   {mod.name}: {link} already exists and is not a link to this pack; "
                  f"move it aside and run this again")
            bad += 1
        else:
            r = subprocess.run(["cmd", "/c", "mklink", "/J", str(link), str(mod)],
                               capture_output=True, text=True)
            print(f"linked    {mod.name}" if r.returncode == 0 else
                  f"FAILED    {mod.name}: {(r.stdout + r.stderr).strip()}")
            bad += r.returncode != 0
    if not unlink and not bad:
        print(f"\nRSMM ({dest}) now sees these mods. Run `rsmm apply` with the game closed.")
    return 1 if bad else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
