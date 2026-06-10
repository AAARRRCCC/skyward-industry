# Skyward Industry

A Create + Create: Aeronautics progression modpack for a small friends server.
**Minecraft 1.21.1 · NeoForge 21.1.233 · 38 mods · packwiz format.**

The pitch: vanilla Create never makes you automate. Here, every tier's core part is
machine-made (gated recipes), airships eat your production (resource sink), vendors
pay for bulk goods but never sell progression (economy), the good markets are far
away (geography), and 25,000 blocks out there is an island that ends the pack
(The Crossing).

## Install — players (Prism Launcher)

1. New instance → Minecraft **1.21.1** → NeoForge **21.1.233**.
2. Drop [`packwiz-installer-bootstrap.jar`](https://github.com/packwiz/packwiz-installer-bootstrap/releases)
   into the instance's `minecraft/` folder.
3. Instance → Edit → Settings → Custom commands → **Pre-launch command**:

   ```
   "$INST_JAVA" -jar packwiz-installer-bootstrap.jar <PACK_TOML_URL>
   ```

   where `<PACK_TOML_URL>` is the raw URL of `pack/pack.toml` (once this repo is on
   GitHub: `https://raw.githubusercontent.com/<user>/skyward-industry/main/pack/pack.toml`;
   for local testing: `file:///C:/Users/rbrad/IndieProj/skyward-industry/pack/pack.toml`).
4. Launch. The installer syncs mods + scripts on every start, so updates are automatic.

## Install — server

```
java -jar packwiz-installer-bootstrap.jar -g -s server <PACK_TOML_URL>
```

then install the NeoForge 21.1.233 server and start. After world creation, copy
`datapacks/skyward/` into `<world>/datapacks/` (see docs/CROSSING_RUNBOOK.md).

### server.properties recommendations

```
view-distance=10          # Sable ships + Create render cost; raise only after profiling
simulation-distance=8     # contraptions tick — this is the expensive knob
sync-chunk-writes=false   # large pregen worlds stall with sync writes
max-tick-time=180000      # physics assembly spikes shouldn't watchdog-kill the server
```

Plus: pregen before launch day (docs/CROSSING_RUNBOOK.md §1), claim outposts as
server team (docs/OUTPOSTS.md).

## Repo map

| Path | What |
|---|---|
| `pack/` | packwiz root — **generated**, rebuild with `py tools/build_pack.py` |
| `kubejs/` | gating scripts; all numbers in `startup_scripts/balance.js` + `economy_balance.js` |
| `config/ftbquests/quests/` | quest book (6 chapters) |
| `datapacks/skyward/` | Crossing loot tables (per-world install) |
| `docs/` | MOD_DECISIONS, PROGRESSION, ECONOMY_RUNBOOK, OUTPOSTS, CROSSING_RUNBOOK |
| `docs/TESTING/` | per-phase manual test checklists (phase2–phase6) |
| `tools/` | manifest lock/build, texture gen, reference validator |

## Tuning loop

Play → log friction in `BALANCE_NOTES.md` → adjust `balance.js`/`economy_balance.js`
→ `py tools/build_pack.py` → commit → **restart** the game/server (they're startup
scripts; `/reload` won't pick them up). Constants only; never edit chapter scripts
for quantity changes.

## Validation without a game client

- `py tools/validate_refs.py` — every item id in quests/scripts exists in the
  registries extracted from the pinned jars; quest dependency graph resolves.
- `node --check kubejs/**/*.js` — script syntax.
- `packwiz refresh` in `pack/` — manifest hash integrity (no-op when clean).
