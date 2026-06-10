// =============================================================================
// SKYWARD INDUSTRY — PROGRESSION BALANCE CONSTANTS
// Every gating quantity in the pack lives here. Playtest tuning = edit this
// file only. See docs/PROGRESSION.md for the intent behind each number.
//
// STARTUP script on purpose: KubeJS 2101 only allows assigning `global` here
// (server scripts read it). Edits need a full game/server restart, not /reload.
// =============================================================================

global.BAL = {
	ch1: {
		// Mixer path (the "real" recipe): cheap per-unit, needs a running mixer.
		alloyMix: { andesite: 2, ironNuggets: 1, output: 2 },
		// Hand path: possible, punishing. ~4x worse per andesite than the mixer.
		alloyGrid: { andesite: 2, ironNuggets: 2, output: 1 },
	},

	ch2: {
		// Sequenced assembly: each loop presses then deploys one andesite alloy.
		// Cost per shaft = 1 create:shaft + loops x 1 alloy.
		calibratedShaft: { loops: 3 },
		// Spout-filled brass casing. mb of lava per casing.
		temperedCasing: { lavaMb: 250 },
		// Each loop deploys 1 electron tube onto a golden sheet core.
		resonantCoil: { loops: 2 },
		// Precision mechanism rebuilt on calibrated shafts.
		// Cost per attempt = 1 calibrated shaft + loops x (cogwheel + large cogwheel + iron nugget).
		precisionMechanism: {
			loops: 3,
			primaryWeight: 80,  // % chance-weight of getting the mechanism vs scrap
			scrapWeight: 20,
		},
	},

	ch3: {
		// Engine assembly: tempered casing core; each loop cuts, presses, then
		// deploys 1 resonant coil + 1 calibrated shaft.
		// 2026-06-09: 4 -> 3 after first creative pass (first ship looked too
		// steep). Next lever if still steep: resonantCoil.loops 2 -> 1.
		engineAssembly: { loops: 3 },
		// Gyroscopic mechanism: precision mechanism core; each loop deploys
		// 1 cogwheel + 1 resonant coil.
		gyroMechanism: { loops: 4 },
		// Deployer wraps wool around sticks. Output per operation (mod default 3).
		envelopePerDeploy: 2,
		// Levitite blend mixing (mod default: 4 powder + 2 zinc nuggets -> 500mb).
		levitite: { endStonePowder: 6, zincNuggets: 4, waterMb: 500, outputMb: 250 },
		// Propellers re-tiered 2026-06-09: wooden (shaft ringed by 4 slabs, cheap,
		// drag penalty) and andesite (create:propeller core, mod-original price)
		// are EARLY game; the propeller bearing eats a calibrated shaft
		// (pattern-encoded in ch3_aeronautics.js). Wooden's drag penalty is
		// EXPERIMENTAL, tuned in kubejs/data/skyward/physics_block_properties/
		// wooden_propeller_drag.json. Measured: scale 2.0 = 0.25pN drag vs
		// 249.45pN prop thrust (negligible) -> now 300.0, targeting ~15% of one
		// prop's thrust assuming linear scaling. Delete the file to remove.
		// Smart propeller output count (mod default 2).
		smartPropellerCount: 1,
		// Aeroworks gyroscope: gyroscopic mechanisms per unit.
		gyroscope: { gyroMechanisms: 2 },
	},

	ch4: {
		// The Crossing tier. Aetherium is loot-only (see datapacks/skyward).
		// NOTE: these counts document the mechanical-crafting patterns in
		// ch4_crossing.js; changing one means editing the pattern there.
		creativeMotor: { aetherium: 12, engineAssemblies: 4, gyroMechanisms: 4, sturdySheets: 4, precisionMechanisms: 1 },
		creativeCrate: { aetherium: 4, brassCasings: 4, itemVaults: 1 },
		creativeFluidTank: { aetherium: 4, copperCasings: 4, fluidTanks: 1 },
	},
}
