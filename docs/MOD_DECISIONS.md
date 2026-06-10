# Mod decisions — Skyward Industry

Audit date: **2026-06-09** (Modrinth API + curse.tools CurseForge proxy; raw captures in
`docs/audit/`). Target: **Minecraft 1.21.1, NeoForge 21.1.233**. Pack format: packwiz.

## Headline verifications (Phase 0 questions)

| Question | Answer |
|---|---|
| Create 6.x for 1.21.1 NeoForge? | **Yes** — Create 6.0.10+mc1.21.1, release channel |
| Create: Aeronautics 1.21.1 NeoForge? | **Yes** — 1.2.1+mc1.21.1 (Modrinth `create-aeronautics`, released 2026-04-14, by ryanhcode / Simulated Team). NeoForge-only, exactly as the spec assumed |
| Sable dependency? | **Yes, required** — Sable 1.2.2 (`sable`). Embeds the Veil rendering library, so Veil needs no separate entry |
| Create: Aeroworks for 1.21.1? | **Yes** — 1.2.11+mc1.21.1 (`create-aeroworks`, MIT). Requires Create + Sable, both present |
| **Create: Numismatics 1.21.1 NeoForge port?** | **Yes — 1.0.20+neoforge-mc1.21.1, LGPL-3.0.** The port exists, so Numismatics is the economy backend. No fallback needed; Lightman's Currency and quest-based sell orders are rejected (below) |
| Aeronautics addon compat vs Create 6.x | Aeronautics 1.2.1, Aeroworks 1.2.11, Numismatics 1.0.20 all declare Create as a required dep of their current 1.21.1 builds and are released against the Create 6.0.x line (verified via Modrinth dependency metadata; there is no 1.21.1 Create other than 6.x) |

## Included — required, both sides (18)

| Mod | Version | Source | Why |
|---|---|---|---|
| Create | 6.0.10+mc1.21.1 | Modrinth | Core. Bundles Flywheel/Ponder on NeoForge (no separate deps declared) |
| Create: Aeronautics | 1.2.1+mc1.21.1 | Modrinth | Core thesis: airships |
| Sable | 1.2.2+mc1.21.1 | Modrinth | Required by Aeronautics (moving-structure engine) |
| Create: Aeroworks | 1.2.11+mc1.21.1 | Modrinth | Gyroscopes, joysticks — Ch.3 sink components |
| ~~Sable: Physics Compat~~ | ~~1.3.0~~ | Modrinth | **Removed at first boot (2026-06-09):** 1.3.0 emits a data format Sable 1.2.2 can't parse (log errors), and every block it tags belongs to mods not in this pack (Aether, Twilight Forest, BoP, Enderite…). Re-add only if those mods join and versions align |
| KubeJS | 2101.7.2-build.368 | Modrinth | All recipe gating + custom items |
| Rhino | 2101.2.7-build.85 | Modrinth | Required by KubeJS |
| Architectury API | 13.0.8+neoforge | Modrinth | Required by FTB Library |
| Create: Numismatics | 1.0.20+neoforge-mc1.21.1 | Modrinth | Economy backend (vendors, blaze bankers, coins) |
| JEI | 19.27.0.340 | Modrinth | Recipe visibility. "Beta" channel is JEI's normal release practice |
| Jade | 15.10.5+neoforge | Modrinth | Block/entity tooltips |
| Lithium | mc1.21.1-0.15.3-neoforge | Modrinth | Server tick performance |
| FerriteCore | 7.0.3-neoforge | Modrinth | Memory usage |
| FTB Quests | 2101.1.26 (file 8216578) | CurseForge | Quest book |
| FTB Teams | 2101.1.10 (file 7878281) | CurseForge | Required by FTB Quests |
| FTB Library | 2101.1.31 (file 7746959) | CurseForge | Required by FTB Quests/Teams/Chunks |
| FTB Chunks | 2101.1.17 (file 8216875) | CurseForge | Claims + map for a friends server |
| FTB XMod Compat | 21.1.8 (file 7715134) | CurseForge | KubeJS/JEI/Jade integration for FTB Quests |

## Included — server side only (2)

| Mod | Version | Why |
|---|---|---|
| Chunky | 1.4.23 | Pregen for The Crossing corridor (admin) |
| WorldEdit | 7.3.8 | Destination build placement (admin) |

## Included — client, optional (marked `optional` in packwiz; default on) (5)

Sodium mc1.21.1-0.6.13-neoforge (newest *stable*; the 0.8.x line for 1.21.1 is alpha —
pinned down deliberately), Mouse Tweaks 2.26.1, Inventory Profiles Next 2.2.5 +
libIPN 6.6.3 + Kotlin for Forge 5.11.0 (IPN's hard deps — enable/disable the trio
together).

**Total: 38 mods** (28 required + 2 server admin + 8 optional client). At the ~40 cap;
nothing else goes in without something coming out. (Originally 25; see the manifest
expansion section below.)

## Manifest expansion — 2026-06-09 review (post-Phase-6)

Added after Brady asked for the big Create addons + Aeronautics extras + the standard
performance suite. All verified for 1.21.1 NeoForge + dependency-checked against the
pack (no new transitive requirements).

**Build/QoL Create addons (both sides):**

