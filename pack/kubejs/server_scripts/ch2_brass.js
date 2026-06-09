// =============================================================================
// CHAPTER 2 — BRASS AGE
// Gate: three custom intermediates exist only to force production lines:
//   calibrated shaft  -> press + deployer loop
//   tempered casing   -> spout (fluid logistics)
//   resonant coil     -> deployer + electron tube line
// The precision mechanism is rebuilt on top of them: multi-machine, multi-line.
// =============================================================================

ServerEvents.recipes(event => {
	const B = global.BAL.ch2

	// --- Calibrated Shaft ------------------------------------------------------
	// Per unit: 1 shaft + loops x 1 andesite alloy, through press + deployer.
	event.custom({
		type: 'create:sequenced_assembly',
		ingredient: { item: 'create:shaft' },
		loops: B.calibratedShaft.loops,
		results: [{ id: 'kubejs:calibrated_shaft' }],
		sequence: [
			{
				type: 'create:pressing',
				ingredients: [{ item: 'kubejs:incomplete_calibrated_shaft' }],
				results: [{ id: 'kubejs:incomplete_calibrated_shaft' }]
			},
			{
				type: 'create:deploying',
				ingredients: [{ item: 'kubejs:incomplete_calibrated_shaft' }, { item: 'create:andesite_alloy' }],
				results: [{ id: 'kubejs:incomplete_calibrated_shaft' }]
			}
		],
		transitional_item: { id: 'kubejs:incomplete_calibrated_shaft' }
	}).id('skyward:ch2/calibrated_shaft')

	// --- Tempered Casing -------------------------------------------------------
	// Spout-fill a brass casing with lava. Forces fluid infrastructure.
	event.custom({
		type: 'create:filling',
		ingredients: [
			{ item: 'create:brass_casing' },
			{ type: 'neoforge:single', amount: B.temperedCasing.lavaMb, fluid: 'minecraft:lava' }
		],
		results: [{ id: 'kubejs:tempered_casing' }]
	}).id('skyward:ch2/tempered_casing')

	// --- Resonant Coil ---------------------------------------------------------
	// Golden sheet core; each loop deploys an electron tube and presses it home.
	event.custom({
		type: 'create:sequenced_assembly',
		ingredient: { item: 'create:golden_sheet' },
		loops: B.resonantCoil.loops,
		results: [{ id: 'kubejs:resonant_coil' }],
		sequence: [
			{
				type: 'create:deploying',
				ingredients: [{ item: 'kubejs:incomplete_resonant_coil' }, { item: 'create:electron_tube' }],
				results: [{ id: 'kubejs:incomplete_resonant_coil' }]
			},
			{
				type: 'create:pressing',
				ingredients: [{ item: 'kubejs:incomplete_resonant_coil' }],
				results: [{ id: 'kubejs:incomplete_resonant_coil' }]
			}
		],
		transitional_item: { id: 'kubejs:incomplete_resonant_coil' }
	}).id('skyward:ch2/resonant_coil')

	// --- Precision Mechanism, rebuilt -------------------------------------------
	// Core is now a calibrated shaft (your own line feeds this one).
	event.remove({ id: 'create:sequenced_assembly/precision_mechanism' })
	event.custom({
		type: 'create:sequenced_assembly',
		ingredient: { item: 'kubejs:calibrated_shaft' },
		loops: B.precisionMechanism.loops,
		results: [
			{ chance: B.precisionMechanism.primaryWeight, id: 'create:precision_mechanism' },
			{ chance: B.precisionMechanism.scrapWeight, id: 'create:shaft' }
		],
		sequence: [
			{
				type: 'create:deploying',
				ingredients: [{ item: 'create:incomplete_precision_mechanism' }, { item: 'create:cogwheel' }],
				results: [{ id: 'create:incomplete_precision_mechanism' }]
			},
			{
				type: 'create:deploying',
				ingredients: [{ item: 'create:incomplete_precision_mechanism' }, { item: 'create:large_cogwheel' }],
				results: [{ id: 'create:incomplete_precision_mechanism' }]
			},
			{
				type: 'create:deploying',
				ingredients: [{ item: 'create:incomplete_precision_mechanism' }, { tag: 'c:nuggets/iron' }],
				results: [{ id: 'create:incomplete_precision_mechanism' }]
			}
		],
		transitional_item: { id: 'create:incomplete_precision_mechanism' }
	}).id('skyward:ch2/precision_mechanism')
})
