# Advancement inventory (quest gating hooks)

`(R)` = recipe-unlock advancement, ignore. Trigger `impossible` = 
granted only by mod code (best kind of gate: fires on real behavior).

## create (create-1.21.1-6.0.10): 102 advancements

- `create:andesite_alloy` — **Sturdier Rocks** — _Obtain some Andesite Alloy, Create's most important resource_  (parent: `create:root`; triggers: ['minecraft:inventory_changed'])
- `create:andesite_casing` — **The Andesite Age** — _Apply Andesite Alloy to stripped wood, creating a basic casing for your machines_  (parent: `create:andesite_alloy`; triggers: ['create:andesite_casing_builtin'])
- `create:anvil_plough` — **Blacksmith Artillery** — _Launch an Anvil with Mechanical Ploughs_  (parent: `create:cart_pickup`; triggers: ['create:anvil_plough_builtin'])
- `create:arm_blaze_burner` — **Combust-o-Tron** — _Instruct a Mechanical Arm to feed your Blaze Burner_  (parent: `create:linked_controller`; triggers: ['create:arm_blaze_burner_builtin'])
- `create:arm_many_targets` — **Organize-o-Tron** — _Program a Mechanical Arm with 10 or more output locations_  (parent: `create:crusher_maxed_0000`; triggers: ['create:arm_many_targets_builtin'])
- `create:backtank` — **Pressure to Go** — _Create a Copper Backtank and make it accumulate air pressure_  (parent: `create:steam_whistle`; triggers: ['create:backtank_builtin'])
- `create:belt` — **Kelp Drive** — _Connect two Shafts with a Mechanical Belt_  (parent: `create:compacting`; triggers: ['create:belt_builtin'])
- `create:belt_funnel_kiss` — **The Parrots and the Flaps** — _Make two Belt-mounted Funnels kiss
§7(Hidden Advancement)_  (parent: `create:mechanical_mixer`; triggers: ['create:belt_funnel_kiss_builtin'])
- `create:brass` — **Real Alloys** — _Create Brass Ingots by alloying Copper and Zinc Ingots in your Blaze-heated Mechanical Mixer_  (parent: `create:diving_suit`; triggers: ['minecraft:inventory_changed'])
- `create:brass_casing` — **The Brass Age** — _Apply Brass Ingots to stripped wood, creating a casing for more sophisticated machines_  (parent: `create:brass`; triggers: ['create:brass_casing_builtin'])
- `create:burner` — **Sentient Fireplace** — _Obtain a Blaze Burner_  (parent: `create:mechanical_mixer`; triggers: ['minecraft:inventory_changed'])
- `create:cardboard` — **Part and Parcel** — _Produce or obtain your first Cardboard_  (parent: `create:mechanical_mixer`; triggers: ['minecraft:inventory_changed'])
- `create:cardboard_armor` — **Full Stealth** — _Sneak around in full Cardboard Armor_  (parent: `create:factory_gauge`; triggers: ['create:cardboard_armor_builtin'])
- `create:cardboard_armor_trim` — **Arts and Crafts** — _Decorate your cardboard equipment with armor trims
§7(Hidden Advancement)_  (parent: `create:cardboard_armor`; triggers: ['create:cardboard_armor_trim_builtin'])
- `create:cart_pickup` — **Strong Arms** — _Pick up a Minecart Contraption with at least 200 attached blocks_  (parent: `create:pulley_maxed`; triggers: ['create:cart_pickup_builtin'])
- `create:chained_drain` — **On a Roll** — _Watch an item move across a row of Item Drains
§7(Hidden Advancement)_  (parent: `create:backtank`; triggers: ['create:chained_drain_builtin'])
- `create:chocolate_bucket` — **A World of Imagination** — _Obtain a bucket of molten chocolate_  (parent: `create:hose_pulley`; triggers: ['minecraft:inventory_changed'])
- `create:chute` — **Vertical Logistics** — _Transport some items by Chute_  (parent: `create:funnel`; triggers: ['create:chute_builtin'])
- `create:clockwork_bearing` — **Contraption o'Clock** — _Assemble a structure mounted on a Clockwork Bearing_  (parent: `create:haunted_bell`; triggers: ['create:clockwork_bearing_builtin'])
- `create:compacting` — **Compactification** — _Use a Mechanical Press and a Basin to create fewer items from more_  (parent: `create:saw_processing`; triggers: ['create:compacting_builtin'])
- `create:conductor` — **Conductor Instructor** — _Instruct a Train driver with a Train Schedule_  (parent: `create:train`; triggers: ['create:conductor_builtin'])
- `create:contraption_actors` — **Moving with Purpose** — _Create a Contraption with drills, saws, or harvesters on board_  (parent: `create:super_glue`; triggers: ['create:contraption_actors_builtin'])
- `create:copper` — **Cuprum Bokum** — _Amass some Copper Ingots for your exploits in fluid manipulation_  (parent: `create:burner`; triggers: ['minecraft:inventory_changed'])
- `create:copper_casing` — **The Copper Age** — _Apply Copper Ingots to stripped wood, creating a waterproof casing for your machines_  (parent: `create:copper`; triggers: ['create:copper_casing_builtin'])
- `create:crafter_lazy_000` — **Desperate Measures** — _Drastically slow down a Mechanical Crafter to procrastinate on proper infrastructure
§7(Hidden Advancement)_  (parent: `create:mechanical_crafter`; triggers: ['create:crafter_lazy_000_builtin'])
- `create:cross_streams` — **Don't Cross the Streams!** — _Watch two fluids meet in your pipe network
§7(Hidden Advancement)_  (parent: `create:backtank`; triggers: ['create:cross_streams_builtin'])
- `create:crusher_maxed_0000` — **Crushing It** — _Operate a pair of Crushing Wheels at maximum speed_  (parent: `create:brass`; triggers: ['create:crusher_maxed_0000_builtin'])
- `create:crushing_wheel` — **Wheels of Destruction** — _Place and power a set of Crushing Wheels_  (parent: `create:mechanical_crafter`; triggers: ['create:crushing_wheel_builtin'])
- `create:cuckoo_clock` — **Is it Time?** — _Witness your Cuckoo Clock announce bedtime_  (parent: `create:stressometer`; triggers: ['create:cuckoo_clock_builtin'])
- `create:deployer` — **Artificial Intelligence** — _Place and power a Deployer, the perfect reflection of yourself_  (parent: `create:rose_quartz`; triggers: ['create:deployer_builtin'])
- `create:display_board_0` — **Dynamic Timetables** — _Forecast a Train's arrival on your Display Board with the help of Display Links_  (parent: `create:track_signal`; triggers: ['create:display_board_0_builtin'])
- `create:display_link` — **Big Data** — _Use a Display Link to visualise information_  (parent: `create:clockwork_bearing`; triggers: ['create:display_link_builtin'])
- `create:diving_suit` — **Ready for the Depths** — _Equip a Diving Helmet and a Copper Backtank, then jump into water_  (parent: `create:backtank`; triggers: ['create:diving_suit_builtin'])
- `create:diving_suit_lava` — **Swimming with the Striders** — _Attempt to take a dive in lava with your netherite diving gear_  (parent: `create:foods`; triggers: ['create:diving_suit_lava_builtin'])
- `create:drain` — **Tumble Draining** — _Watch a fluid-containing item be emptied by an Item Drain_  (parent: `create:spout`; triggers: ['create:drain_builtin'])
- `create:ejector_maxed` — **Springboard Champion** — _Get launched more than 30 blocks by a Weighted Ejector_  (parent: `create:windmill_maxed`; triggers: ['create:ejector_maxed_builtin'])
- `create:encased_fan` — **Wind Maker** — _Place and power an Encased Fan_  (parent: `create:mechanical_press`; triggers: ['create:encased_fan_builtin'])
- `create:extendo_grip` — **Boioioing!** — _Get hold of an Extendo Grip_  (parent: `create:potato_cannon`; triggers: ['create:extendo_grip_builtin'])
- `create:extendo_grip_dual` — **To Full Extent** — _Dual-wield Extendo Grips for superhuman reach
§7(Hidden Advancement)_  (parent: `create:mechanical_crafter`; triggers: ['create:extendo_grip_dual_builtin'])
- `create:factory_gauge` — **High Logistics** — _Trigger an automatic package request using Factory Gauges_  (parent: `create:table_cloth_shop`; triggers: ['create:factory_gauge_builtin'])
- `create:fan_processing` — **Processing by Particle** — _Use an Encased Fan to process materials_  (parent: `create:encased_fan`; triggers: ['create:fan_processing_builtin'])
- `create:fist_bump` — **Pound It, Bro!** — _Make two Deployers fist-bump
§7(Hidden Advancement)_  (parent: `create:mechanical_crafter`; triggers: ['create:fist_bump_builtin'])
- `create:foods` — **Balanced Diet** — _Create Chocolate Glazed Berries, a Honeyed Apple, and a Sweet Roll all from the same Spout_  (parent: `create:steam_engine_maxed`; triggers: ['create:foods_builtin'])
- `create:frogport` — **Hungry hoppers** — _Catch packages from your Chain Conveyor using a Frogport_  (parent: `create:stock_ticker`; triggers: ['create:frogport_builtin'])
- `create:funnel` — **Airport Aesthetic** — _Extract or insert items into a container using a Funnel_  (parent: `create:belt`; triggers: ['create:funnel_builtin'])
- `create:glass_pipe` — **Flow Discovery** — _Use your Wrench on a pipe that contains a fluid_  (parent: `create:mechanical_pump_0`; triggers: ['create:glass_pipe_builtin'])
- `create:hand_crank_000` — **Workout Session** — _Use a Hand Crank until fully exhausted
§7(Hidden Advancement)_  (parent: `create:mechanical_mixer`; triggers: ['create:hand_crank_000_builtin'])
- `create:haunted_bell` — **Shadow Sense** — _Toll a Haunted Bell_  (parent: `create:brass`; triggers: ['create:haunted_bell_builtin'])
- `create:honey_drain` — **Autonomous Bee-Keeping** — _Use pipes to pull honey from a Bee Nest or Beehive_  (parent: `create:chocolate_bucket`; triggers: ['create:honey_drain_builtin'])
- `create:hose_pulley` — **Industrial Spillage** — _Lower a Hose Pulley and watch it drain or fill a body of fluid_  (parent: `create:water_supply`; triggers: ['create:hose_pulley_builtin'])
- `create:hose_pulley_lava` — **Tapping the Mantle** — _Pump from a body of lava large enough to be considered infinite_  (parent: `create:copper`; triggers: ['create:hose_pulley_lava_builtin'])
- `create:lava_wheel_00000` — **Magma Wheel** — _This shouldn't have worked
§7(Hidden Advancement)_  (parent: `create:mechanical_mixer`; triggers: ['create:lava_wheel_00000_builtin'])
- `create:linked_controller` — **Remote Activation** — _Activate a Redstone Link using a Linked Controller_  (parent: `create:extendo_grip`; triggers: ['create:linked_controller_builtin'])
- `create:long_train` — **Ambitious Endeavours** — _Create a Train with at least 6 carriages_  (parent: `create:track_crafting_factory`; triggers: ['create:long_train_builtin'])
- `create:long_travel` — **Field Trip** — _Leave a Train Seat over 5000 blocks away from where you started travelling_  (parent: `create:long_train`; triggers: ['create:long_travel_builtin'])
- `create:mechanical_arm` — **Busy Hands** — _Watch your Mechanical Arm transport its first item_  (parent: `create:speed_controller`; triggers: ['create:mechanical_arm_builtin'])
- `create:mechanical_crafter` — **Automated Assembly** — _Place and power some Mechanical Crafters_  (parent: `create:mechanical_arm`; triggers: ['create:mechanical_crafter_builtin'])
- `create:mechanical_mixer` — **Mixing It Up** — _Combine ingredients in a Mechanical Mixer_  (parent: `create:chute`; triggers: ['create:mechanical_mixer_builtin'])
- `create:mechanical_press` — **Bonk!** — _Create some sheets in a Mechanical Press_  (parent: `create:andesite_casing`; triggers: ['create:mechanical_press_builtin'])
- `create:mechanical_pump_0` — **Under Pressure** — _Place and power a Mechanical Pump_  (parent: `create:copper`; triggers: ['create:mechanical_pump_0_builtin'])
- `create:millstone` — **Embrace the Grind** — _Use a Millstone to pulverise materials_  (parent: `create:shifting_gears`; triggers: ['create:millstone_builtin'])
- `create:musical_arm` — **DJ Mechanico** — _Watch a Mechanical Arm operate your Jukebox
§7(Hidden Advancement)_  (parent: `create:mechanical_crafter`; triggers: ['create:musical_arm_builtin'])
- `create:package_chute_throw` — **Nothing but net** — _Land your cardboard package throw in an item chute
§7(Hidden Advancement)_  (parent: `create:cardboard_armor`; triggers: ['create:package_chute_throw_builtin'])
- `create:packager` — **Post Production** — _Package items from an inventory using the Packager_  (parent: `create:cardboard`; triggers: ['create:packager_builtin'])
- `create:pipe_organ` — **The Pipe Organ** — _Attach 12 uniquely pitched Steam Whistles to a single Fluid Tank
§7(Hidden Advancement)_  (parent: `create:backtank`; triggers: ['create:pipe_organ_builtin'])
- `create:portable_storage_interface` — **Drive-by Exchange** — _Use a Portable Storage Interface to take or insert items into a Contraption_  (parent: `create:contraption_actors`; triggers: ['create:portable_storage_interface_builtin'])
- `create:potato_cannon` — **Fwoomp!** — _Defeat an enemy with your Potato Cannon_  (parent: `create:display_link`; triggers: ['create:potato_cannon_builtin'])
- `create:potato_cannon_collide` — **Veggie Fireworks** — _Cause Potato Cannon projectiles of different types to collide with each other_  (parent: `create:arm_many_targets`; triggers: ['create:potato_cannon_collide_builtin'])
- `create:precision_mechanism` — **Complex Curiosities** — _Assemble a Precision Mechanism_  (parent: `create:deployer`; triggers: ['minecraft:inventory_changed'])
- `create:pulley_maxed` — **Rope to Nowhere** — _Extend a Rope Pulley over 200 blocks deep_  (parent: `create:ejector_maxed`; triggers: ['create:pulley_maxed_builtin'])
- `create:red_signal` — **Expert Driver** — _Run a red Train Signal
§7(Hidden Advancement)_  (parent: `create:track_signal`; triggers: ['create:red_signal_builtin'])
- `create:root` — **Welcome to Create** — _Here Be Contraptions_  (parent: ``; triggers: ['minecraft:inventory_changed'])
- `create:rose_quartz` — **Supercharged** — _Polish some Rose Quartz_  (parent: `create:brass_casing`; triggers: ['minecraft:inventory_changed'])
- `create:saw_processing` — **Workshop's Most Feared** — _Use an upright Mechanical Saw to process materials_  (parent: `create:fan_processing`; triggers: ['create:saw_processing_builtin'])
- `create:self_deploying` — **Self-Driving Cart** — _Create a Minecart Contraption that places tracks in front of itself_  (parent: `create:potato_cannon_collide`; triggers: ['create:self_deploying_builtin'])
- `create:shifting_gears` — **Shifting Gears** — _Connect a Large Cogwheel to a Small Cogwheel, allowing you to change the speed of your Contraption_  (parent: `create:windmill`; triggers: ['create:shifting_gears_builtin'])
- `create:speed_controller` — **Engineers hate this simple trick!** — _Fine-tune your Contraption with a Rotation Speed Controller_  (parent: `create:precision_mechanism`; triggers: ['create:speed_controller_builtin'])
- `create:spout` — **Sploosh** — _Watch a fluid-containing item be filled by a Spout_  (parent: `create:copper_casing`; triggers: ['create:spout_builtin'])
- `create:steam_engine` — **The Powerhouse** — _Use a Steam Engine to generate torque_  (parent: `create:drain`; triggers: ['create:steam_engine_builtin'])
- `create:steam_engine_maxed` — **Full Steam** — _Run a boiler at the maximum level of power_  (parent: `create:hose_pulley_lava`; triggers: ['create:steam_engine_maxed_builtin'])
- `create:steam_whistle` — **Voice of an Angel** — _Activate a Steam Whistle_  (parent: `create:steam_engine`; triggers: ['create:steam_whistle_builtin'])
- `create:stock_ticker` — **Order Up!** — _Employ a mob at your stock ticker and make your first requests_  (parent: `create:packager`; triggers: ['create:stock_ticker_builtin'])
- `create:stressometer` — **Stress for Nerds** — _Get an exact readout with the help of Engineer's Goggles and a Stressometer_  (parent: `create:wrench_goggles`; triggers: ['create:stressometer_builtin'])
- `create:stressometer_maxed` — **Perfectly Stressed** — _Get a 100% readout from a Stressometer
§7(Hidden Advancement)_  (parent: `create:mechanical_mixer`; triggers: ['create:stressometer_maxed_builtin'])
- `create:sturdy_sheet` — **The Sturdiest Rocks** — _Assemble a Sturdy Sheet by refining Powdered Obsidian_  (parent: `create:crushing_wheel`; triggers: ['minecraft:inventory_changed'])
- `create:super_glue` — **Area of Connect** — _Super Glue some blocks into a group_  (parent: `create:millstone`; triggers: ['create:super_glue_builtin'])
- `create:table_cloth_shop` — **Open for business** — _Put items up for sale using a Table Cloth_  (parent: `create:frogport`; triggers: ['create:table_cloth_shop_builtin'])
- `create:track_0` — **A New Gauge** — _Obtain some Train Tracks_  (parent: `create:sturdy_sheet`; triggers: ['minecraft:inventory_changed'])
- `create:track_crafting_factory` — **Track Factory** — _Produce more than 1000 Train Tracks with the same Mechanical Press_  (parent: `create:sturdy_sheet`; triggers: ['create:track_crafting_factory_builtin'])
- `create:track_signal` — **Traffic Control** — _Place a Train Signal_  (parent: `create:conductor`; triggers: ['create:track_signal_builtin'])
- `create:train` — **All Aboard!** — _Assemble your first Train_  (parent: `create:train_casing_00`; triggers: ['create:train_builtin'])
- `create:train_casing_00` — **The Locomotive Age** — _Use Sturdy Sheets to create a casing for railway components_  (parent: `create:sturdy_sheet`; triggers: ['create:train_casing_00_builtin'])
- `create:train_crash` — **Terrible Service** — _Witness a Train crash as a passenger
§7(Hidden Advancement)_  (parent: `create:track_signal`; triggers: ['create:train_crash_builtin'])
- `create:train_crash_backwards` — **Blind Spot** — _Crash into another Train while driving backwards
§7(Hidden Advancement)_  (parent: `create:track_signal`; triggers: ['create:train_crash_backwards_builtin'])
- `create:train_portal` — **Dimensional Commuter** — _Ride a Train through a portal_  (parent: `create:train_whistle`; triggers: ['create:train_portal_builtin'])
- `create:train_roadkill` — **Road Kill** — _Run over an enemy with your Train
§7(Hidden Advancement)_  (parent: `create:track_signal`; triggers: ['create:train_roadkill_builtin'])
- `create:train_whistle` — **Choo Choo!** — _Assemble a Steam Whistle to your Train and activate it while driving_  (parent: `create:track_0`; triggers: ['create:train_whistle_builtin'])
- `create:water_supply` — **Puddle Collector** — _Use the pulling end of a Fluid Pipe or Mechanical Pump to collect water_  (parent: `create:glass_pipe`; triggers: ['create:water_supply_builtin'])
- `create:water_wheel` — **Harnessed Hydraulics** — _Place a Water Wheel and use it to generate torque_  (parent: `create:andesite_alloy`; triggers: ['create:water_wheel_builtin'])
- `create:windmill` — **A mild Breeze** — _Assemble a windmill and use it to generate torque_  (parent: `create:water_wheel`; triggers: ['create:windmill_builtin'])
- `create:windmill_maxed` — **A strong Breeze** — _Assemble a windmill of maximum strength_  (parent: `create:andesite_alloy`; triggers: ['create:windmill_maxed_builtin'])
- `create:wrench_goggles` — **Kitted Out** — _Equip Engineer's Goggles and a Wrench_  (parent: `create:portable_storage_interface`; triggers: ['minecraft:inventory_changed'])

