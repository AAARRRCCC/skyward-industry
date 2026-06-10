# Placement runbook — shops & outposts without hand-building

Two supply lines: **generated schematics** (repo-made, in `admin_assets/schematics/`)
for everything commercial and repeatable, and **community schematics** (downloaded)
for the four outpost landmark builds + the Crossing island.

## 1. Generated stock (ready now)

| File | Size | Use |
|---|---|---|
| `market_stall_red/lime/blue/yellow.schem` | 7x6 footprint | One vendor each. Spawn market = ~10 buy stalls + ~16 sell stalls; mix colors |
| `vendor_kiosk.schem` | 3x3 footprint | Single vendor at outposts / tight spots |

Conventions (same in every file):
- **Gold block = vendor goes here.** Break it, place the creative vendor in its
  spot, configure per `economy_balance.js` / `OUTPOSTS.md`, item frame on the
  awning post by hand if you want signage.
- Front (counter + awning overhang) faces **south**; `//rotate 90` as needed.
- Each paste includes its own floor; flatten ground first, then `//paste -a`.

Regenerate / restyle: edit `tools/gen_schematics.py` (wood type, wool colors,
sizes are all constants) and rerun `py tools/gen_schematics.py`. Tell the agent
what to change and you'll get new variants — docks, crane gantries, a covered
market hall, outpost cores are all generatable on request once you've judged
the stall style in-game.

## 2. Paste workflow (WorldEdit)

WorldEdit now ships on both sides (manifest change 2026-06-10), so this works in
your single-player test world after a relaunch.

1. Files live in `<instance>/minecraft/config/worldedit/schematics/` (already
   copied into `playtesting`; on the server it's `config/worldedit/schematics/`).
2. In-game (OP / cheats on):
   ```
   //schem load market_stall_red
   //paste -a            (stand where the stall's SW corner should go)
   //undo                (wrong spot? move and re-paste)
   //rotate 90           (after load, before paste, to face another way)
   ```
3. Market layout that reads well: stalls in two facing rows, 3-block aisle,
   alternating awning colors, kiosks at the ends. 26 vendors ≈ 13 stalls per
   side of a plaza, or split across a couple of streets.

## 3. Community landmarks (download these, don't build)

Direct-download libraries that serve WorldEdit `.schem` (check each page's
credit/usage note; all three host free files):

- [Abfielder's schematic library](https://abfielder.com/) — largest, every file
  in .schem + litematic + materials CSV. Browse: docks/harbors ("Kelpwright"),
  industrial/foundry builds ("Cinderfall"), desert towers ("Glasswind"),
  train stations ("Highmoor"), floating/sky islands (the Crossing).
- [MineSchematic](https://www.mineschematic.com/) — smaller free library.
- [Schemat.io](https://schemat.io/schematics) — community uploads, filterable.

Per-outpost shopping list (one landmark each, ~60-120 block footprint):

| Outpost | Search terms | The generated stalls then provide |
|---|---|---|
| Kelpwright Docks | "dock", "fishing village", "harbor crane" | 2 buy + 3 sell vendors on the boardwalk |
| Cinderfall Forge | "foundry", "blacksmith", "industrial factory" | vendors in the forge hall |
| Glasswind Spires | "desert tower", "observatory", "sandstone temple" | vendors at the tower base |
| Highmoor Terminus | "train station", "rail depot", "alpine station" | vendors on the platform |
| Crossing island | "floating island", "sky island ruin", "airship wreck" | no vendors; loot chests per CROSSING_RUNBOOK |

Workflow: download `.schem` → drop in the schematics folder → paste at the
outpost coordinates from `OUTPOSTS.md` → pad edges into the terrain by hand
(ten minutes of dirt-blending hides any paste seam) → place vendors + claim
chunks per the outpost checklist.

## 4. Division of labor

- Agent: generates all commercial/repeatable structures, adjusts on feedback.
- Brady: picks landmarks (taste call), pastes everything, places vendors,
  blends terrain. Budget ≈ one evening for the spawn market + one per outpost.
