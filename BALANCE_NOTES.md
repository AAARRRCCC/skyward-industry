# Balance notes — playtest log

The expected long tail: log friction here, the constants get revised in response.
One entry per session. Don't editorialize less — "felt bad" is data.

## Template (copy per session)

```
### YYYY-MM-DD — <who played> — <chapter reached>
- Session length:
- What was built:
- Friction (be specific — "X took N minutes/hours and felt <bad/fine/good>"):
- Money: earned ___ spurs/hour doing ___; bought ___
- Anything bypassed or cheesed:
- One number to change and why:
```

## Known watch-list (agent's pre-registered suspicions)

- `BAL.ch2.precisionMechanism.primaryWeight` (80%) — if scrap feels like a slot
  machine, push to 90 or make it deterministic.
- `BAL.ch3.engineAssembly.loops` (4) — the single biggest lever on ship cost. A
  weekend-feel cargo hauler should want ~12–20 engines total including spares.
- `BAL.ch1.alloyGrid` — if anyone hand-crafts past the first hour, make it worse;
  if bootstrap feels impossible, make it better. Target: ~16 hand alloys then never again.
- `ECON.buy` engine assembly at 400 — if players sell engines instead of flying them,
  cut it; the sink must outbid the faucet.
- Levitite output (250mb) — no data yet on per-ship lift consumption; first ship
  build will calibrate.

## Sessions

### 2026-06-09 — Brady — creative verification (phase2 checklist)
- Session length: first pass, creative
- What was built: mixer alloy line, calibrated shaft line (press+deployer),
  tempered casing spout, precision mechanism 3-deployer line
- Friction: **first airship looks too expensive** for the "few hours of factory
  output" target — engine assembly's per-unit intermediate bill is the driver
- Money: n/a (economy not yet placed)
- Anything bypassed or cheesed: nothing found; old cheap recipes confirmed gone
- Change applied: `BAL.ch3.engineAssembly.loops` 4 → 3 (−25% coils/shafts per
  engine). Next lever if still steep after a survival build: `resonantCoil.loops`
  2 → 1. Also documented the "budget hopper" path (wooden propellers + plain
  propeller bearing + 1 portable engine, no gyroscope) in PROGRESSION.md
