# Progression map — Skyward Industry

Why this pack exists: vanilla Create lets you hand-craft everything, so factories are
optional scenery. Here every tier's core material requires automated processes from the
previous tier, the airship eats the factory's output, and the factory's customer is the
shipyard. All quantities live in `kubejs/startup_scripts/balance.js` (`global.BAL`).

## Chapter 1 — Andesite Age (expected: 3–6 hours)

**Gate:** andesite alloy is a *mixer product*. Grid recipe exists but is ~4x worse per
andesite and eats full nuggets — fine for your first ~16 alloy, miserable at 200.

| Recipe | Path | Cost (per `balance.js`) |
|---|---|---|
| `skyward:ch1/andesite_alloy_mixing` | Mechanical Mixer | 2 andesite + 1 iron nugget → 2 alloy |
| `skyward:ch1/andesite_alloy_mixing_zinc` | Mechanical Mixer | zinc-nugget parity route |
| `skyward:ch1/andesite_alloy_by_hand` | Crafting grid | 2 andesite + 2 iron nuggets → 1 alloy |

What this makes attractive: cobble→andesite supply, an iron farm (washing/crushing),
kelp/tree farms for fuel and rope. The wall to brass is volume: a press, mixer, saw,
deployer line and the casings under them are ~hundreds of alloy.

## Chapter 2 — Brass Age (expected: 8–15 hours)

**Gate:** three custom intermediates that cannot be hand-made at all — they only come
out of machine lines — and the precision mechanism is rebuilt on top of them.

| Item | Line required | Cost per unit |
|---|---|---|
| `kubejs:calibrated_shaft` | press + deployer (sequenced assembly, 3 loops) | 1 shaft + 3 andesite alloy |
| `kubejs:tempered_casing` | spout (fluid line) | 1 brass casing + 250mb lava |
| `kubejs:resonant_coil` | deployer + press (2 loops) | 1 golden sheet + 2 electron tubes |
| `create:precision_mechanism` | 3-deployer assembly line (3 loops) | 1 calibrated shaft + 3 cogwheels + 3 large cogwheels + 3 iron nuggets, 80% yield |

Design note: the 80/20 yield on precision mechanisms is the only stochastic recipe in
the pack — enough to make overbuilding lines feel right, not enough to be a casino.

## Chapter 3 — Aeronautics Age (expected: 15–30 hours to first real ship)

**Gate:** every ship component eats Ch.2 intermediates in bulk.

| Component | Cost per unit (see `BAL.ch3`) |
|---|---|
| `simulated:engine_assembly` | 1 tempered casing + 3 resonant coils + 3 calibrated shafts (saw→press→2 deployers, 3 loops; tuned down from 4 on 2026-06-09) |
| `simulated:gyroscopic_mechanism` | 1 precision mechanism + 4 cogwheels + 4 resonant coils |
| `simulated:red_portable_engine` | engine assembly + tempered casing + blast furnace |
| `aeronautics:*_envelope` | deployer-only (grid recipes removed), 2 per wool+stick |
| `aeronautics:levitite_blend` | 6 end stone powder + 4 zinc nuggets + 500mb water → 250mb (heated) |
| `aeronautics:wooden_propeller` | shaft ringed by 4 slabs — cheap EARLY thrust, carries an experimental drag penalty (slower ships) |
| `aeronautics:andesite_propeller` | create:propeller + slab + shaft (mod original) — early thrust, no drag penalty. Free 1:1 wooden↔andesite conversions removed |
| `aeronautics:propeller_bearing` | slab + **calibrated shaft** + brass casing — the large-ship propulsion mount, deliberately later-tier than the propellers |
| `aeronautics:smart_propeller` | propeller + gyroscopic mechanism + brass casing → **1** (was 2) |
| `aeroworks:gyroscope` | flywheel + gimbal sensor + brass casing + 2 gyroscopic mechanisms |
| `aeroworks:joystick` / servos | re-keyed onto calibrated shafts / resonant coils |
| `simulated:physics_assembler` | now needs a precision mechanism + brass casing (shipbuilding starts in brass age) |

**The budget hopper** (the intended first ship): wooden propellers straight on
shafts, ONE portable engine, steering wheel + throttle, ~30 envelopes. No
propeller bearing, no gyroscope, no smart propellers — bearings are large-ship
tech and the rest are comfort upgrades, priced accordingly. Bill ≈ 2 tempered
casings, ≈ 3 resonant coils, ≈ 3 calibrated shafts, 1 precision mechanism (for
the physics assembler). Wooden props fly slower (drag penalty); upgrading to
andesite props is the first cheap performance win.

Rough bill for a comfortable hopper (2 engines, 1 gyroscope, controls, ~30
envelopes): ≈ 8 tempered casings, ≈ 35 resonant coils, ≈ 30 calibrated shafts,
≈ 6 precision mechanisms → ≈ 100 alloy, ≈ 70 electron tubes, a lava line, a wool
farm. A cargo hauler runs 4–6x that. That is the resource sink doing its job.

## Chapter 4 — Crossing Tier (post-voyage)

**Gate:** `kubejs:aetherium` — loot-only, found in chests at the Crossing destination
(~25k blocks out; see `docs/CROSSING_RUNBOOK.md`). No recipe, by design; its tooltip
says where it comes from and Chapter 5 of the quest book is visible from day one.

| Recipe | Cost |
|---|---|
| `skyward:ch4/creative_motor` | 12 aetherium + 4 engine assemblies + 4 gyroscopic mechanisms + 4 sturdy sheets + 1 precision mechanism (mechanical crafter) |
| `skyward:ch4/creative_crate` | 4 aetherium + 4 brass casings + item vault |
| `skyward:ch4/creative_fluid_tank` | 4 aetherium + 4 copper casings + fluid tank |
| `skyward:ch4/aetherium_block` | 9 aetherium ↔ block, reversible |

A full creative-motor run needs multiple Crossing voyages or a generous site loot
stock — tune chest counts in the runbook, not the recipes.

## Invariants (check these when tuning)

1. No gated item is purchasable (economy sells decor/enchants/schematics only).
2. Every removed recipe has a JEI-visible replacement.
3. Hand-crafting is never the efficient path after the first hour of a chapter.
4. All numbers live in `balance.js` / `economy_balance.js`.
