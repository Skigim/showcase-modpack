# showcase-modpack

Two [RSMM](https://github.com/Ovilli/RavenswatchModManager) mods for filming
and practising Ravenswatch boss fights. Both are set from their settings panel
in the RSMM app. For the camera, use Ovilli's **camera-control** mod from the
[RSMM registry](https://rsmm.me/registry), which sets rotation, tilt, distance
and look height live.

| Mod | What it does | Takes effect |
|---|---|---|
| **Boss Showcase** | Choose which attacks each chapter boss uses: switch a boss on, then give each attack a weight (0 = never). | Next launch |
| **Ghost Mode** | Hides the hero, its ground shadow, aim arrow and lifebar, and the hero can't be hurt. Enemies still target it. For roaming the map unseen as Scarlet, *Scarlet Cloak* makes her human DEFENSE last until something ends it. Each part has its own switch. | Next launch |

Boss Showcase changes nothing until you switch a boss on. Ghost Mode has every
part on by default except *Scarlet Cloak*.

## Status

**Ghost Mode** is tested in game with every switch, *Scarlet Cloak* included,
and is on the [RSMM store](https://rsmm.me/registry) as `ghost-mode`.

**Boss Showcase** is proven in game (2026-10-15, Chapter 1, Tentacle Master)
for one attack at a time. Untested: several attacks at once, and the Chapter 2
(Faceless) and Chapter 3 (Hands) bosses. For Hands only the both-hands attacks
are controlled; each hand's own attacks still roll. It is one fixed manifest
whose steps the settings switch on and off (`when`) and fill in (`config`),
and that form is tested in game.

## Use

1. In the RSMM app, open the mod's settings.
2. **Boss Showcase**: switch a boss on, set the weight of each attack you want
   above 0 and the rest to 0, and set *attacks drawn per cycle* to how many are
   above 0. For one attack on repeat: that attack 1, the others 0, draws 1.
3. **Ghost Mode**: switch off any part you don't want. To walk the map without
   enemies aggroing, switch on *Scarlet Cloak*, play Scarlet, and cast her
   DEFENSE once in human form. It lasts until you turn into the wolf or use
   another ability, then cast it again. Other heroes have no such switch yet.
4. Close the game and apply. The change shows on the next launch.

Don't stand in cinematics while filming: they make the hero Concealed.

## Developing

Needs Windows, Python 3.11+, and an
[RSMM](https://github.com/Ovilli/RavenswatchModManager) checkout.

1. Copy `paths.example.toml` to `paths.toml` and set `rsmm` to your
   RavenswatchModManager folder.
2. Double-click **Link mods.cmd**. It adds a link for each mod into RSMM's
   `mods/`, so RSMM builds them from this folder.
3. With the game closed, run `rsmm apply`.

`python tools/link_mods.py --unlink` removes the links again.

## Online play

Both mods change the game, so use them solo.

## Game data

This repo holds only manifests and settings. `rsmm apply` builds the patched
game files from your own install into each mod's `assets/`, and `.gitignore`
keeps them out of the repo, since they derive from the game's copyrighted
data. Pack or publish from a folder without `assets/`, so the zip holds only
the manifest and settings.

## License

MIT, see [LICENSE](LICENSE).