## create-aeronautics (1): 10 advancements

- `aeronautics:for_every_action` — **For Every Action...** — _Place and power a Propeller to generate Thrust_  (parent: `aeronautics:head_in_the_clouds`; triggers: ['aeronautics:for_every_action_builtin'])
- `aeronautics:ghostbuster` — **Ghostbuster** — _Kill a Phantom using a Mounted Potato Cannon_  (parent: `aeronautics:heavier_artillery`; triggers: ['aeronautics:ghostbuster_builtin'])
- `aeronautics:head_in_the_clouds` — **Head in the Clouds** — _Fill an airtight Envelope structure with hot air_  (parent: `aeronautics:root`; triggers: ['aeronautics:head_in_the_clouds_builtin'])
- `aeronautics:heavier_artillery` — **Heavier Artillery** — _Fire a vegetable from a Mounted Potato Cannon_  (parent: `aeronautics:root`; triggers: ['aeronautics:heavier_artillery_builtin'])
- `aeronautics:high_fashion` — **High Fashion** — _Obtain a pair of Aviator's Goggles_  (parent: `aeronautics:root`; triggers: ['minecraft:inventory_changed'])
- `aeronautics:in_thrust_we_trust` — **In Thrust We Trust** — _Assemble a Propeller Bearing to generate more Thrust_  (parent: `aeronautics:for_every_action`; triggers: ['aeronautics:in_thrust_we_trust_builtin'])
- `aeronautics:now_available_in_pink` — **Now Available in Pink!** — _Crystallize Levitite Blend into Pearlescent Levitite
§7(Hidden Advancement)_  (parent: `aeronautics:unidentified_floating_object`; triggers: ['aeronautics:now_available_in_pink_builtin'])
- `aeronautics:root` — **Create Aeronautics** — _Up Up and Away_  (parent: ``; triggers: ['minecraft:inventory_changed'])
- `aeronautics:song_of_the_sky` — **Song of the Sky** — _Toss a music disc into the clouds to create something new_  (parent: `aeronautics:head_in_the_clouds`; triggers: ['minecraft:inventory_changed'])
- `aeronautics:unidentified_floating_object` — **Unidentified Floating Object** — _Crystallize Levitite Blend into Levitite_  (parent: `aeronautics:head_in_the_clouds`; triggers: ['aeronautics:unidentified_floating_object_builtin'])

