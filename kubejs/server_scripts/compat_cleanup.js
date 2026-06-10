// =============================================================================
// COMPAT / CLEANUP
// Gating removals live with their replacements in the chapter files (no dead
// ends — see docs/CONVENTIONS.md). This file holds playtest-discovered recipe
// conflicts and third-party data fixes, so the chapter files stay pure
// progression.
// =============================================================================

ServerEvents.recipes(event => {
	// Create Deco 2.1.3 ships `createdeco:placard` with a typo'd ingredient
	// ({"id": "minecraft:white_dye"} where the codec wants {"item": ...}), which
	// errors in the log on every world load / reload. Replace it with what the
	// mod meant: un-dye any colored placard back to the plain create:placard.
	// Drop both when Create Deco fixes it upstream.
	event.remove({ id: 'createdeco:placard' })
	event.shapeless(Item.of('create:placard', 1), ['#createdeco:placards', 'minecraft:white_dye'])
		.id('skyward:compat/placard_undye')
})
