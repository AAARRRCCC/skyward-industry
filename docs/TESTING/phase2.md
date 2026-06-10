# Phase 2 manual test checklist — progression gating

Run in a fresh single-player creative world (cheats on). Open the log
(`logs/latest.log`) first: search for `KubeJS` — there must be **zero errors**
(`ERR`/`Failed to load`). `/kubejs errors` in-game should be empty.

## A. Custom items exist and look right

`/give @s` each, confirm texture + tooltip:

- [ ] `kubejs:calibrated_shaft`, `kubejs:tempered_casing`, `kubejs:resonant_coil`
- [ ] `kubejs:incomplete_calibrated_shaft` ("Uncalibrated Shaft"), `kubejs:incomplete_resonant_coil`
- [ ] `kubejs:aetherium` (epic purple name, glint, tooltip), `kubejs:aetherium_block` (places, amethyst sound, needs iron pick)
- [ ] `kubejs:ships_log_1` … `ships_log_4` (lore tooltips)

## B. Ch.1 — andesite alloy gate

In JEI, look up Andesite Alloy (recipes FOR it):

- [x] Exactly 3 recipes: mixer (iron nugget), mixer (zinc nugget), grid (2 andesite + 2 iron nuggets → 1) *(verified 2026-06-09; Create's JEI also mirrors the grid recipe in its "automated crafting" category — same recipe, not a 4th path)*
- [x] Create's old grid recipes (andesite + iron nugget → 2) are GONE *(verified 2026-06-09)*
- [ ] Build a mixer+basin in creative; 2 andesite + 1 iron nugget mixes into 2 alloy, no heat needed

## C. Ch.2 — intermediates

- [x] JEI on Calibrated Shaft shows sequenced assembly: shaft core, press → deploy alloy, 3 loops *(verified 2026-06-09)*
- [x] Run the line for real: depot/belt + press + deployer; confirm the transitional item is "Uncalibrated Shaft" and output is deterministic (no scrap) *(line built + shaft produced 2026-06-09)*
- [x] Spout with lava over a depot fills Brass Casing → Tempered Casing at 250mb *(verified 2026-06-09)*
- [ ] Resonant Coil assembly works (golden sheet core, deploy electron tube, press, x2)
- [x] Precision Mechanism: old golden-sheet assembly GONE from JEI; new one takes calibrated shaft, deploys cogwheel/large cogwheel/iron nugget, 3 loops, ~80% yield (run ~10, expect 1–3 shafts back) *(setup verified 2026-06-09)*

## D. Ch.3 — aeronautics sink

- [x] JEI on Engine Assembly: tempered-casing core, saw → press → deploy coil → deploy calibrated shaft. Old iron-sheet recipe GONE *(verified 2026-06-09; loops since tuned 4→3)*
- [x] Gyroscopic Mechanism: precision-mechanism core, deploys cogwheel + coil, 4 loops. Old recipe GONE *(verified 2026-06-09)*
- [ ] Envelopes (spot-check 3 colors): grid recipe GONE, deployer recipe gives 2 (not 3)
- [ ] Levitite Blend: 6 end stone powder + 4 zinc nuggets + 500mb water → 250mb, heated basin
- [x] Wooden Propeller recipe exists; BOTH 1:1 wooden↔andesite conversion recipes
      are GONE *(verified 2026-06-09; recipe since reshaped to shaft + 4 slabs)*
- [ ] Wooden Propeller: shaft ringed by 4 wooden slabs
- [ ] Andesite Propeller: create:propeller + slab + shaft (mod-original restored)
- [ ] Propeller Bearing: slab + calibrated shaft + brass casing (was iron sheet)
- [ ] EXPERIMENTAL drag penalty, round 3: calibrated from flight data
      (scale 300 ≈ 169pN, immobilized a one-prop ship with 80pN hull drag;
      scale 2 ≈ 0.25pN). Now floating_scale = 65.0 targeting ~37pN ≈ 15% of one
      prop's thrust. Verify the wooden-prop ship MOVES and is modestly slower
      than the andesite twin; tune in kubejs/data/skyward/
      physics_block_properties/wooden_propeller_drag.json, or delete the file
      to drop the whole idea
- [ ] Smart Propeller crafts 1 (not 2)
- [ ] Portable Engine (red): tempered casing on top (not iron sheet)
- [ ] Physics Assembler needs precision mechanism + brass casing
- [ ] Aeroworks: gyroscope = flywheel + gimbal sensor + brass casing + 2 gyroscopic mechanisms (shapeless); joystick wants calibrated shaft; both servos want a resonant coil
- [ ] Mechanical crafter accepts the joystick recipe (5-row pattern renders in JEI)

## E. Ch.4 — crossing tier

- [ ] Creative Motor recipe visible in JEI (mechanical crafting 5x5, 12 aetherium)
- [ ] Creative Crate + Creative Fluid Tank recipes visible
- [ ] Aetherium itself has NO recipe in JEI (loot-only is intentional) but DOES have a tooltip pointing at the Crossing
- [ ] Aetherium block ↔ 9 aetherium round-trips

## F. No dead ends / regressions

- [ ] JEI search "envelope": every color still has a visible (deployer) recipe
- [ ] Trains: railway casing etc. unchanged (we didn't touch them)
- [ ] Numismatics coin recipes unchanged
- [ ] Survival sanity: nothing in B–D is craftable in a bare 3x3 except the punishing alloy recipe and propeller/bearing-style shaped recipes that explicitly use machine-made parts

## Checkpoint (mandatory before Ch.3 numbers are finalized)

Playtest Ch.1–2 pacing in survival (solo or duo): how long to first mixer? First brass?
First precision mechanism line? Log times + friction in `BALANCE_NOTES.md`; Phase 6
adjusts `balance.js` from that log.