| Mod | Version | Why |
|---|---|---|
| Create: Connected | 1.2.2-mc1.21.1 | Kinetics QoL parts; no gating bypass |
| Copycats+ | 3.0.4 | Hull/building blocks for ships |
| Copycats+ aeronautics weight | 1.1.1 | Proper mass values for copycat blocks on ships |
| Create Deco | 2.1.3 | Outpost/ship aesthetics |
| Sable: Weighted — Create: Deco | 1.0.2 | Mass tags for Deco blocks on ships |

**Aeronautics extras (both sides):** FTB Chunks: Sable Aerospace 1.0.1 (claims vs.
flying-ship interplay — closes a real jank source since we ship FTB Chunks),
Sable Schematic Tool 0.2.6 (players save ships to files; doubles as admin ship backup)
+ **LDLib 2.2.18** — hard dep of Schematic Tool's UI that its Modrinth metadata fails
to declare (caught on first boot; `tools/check_jar_deps.py` now verifies deps from
the jars' own mods.toml so this class of miss can't recur).

**Performance suite:** ModernFix 5.27.12, Clumps 19.0.0.1, Spark 1.10.124 (both sides);
Entity Culling 1.10.2, ImmediatelyFast 1.6.10, Dynamic FPS 3.11.4 (client, optional).
⚠ Entity Culling is the first thing to disable if Sable ships flicker or vanish at
angles — culling vs. moving sub-level structures is a known category of weirdness.

**Considered in the same review and still excluded:**
- **Create: Steam 'n' Rails** — no 1.21.1 NeoForge build exists (checked Modrinth AND
  CurseForge). Re-audit if/when they port.
- **Crafts & Additions** — electricity sidesteps "rotation is infrastructure".
- **Enchantment Industry** — automated enchanting would gut the vendor enchanted-book
  coin sink (our largest money drain). Revisit only with a replacement sink designed.
- **Diesel Generators, Interiors, Create: Trimmed** — nice-to-have tier; cap pressure.

## Excluded, with reasons

- **Lightman's Currency** (2.3.0.4g exists for 1.21.1) — fallback not needed; Numismatics
  port verified. Numismatics wins on Create-native integration (brass/sturdy aesthetic,
  blaze banker, vendor blocks) and smaller scope.
- **Quest-based sell orders** — fallback not needed (same reason).
- **EMI** (1.1.24 exists) — JEI chosen instead: Create ships a first-party JEI plugin, so
  sequenced assembly / fan processing / mixing recipes are guaranteed visible, which the
  gating design depends on ("every removed recipe must have a visible replacement").
  Create-EMI integration on 1.21.1 is third-party and unverified. Revisit only if JEI
  performance bothers anyone.
- **Create Aeronautics: Compatability** (sic, 1.1.2) — band-aid mod for specific mod
  conflicts we don't currently have. Add only if a real incompatibility shows up in testing.
- **InventorySorter (cpw)** — no 1.21.1 NeoForge build on Modrinth. IPN trio covers it
  client-side.
- ~~Copycats+ aeronautics weight~~, ~~FTB Chunks: Sable Aerospace~~, ~~ModernFix etc.~~ —
  originally excluded for leanness; **added in the 2026-06-09 manifest expansion** (above).

## License / distribution flags

- packwiz packs distribute **metadata + hashes only**; players download jars directly from
  Modrinth CDN / CurseForge API at install time. No file redistribution happens, so ARR-ish
  licenses are fine to *reference*.
- Create Aeronautics: custom "Simulated Project License"; Sable: PolyForm Shield — both
  hosted on Modrinth by their authors, fetched from Modrinth CDN. OK.
- All five FTB mods report `allowModDistribution: true` on the CurseForge API (verified in
  `docs/audit/curseforge_audit.json`), so packwiz-installer can auto-download them. No
  manual-download fallbacks needed.

## Tooling note: hand-generated packwiz tree

The dev sandbox couldn't execute the packwiz binary, so `pack/` is generated by
`tools/build_pack.py` (same on-disk format: sha512 Modrinth downloads, murmur2
CurseForge metadata mode, sha256 index). **Brady: validate once with real packwiz:**

```
cd pack
packwiz refresh
git diff   # expect: no changes, or formatting-only rewrites of *.pw.toml
```

Version bumps later: edit/re-run `tools/make_manifest.py`, then `tools/build_pack.py`
(or just use `packwiz mr install <slug>` normally once you're driving).

## Install instructions (Brady)

**Client (Prism Launcher):**
1. New instance → Minecraft 1.21.1 → NeoForge 21.1.233.
2. Download [`packwiz-installer-bootstrap.jar`](https://github.com/packwiz/packwiz-installer-bootstrap/releases) into the instance's `minecraft/` folder.
3. Instance → Edit → Settings → Custom commands → Pre-launch command:
   `"$INST_JAVA" -jar packwiz-installer-bootstrap.jar file:///C:/Users/rbrad/IndieProj/skyward-industry/pack/pack.toml`
4. Launch. (Published URL:
   `https://raw.githubusercontent.com/AAARRRCCC/skyward-industry/main/pack/pack.toml`
   — the local file:/// form still works for offline testing.)

**Server:**
```
java -jar packwiz-installer-bootstrap.jar -g -s server file:///C:/Users/rbrad/IndieProj/skyward-industry/pack/pack.toml
```
then install the NeoForge 21.1.233 server normally and start it.

## Checkpoint (mandatory, Phase 0)

Boot the pack once and confirm it reaches a world: all 20 required mods load, JEI opens,
a Create ponder plays, and `/ftbquests` opens an (empty) book. Report any crash log back
before Phase 2 scripting begins.