## create-aeronautics (1): 30 advancements

- `simulated:a_calculated_connection` — **A Calculated Connection** — _Successfully align and connect two Docking Connectors_  (parent: `simulated:opposite_attract`; triggers: ['simulated:a_calculated_connection_builtin'])
- `simulated:applied_kinematics` — **Applied Kinematics** — _Obtain a Physics Assembler, the heart of every Simulated Contraption_  (parent: `simulated:root`; triggers: ['minecraft:inventory_changed'])
- `simulated:big_beam` — **Big Beam** — _Power a Laser Pointer. Please do not stare directly into the Laser Pointer_  (parent: `simulated:no_pressure`; triggers: ['simulated:big_beam_builtin'])
- `simulated:call_of_the_void` — **Call of the Void** — _Visit a glimmering sea at the end of the world
§7(Hidden Advancement)_  (parent: `simulated:applied_kinematics`; triggers: ['simulated:call_of_the_void_builtin'])
- `simulated:can_we_get_much_higher` — **Can We Get Much Higher?** — _Observe an Altitude Sensor at 0% atmospheric pressure
§7(Hidden Advancement)_  (parent: `simulated:no_pressure`; triggers: ['simulated:can_we_get_much_higher_builtin'])
- `simulated:convoluted_circumvolutions` — **Convoluted Circumvolutions** — _Obtain a Gyroscopic Mechanism_  (parent: `simulated:no_pressure`; triggers: ['minecraft:inventory_changed'])
- `simulated:far_from_home` — **Far From Home** — _Set a Navigation Table's target to a location over 5000 blocks away
§7(Hidden Advancement)_  (parent: `simulated:thataway`; triggers: ['simulated:far_from_home_builtin'])
- `simulated:get_a_grip` — **Get a Grip!** — _Grab on to a Handle_  (parent: `simulated:applied_kinematics`; triggers: ['simulated:get_a_grip_builtin'])
- `simulated:got_a_grip` — **Got a Grip!** — _Break a very long fall by grabbing on to a Handle
§7(Hidden Advancement)_  (parent: `simulated:get_a_grip`; triggers: ['simulated:got_a_grip_builtin'])
- `simulated:i_declare_thee` — **I Declare Thee...** — _Name a Simulated Contraption using a Nameplate_  (parent: `simulated:not_gonna_sugarcoat_it`; triggers: ['simulated:i_declare_thee_builtin'])
- `simulated:i_paid_for_the_whole_typewriter` — **I Paid for the Whole Typewriter** — _Bind 26 or more keys to frequencies on the Linked Typewriter
§7(Hidden Advancement)_  (parent: `simulated:get_a_grip`; triggers: ['simulated:i_paid_for_the_whole_typewriter_builtin'])
- `simulated:learning_the_ropes` — **Learning the Ropes** — _Connect a Rope Connector or Rope Spool with Rope_  (parent: `simulated:applied_kinematics`; triggers: ['simulated:learning_the_ropes_builtin'])
- `simulated:measure_once_build_twice` — **Measure Once, Build Twice** — _Inspect a Contraption Diagram_  (parent: `simulated:not_gonna_sugarcoat_it`; triggers: ['simulated:measure_once_build_twice_builtin'])
- `simulated:must_come_up` — **...Must Come Up** — _Watch a Spring item bounce a great distance
§7(Hidden Advancement)_  (parent: `simulated:what_goes_down`; triggers: ['simulated:must_come_up_builtin'])
- `simulated:my_eye` — **My Eye!** — _Shine a laser into a Laser Sensor and activate it_  (parent: `simulated:big_beam`; triggers: ['simulated:my_eye_builtin'])
- `simulated:nearsighted` — **Nearsighted** — _Obtain and place an Optical Sensor to show you what's right there_  (parent: `simulated:big_beam`; triggers: ['minecraft:placed_block'])
- `simulated:no_pressure` — **No Pressure** — _Obtain and place an Altitude Sensor_  (parent: `simulated:applied_kinematics`; triggers: ['minecraft:placed_block'])
- `simulated:not_gonna_sugarcoat_it` — **Not Gonna Sugarcoat It** — _Use Honey Glue to connect a group of blocks for assembly_  (parent: `simulated:applied_kinematics`; triggers: ['simulated:not_gonna_sugarcoat_it_builtin'])
- `simulated:opposite_attract` — **Opposites Attract** — _Place and power a Redstone Magnet_  (parent: `simulated:applied_kinematics`; triggers: ['simulated:opposite_attract_builtin'])
- `simulated:rewind_time` — **Rewind Time** — _Watch a Torsion Spring unwind to its original position_  (parent: `simulated:what_goes_down`; triggers: ['simulated:rewind_time_builtin'])
- `simulated:root` — **Create Simulated** — _Physics Be Upon Ye_  (parent: ``; triggers: ['minecraft:inventory_changed'])
- `simulated:speed_is_key` — **Speed is Key** — _Obtain and place a Velocity Sensor to satiate your need for speed_  (parent: `simulated:no_pressure`; triggers: ['minecraft:placed_block'])
- `simulated:steamless_engine` — **Steamless Engine** — _Place and power a Portable Engine_  (parent: `simulated:unpowered_steering`; triggers: ['simulated:steamless_engine_builtin'])
- `simulated:stuck_together` — **Stuck Together** — _Craft a Plunger Launcher_  (parent: `simulated:learning_the_ropes`; triggers: ['minecraft:inventory_changed'])
- `simulated:that_should_do_for_now` — **That Should Do For Now** — _Place over 10 hours of fuel into a Portable Engine
§7(Hidden Advancement)_  (parent: `simulated:steamless_engine`; triggers: ['simulated:that_should_do_for_now_builtin'])
- `simulated:thataway` — **Thataway!** — _Obtain and place a Navigation Table to point you in the right direction_  (parent: `simulated:no_pressure`; triggers: ['minecraft:placed_block'])
- `simulated:the_definition_of_up` — **The Definition of "Up"** — _Obtain and place a Gimbal Sensor to help you keep balance_  (parent: `simulated:convoluted_circumvolutions`; triggers: ['minecraft:placed_block'])
- `simulated:unpowered_steering` — **Unpowered Steering** — _Grab and spin a Steering Wheel_  (parent: `simulated:get_a_grip`; triggers: ['simulated:unpowered_steering_builtin'])
- `simulated:what_goes_down` — **What Goes Down...** — _Boing! Obtain a Spring item_  (parent: `simulated:get_a_grip`; triggers: ['minecraft:inventory_changed'])
- `simulated:you_spin_me_right_round` — **You Spin Me Right Round** — _Assemble a Simulated Contraption using a Swivel Bearing_  (parent: `simulated:applied_kinematics`; triggers: ['simulated:you_spin_me_right_round_builtin'])

