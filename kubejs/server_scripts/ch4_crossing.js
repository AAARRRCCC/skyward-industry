// =============================================================================
// CHAPTER 4 — THE CROSSING TIER
// Aetherium has no recipe. It exists only in loot chests at the Crossing
// destination (datapacks/skyward). Everything here mixes Ch.3 output with it.
// Counts in these mechanical-crafting patterns are documented in balance.js
// (ch4); editing a count means editing the pattern here.
// =============================================================================

ServerEvents.recipes(event => {
	// --- Aetherium storage block (and back) ------------------------------------
	event.shaped(Item.of('kubejs:aetherium_block', 1), [
		'AAA',
		'AAA',
		'AAA'
	], {
		A: 'kubejs:aetherium'
	}).id('skyward:ch4/aetherium_block')
	event.shapeless(Item.of('kubejs:aetherium', 9), ['kubejs:aetherium_block'])
		.id('skyward:ch4/aetherium_from_block')

	// --- Creative Motor ----------------------------------------------------------
	// 12 aetherium, 4 engine assemblies, 4 gyroscopic mechanisms, 4 sturdy
	// sheets, 1 precision mechanism. The factory's graduation certificate.
	event.custom({
		type: 'create:mechanical_crafting',
		accept_mirrored: false,
		category: 'misc',
		key: {
			A: { item: 'kubejs:aetherium' },
			E: { item: 'simulated:engine_assembly' },
			G: { item: 'simulated:gyroscopic_mechanism' },
			S: { item: 'create:sturdy_sheet' },
			P: { item: 'create:precision_mechanism' }
		},
		pattern: [
			'SAAAS',
			'AGEGA',
			'AEPEA',
			'AGEGA',
			'SAAAS'
		],
		result: { count: 1, id: 'create:creative_motor' },
		show_notification: false
	}).id('skyward:ch4/creative_motor')

	// --- Small post-game tier: creative logistics ---------------------------------
	event.custom({
		type: 'create:mechanical_crafting',
		accept_mirrored: false,
		category: 'misc',
		key: {
			A: { item: 'kubejs:aetherium' },
			C: { item: 'create:brass_casing' },
			V: { item: 'create:item_vault' }
		},
		pattern: ['ACA', 'CVC', 'ACA'],
		result: { count: 1, id: 'create:creative_crate' },
		show_notification: false
	}).id('skyward:ch4/creative_crate')

	event.custom({
		type: 'create:mechanical_crafting',
		accept_mirrored: false,
		category: 'misc',
		key: {
			A: { item: 'kubejs:aetherium' },
			C: { item: 'create:copper_casing' },
			T: { item: 'create:fluid_tank' }
		},
		pattern: ['ACA', 'CTC', 'ACA'],
		result: { count: 1, id: 'create:creative_fluid_tank' },
		show_notification: false
	}).id('skyward:ch4/creative_fluid_tank')
})
