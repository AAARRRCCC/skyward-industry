# World shape — the charted disk and the long water

Brady's brief: a bounded world (~20k around spawn), "void" beyond it except the
Crossing island, and Distant Horizons LODs pregenerated so every player sees the
whole world the moment they join.

## Terrain: Tectonic (added 2026-06-10)

The spec's "no custom worldgen" rule was a guard against *agent-authored*
worldgen, not a vanilla-terrain aesthetic choice; Brady amended it for
established worldgen mods. **Tectonic 3.0.22 + Lithostitched** now ship in the
pack: dramatically larger mountains, real foothills, and (config) **Increased
Height = max build/generation height y640**.

**MUST DO before world creation, server side:**
1. Open the Tectonic config (config screen in-game on the client that prepares
   the server world, or its config file under `config/`) and enable
   **Increased Height**. Consider **Vertical Scale** to taste.
2. Copy the resulting `config/tectonic*` file into this repo's `config/` dir so
   the pack ships it and every client matches the server. (Flag it to the agent
   and it gets committed + synced.)
3. THEN create the world / start pregen. Worldgen choices do not retrofit —
   changing them after pregen means starting over.

Knock-on effects, already accounted for below: pregen is slower (Tectonic's
density functions cost more per chunk — budget extra overnight time); DH vistas
get better, not worse; the Crossing island schematic floats and pastes at any
altitude. One open test: Aeronautics' atmosphere/lift model vs y640 terrain
(does envelope lift or the 0%-pressure ceiling care about the taller world?) —
check during the phase2 flight tests and log it in BALANCE_NOTES.

## The honest engineering correction

**True void beyond a radius is off the table** without custom worldgen: vanilla
datapack density functions have no horizontal-distance primitive, the pack spec
bans custom worldgen, and a hard border at 20k would make the island at 25k
unreachable (vanilla worldborder is square and exception-less; ChunkyBorder is
shaped but also exception-less).

**What we do instead — same feel, verified tooling:**

| Layer | Tool | Shape |
|---|---|---|
| Hard wall | ChunkyBorder 1.2.18 (circle) | **r = 26,000** around spawn — contains the island, nobody walks off the edge of the simulation |
| The charted world | Chunky pregen + DH LOD pregen | **r = 20,000** disk: terrain + LODs for everything civilization touches |
| The long water | *nothing* | the 20k→26k ring is never pregenerated and never LOD'd. In Distant Horizons it renders as open fog past the edge of the charts. Flying the Crossing means leaving the rendered world behind — which is the brief, achieved without faking void |
| The island | Chunky + DH pregen disk at the site | LODs exist, but DH only renders LODs within client LOD range (~4–8k), so it fades into view mid-crossing like a landfall sighting |

Result for players: join → the entire 20k world is visible to the horizon
instantly. Fly east past 20k → the charts run out, fog, nothing — until the
island resolves out of it. The world has a shape and an edge, and the edge means
something.

## Setup (server console; do AFTER picking the site bearing)

1. **Terrain pregen** (overnight; see CROSSING_RUNBOOK §1 — same disks):
   ```
   chunky shape circle
   chunky center 0 0
   chunky radius 20000
   chunky start
   ```
   then the island disk (r 1024 at the site) and the corridor strip if you want
   smooth live-gen during crossings (optional now — the ring being slow to
   generate live is *flavor*).
2. **The wall:**
   ```
   chunky shape circle
   chunky center 0 0
   chunky radius 26000
   chunky border add
   ```
   (ChunkyBorder uses the current Chunky selection. Set AFTER pregen tasks so
   you don't clobber the selection mid-run; `chunky border list` to confirm.)
3. **LOD pregen** (Distant Horizons, server-side; slower than chunk pregen —
   budget a day or two of background time):
   ```
   /dh pregen start minecraft:overworld 0 0 20000
   /dh pregen start minecraft:overworld <siteX> <siteZ> 1024
   ```
   Progress: `/dh pregen status`. DH generates LODs from existing chunks fast
   (they're pregenerated) — it's the un-pregenerated ring that would crawl,
   which is why we don't LOD it.
4. **Verify on a client:** fresh player joins at spawn → distant mountains
   render immediately. Fly to 20k → world visibly ends. The wall at 26k stops
   movement with a shimmer.

## Caveats (read before launch day)

- **DH 3.0.3-b is beta-channel** for 1.21.1 NeoForge (the project's normal
  cadence). If LOD sharing misbehaves on the server build, drop to the newest
  2.3.x for 1.21.1 — the commands above are the same. Log it in BALANCE_NOTES.
- DH is in the pack as **optional (default on)** — anyone whose GPU hates it can
  untick it in the installer or disable it in-game; they just lose the vista.
- LOD sharing means once anyone flies the crossing with distant generation on,
  corridor LODs may propagate to other clients. We call that "the route gets
  charted" and consider it a feature.
- ChunkyBorder is server-side only; no client install needed.
- server.properties stays at normal view-distance — DH replaces the need to
  crank it.
