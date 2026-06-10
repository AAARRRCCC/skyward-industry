# Skyward Industry

**A Create + Create: Aeronautics progression pack where the factory finally has a customer.**

![Minecraft 1.21.1](https://img.shields.io/badge/Minecraft-1.21.1-44aa44)
![NeoForge 21.1.233](https://img.shields.io/badge/NeoForge-21.1.233-e68a3a)
![Mods 45](https://img.shields.io/badge/mods-45-4a8fd4)
![Format packwiz](https://img.shields.io/badge/format-packwiz-8a8a8a)
![Status playtesting](https://img.shields.io/badge/status-private_playtesting-c4a000)

Vanilla Create has a problem: you never actually *need* the factory. You can
hand-craft your way to everything, so automation is scenery. This pack fixes that
with five interlocking systems:

| Pillar | How |
|---|---|
| **Gating** | Each tier's core part is machine-made. Hand routes exist, but they're punishing on purpose |
| **Sink** | Airships eat bulk intermediates. The factory's customer is the shipyard |
| **Geography** | The good markets are 3â€“8k blocks out. Distance is why ships exist |
| **Economy** | Admin vendors buy your bulk goods and sell *only* progression-neutral things. Money never buys progress |
| **The Crossing** | 25,000 blocks out there's an island with the only material that gates the Creative Motor. The last chapter of the quest book is visible from day one |

## Progression at a glance

1. **Andesite Age** â€” andesite alloy moves to the mechanical mixer; your first lines pay rent at the spawn market
2. **Brass Age** â€” three custom intermediates (calibrated shaft, tempered casing, resonant coil) that *cannot* be hand-crafted, and a precision mechanism rebuilt on top of them
3. **Aeronautics Age** â€” engines, gyros, envelopes, and propellers re-priced to eat your production; first flight, then a cargo hauler
4. **Crossing Tier** â€” aetherium-gated creative-tier endgame
5. **The Crossing** â€” the voyage itself. Fit out a ship, cross the long water, come home heavier

Full tier map with costs and rationale: [`docs/PROGRESSION.md`](docs/PROGRESSION.md).

## Install

> **Status:** private playtesting. If you're reading this you're probably Brady or
> one of his friends and the server isn't open yet.

**Players (Prism Launcher):**
1. New instance â†’ Minecraft **1.21.1** â†’ NeoForge **21.1.233**
2. Drop [`packwiz-installer-bootstrap.jar`](https://github.com/packwiz/packwiz-installer-bootstrap/releases) into the instance's `minecraft/` folder
3. Instance â†’ Edit â†’ Settings â†’ Custom commands â†’ **Pre-launch command**:
   ```
   "$INST_JAVA" -jar packwiz-installer-bootstrap.jar https://raw.githubusercontent.com/AAARRRCCC/skyward-industry/main/pack/pack.toml
   ```
4. Launch. Mods + scripts sync on every start, so pack updates are automatic.

**Server:**
```
java -jar packwiz-installer-bootstrap.jar -g -s server https://raw.githubusercontent.com/AAARRRCCC/skyward-industry/main/pack/pack.toml
```
then install the NeoForge 21.1.233 server and start it. After world creation, copy
`datapacks/skyward/` into `<world>/datapacks/` (see [`docs/CROSSING_RUNBOOK.md`](docs/CROSSING_RUNBOOK.md)).

Recommended `server.properties`:
```
view-distance=10          # Sable ships + Create render cost; raise only after profiling
simulation-distance=8     # contraptions tick; this is the expensive knob
sync-chunk-writes=false   # large pregen worlds stall with sync writes
max-tick-time=180000      # physics assembly spikes shouldn't watchdog-kill the server
```

## Repo map

| Path | What |
|---|---|
| `pack/` | packwiz root â€” **generated**, rebuild with `py tools/build_pack.py` |
| `kubejs/` | gating scripts; every tunable number lives in `startup_scripts/balance.js` + `economy_balance.js` |
| `config/ftbquests/quests/` | the quest book |
| `datapacks/skyward/` | Crossing loot tables (per-world install) |
| `admin_assets/schematics/` | generated WorldEdit schematics (market stalls, kiosks) |
| `docs/` | design + runbooks: mod decisions, progression, economy, outposts, placement, the Crossing |
| `docs/TESTING/` | per-phase manual test checklists with live verification status |
| `tools/` | manifest lock/build, jar inspection, texture + schematic generators, reference validators |

## How this pack is maintained

- **Constants over magic numbers.** Playtest friction goes in [`BALANCE_NOTES.md`](BALANCE_NOTES.md);
  fixes are one-line edits to the balance files, never to chapter scripts.
- **Verified against the jars, not memory.** Item IDs, recipe shapes, and advancement
  triggers are extracted from the pinned mod jars into `docs/audit/`;
  `tools/validate_refs.py` cross-checks every reference in quests and scripts.
- **No file redistribution.** packwiz ships metadata + hashes; players download mods
  directly from Modrinth/CurseForge at install time. Inclusion reasoning per mod,
  including rejected alternatives, lives in [`docs/MOD_DECISIONS.md`](docs/MOD_DECISIONS.md).
