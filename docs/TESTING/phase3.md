# Phase 3 manual test checklist — economy

Pre-req: phase2 checklist passed; a creative test world.

## A. Configs load

- [ ] `/kubejs errors` clean after adding economy_balance.js (it's constants-only —
      any error here is a syntax slip)
- [ ] Numismatics blocks present: `/give @s numismatics:vendor`, `creative_vendor`,
      `blaze_banker`, `bank_terminal`, coins (`numismatics:spur` … `numismatics:sun`)
- [ ] Coin tooltip values match the table in economy_balance.js header
      (spur 1 / bevel 8 / sprocket 16 / cog 64 / crown 512 / sun 4096).
      **If they differ, fix the header + ECONOMY_RUNBOOK before any vendor is placed.**

## B. Earn loop (player side)

- [ ] Place a creative vendor, owner-configure: buying, andesite alloy, 1 spur
- [ ] As a second account (or survival-mode self), sell 64 alloy → receive 64 spurs
      (1 cog after change-making)
- [ ] Sell 1 calibrated shaft at 16 → paid correctly
- [ ] Vendor refuses items that don't match the configured good

## C. Spend loop

- [ ] Creative vendor selling Mending book at 2048 spurs: buy succeeds with mixed
      coins; correct change
- [ ] Buy 64 limestone at 2 spurs each
- [ ] Confirm bought decor/books contain nothing usable in any JEI-visible gated
      recipe (spot-check: limestone, quartz, name tag)

## D. Banking

- [ ] Bind a bank card at a blaze banker; deposit coins via bank terminal
- [ ] Card-paid purchase at a vendor works; balance decrements

## E. Isolation audit (the hard rule)

- [ ] For every item in ECON.sell: JEI "recipes using this item" shows NO skyward:
      recipe and no aeronautics/simulated/aeroworks component recipe
- [ ] grep check (already done in code review, re-verify after any sell-list edit):
      nothing from ECON.sell appears in kubejs/server_scripts/ch*.js

## F. Full loop timing (balance datapoint)

- [ ] In survival with a small Ch.1 mixer setup: time 30 minutes of alloy production,
      sell it all, record spurs/hour into BALANCE_NOTES.md (target: a music disc
      should cost ~1 evening of casual Ch.1 play; Mending ~2h of Ch.2 factory)
