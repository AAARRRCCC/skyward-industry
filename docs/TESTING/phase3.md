# Phase 3 manual test checklist — economy

Pre-req: phase2 checklist passed; a creative test world.

**2026-06-10 smoke test (Brady): PASSED.** Coin values confirmed exactly as assumed,
buy + sell loops work through a creative vendor, banking (card + terminal) works.
Vendor usage for reference: shift-right-click = owner config, right-click = trade;
"Mode: Buy" = players buy from it, "Mode: Sell" = players sell to it (hold the stack
in hand).

## A. Configs load

- [x] `/kubejs errors` clean (verified in first-boot log: 0 errors all script types)
- [x] Numismatics blocks present *(2026-06-10)*
- [x] Coin tooltip values match the table in economy_balance.js header
      (spur 1 / bevel 8 / sprocket 16 / cog 64 / crown 512 / sun 4096) *(2026-06-10:
      confirmed correct)*

## B. Earn loop (player side)

- [x] Vendor in sell-to mode pays out for configured goods *(2026-06-10)*
- [ ] Sell 1 calibrated shaft at 16 → paid correctly
- [ ] Vendor refuses items that don't match the configured good

## C. Spend loop

- [x] Vendor in buy-from mode dispenses goods for coins with correct change *(2026-06-10)*
- [ ] Confirm bought decor/books contain nothing usable in any JEI-visible gated
      recipe (spot-check: limestone, quartz, name tag)

## D. Banking

- [x] Bind a bank card at a blaze banker; deposit coins via bank terminal *(2026-06-10)*
- [x] Card-paid purchase at a vendor works; balance decrements *(2026-06-10)*

## E. Isolation audit (the hard rule)

- [ ] For every item in ECON.sell: JEI "recipes using this item" shows NO skyward:
      recipe and no aeronautics/simulated/aeroworks component recipe
- [ ] grep check (already done in code review, re-verify after any sell-list edit):
      nothing from ECON.sell appears in kubejs/server_scripts/ch*.js

## F. Full loop timing (balance datapoint)

- [ ] In survival with a small Ch.1 mixer setup: time 30 minutes of alloy production,
      sell it all, record spurs/hour into BALANCE_NOTES.md (target: a music disc
      should cost ~1 evening of casual Ch.1 play; Mending ~2h of Ch.2 factory)
