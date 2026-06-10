# Skyward: bind Crossing loot tables. Run ONCE, positioned at the paste
# anchor (the lodestone = schematic min corner):
#   /execute positioned <ax> <ay> <az> run function skyward:bind_loot
data merge block ~100 ~46 ~62 {LootTable:"skyward:chests/crossing_landfall"}
data merge block ~46 ~38 ~73 {LootTable:"skyward:chests/crossing_vault"}
data merge block ~111 ~43 ~64 {LootTable:"skyward:chests/crossing_cache"}
data merge block ~94 ~46 ~55 {LootTable:"skyward:chests/crossing_cache"}
data merge block ~86 ~47 ~52 {LootTable:"skyward:chests/crossing_cache"}
data merge block ~74 ~48 ~64 {LootTable:"skyward:chests/crossing_cache"}
data merge block ~60 ~50 ~72 {LootTable:"skyward:chests/crossing_cache"}
data merge block ~55 ~50 ~64 {LootTable:"skyward:chests/crossing_cache"}
data merge block ~37 ~46 ~71 {LootTable:"skyward:chests/crossing_cache"}
data merge block ~64 ~33 ~92 {LootTable:"skyward:chests/crossing_cache"}
tellraw @a {"text":"[Skyward] Crossing loot bound: 10 containers.","color":"aqua"}
