# The Crossing — placement runbook (Brady)

Everything agent-side is done: `kubejs:aetherium` (+block, tags, tooltips), Ch.4
recipes, the quest chapter, three loot tables, and four ship's-log lore items. This
document is the one session of admin work that turns them into a destination.

## 0. Pick the spot (10 min, before pregen)

- Default: **(25,000, 0)** — due east. Override if your seed has a better story:
  load the seed in a map tool (e.g. Chunkbase) and prefer a bearing that crosses a
  large ocean ("the long water") and does NOT pass Highmoor (north) — the Crossing
  should leave the trade lanes behind.
- Decide site center coords now; everything below uses `X Z` for them.
- Post the bearing in-world: a lectern book + map marker at Highmoor Terminus
  ("Survey bearing: due east, 25,000. DON'T.").

## 1. Pregen (runs overnight, do it first)

Server console (Chunky is server-side):

```
chunky shape circle
chunky center <X> <Z>
chunky radius 1024
chunky start
```

Then the flight corridor (a strip, not a disk — much cheaper). For spawn→site due
east at z=0:

```
chunky shape rectangle
chunky corners 0 -512 <X+512> 512
chunky start
```

Notes: run one task at a time (`chunky pause` / `chunky continue`); corridor at ~width
1024 is plenty — players straying further generate chunks live, which is fine in ones
and twos. Total is roughly 360k chunks; expect hours, not minutes — overnight it.

## 2. The build (one paste)

**The site is pre-built**: `admin_assets/schematics/crossing_island.schem` is a
generated 128x128 floating island — landfall wreck on the east rim (hold chest
inside), gravel breadcrumb path, ruined observatory, a vault chamber 12 blocks under
it (stairwell down the tower's center), 8 cache barrels, oxidized-copper "teal vein"
cliffs, warped flora, and 4 mineable aetherium blocks hidden in the rock. All ten
loot containers are already placed; their offsets are baked into a bind function.
Regenerate or restyle anytime: `py tools/gen_crossing_site.py` (deterministic seed).

Paste workflow (in-game, OP):

1. Copy the .schem into `config/worldedit/schematics/` (server side).
2. Fly to the site center, then position yourself at the intended **min corner**:
   roughly site-center minus (64, ~40, 64). The island's ground sits ~40-50 blocks
   above schematic bottom, so stand where y ≈ cruise altitude - 45. **Write down
   your block coords — this is the ANCHOR (ax, ay, az).**
3. `//schem load crossing_island` then `//paste -a` (skips air; the island floats,
   so anything under it stays untouched).
4. Check the lodestone: it pastes at the anchor itself, marking local (0,0,0).
   Wrong spot? `//undo`, reposition, re-paste.
5. Prefer a hand-made or community build instead? The old sourcing notes live in
   docs/PLACEMENT.md; if you swap the island out, you place + bind chests manually
   per §3's table instead of using the function.

## 3. Loot binding (1 command)

Every container offset was recorded at generation time into
`skyward:bind_loot` (ships with the datapack). After §4's datapack install, run
ONCE with the anchor coords from step 2:

```
/execute positioned <ax> <ay> <az> run function skyward:bind_loot
```

You'll get an aqua confirmation: `[Skyward] Crossing loot bound: 10 containers.`
Then open nothing — verify with a spot-check as a second account, or trust the
walk-through in §6. Manual fallback (or for extra chests you add):

| Where | Table |
|---|---|
| Landfall wreck hold | `skyward:chests/crossing_landfall` |
| Cache barrels (8 placed) | `skyward:chests/crossing_cache` |
| Vault dais chest | `skyward:chests/crossing_vault` |

Stock math: landfall (2–4) + 8 caches (1–3 each) + vault (6–10) ≈ **16–34 aetherium
per full clear**, vs 12 for a creative motor. One expedition = one motor with change.
Containers do NOT refill; for repeat-visit servers, add barrels and bind them
manually during maintenance. Four aetherium BLOCKS (36 aetherium) are also minable —
one under the vault chest, three hidden in the cliffs. Finding the furniture
valuable is intended post-game greed; it's capped so loot stays the main source.

Optional flavor: drop extra `kubejs:ships_log_2/3` items in item frames along the
breadcrumb path (`/give` yourself; they're normal items).

## 4. Datapack install (2 min, once)

The loot tables ship in the repo, not the packwiz pack (datapacks are per-world):

1. Copy `datapacks/skyward/` into `<world>/datapacks/skyward/` on the server.
2. `/reload`, then verify: `/datapack list` shows `"file/skyward"` enabled, and
   `/loot give @s loot skyward:chests/crossing_cache` hands you items.
3. Re-copy + `/reload` whenever the repo version changes.

## 5. Quest wiring (5 min)

Works as shipped: "Past the mark" and the landfall/aetherium/homecoming quests use
checkmarks + item detection — zero config. Optional upgrade once coords are final:

- In-game: quest book → admin edit mode (`/ftbquests editing_mode`) → open
  "Past the 20,000 mark" → replace the checkmark task with a **Location** task:
  dimension `minecraft:overworld`, centered on the site, radius ~768. Same for
  "Landfall" if you'd rather it trigger on arrival than on the log pickup.
- SNBT alternative (server stopped, edit
  `config/ftbquests/quests/chapters/the_crossing.snbt`, task `2F00000000000003`):

```snbt
{
	id: "2F00000000000003"
	type: "location"
	dimension: "minecraft:overworld"
	ignore_dimension: false
	position: [<X>, 80, <Z>]
	radius: 768
}
```

## 6. Final walk-through checklist

- [ ] Fly the corridor: no obvious pregen seams at the site
- [ ] Landfall chest: log I + aetherium inside
- [ ] Vault chest: log IV + 6–10 aetherium
- [ ] Every cache chest opens with loot (a silent empty chest = typo'd LootTable id)
- [ ] `/loot give` test passes for all three tables
- [ ] Highmoor lectern posts the bearing
- [ ] A fresh account sees Chapter 5 quest 1 on day one
