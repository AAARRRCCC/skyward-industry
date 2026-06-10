// =============================================================================
// COMPAT / CLEANUP
// Gating removals live with their replacements in the chapter files (no dead
// ends — see docs/CONVENTIONS.md). This file holds playtest-discovered recipe
// conflicts and third-party data fixes, so the chapter files stay pure
// progression.
//
// NOTE: data-file-level fixes live in kubejs/data/ (KubeJS virtual datapack,
// overrides mod data before the vanilla parser sees it). Current overrides:
//   - kubejs/data/createdeco/recipe/placard.json — Create Deco 2.1.3 ships this
//     recipe with a typo'd ingredient ({"id": ...} instead of {"item": ...})
//     that errors on every load. Delete the override when fixed upstream.
// =============================================================================

ServerEvents.recipes(event => {
	// (nothing yet — script-level conflicts go here)
})
