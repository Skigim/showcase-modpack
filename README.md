# showcase-modpack

Three [RSMM](https://github.com/Ovilli/RavenswatchModManager) mods for filming
Ravenswatch bosses for a wiki: force a boss to repeat one attack, take the hero
out of the shot, and pull the camera back. Plus a small window that sets all of
it.

| Mod | What it does | Takes effect |
|---|---|---|
| **BossAttackRoll** | Each chapter boss uses only the attacks you pick. | Next launch |
| **WikiScene** | Hides the hero, its ground shadow, aim arrow and lifebar; the hero can't be hurt, and bosses still target it. Each part is a toggle. | Next launch |
| **WikiZoom** | Sets the camera distance, live while the game runs. | Live |

As shipped, BossAttackRoll and WikiScene change nothing until you pick something.
WikiZoom starts at twice the normal distance.

## Status

Proven in game (2026-10-15, Chapter 1, Tentacle Master): single-attack pools,
every WikiScene toggle, and live zoom. Untested: pools of more than one attack,
and the Chapter 2 (Faceless) and Chapter 3 (Hands) bosses. For Hands only the
both-hands attacks are controlled; each hand's own attacks still roll.

## Install

Needs Windows, Python 3.11+, and a working
[RSMM](https://github.com/Ovilli/RavenswatchModManager) checkout with its
loader installed (`rsmm install-loader`), which WikiZoom needs.

1. Clone this repo anywhere.
2. Copy `paths.example.toml` to `paths.toml` and set `rsmm` (your
   RavenswatchModManager folder) and `game` (your Ravenswatch folder).
3. Double-click **Link mods.cmd**. It adds a link for each mod into RSMM's
   `mods/`, so RSMM builds them from this folder.
4. With the game closed, run `rsmm apply` (or press Save in the window below).

`python tools/link_mods.py --unlink` removes the links again.

## Use

- **Wiki setup.cmd** opens the window: a camera slider, the hero toggles, and a
  checkbox per boss attack (all ticked = normal), each section with
  *Reset to normal*. Save installs everything with the game closed. While the
  game runs, only the camera can change, and the window locks the rest.
- **tools/boss_attacks/attacks.txt**, then **Apply boss attacks.cmd**: the same
  attack choice as a text file.
- `python tools/boss_attacks/boss_attacks.py <boss> <attack> ...` from a
  terminal, `... list` for names.
- **mods/WikiZoom/config.toml**: `distance` (normal is 33, 0 = the game's own
  camera), read live.

Don't press the zoom key or stand in cinematics while filming.

## Online play

WikiZoom only touches the camera, so RSMM counts it as client-only: an install
running only WikiZoom is vanilla online. BossAttackRoll and WikiScene change the
game, so use them solo.

## Game data

This repo holds only manifests, Lua and tools. `rsmm apply` builds the patched
game files from your own install, and `.gitignore` keeps them out of the repo,
since they derive from the game's copyrighted data.

`rsmm pack <id>` zips a mod the way RSMM shares them. Packed after an apply
with choices made, a BossAttackRoll or WikiScene zip includes that patched
game file.

## License

MIT, see [LICENSE](LICENSE).