## numismatics (CreateNumismatics-1.0.20+neoforge-mc1.21.1): 4 advancements

- `numismatics:is_this_legal` — **Is This Legal?** — _Buy coins for less than they are worth
§7(Hidden Advancement)_  (parent: `numismatics:money_laundering`; triggers: ['numismatics:is_this_legal_builtin'])
- `numismatics:money_laundering` — **Money Laundering** — _Buy coins in a vendor
§7(Hidden Advancement)_  (parent: `numismatics:root`; triggers: ['numismatics:money_laundering_builtin'])
- `numismatics:questionable_investment` — **Questionable Investment** — _Buy coins for more than they are worth
§7(Hidden Advancement)_  (parent: `numismatics:money_laundering`; triggers: ['numismatics:questionable_investment_builtin'])
- `numismatics:root` — **Welcome to Numismatics** — _Here Be Riches_  (parent: ``; triggers: ['minecraft:inventory_changed'])

## create-connected (create_connected-1.2.2-mc1.21.1): 9 advancements

- `create_connected:brass_gearbox` — **Serious Organization** — _Place down a Brass Gearbox_  (parent: `create_connected:root`; triggers: ['minecraft:placed_block'])
- `create_connected:control_chip` — **Precise Fabrication** — _Assemble a Control Chip_  (parent: `create_connected:root`; triggers: ['minecraft:inventory_changed'])
- `create_connected:kinetic_battery` — **Fully Charged** — _Charge a Kinetic Battery to full_  (parent: `create_connected:root`; triggers: ['create_connected:kinetic_battery_builtin'])
- `create_connected:overpowered_brake_0` — **Overpowered** — _Keep a network running at speed with a powered brake attached
§7(Hidden Advancement)_  (parent: `create_connected:root`; triggers: ['create_connected:overpowered_brake_0_builtin'])
- `create_connected:overstress_clutch` — **Circuit Breaker** — _Trigger an Overstress Clutch_  (parent: `create_connected:shear_pin`; triggers: ['create_connected:overstress_clutch_builtin'])
- `create_connected:pulse_generator_infinite_loop` — **Infinite Loop** — _Overload a Sequenced Pulse Generator with a buggy program
§7(Hidden Advancement)_  (parent: `create_connected:sequenced_pulse_generator`; triggers: ['create_connected:pulse_generator_infinite_loop_builtin'])
- `create_connected:root` — **Welcome to Create: Connected** — _Gadgets for all situations_  (parent: ``; triggers: ['minecraft:inventory_changed'])
- `create_connected:sequenced_pulse_generator` — **Computational Supremacy** — _Place down a Sequenced Pulse Generator_  (parent: `create_connected:control_chip`; triggers: ['minecraft:placed_block'])
- `create_connected:shear_pin` — **Snap!** — _Blow a Shear Pin_  (parent: `create_connected:root`; triggers: ['create_connected:shear_pin_builtin'])

