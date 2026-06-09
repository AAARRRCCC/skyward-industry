// =============================================================================
// SKYWARD INDUSTRY — ECONOMY CONSTANTS (canonical price source)
// Vendors are physical Numismatics blocks configured in-game; this file is the
// single source of truth the admin configures them FROM (see
// docs/ECONOMY_RUNBOOK.md and docs/OUTPOSTS.md). All prices in SPURS.
//
// Coin denominations (verify against in-game coin tooltips on first boot):
//   spur 1 | bevel 8 | sprocket 16 | cog 64 | crown 512 | sun 4096
//
// HARD RULE (review-enforced): nothing in ECON.sell may appear in any gated
// recipe in ch1-ch4, nor be trivially convertible into a gated input.
// Known traps, deliberately excluded from sell lists:
//   - wool, sticks            -> envelope deploying inputs
//   - blast furnace           -> portable engine input
//   - planks/logs             -> craft into sticks
//   - crimsite/asurine/veridium/ochrum -> crush into metal nuggets
//   - end stone               -> levitite input
// =============================================================================

global.ECON = {
	// --- Admin BUYS from players (the money faucet; one good per major line) ---
	buy: {
		'create:andesite_alloy': 1,        // Ch.1 mixer line
		'create:iron_sheet': 2,            // press line
		'create:brass_ingot': 4,           // brass line
		'create:cardboard': 1,             // pulp/saw line
		'create:electron_tube': 12,        // rose quartz line
		'kubejs:calibrated_shaft': 16,     // Ch.2 flagship
		'kubejs:resonant_coil': 30,        // Ch.2 electron-tube line
		'kubejs:tempered_casing': 30,      // Ch.2 fluid line
		'create:precision_mechanism': 96,  // Ch.2 capstone
		'simulated:engine_assembly': 400,  // Ch.3 capstone
	},

	// Outposts pay this multiple for their two specialty goods (geography pillar).
	premiumMultiplier: 1.5,

	// --- Admin SELLS to players (the money sink; progression-neutral ONLY) ----
	sell: {
		// decorative mineral palettes (none crushable into metals)
		'create:limestone': 2,
		'create:scoria': 2,
		'create:scorchia': 2,
		'minecraft:calcite': 2,
		'minecraft:smooth_basalt': 2,
		'minecraft:quartz_block': 8,
		'minecraft:purpur_block': 8,
		'minecraft:prismarine': 8,
		'minecraft:amethyst_block': 12,
		// schematic / cosmetic gear
		'create:empty_schematic': 16,
		'create:schematic_and_quill': 64,
		'minecraft:name_tag': 128,
		// music discs
		'minecraft:music_disc_cat': 256,
		'minecraft:music_disc_blocks': 256,
		'minecraft:music_disc_stal': 256,
		'aeronautics:music_disc_cloud_skipper': 512,
		// enchanted books (sold as pre-enchanted via vendor stock)
		'enchanted_book/unbreaking_3': 512,
		'enchanted_book/efficiency_5': 768,
		'enchanted_book/fortune_3': 1024,
		'enchanted_book/protection_4': 1024,
		'enchanted_book/feather_falling_4': 768,
		'enchanted_book/mending': 2048,
	},

	// STRETCH (flagged, not built): weekly rotating buy orders — pick 2 goods
	// each Monday, premium 2x at the capital vendor. Needs admin rotation only;
	// no code. Revisit after first balance pass.
}
