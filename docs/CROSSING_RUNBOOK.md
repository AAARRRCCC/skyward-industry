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

## 2. The build

You need, minimum:
1. **Landfall point** — a wrecked survey ship or dock at the island's edge.
2. **The site** — a sky-island / ruin / observatory, your call. 60–100 block footprint
   reads well from a ship.
3. **The vault** — one enclosed room, slightly hidden (under the ruin, behind a
   waterfall, top of the spire), holding the single vault chest.

Schematic sourcing (free, paste-ready): search "sky island", "floating ruin",
"airship wreck" on minecraft-schematics.com, Planet Minecraft (filter: schematic
downloads), or GrabCraft. Anything `.schem`/`.schematic` loads in WorldEdit. Prefer
builds under ~150x150; you can terraform edges by hand faster than fixing a megabuild.

WorldEdit paste workflow (in-game, OP):

```
//schem load <filename>        (file goes in config/worldedit/schematics/)
//paste -a                     (-a skips air; stand where the build's origin should be)
//undo                         (if the anchor was wrong; reposition and re-paste)
```

If the schematic origin is awkward: paste in a throwaway superflat first, `//copy`
from a corner you choose (stand there, select with //pos1 //pos2), save your own
version with `//schem save skyward_site`.

## 3. Loot chests (15 min)

Place plain chests (or barrels) by hand, then bind loot tables — each chest rolls its
table on first open:

| Where | How many | Command (look at the chest, use its coords) |
|---|---|---|
| Landfall wreck | exactly 1 | `/data merge block <x> <y> <z> {LootTable:"skyward:chests/crossing_landfall"}` |
| Scattered around the site | 6–10 | `/data merge block <x> <y> <z> {LootTable:"skyward:chests/crossing_cache"}` |
| The vault | exactly 1 | `/data merge block <x> <y> <z> {LootTable:"skyward:chests/crossing_vault"}` |

Stock math: landfall (2–4) + 8 caches (1–3 each) + vault (6–10) ≈ **16–34 aetherium
per full clear**. A creative motor needs 12. One expedition = one motor with change,
two visits for the post-game set — tune by adding/removing cache chests, not by
editing recipes. Chests do NOT refill; if the server wants repeat visits to matter,
place a second ring of caches deeper into the island or re-merge the NBT on looted
chests during a maintenance window.

Optional flavor: drop extra `kubejs:ships_log_2/3` items in item frames along a
breadcrumb path from landfall to vault (`/give` yourself; they're normal items).

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
