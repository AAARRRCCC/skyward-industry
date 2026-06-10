# Changelog

## [Unreleased]

### Placement tooling (2026-06-10)
- tools/gen_schematics.py: generates WorldEdit .schem files (Sponge v2, hand-
  rolled NBT, self-validating). First set: 4 market stall variants + vendor
  kiosk in admin_assets/schematics/; gold block = vendor position convention.
- WorldEdit side server -> both so single-player build prep works.
- docs/PLACEMENT.md: paste workflow, market layout guidance, curated community
  schematic sources per outpost landmark.

### Fix: placard override via virtual datapack (2026-06-09)
- The KubeJS-side remove couldn't suppress Create Deco's malformed placard
  recipe (unparseable recipes pass through to vanilla). Now overridden at the
  data level: kubejs/data/createdeco/recipe/placard.json ships the corrected
  JSON, so the vanilla parser never sees the broken file.

### Fix: first-boot log triage (2026-06-09)
- KubeJS loaded 0 errors (3/3 startup, 5/5 server) — script-load acceptance met.
- Removed Sable: Physics Compat (39 → 38 mods): 1.3.0 data format incompatible
  with Sable 1.2.2, and it only tags blocks from mods we don't ship.
- compat_cleanup.js: replaced Create Deco's malformed `createdeco:placard`
  un-dye recipe (upstream typo: ingredient `id` vs `item`).
- Remaining log noise (mixin probes, libIPN/IPN pack-icon paths, simulated
  rope_connector model) is third-party and cosmetic; no action.

### Fix: global assignment in server scripts (2026-06-09, first boot)
- KubeJS 2101 forbids assigning `global` outside startup scripts. Moved
  balance.js + economy_balance.js to kubejs/startup_scripts/ (contents
  unchanged; server scripts still read global.BAL/global.ECON).
- Tuning consequence documented everywhere: balance edits need a restart,
  /kubejs reload is not enough.

### Fix: LDLib dependency (2026-06-09, first boot)
- First boot caught: Sable Schematic Tool requires LDLib (modid `ldlib2`) ≥ 2.2.6
  but does not declare it on Modrinth. Added ldlib 2.2.18 (38 → 39 mods).
- New tools/check_jar_deps.py: reads neoforge.mods.toml inside every jar
  (jar-in-jar aware) and verifies all required modids are provided — the
  registry-metadata dep check is no longer trusted on its own.

### Manifest expansion (2026-06-09, post-review)
- +13 mods (25 → 38): Create: Connected, Copycats+ (+weight compat), Create Deco
  (+weight compat), FTB Chunks: Sable Aerospace, Sable Schematic Tool, ModernFix,
  Clumps, Spark, Entity Culling / ImmediatelyFast / Dynamic FPS (client optional).
- Dependency-checked: no new transitive requirements.
- Still excluded with reasons (MOD_DECISIONS.md): Steam 'n' Rails (no 1.21.1 NeoForge
  build anywhere), Crafts & Additions, Enchantment Industry, Diesel Generators.

### Phase 6 — polish & balance support (2026-06-09)
- README.md: friend-facing install (packwiz-installer pre-launch command), server
  install, server.properties recommendations, repo map, tuning loop.
- BALANCE_NOTES.md: session log template + pre-registered tuning watch-list.
- docs/TESTING/phase6.md release checklist.

### Phase 5 — Crossing support package (2026-06-09)
- Datapack (pack_format 48): 3 chest loot tables (landfall / cache / vault);
  one full site clear yields ~16-34 aetherium vs 12 for a creative motor.
- docs/CROSSING_RUNBOOK.md: Chunky pregen (site disk + corridor strip), WorldEdit
  paste workflow, chest LootTable binding commands, datapack install, optional
  location-task quest wiring, walk-through checklist.
- Ship's-log lore items shipped in Phase 2 registration; stocked via loot + frames.
- docs/TESTING/phase5.md.

### Phase 4 — quest book (2026-06-09)
- 6 FTB Quests chapters (33 quests): Welcome, Andesite, Brass, Aeronautics,
  Crossing Tier, The Crossing (visible from day one, locked, shows the ending).
- Rewards are coins/consumables/xp only; showcase checkmark quests for vessel
  milestones; cross-chapter dependency graph validated (tools/validate_refs.py:
  118 unique ids, 39 deps resolve, 85 item refs exist in extracted registries).
- docs/TESTING/phase4.md.

### Phase 3 — economy (2026-06-09)
- Backend: Numismatics (per Phase 0). economy_balance.js is the canonical price
  source (10 buy goods, ~20 sell goods, 1.5x outpost premium).
- Sell-list isolation verified by grep: nothing sellable appears in any gated recipe;
  trap items (wool, sticks, blast furnace, crushable ore-stones) documented + excluded.
- docs/ECONOMY_RUNBOOK.md (vendor/banker setup), docs/OUTPOSTS.md (4 outpost specs),
  docs/TESTING/phase3.md (earn-and-spend loop).
- Stretch flagged, not built: weekly rotating buy orders.

### Phase 2 — progression gating (2026-06-09)
- Verified all item IDs / recipe JSON shapes against the actual 1.21.1 jars
  (docs/audit/jars/, docs/audit/recipes_aero.md) — Aeronautics post-dates training data.
- Ch.1: andesite alloy is mixer-made; punishing hand fallback retained.
- Ch.2: custom intermediates (calibrated shaft, tempered casing, resonant coil);
  precision mechanism rebuilt on them (80% yield).
- Ch.3: engine assembly, gyroscopic mechanism, envelopes, levitite, propellers,
  Aeroworks parts, physics assembler all re-priced to eat Ch.2 output.
- Ch.4: creative motor/crate/fluid tank gated behind loot-only aetherium.
- Custom textures generated (tools/gen_textures.py); balance constants in balance.js.
- docs/PROGRESSION.md, docs/TESTING/phase2.md.

### Phase 1 — scaffolding (2026-06-09)
- Repo layout: kubejs/, config/ftbquests/quests/, datapacks/skyward/, docs/TESTING/.
- docs/CONVENTIONS.md (file naming, namespacing, gating rules, comment style).
- .gitattributes (LF enforcement — packwiz hashes are byte-sensitive), .gitignore.

### Phase 0 — manifest (2026-06-09)
- Verified full 1.21.1 NeoForge stack; pinned 25 mods (docs/MOD_DECISIONS.md).
- Economy decision: Create: Numismatics 1.0.20 (port exists; no fallback needed).
- packwiz tree generated by tools/build_pack.py; validate with `packwiz refresh`.
