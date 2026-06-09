# Phase 6 final pass — release checklist

The "ship it to friends" gate. Run on the real server install.

- [ ] Client boots to menu with zero red log lines (warnings from libraries are fine;
      anything mentioning kubejs/ftbquests/skyward is not)
- [ ] `/kubejs errors` empty in a fresh world
- [ ] JEI loads with no "recipe errors" toast; search "skyward" shows all custom
      recipe ids working
- [ ] All phase2–phase5 checklists green
- [ ] `packwiz refresh` in pack/ → no diff
- [ ] README install steps followed verbatim by one friend on a clean machine —
      they reach the server without help (the real acceptance test)
- [ ] Server: overnight stability with one ship assembled and parked (Sable physics
      idle cost), MSPT < 30 with 3 players
- [ ] First BALANCE_NOTES.md entry written after the first group session
