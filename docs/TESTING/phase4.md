# Phase 4 manual test checklist — quest book (expanded, 124 quests)

Pre-req: phase2 passed. Fresh world (quest progress is per-world). The 2026-06-10
expansion replaced most checkmarks with advancement/item/observation gates; the
point of this pass is confirming the gates FIRE, not just that quests render.

## A. Book opens and renders

- [ ] Book opens; no log errors
- [ ] Eight chapters in order: Welcome, Andesite Age, Brass Age, Aeronautics Age,
      Crossing Tier, The Crossing, The Ledger, Company Town
- [ ] All chapter icons render (a purple-black icon = bad item id, report it)
- [ ] Secret quests are NOT visible on a fresh profile (lava wheel, hand crank,
      fist bump, 0% atmosphere, ghostbuster, glimmering sea, pink levitite, DJ)

## B. Day-one visibility

- [ ] New profile: The Crossing chapter visible; survey brief completable now
- [ ] The Ledger + Company Town unlock off Welcome quests (market visit / brief)
- [ ] Crossing Tier quests all locked behind Homecoming

## C. Advancement gates fire (the critical pass — spot-check in creative)

- [ ] Place + power a water wheel → "Something turns" ticks (NOT on item pickup)
- [ ] Right-click stripped log with alloy → "The Andesite Age" ticks
- [ ] Press a sheet → "Heavy industry, small"; mix anything → "The real recipe"
- [ ] Wash something with a fan → "Processing by particle"
- [ ] Equip goggles + wrench together → "Kitted out"
- [ ] Obtain blaze burner → Brass chapter root opens
- [ ] Hose pulley in big lava → "Tapping the mantle"; spout-fill → "Sploosh"
- [ ] Deployer placed + powered → "Artificial intelligence"
- [ ] Train assembled → "All aboard"; 5000-block ride → "Field trip"
- [ ] Honey-glue blocks → "Not gonna sugarcoat it"; grab handle → "Get a grip";
      spin steering wheel → "Unpowered steering"
- [ ] Fill envelope with hot air → "Head in the clouds"
- [ ] Power a propeller → "For every action"
- [ ] Place + power portable engine → "Steamless engine"
- [ ] Place gimbal / altitude / nav table → respective avionics quests
- [ ] **Nameplate a ship → "First flight" completes** (the christening gate)
- [ ] Nav target >5000 blocks → "Trade winds"
- [ ] Buy coins at a change-machine vendor → "Exchange rate" (needs the cog-for-
      spurs vendor from ECONOMY_RUNBOOK §capital shop step 5)
- [ ] Table cloth shop → "Open for business"; packager → "Post production"
- [ ] Cuckoo clock at dusk → "Interior design"

## D. Item + observation gates

- [ ] Stare at a creative vendor ~1s → "Money exists" ticks (won't tick on player-
      crafted regular vendors)
- [ ] Multi-task quests need ALL parts (the bridge: gyroscope AND joystick;
      fit-out: fuel advancement AND 3 item stacks)
- [ ] "The trade route" repeats and CONSUMES 16 aetherium per completion; nothing
      else consumes items on completion (spot-check homecoming leaves your 12)
- [ ] Archive quest ticks per-log, doesn't need all four at once

## E. Reward audit

- [ ] No reward anywhere grants a gated item (coins/xp/food/torches/signs/rockets only)
- [ ] Ledger money-milestone quests pay xp, not coins (no money-for-money loop)

## F. Pacing read-through (subjective, you're the editor)

- [ ] Each chapter's spine reads in build order; branches never block the spine
- [ ] No description over ~4 short paragraphs; tone stays dry; flag any clunkers
      in BALANCE_NOTES.md
