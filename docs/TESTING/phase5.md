# Phase 5 manual test checklist — Crossing support package

Pre-req: datapack copied into the test world (`<world>/datapacks/skyward/`), `/reload`.

## A. Datapack loads

- [ ] `/datapack list` shows `"file/skyward"` enabled; no errors in log on /reload
- [ ] `/loot give @s loot skyward:chests/crossing_landfall` → ships_log_1 + 2–4
      aetherium + supplies
- [ ] `/loot give @s loot skyward:chests/crossing_cache` x5 → aetherium 1–3 each;
      occasional log II/III
- [ ] `/loot give @s loot skyward:chests/crossing_vault` → ships_log_4 + 6–10
      aetherium + a bonus item

## B. Chest binding

- [ ] Place a chest, `/data merge block ~ ~ ~1 {LootTable:"skyward:chests/crossing_cache"}`,
      open it as a NON-op second account → loot rolls
- [ ] Once opened, loot does not re-roll

## C. End-to-end Ch.4 (creative)

- [ ] With looted aetherium: craft aetherium block ↔ 9 aetherium
- [ ] Mechanical crafter array accepts the creative motor recipe; output works as a
      rotation source
- [ ] Quest chain: pick up ships_log_1 → "Landfall" completes; aetherium → "Aetherium"
      completes; Homecoming checkmark unlocks Crossing Tier chapter

## D. Lore items

- [ ] All four logs: texture, name ("Ship's Log, Entry I" … "Final Entry"),
      tooltip story lines render, stack size 1
