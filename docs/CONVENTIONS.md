# Conventions — Skyward Industry

## Repo layout

```
/pack/                  packwiz root — GENERATED, do not hand-edit (tools/build_pack.py)
/kubejs/                source of truth for scripts; synced into pack/ at build
  server_scripts/       recipes, tags, economy logic
  startup_scripts/      item/block registration (runs on both sides)
  client_scripts/       tooltips, JEI info pages
/config/ftbquests/quests/   quest book SNBT; synced into pack/ at build
/datapacks/skyward/     loot tables + tags only. NOT shipped via packwiz —
                        admin copies into <world>/datapacks/ (see CROSSING_RUNBOOK)
/docs/                  design + runbooks; /docs/TESTING/ has per-phase checklists
/tools/                 manifest + pack build scripts (python)
```

Build cycle after editing kubejs/, config/, or the mod list:

```
py tools/build_pack.py      # regenerates pack/ (pw.tomls, synced dirs, index, hashes)
```

## KubeJS files

One file per concern, numbered for load-order readability (KubeJS loads
alphabetically; our scripts must not depend on order, the numbers are for humans):

- `server_scripts/balance.js` — ALL progression quantities/multipliers. The only file
  you touch when tuning. No literal counts anywhere else — `global.BAL` only.
- `server_scripts/economy_balance.js` — ALL prices. Same rule, `global.ECON`.
- `server_scripts/ch1_andesite.js` … `ch4_crossing.js` — one file per chapter.
- `server_scripts/compat_cleanup.js` — dead-end removals, JEI hiding, misc.
- `startup_scripts/items.js` — custom item/block registration.
- `client_scripts/tooltips.js` — item lore/tooltip hints.

## Namespacing

- Recipe IDs: `skyward:<chapter>/<output_name>` (e.g. `skyward:ch2/calibrated_shaft`).
  Always set explicit IDs on added recipes so logs and quest files can reference them.
- Custom items: registered under the `kubejs:` namespace (KubeJS default — safest with
  the registry; the design doc's `skyward:aetherium` is realized as `kubejs:aetherium`).
- Tags we own: `skyward:<thing>` (e.g. `#skyward:aetherium_tier_inputs`).
- Use `c:` convention tags for materials when matching (e.g. `#c:ingots/brass`), exact
  IDs when gating (gates must not be satisfiable by lookalike items from other mods).

## Recipe gating rules (enforced in review)

1. **Replace, don't shadow.** Remove the vanilla/mod recipe first (`event.remove`),
   then add the gated one. A surviving cheap recipe is a balance bug.
2. **No dead ends.** Every removed recipe gets a JEI-visible replacement in the same
   script block. If an item is removed from progression entirely, hide it client-side
   and strip it from loot.
3. **Constants only.** Quantities come from `global.BAL` / `global.ECON`. A numeric
   literal in a chapter file is a review failure.
4. **Sell-list isolation.** Nothing the economy sells may appear in any gated recipe
   (grep the sell list against ch*.js before merging economy changes).

## Comment style

Top of each chapter file: a 3–6 line block stating the chapter's gate ("what you must
automate before this is reasonable"). Per-recipe comments only where the *intent* isn't
obvious from the ID — explain why a gate exists, never what the code does.

## Quest SNBT

- One file per chapter: `config/ftbquests/quests/chapters/<n>_<name>.snbt`.
- Quest IDs are random hex (FTB Quests convention); keep them stable once committed —
  player progress is keyed to them.
- Rewards: consumables/coins only. Never gated intermediates (pillar 4).

## Git

- Branch per phase: `phase-N-<slug>`, merged to `main` with `--no-ff`.
- `CHANGELOG.md` entry per merge.
- LF endings everywhere (`.gitattributes` enforces; packwiz hashes are byte-sensitive).
