# Economy runbook — Numismatics admin setup (Brady)

Backend decision: **Create: Numismatics 1.0.20** (Phase 0 verified the 1.21.1 NeoForge
port; see docs/MOD_DECISIONS.md). Prices are canonical in
`kubejs/startup_scripts/economy_balance.js` — if you change a price, change it there
first, then update the vendor.

## Concepts (5-minute orientation)

- **Coins:** spur (1) → bevel (8) → sprocket (16) → cog (64) → crown (512) → sun (4096).
  Verify the values against coin tooltips on first boot; all prices in our tables are
  written in spurs.
- **Vendor** (`numismatics:vendor`): sells OR buys one item type, against a bank
  account. Sneak-right-click to configure as owner.
- **Creative Vendor** (`numismatics:creative_vendor`): admin-only variant with
  infinite stock / infinite money. **Use this for all admin shops.**
- **Blaze Banker** (`numismatics:blaze_banker`): holds an account; right-click with a
  bank card to bind. Players use **Bank Terminals** + cards for their own balances.
- Players never need a bank account to USE a vendor — coins work directly.

## Capital shop (spawn town) — one-time setup

1. Creative mode, OP, with `economy_balance.js` open beside you.
2. Place one **Creative Vendor per buy-list row** (10 total), set mode to **buying**:
   - stock item: the listed good; price: the spur value from `ECON.buy`
   - label the shop stall with the item on an item frame
3. Place one **Creative Vendor per sell-list row**, mode **selling**, prices from
   `ECON.sell`. For enchanted books: put the exact enchanted book (e.g. Mending) into
   the vendor as the trade item — one vendor per book.
4. Put a **Bank Terminal** + a stack of blank **bank cards** in a chest labeled "open
   your account here" next to a **Blaze Banker**.
5. One **change machine**: a creative vendor in sell mode offering **1 cog for 64
   spurs** (fair exchange). This is what fires the `numismatics:money_laundering`
   advancement behind the quest book's "Exchange rate" quest — without this vendor
   that quest is uncompletable, so it's required, not flavor.

Time estimate: ~45 minutes for all ~27 vendors.

## Outpost shops

Four outposts, each with 2 premium-buy vendors (price = `buy x premiumMultiplier`,
round UP to whole spurs) and 1–3 themed sell vendors. Exact stock per outpost is in
`docs/OUTPOSTS.md`. Same creative-vendor procedure as above.

## Invariants (check before opening the server)

- [ ] No vendor sells anything on the trap list in `economy_balance.js` header
      (wool, sticks, planks, blast furnaces, crimsite/asurine/veridium/ochrum, end stone).
- [ ] No vendor sells any `kubejs:*` item or any item appearing in `ch*.js` recipes.
- [ ] Every buy-list vendor pays out (test-sell one item of each).
- [ ] Buy prices match `ECON.buy` exactly; premium = 1.5x at outposts.

## Money flow sanity (why these numbers)

A modest Ch.2 line making 60 calibrated shafts/hour earns ~960 spurs (~2 crowns)/hour
of AFK-adjacent income. A Mending book at 2048 is therefore ~2 hours of mid-game
factory output — luxury, not trivial. Engine assemblies at 400 each mean a Ch.3
player banks a crown per ~1.3 engines; that funds decor and discs, never progression
(nothing gated is sold, at any price).
