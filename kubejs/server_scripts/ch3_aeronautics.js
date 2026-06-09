// =============================================================================
// CHAPTER 3 — AERONAUTICS AGE
// Gate: every airship component is re-priced to eat Ch.2 intermediates in bulk.
// The shipyard is the factory's customer. Target: minimal hopper ~ a few hours
// of factory output; cargo hauler ~ a weekend of scaled-up lines.
// =============================================================================

ServerEvents.recipes(event => {
	const B = global.BAL.ch3

	// --- Engine Assembly (simulated) --------------------------------------------
	// Tempered casing core; per loop: saw cut, press, deploy resonant coil,
	// deploy calibrated shaft. Cost/unit = 1 casing + loops x (coil + shaft).
	event.remove({ id: 'simulated:sequenced_assembly/engine_assembly' })
	event.custom({
		type: 'create:sequenced_assembly',
		ingredient: { item: 'kubejs:tempered_casing' },
		loops: B.engineAssembly.loops,
		results: [{ id: 'simulated:engine_assembly' }],
		sequence: [
			{
				type: 'create:cutting',
				ingredients: [{ item: 'simulated:incomplete_engine_assembly' }],
				results: [{ id: 'simulated:incomplete_engine_assembly' }]
			},
			{
				type: 'create:pressing',
				ingredients: [{ item: 'simulated:incomplete_engine_assembly' }],
				results: [{ id: 'simulated:incomplete_engine_assembly' }]
			},
			{
				type: 'create:deploying',
				ingredients: [{ item: 'simulated:incomplete_engine_assembly' }, { item: 'kubejs:resonant_coil' }],
				results: [{ id: 'simulated:incomplete_engine_assembly' }]
			},
			{
				type: 'create:deploying',
				ingredients: [{ item: 'simulated:incomplete_engine_assembly' }, { item: 'kubejs:calibrated_shaft' }],
				results: [{ id: 'simulated:incomplete_engine_assembly' }]
			}
		],
		transitional_item: { id: 'simulated:incomplete_engine_assembly' }
	}).id('skyward:ch3/engine_assembly')

	// --- Gyroscopic Mechanism (simulated) ----------------------------------------
	// Precision mechanism core; per loop deploys a cogwheel and a resonant coil.
	event.remove({ id: 'simulated:sequenced_assembly/gyroscopic_mechanism' })
	event.custom({
		type: 'create:sequenced_assembly',
		ingredient: { item: 'create:precision_mechanism' },
		loops: B.gyroMechanism.loops,
		results: [{ id: 'simulated:gyroscopic_mechanism' }],
		sequence: [
			{
				type: 'create:deploying',
				ingredients: [{ item: 'simulated:incomplete_gyroscopic_mechanism' }, { item: 'create:cogwheel' }],
				results: [{ id: 'simulated:incomplete_gyroscopic_mechanism' }]
			},
			{
				type: 'create:deploying',
				ingredients: [{ item: 'simulated:incomplete_gyroscopic_mechanism' }, { item: 'kubejs:resonant_coil' }],
				results: [{ id: 'simulated:incomplete_gyroscopic_mechanism' }]
			}
		],
		transitional_item: { id: 'simulated:incomplete_gyroscopic_mechanism' }
	}).id('skyward:ch3/gyroscopic_mechanism')

	// --- Envelopes: deployer-only, reduced yield ---------------------------------
	// Grid recipes go; the deployer line (wool + stick) is the hull plant.
	const COLORS = ['white', 'orange', 'magenta', 'light_blue', 'yellow', 'lime',
		'pink', 'gray', 'light_gray', 'cyan', 'purple', 'blue',
		'brown', 'green', 'red', 'black']
	COLORS.forEach(color => {
		event.remove({ id: `aeronautics:${color}_envelope` })
		event.remove({ id: `aeronautics:deploying/deploying_envelope_${color}` })
		event.custom({
			type: 'create:deploying',
			ingredients: [{ item: `minecraft:${color}_wool` }, { item: 'minecraft:stick' }],
			results: [{ id: `aeronautics:${color}_envelope`, count: B.envelopePerDeploy }]
		}).id(`skyward:ch3/envelope_${color}`)
	})

	// --- Levitite blend: pricier brew --------------------------------------------
	event.remove({ id: 'aeronautics:mixing/levitite_blend' })
	let levititeIngredients = []
	for (let i = 0; i < B.levitite.endStonePowder; i++) levititeIngredients.push({ item: 'aeronautics:end_stone_powder' })
	for (let i = 0; i < B.levitite.zincNuggets; i++) levititeIngredients.push({ tag: 'c:nuggets/zinc' })
	levititeIngredients.push({ type: 'neoforge:tag', amount: B.levitite.waterMb, tag: 'c:water' })
	event.custom({
		type: 'create:mixing',
		heat_requirement: 'heated',
		ingredients: levititeIngredients,
		results: [{ amount: B.levitite.outputMb, id: 'aeronautics:levitite_blend' }]
	}).id('skyward:ch3/levitite_blend')

	// --- Propellers ----------------------------------------------------------------
	// Andesite propeller: built, not upgraded. Conversion shortcut removed.
	event.remove({ id: 'aeronautics:andesite_propeller' })
	event.remove({ id: 'aeronautics:andesite_propeller_from_andesite' })
	event.shaped(Item.of('aeronautics:andesite_propeller', 1), [
		'A A',
		' S ',
		'A A'
	], {
		A: 'create:andesite_alloy',
		S: 'kubejs:calibrated_shaft'
	}).id('skyward:ch3/andesite_propeller')

	// Smart propeller: same build, but one per craft (mod default was two).
	event.remove({ id: 'aeronautics:smart_propeller' })
	event.shaped(Item.of('aeronautics:smart_propeller', B.smartPropellerCount), [
		'P',
		'G',
		'B'
	], {
		P: 'create:propeller',
		G: 'simulated:gyroscopic_mechanism',
		B: 'create:brass_casing'
	}).id('skyward:ch3/smart_propeller')

	// --- Portable engine: tempered casing jacket ------------------------------------
	event.remove({ id: 'simulated:red_portable_engine' })
	event.shaped(Item.of('simulated:red_portable_engine', 1), [
		'G',
		'E',
		'B'
	], {
		G: 'kubejs:tempered_casing',
		E: 'simulated:engine_assembly',
		B: 'minecraft:blast_furnace'
	}).id('skyward:ch3/red_portable_engine')

	// --- Physics assembler: shipbuilding starts in the brass age ---------------------
	event.remove({ id: 'simulated:physics_assembler' })
	event.shaped(Item.of('simulated:physics_assembler', 1), [
		' N ',
		'ARA'
	], {
		N: 'create:precision_mechanism',
		R: 'create:brass_casing',
		A: 'create:andesite_alloy'
	}).id('skyward:ch3/physics_assembler')

	// --- Aeroworks: gyroscope, joystick, servos ---------------------------------------
	event.remove({ id: 'aeroworks:gyroscope' })
	let gyroscopeIngredients = ['create:flywheel', 'simulated:gimbal_sensor', 'create:brass_casing']
	for (let i = 0; i < B.gyroscope.gyroMechanisms; i++) gyroscopeIngredients.push('simulated:gyroscopic_mechanism')
	event.shapeless(Item.of('aeroworks:gyroscope', 1), gyroscopeIngredients)
		.id('skyward:ch3/gyroscope')

	event.remove({ id: 'aeroworks:joystick' })
	event.custom({
		type: 'create:mechanical_crafting',
		accept_mirrored: false,
		category: 'misc',
		key: {
			L: { item: 'create:redstone_link' },
			P: { item: 'create:precision_mechanism' },
			S: { item: 'kubejs:calibrated_shaft' },
			B: { tag: 'c:ingots/brass' }
		},
		pattern: [' L ', ' P ', ' S ', ' B ', 'BBB'],
		result: { count: 1, id: 'aeroworks:joystick' },
		show_notification: false
	}).id('skyward:ch3/joystick')

	event.remove({ id: 'aeroworks:mechanical_servo' })
	event.shaped(Item.of('aeroworks:mechanical_servo', 1), [
		' A ',
		'DBD',
		' C '
	], {
		A: 'create:precision_mechanism',
		B: 'create:sequenced_gearshift',
		C: 'kubejs:resonant_coil',
		D: '#c:ingots/brass'
	}).id('skyward:ch3/mechanical_servo')

	event.remove({ id: 'aeroworks:stepper_servo' })
	event.shaped(Item.of('aeroworks:stepper_servo', 1), [
		' A ',
		'BCB',
		' D '
	], {
		A: 'create:precision_mechanism',
		B: 'create:sequenced_gearshift',
		C: '#c:ingots/brass',
		D: 'kubejs:resonant_coil'
	}).id('skyward:ch3/stepper_servo')
})
