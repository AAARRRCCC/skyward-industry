# Quest book design — Skyward Industry

Expansion of 2026-06-10. Shipped: **130 quests across 9 chapters**
(Welcome 6 · Andesite 22 · Brass 25 · Aeronautics 27 · Crossing Tier 8 ·
The Crossing 10 · The Ledger 12 · Company Town 14 · The Flight Computer 6).

## Gating philosophy (the no-spam rule)

Brady's rule: no frivolous checkmarks that can be clicked through. Priority order of
task types, with the full advancement inventory in `docs/audit/advancements.md`:

1. **Advancement tasks** — the gold standard. Create/Aeronautics/Simulated/Numismatics
   advancements fire from mod code on real behavior ("fill an envelope with hot air",
   "place and power a portable engine", "name a contraption with a nameplate"). ~55
   quests use these.
2. **Item tasks** — for production milestones where the *quantity* is the point
   (16 calibrated shafts) or loot collection (ship's logs). ~55 quests.
3. **Observation tasks** — "stand at an admin market" gates on looking at a
   `numismatics:creative_vendor`, which only admins can place. 1 quest.
4. **Checkmarks** — exactly **5** of 124: two chapter-opening reads (Welcome, the
   survey brief), roll credits (ceremonial), claim-a-chunk (undetectable by design),
   and the 20k mark (admin-wireable to a location task; bracketed by real gates on
   both sides, so clicking it early gains nothing — Landfall still requires
   physically looting the site). None pays more than a token.

Hidden/secret quests use `hide_until_deps_complete` so the book doesn't spoil the
mod's hidden advancements; they pay better than their neighbors.

Reward policy unchanged: coins/food/xp only, never gated items. Scale: minor 8–16
spurs · standard 1–2 sprockets · solid 1 cog · milestone 1–2 crowns · capstone 1 sun.

## Chapter map

### 0 Welcome (6) — orientation, two clicks max
brief (checkmark) → recipe viewer (adv `create:root`) / claim (checkmark) /
market visit (observation creative_vendor) / first night (adv `minecraft:adventure/sleep_in_bed`) /
union card (item wrench)

### 1 Andesite Age (22) — the full Create basics arc
Spine: 16 alloy → water wheel (adv) → press (adv) → andesite casing (adv) → mixer
(adv, fires on your first mixed alloy) → compacting (adv) → 256-alloy capstone.
Branches: windmill, shifting gears, encased fan → fan processing (washing, the iron
farm enabler), saw processing, millstone, belts → funnels → chutes, super glue →
contraption actors (tree farm/quarry beat), vault (item), kitted out (goggles+wrench
adv). Secrets: lava wheel, hand-crank exhaustion.

### 2 Brass Age (24) — heat, fluids, precision; trains branch
Spine: blaze burner (adv) → 16 brass (item) → brass casing (adv) → rose quartz (adv)
→ deployer (adv) → the three custom lines (items, kept from v1) → precision mechanism
(4x item) → mechanical crafter (adv).
Fluids branch: copper casing → pump → infinite lava (adv `hose_pulley_lava`, feeds
the quench) → spout (adv) → tempered casing (item).
Power branch: steam engine (adv). Crushing branch: crushing wheels (adv) → max-speed
crushers (adv). Logistics: mechanical arm (adv).
Trains branch (6): sturdy sheet (adv) → railway casing (adv) → 64 tracks (item) →
first train (adv) → schedule (adv) → 5000-block journey (adv `long_travel` — the
pre-airship Highmoor run). Secret: deployer fist-bump.

### 3 Aeronautics Age (25) — shipwright school; offroad branch
Assembly basics: physics assembler (item) → honey glue (adv) → handles (adv) →
steering (adv). Lift: 32 envelopes (item) → hot air fill (adv `head_in_the_clouds`).
Thrust: propeller powered (adv) → propeller bearing assembled (adv
`in_thrust_we_trust`). Levitite: 32 end stone powder (item, End access) →
crystallize (adv). Engines: engine assembly 1 then 4 (items) → portable engine
placed+powered (adv `steamless_engine`). Avionics: gyro mech x2 (item) → gimbal,
altitude, nav table (advs) → the bridge (gyroscope+joystick items).
**First flight = adv `i_declare_thee`: the mod itself detects christening a named
ship. "Name her" is now enforced.** Then: set course >5000 (adv `far_from_home` =
outpost run), the hauler (item kit: 8 engine assemblies + docking connector, after
docking adv). Ropes + docking (advs). Secrets: 0% atmosphere, phantom vs potato
cannon. Offroad (3): tires+mounts (items), borehead, rockcutter.

### 4 Crossing Tier (8) — post-game
Solid proof (block), Creative Motor (item, capstone), creative crate/tank (items,
optional), pearlescent levitite (hidden adv), cloud-skipper disc (adv
`song_of_the_sky`), full archive (all 4 ship's logs), roll credits (checkmark).

### 5 The Crossing (10) — the voyage
Brief (checkmark, day-one visible) → fit-out (REAL kit: adv `that_should_do_for_now`
10h fuel + levitite bucket + 16 spare envelopes + rations) → past-20k (checkmark,
admin-wireable to location task; bracketed by real gates) → landfall (log I item) →
cache hunt (logs II+III) → the vault (log IV) → aetherium (item) → homecoming
(12 aetherium = one motor's worth) → second expedition (repeatable, consumes 16
aetherium). Secret: call of the void.

### 6 The Ledger (12) — economy arc, all real gates
First spur → first cog → first crown → first sun (items; money accumulates through
play). Vendor exchange (adv `money_laundering`), town bank (blaze banker item),
player shop (adv `table_cloth_shop`), then Create 6's logistics-economy chain:
cardboard (adv) → packager (adv) → stock ticker (adv) → frogport (adv) → factory
gauge (adv, capstone).

### 8 The Flight Computer (6) — CC: Tweaked, visibly optional
Every quest carries `optional: true` and the chapter says so in its first
description: computers are a parallel toy, never required. Item-gated on CC
hardware (computer → turtle/monitors/modems → advanced computer + cable into a
christened ship → pocket remote). Quest IDs `4C`/`5C`/`6C`.

### 7 Company Town (14) — decor sidequests that feed the coin sink
Item milestones in Create Deco (lamps, catwalks, containers, hulls, mesh, bars,
windows), Copycats+ (blocks, panels), placards, nameplates, sails; cuckoo-clock
bedtime (adv) and jukebox arm (hidden adv). Rewards skew coin-heavy on purpose:
this chapter pays for paint.

## ID allocation

Existing prefixes kept (quests `0A`–`0F`, rewards `1X`, tasks `2X`). New chapters:
The Ledger quests `4A...`, rewards `5A...`, tasks `6A...`; Company Town `4B`/`5B`/`6B`.
Additional tasks/rewards on a quest use a high-nibble offset from the quest number:
second = +0xA0, third = +0xB0, fourth = +0xC0 (e.g. quest `..09` → tasks `..09`,
`..A9`, `..B9`). Never renumber a shipped ID.

## Flow invariants (checked in the review pass)

1. Every chapter's first quest is reachable the moment its chapter-gate completes.
2. No quest depends on a sibling that teaches a *later* machine.
3. A player following only the spine never hits a wall that a branch was supposed
   to teach (branches are enrichment, not hidden prerequisites).
4. Advancement-gated quests must be *causable on purpose* (no "witness a train
   crash" style gates in required paths; those are secrets).
5. Checkmark count stays ≤ 4.
