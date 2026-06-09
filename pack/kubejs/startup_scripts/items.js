// Custom item/block registration for Skyward Industry.
// All custom content registers under the kubejs: namespace (KubeJS requirement);
// design-doc names like "skyward:aetherium" are realized as kubejs:aetherium.

StartupEvents.registry('item', event => {
	// --- Ch.2 line-forcing intermediates -------------------------------------
	event.create('calibrated_shaft')
		.displayName('Calibrated Shaft')
		.texture('kubejs:item/calibrated_shaft')
		.tooltip('A shaft trued to aeronautic tolerances. Press and deployer work, not hand work.')

	event.create('tempered_casing')
		.displayName('Tempered Casing')
		.texture('kubejs:item/tempered_casing')
		.tooltip('Brass casing quenched in lava. The spout knows the recipe.')

	event.create('resonant_coil')
		.displayName('Resonant Coil')
		.texture('kubejs:item/resonant_coil')
		.tooltip('Hums faintly when brought near rotational force.')

	// Transitional items for the custom sequenced-assembly lines (the thing
	// sitting on the depot mid-process). Never obtainable as a final product.
	event.create('incomplete_calibrated_shaft')
		.displayName('Uncalibrated Shaft')
		.texture('kubejs:item/calibrated_shaft')
	event.create('incomplete_resonant_coil')
		.displayName('Unwound Coil')
		.texture('kubejs:item/resonant_coil')

	// --- Ch.4 exotic ----------------------------------------------------------
	event.create('aetherium')
		.displayName('Aetherium')
		.texture('kubejs:item/aetherium')
		.rarity('epic')
		.glow(true)
		.tag('skyward:aetherium')
		.tooltip('Found only beyond the long water. No furnace makes this.')

	// --- Crossing-site lore items (stocked by hand, see CROSSING_RUNBOOK) -----
	event.create('ships_log_1')
		.displayName("Ship's Log, Entry I")
		.texture('kubejs:item/ships_log_1')
		.rarity('uncommon')
		.maxStackSize(1)
		.tooltip("Day 4. Compass useless past the shelf. We steer by the static now — it pulls.")
	event.create('ships_log_2')
		.displayName("Ship's Log, Entry II")
		.texture('kubejs:item/ships_log_2')
		.rarity('uncommon')
		.maxStackSize(1)
		.tooltip('Day 9. Engine two ate its last coil. Dropping ballast. The island is real.')
	event.create('ships_log_3')
		.displayName("Ship's Log, Entry III")
		.texture('kubejs:item/ships_log_3')
		.rarity('uncommon')
		.maxStackSize(1)
		.tooltip('Day 11. The ore glows teal in the dark. It does not want to be smelted. We will not be telling the office.')
	event.create('ships_log_4')
		.displayName("Ship's Log, Final Entry")
		.texture('kubejs:item/ships_log_4')
		.rarity('rare')
		.maxStackSize(1)
		.tooltip('If you found this, the ship held. Take the teal stone. Leave the rest for the next crew.')
})

StartupEvents.registry('block', event => {
	event.create('aetherium_block')
		.displayName('Block of Aetherium')
		.soundType('amethyst')
		.hardness(3)
		.resistance(9)
		.requiresTool(true)
		.tagBlock('minecraft:mineable/pickaxe')
		.tagBlock('minecraft:needs_iron_tool')
})
