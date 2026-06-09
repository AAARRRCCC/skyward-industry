# Phase 4 manual test checklist — quest book

Pre-req: phase2 passed. Fresh world (quest progress is per-world).

## A. Book opens and renders

- [ ] Quest book opens (default key, or `/ftbquests open_book`); no log errors on open
- [ ] Six chapters in order: Welcome, Andesite Age, Brass Age, Aeronautics Age,
      Crossing Tier, The Crossing
- [ ] Chapter icons render (campfire, alloy, brass, smart propeller, aetherium block,
      aetherium) — a missing-texture icon means a bad item id, report it

## B. Day-one visibility (the "show the ending" rule)

- [ ] In a NEW profile with zero progress: "The Crossing" chapter is visible and its
      first quest ("The Crossing" survey brief) is completable immediately
- [ ] Later Crossing quests show locked (silhouette + lock), not hidden
- [ ] Crossing Tier chapter quests show locked until Homecoming completes

## C. Dependency graph sanity

- [ ] Welcome root completes by clicking the checkmark; its 3 children unlock
- [ ] Andesite: "The hard way" (16 alloy) → water wheel/press branch → mixer → saw +
      256-alloy milestone. No quest floats unconnected
- [ ] Brass roots off the 256-alloy milestone; the three "Line" quests all gate
      The Mechanism (needs all three)
- [ ] Aeronautics roots off The Mechanism; First Flight needs Hull plant + Engine
      works; The Hauler needs Series production + First Flight
- [ ] The Crossing's "Fit for the long water" needs both the survey brief AND
      The Hauler (cross-chapter dep renders)

## D. Task + reward mechanics (creative spot checks)

- [ ] Item tasks tick on pickup: give yourself 16 andesite alloy → "The hard way"
      completes, pays 16 spurs
- [ ] Checkmark tasks complete on click
- [ ] Multi-task quest ("The bridge": gyroscope + joystick) requires both
- [ ] Optional quests (Iron roads, both post-game logistics) show as optional pins
- [ ] Reward items land in inventory; xp_levels rewards grant levels
- [ ] No reward anywhere grants a gated intermediate (eyeball the payout of each —
      it's coins, food, torches, signs, rockets, xp only)

## E. Tone pass (subjective, you're the editor)

- [ ] No quest description runs past ~5 short paragraphs
- [ ] Flavor reads dry, not wacky; fix anything that lands wrong and note it in
      BALANCE_NOTES.md
