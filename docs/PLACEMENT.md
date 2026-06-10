# Placement runbook — shops & outposts without hand-building

**Pivot v2 (2026-06-10):** generic vanilla schematic sites and fully-generated
architecture both failed the quality bar (mooring station verdict: "doesn't look
very good"). The answer is **[CreateMod.com](https://createmod.com/schematics)** —
the Create community's own schematic repository: builds made OF Create blocks IN
Create's industrial style, so they look native to this pack. 482 airship builds
alone, plus warehouses, factories, train yards, markets.

The build plan:

- **Outposts = a moored trade airship + a flat dock.** Brady browses
  [Top 10 Create Aeronautics Airships](https://createmod.com/collections/b6c88d77a02d7bb)
  (or the [airship-dock category](https://createmod.com/search/airship-dock)) and
  picks one mid-size ship per outpost — four different ships = four outposts with
  personality. The ground level is just a dock platform + generated kiosks.
- **Central market:** candidates on the same site (e.g.
  [Simple Market](https://createmod.com/schematics/simple-market-vanillia),
  [The Warehouse](https://createmod.com/schematics/the-warehouse)) or Brady's own
  find elsewhere.
- **The Crossing:** natural far-out terrain; centerpiece = a community airship
  pasted as a wreck (tilt/bury it, knock holes with WorldEdit spheres of air).

**Workflow for any CreateMod.com download** (.nbt, schematicannon format):

```
py tools/nbt2schem.py path\to\download.nbt     # writes download.schem beside it
```

drop the .schem in the WorldEdit schematics folder, paste as usual. Two caveats:
chest contents / Create machine configs don't survive (static shell only — fine
for landmarks), and blocks from mods we don't ship paste as air (prefer builds
listing Create / Create Aeronautics / vanilla as their only deps; "Bits and Bobs"
or "Framed Blocks" builds will have holes).

Alternative placement that needs no conversion: Create's own schematic table +
schematicannon work in-game with the raw .nbt (put it in `<instance>/minecraft/
schematics/`) — thematically cute for spawn-town lore, slower for admin work.

The older notes below (generated mooring station, vanilla-site landmark table)
are retained as reference/fallback.

## 1. Generated stock (ready now)

| File | Size | Use |
|---|---|---|
| `mooring_station.schem` | 19x19, 24 tall | **A complete outpost.** Mooring mast + docking ring + crane + 2 kiosks + mast counter (3 gold vendor markers) + containers. Paste once per outpost site |
| `industrial_stall_iron/copper/andesite.schem` | 7x6 footprint | **The preferred stall set** (Brady: "more industrial"). Create/Create Deco palette: support pillars, catwalk canopy, hull counters, girder rails |
| `industrial_kiosk.schem` | 3x3 footprint | Single vendor, industrial palette |
| `market_stall_red/lime/blue/yellow.schem` | 7x6 footprint | Original wool-awning set; kept for outposts that want a softer look (Kelpwright?) |
| `vendor_kiosk.schem` | 3x3 footprint | Wool-set kiosk |

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

**Picked candidates (2026-06-10)** — all free downloads on Abfielder; pick the
one that fits your seed's terrain. Download tip: each page offers format
conversion — choose **.schem (WorldEdit)** when downloading.

| Location | First pick | Alternates |
|---|---|---|
| Kelpwright Docks | [Fishing Dock by disruptive builds](https://abfielder.com/Products/ProductDetails.php?id=2706) | [Riverside Docks by Sir Silver](https://abfielder.com/schematicdetail/sir-silver/riverside-docks/2053); [Suspended Fishing House](https://abfielder.com/Products/ProductDetails.php?id=6259) as a flavor satellite |
| Cinderfall Forge | [Industrial Factory by Randymix](https://abfielder.com/schematicdetail/randymix/industrial-factory/1064) | [Industrial Dockside Factory](https://abfielder.com/schematicdetail/randymix/industrial-dockside-factory/1066); [Steampunk Factory](https://abfielder.com/Products/ProductDetails.php?id=10175) |
| Glasswind Spires | [The Desert Temple of Menhir by Eternal Dawn](https://abfielder.com/schematicdetail/eternal-dawn/the-desert-temple-of-menhir/647) | [Fantasy Desert Style Temple](https://abfielder.com/schematicdetail/eternal-dawn/fantasy-desert-style-temple/691); more under the [Desert tag](https://abfielder.com/browseSchematics?TagID=124) |
| Highmoor Terminus | [Railway Station with Train by Randymix](https://abfielder.com/schematicdetail/randymix/railway-station-with-train/1067) | [Wild West Train Station](https://abfielder.com/schematicdetail/abfielder/wild-west-train-station/139); [Railroad Station](https://abfielder.com/Products/ProductDetails.php?id=6302) |
| Crossing island | [Floating Island Mega Base by TIDZIMI](https://abfielder.com/schematicdetail/tidzimi/floating-island-mega-base/1463) | [Mossy Floating Island (small)](https://abfielder.com/Products/ProductDetails.php?id=10868) x2-3 as outlying cache islets |
| Crossing landfall wreck | [Steampunk Airship](https://abfielder.com/Products/ProductDetails.php?id=3580) pasted half-buried at the island's edge = the crashed survey ship | — |

Downloaded builds go in the same schematics folder but are NOT committed to the
repo (they're other people's builds; we link, not re-host).

Workflow: download `.schem` → drop in the schematics folder → paste at the
outpost coordinates from `OUTPOSTS.md` → pad edges into the terrain by hand
(ten minutes of dirt-blending hides any paste seam) → place vendors + claim
chunks per the outpost checklist.

## 4. Division of labor

- Agent: generates all commercial/repeatable structures, adjusts on feedback.
- Brady: picks landmarks (taste call), pastes everything, places vendors,
  blends terrain. Budget ≈ one evening for the spawn market + one per outpost.
