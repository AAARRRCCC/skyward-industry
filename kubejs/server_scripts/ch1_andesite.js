// =============================================================================
// CHAPTER 1 — ANDESITE AGE
// Gate: andesite alloy leaves the crafting grid. The mechanical mixer is the
// real recipe; a deliberately bad grid recipe stays in so a fresh spawn can
// bootstrap their first press/mixer without it ever being worth scaling.
// =============================================================================

ServerEvents.recipes(event => {
	const B = global.BAL.ch1

	// Wipe every stock route to andesite alloy (Create's two grid recipes and
	// any processing routes). Ours below are the only ways in.
	event.remove({ output: 'create:andesite_alloy' })

	// --- The real recipe: mechanical mixing -----------------------------------
	let mixIngredients = []
	for (let i = 0; i < B.alloyMix.andesite; i++) mixIngredients.push({ item: 'minecraft:andesite' })
	for (let i = 0; i < B.alloyMix.ironNuggets; i++) mixIngredients.push({ tag: 'c:nuggets/iron' })
	event.custom({
		type: 'create:mixing',
		ingredients: mixIngredients,
		results: [{ id: 'create:andesite_alloy', count: B.alloyMix.output }]
	}).id('skyward:ch1/andesite_alloy_mixing')

	// Zinc parity route (Create shipped one; keep the choice, same price).
	let mixZinc = []
	for (let i = 0; i < B.alloyMix.andesite; i++) mixZinc.push({ item: 'minecraft:andesite' })
	for (let i = 0; i < B.alloyMix.ironNuggets; i++) mixZinc.push({ tag: 'c:nuggets/zinc' })
	event.custom({
		type: 'create:mixing',
		ingredients: mixZinc,
		results: [{ id: 'create:andesite_alloy', count: B.alloyMix.output }]
	}).id('skyward:ch1/andesite_alloy_mixing_zinc')

	// --- The hand fallback: punishing, on purpose ------------------------------
	let gridIngredients = []
	for (let i = 0; i < B.alloyGrid.andesite; i++) gridIngredients.push('minecraft:andesite')
	for (let i = 0; i < B.alloyGrid.ironNuggets; i++) gridIngredients.push('#c:nuggets/iron')
	event.shapeless(Item.of('create:andesite_alloy', B.alloyGrid.output), gridIngredients)
		.id('skyward:ch1/andesite_alloy_by_hand')
})