## farmers-delight (FarmersDelight-1.21.1-1.3.2): 21 advancements

- `farmersdelight:main/craft_knife` — **Hunt and Gather** — _Craft a Knife to scavenge extra goods from plants and animals_  (parent: `farmersdelight:main/root`; triggers: ['minecraft:inventory_changed'])
- `farmersdelight:main/eat_nourishing_food` — **Nourishing!** — _A balanced and diverse meal will keep you fed and healthy for a long time!_  (parent: `farmersdelight:main/place_cooking_pot`; triggers: ['minecraft:effects_changed'])
- `farmersdelight:main/get_fd_seed` — **Crops of the Wild** — _Four new crops may be found in the wild, across many climates... or maybe in a chest somewhere._  (parent: `farmersdelight:main/root`; triggers: ['minecraft:inventory_changed'])
- `farmersdelight:main/get_ham` — **Wild Butcher** — _Use a Knife to extract Ham from Pigs or Hoglins_  (parent: `farmersdelight:main/craft_knife`; triggers: ['minecraft:inventory_changed'])
- `farmersdelight:main/get_mushroom_colony` — **Fungus Among Us** — _Shear a fully mature Mushroom Colony. To grow them like this, you'll need a very rich soil..._  (parent: `farmersdelight:main/get_fd_seed`; triggers: ['minecraft:inventory_changed'])
- `farmersdelight:main/get_rich_soil` — **Plant Food** — _Organic Compost slowly decays into Rich Soil, an upgrade for your farms!_  (parent: `farmersdelight:main/place_organic_compost`; triggers: ['minecraft:inventory_changed'])
- `farmersdelight:main/harvest_ropelogged_tomato` — **Tall-mato** — _Hang some rope above a tomato crop to make it grow taller_  (parent: `farmersdelight:main/get_fd_seed`; triggers: ['minecraft:default_block_use'])
- `farmersdelight:main/harvest_straw` — **Grasping at Straws** — _Harvest grass, wheat or rice with a Knife to collect Straw_  (parent: `farmersdelight:main/craft_knife`; triggers: ['minecraft:inventory_changed'])
- `farmersdelight:main/hit_raider_with_rotten_tomato` — **Boo! Hiss!** — _Throw a Rotten Tomato at one of these pesky raiders!_  (parent: `farmersdelight:main/harvest_ropelogged_tomato`; triggers: ['minecraft:player_hurt_entity'])
- `farmersdelight:main/master_chef` — **Master Chef** — _Eat a course of every meal available!_  (parent: `farmersdelight:main/place_feast`; triggers: ['minecraft:consume_item'])
- `farmersdelight:main/obtain_netherite_knife` — **If You Can't Take the Heat...** — _Spend a whole Netherite Ingot to upgrade your knife! Or get out of the kitchen._  (parent: `farmersdelight:main/use_cutting_board`; triggers: ['minecraft:inventory_changed'])
- `farmersdelight:main/place_campfire` — **Bonfire Lit** — _Place down a Campfire to cook some food_  (parent: `farmersdelight:main/root`; triggers: ['minecraft:placed_block'])
- `farmersdelight:main/place_cooking_pot` — **Dinner's Served!** — _Put down a Cooking Pot and start preparing meals!_  (parent: `farmersdelight:main/place_campfire`; triggers: ['minecraft:placed_block'])
- `farmersdelight:main/place_feast` — **A Glorious Feast** — _Some meals are big enough to be placed down and shared with friends!_  (parent: `farmersdelight:main/eat_nourishing_food`; triggers: ['minecraft:placed_block'])
- `farmersdelight:main/place_organic_compost` — **Advanced Composting** — _Place down some Organic Compost. It composts better with sun, water and mushrooms!_  (parent: `farmersdelight:main/harvest_straw`; triggers: ['minecraft:placed_block'])
- `farmersdelight:main/place_skillet` — **Sizzling Hot!** — _Sneak to place your Skillet down as a block_  (parent: `farmersdelight:main/use_skillet`; triggers: ['minecraft:placed_block'])
- `farmersdelight:main/plant_all_crops` — **Crop Rotation** — _Cultivate every food-related plant you can find, such as vegetables, fruits, fungi or roots!_  (parent: `farmersdelight:main/plant_rice`; triggers: ['minecraft:placed_block'])
- `farmersdelight:main/plant_rice` — **Dipping Your Roots** — _Plant grains of Rice in a shallow water puddle_  (parent: `farmersdelight:main/get_fd_seed`; triggers: ['minecraft:placed_block'])
- `farmersdelight:main/root` — **Farmer's Delight** — _A world of flavor awaits you!_  (parent: ``; triggers: ['minecraft:inventory_changed'])
- `farmersdelight:main/use_cutting_board` — **Watch Your Fingers** — _With a tool in hand, use a Cutting Board to break down an item_  (parent: `farmersdelight:main/craft_knife`; triggers: ['farmersdelight:use_cutting_board'])
- `farmersdelight:main/use_skillet` — **Portable Cooking** — _Skillets let you cook on the go. Stand near heat, then hold food in your other hand!_  (parent: `farmersdelight:main/place_campfire`; triggers: ['minecraft:consume_item'])
