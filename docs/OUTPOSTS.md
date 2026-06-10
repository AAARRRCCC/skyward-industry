# Trade outposts — placement & stock specs

Four outposts on a 3–8k ring around spawn. Each pays **1.5x** (`ECON.premiumMultiplier`)
for two specialty goods and sells a small themed palette. Distance + specialization is
the geography pillar: hauling 10 stacks of cargo 6k blocks is an airship's job (rail or
mule before Ch.3 — that's the point).

Builds are human-placed (WorldEdit or by hand; free build sourcing ideas in
CROSSING_RUNBOOK §schematics). Suggested coordinates assume spawn ≈ (0,0); slide each
along its bearing to the nearest matching biome — the bearing spread matters more than
the exact radius.

Premium prices below are `ECON.buy x 1.5`, rounded up.

## 1. Kelpwright Docks — ocean boardwalk, ~3,500 east

- **Where:** (+3500, ~0), warm/lukewarm ocean coast. Stilt boardwalk, drying racks,
  one crane over the water.
- **Buys at premium:** cardboard 2 (1.5→2), andesite alloy 2 (1.5→2)
- **Sells:** prismarine 8, calcite 2, music_disc_cat 256
- **Why go:** earliest outpost; a kelp/paper barge run is the tutorial for cargo
  logistics before airships exist.

## 2. Cinderfall Forge — volcanic foundry, ~5,000 south

- **Where:** (~0, +5000), basalt deltas / exposed lava lake. Black-stone foundry,
  chimneys, slag heaps.
- **Buys at premium:** iron sheet 3, tempered casing 45
- **Sells:** scoria 2, scorchia 2, smooth_basalt 2, music_disc_stal 256
- **Why go:** the tempered-casing premium makes a lava-side satellite factory worth
  building — your first remote production site.

## 3. Glasswind Spires — desert observatory, ~6,500 west

- **Where:** (-6500, ~0), desert with exposed terracotta if possible. Sandstone
  towers, brass telescopes, glass domes.
- **Buys at premium:** electron tube 18, resonant coil 45
- **Sells:** quartz_block 8, purpur_block 8, amethyst_block 12,
  enchanted_book/efficiency_5 768, enchanted_book/unbreaking_3 512
- **Why go:** premium on the electronics line; the books make it the mid-game
  shopping trip.

## 4. Highmoor Terminus — alpine rail-end, ~8,000 north

- **Where:** (~0, -8000), jagged peaks / snowy slopes. A train terminus that the rails
  never reached — buffer stops pointing at a cliff, waiting room, tall clock tower.
- **Buys at premium:** precision mechanism 144, engine assembly 600
- **Sells:** enchanted_book/mending 2048, enchanted_book/fortune_3 1024,
  enchanted_book/protection_4 1024, enchanted_book/feather_falling_4 768,
  music_disc_blocks 256, aeronautics:music_disc_cloud_skipper 512,
  name_tag 128, empty_schematic 16, schematic_and_quill 64
- **Why go:** the endgame store, deliberately at the far edge of pre-airship travel.
  Hauling engine assemblies here at 600 each is the first real cargo-hauler contract.

## Vendor checklist per outpost

- [ ] 2 creative vendors in **buy** mode (premium prices above)
- [ ] 1–3 creative vendors in **sell** mode (themed stock above)
- [ ] 1 item frame per vendor showing the traded good
- [ ] Lectern with a book: outpost name + what it buys (one paragraph, in-world voice)

## Anti-theft (the moored ships are decor, not loot)

Two layers, both already in the pack:

1. **FTB Chunks server-team claim** over the whole outpost INCLUDING the full
   footprint of the moored ship plus a 1-chunk margin (map `M` → admin panel →
   claim as Server team). This blocks breaking, placing, and interacting — so no
   honey glue, no merging glue, no assembler placement by players.
2. **FTB Chunks: Sable Aerospace** (shipped) explicitly denies Sable assembly on
   structures inside claimed territory ("Closed airspace — this Sable structure
   is inside claimed territory") and enforces claimed airspace against incoming
   ships, with approach warnings. Players can't fly their own ship in and merge
   the parked one into it either.

Verification (run once, second account, at the first finished outpost):
- [ ] Can't break ship or shop blocks
- [ ] Can't place merging glue / apply honey glue on the ship
- [ ] Physics assembler aimed at the ship refuses ("closed airspace" message)
- [ ] Flying your own ship at the outpost produces the airspace warning and
      doesn't let you park inside/merge
- [ ] Vendors still tradeable (claims must not block right-click trading — if
      they do, loosen the claim's interaction settings to allow block use, or
      keep vendors on unclaimed border chunks and re-test griefability)

Paranoia fallback if anything above fails in testing: hide 2–3 bedrock blocks
inside the ship's hull interior — even a successful assembly attempt can't take
unbreakable blocks, and WorldEdit places them invisibly.

## Quest hooks (wired in Phase 4)

Each outpost has a "first visit" checkmark quest and the Highmoor delivery quest
("Commission a cargo hauler") expects a sell of 8 engine assemblies there.
