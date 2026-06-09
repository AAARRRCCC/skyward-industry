# Jar inspection: create (6.0.10+mc1.21.1)

namespaces: ['c', 'create', 'curios', 'minecraft', 'neoforge', 'quark']

recipe files: 2933; distinct types: 26

## type `?`  (example: data/create/tags/recipe_serializer/automation_ignore.json)
```json
{
  "values": [
    {
      "id": "occultism:spirit_trade",
      "required": false
    },
    {
      "id": "occultism:ritual",
      "required": false
    }
  ]
}
```

## type `create:compacting`  (example: data/create/recipe/compacting/diorite_from_flint.json)
```json
{
  "type": "create:compacting",
  "ingredients": [
    {
      "item": "minecraft:flint"
    },
    {
      "item": "minecraft:flint"
    },
    {
      "item": "minecraft:calcite"
    },
    {
      "type": "neoforge:single",
      "amount": 100,
      "fluid": "minecraft:lava"
    }
  ],
  "results": [
    {
      "id": "minecraft:diorite"
    }
  ]
}
```

## type `create:crushing`  (example: data/create/recipe/crushing/raw_nickel.json)
```json
{
  "neoforge:conditions": [
    {
      "type": "neoforge:not",
      "value": {
        "type": "neoforge:tag_empty",
        "tag": "c:raw_materials/nickel"
      }
    }
  ],
  "type": "create:crushing",
  "ingredients": [
    {
      "tag": "c:raw_materials/nickel"
    }
  ],
  "processing_time": 400,
  "results": [
    {
      "id": "create:crushed_raw_nickel"
    },
    {
      "chance": 0.75,
      "id": "create:experience_nugget"
    }
  ]
}
```

## type `create:cutting`  (example: data/create/recipe/cutting/andesite_alloy.json)
```json
{
  "type": "create:cutting",
  "ingredients": [
    {
      "item": "create:andesite_alloy"
    }
  ],
  "processing_time": 200,
  "results": [
    {
      "count": 6,
      "id": "create:shaft"
    }
  ]
}
```

## type `create:deploying`  (example: data/create/recipe/deploying/cogwheel.json)
```json
{
  "type": "create:deploying",
  "ingredients": [
    {
      "item": "create:shaft"
    },
    {
      "tag": "minecraft:planks"
    }
  ],
  "results": [
    {
      "id": "create:cogwheel"
    }
  ]
}
```

## type `create:emptying`  (example: data/create/recipe/emptying/honey_bottle.json)
```json
{
  "type": "create:emptying",
  "ingredients": [
    {
      "item": "minecraft:honey_bottle"
    }
  ],
  "results": [
    {
      "id": "minecraft:glass_bottle"
    },
    {
      "amount": 250,
      "id": "create:honey"
    }
  ]
}
```

## type `create:filling`  (example: data/create/recipe/filling/honey_bottle.json)
```json
{
  "type": "create:filling",
  "ingredients": [
    {
      "item": "minecraft:glass_bottle"
    },
    {
      "type": "neoforge:tag",
      "amount": 250,
      "tag": "c:honey"
    }
  ],
  "results": [
    {
      "id": "minecraft:honey_bottle"
    }
  ]
}
```

## type `create:haunting`  (example: data/create/recipe/haunting/infested_stone.json)
```json
{
  "type": "create:haunting",
  "ingredients": [
    {
      "item": "minecraft:stone"
    }
  ],
  "results": [
    {
      "id": "minecraft:infested_stone"
    }
  ]
}
```

## type `create:item_application`  (example: data/create/recipe/item_application/brass_casing_from_log.json)
```json
{
  "type": "create:item_application",
  "ingredients": [
    {
      "tag": "c:stripped_logs"
    },
    {
      "tag": "c:ingots/brass"
    }
  ],
  "results": [
    {
      "id": "create:brass_casing"
    }
  ]
}
```

## type `create:item_copying`  (example: data/create/recipe/crafting/curiosities/item_copying.json)
```json
{
  "type": "create:item_copying",
  "category": "misc"
}
```

## type `create:mechanical_crafting`  (example: data/create/recipe/mechanical_crafting/crushing_wheel.json)
```json
{
  "type": "create:mechanical_crafting",
  "accept_mirrored": false,
  "category": "misc",
  "key": {
    "A": {
      "item": "create:andesite_alloy"
    },
    "P": {
      "tag": "minecraft:planks"
    },
    "S": {
      "tag": "c:stones"
    }
  },
  "pattern": [
    " AAA ",
    "AAPAA",
    "APSPA",
    "AAPAA",
    " AAA "
  ],
  "result": {
    "count": 2,
    "id": "create:crushing_wheel"
  },
  "show_notification": false
}
```

## type `create:milling`  (example: data/create/recipe/milling/short_grass.json)
```json
{
  "type": "create:milling",
  "ingredients": [
    {
      "item": "minecraft:short_grass"
    }
  ],
  "processing_time": 50,
  "results": [
    {
      "chance": 0.25,
      "id": "minecraft:wheat_seeds"
    }
  ]
}
```

## type `create:mixing`  (example: data/create/recipe/mixing/lava_from_cobble.json)
```json
{
  "type": "create:mixing",
  "heat_requirement": "superheated",
  "ingredients": [
    {
      "tag": "c:cobblestones"
    }
  ],
  "results": [
    {
      "amount": 50,
      "id": "minecraft:lava"
    }
  ]
}
```

## type `create:pressing`  (example: data/create/recipe/pressing/cardboard.json)
```json
{
  "type": "create:pressing",
  "ingredients": [
    {
      "item": "create:pulp"
    }
  ],
  "results": [
    {
      "id": "create:cardboard"
    }
  ]
}
```

## type `create:sandpaper_polishing`  (example: data/create/recipe/sandpaper_polishing/rose_quartz.json)
```json
{
  "type": "create:sandpaper_polishing",
  "ingredients": [
    {
      "item": "create:rose_quartz"
    }
  ],
  "results": [
    {
      "id": "create:polished_rose_quartz"
    }
  ]
}
```

## type `create:sequenced_assembly`  (example: data/create/recipe/sequenced_assembly/precision_mechanism.json)
```json
{
  "type": "create:sequenced_assembly",
  "ingredient": {
    "tag": "c:plates/gold"
  },
  "loops": 5,
  "results": [
    {
      "chance": 120.0,
      "id": "create:precision_mechanism"
    },
    {
      "chance": 8.0,
      "id": "create:golden_sheet"
    },
    {
      "chance": 8.0,
      "id": "create:andesite_alloy"
    },
    {
      "chance": 5.0,
      "id": "create:cogwheel"
    },
    {
      "chance": 3.0,
      "id": "minecraft:gold_nugget"
    },
    {
      "chance": 2.0,
      "id": "create:shaft"
    },
    {
      "chance": 2.0,
      "id": "create:crushed_raw_gold"
    },
    {
      "id": "minecraft:iron_ingot"
    },
    {
      "id": "minecraft:clock"
    }
  ],
  "sequence": [
    {
      "type": "create:deploying",
      "ingredients": [
        {
          "item": "create:incomplete_precision_mechanism"
        },
        {
          "item": "create:cogwheel"
        }
      ],
      "results": [
        {
          "id": "create:incomplete_precision_mechanism"
        }
      ]
    },
    {
      "type": "create:deploying",
      "ingredients": [
        {
          "item": "create:incomplete_precision_mechanism"
        },
        {
          "item": "create:large_cogwheel"
        }
      ],
      "results": [
        {
          "id": "create:incomplete_precision_mechanism"
        }
      ]
    },
    {
      "type": "create:deploying",
      "ingredients": [
        {
          "item": "create:incomplete_precision_mechanism"
        },
        {
          "tag": "c:nuggets/iron"
        }
      ],
      "results": [
        {
          "id": "create:incomplete_precision_mechanism"
        }
      ]
    }
  ],
  "transitional_item": {
    "id": "create:incomplete_precision_mechanism"
  }
}
```

## type `create:splashing`  (example: data/create/recipe/splashing/industrial_iron_window_pane.json)
```json
{
  "type": "create:splashing",
  "ingredients": [
    {
      "item": "create:industrial_iron_window_pane"
    }
  ],
  "results": [
    {
      "id": "create:weathered_iron_window_pane"
    }
  ]
}
```

## type `create:toolbox_dyeing`  (example: data/create/recipe/crafting/curiosities/toolbox_dyeing.json)
```json
{
  "type": "create:toolbox_dyeing",
  "category": "misc"
}
```

## type `minecraft:blasting`  (example: data/create/recipe/blasting/ingot_aluminum_compat_immersiveengineering.json)
```json
{
  "neoforge:conditions": [
    {
      "type": "neoforge:mod_loaded",
      "modid": "immersiveengineering"
    }
  ],
  "type": "minecraft:blasting",
  "category": "blocks",
  "cookingtime": 100,
  "experience": 0.1,
  "ingredient": {
    "item": "create:crushed_raw_aluminum"
  },
  "result": {
    "id": "immersiveengineering:ingot_aluminum"
  }
}
```

## type `minecraft:campfire_cooking`  (example: data/create/recipe/campfire_cooking/bread.json)
```json
{
  "type": "minecraft:campfire_cooking",
  "category": "food",
  "cookingtime": 600,
  "experience": 0.0,
  "ingredient": {
    "item": "create:dough"
  },
  "result": {
    "count": 1,
    "id": "minecraft:bread"
  }
}
```

## type `minecraft:crafting_shaped`  (example: data/create/recipe/cut_scorchia_wall.json)
```json
{
  "type": "minecraft:crafting_shaped",
  "category": "building",
  "key": {
    "X": {
      "item": "create:cut_scorchia"
    }
  },
  "pattern": [
    "XXX",
    "XXX"
  ],
  "result": {
    "count": 6,
    "id": "create:cut_scorchia_wall"
  }
}
```

## type `minecraft:crafting_shapeless`  (example: data/create/recipe/polished_cut_scoria_slab_recycling.json)
```json
{
  "type": "minecraft:crafting_shapeless",
  "category": "building",
  "ingredients": [
    {
      "item": "create:polished_cut_scoria_slab"
    },
    {
      "item": "create:polished_cut_scoria_slab"
    }
  ],
  "result": {
    "count": 1,
    "id": "create:polished_cut_scoria"
  }
}
```

## type `minecraft:smelting`  (example: data/create/recipe/smelting/ingot_aluminum_compat_immersiveengineering.json)
```json
{
  "neoforge:conditions": [
    {
      "type": "neoforge:mod_loaded",
      "modid": "immersiveengineering"
    }
  ],
  "type": "minecraft:smelting",
  "category": "blocks",
  "cookingtime": 200,
  "experience": 0.1,
  "ingredient": {
    "item": "create:crushed_raw_aluminum"
  },
  "result": {
    "id": "immersiveengineering:ingot_aluminum"
  }
}
```

## type `minecraft:smithing_transform`  (example: data/create/recipe/crafting/appliances/netherite_backtank.json)
```json
{
  "type": "minecraft:smithing_transform",
  "addition": {
    "tag": "c:ingots/netherite"
  },
  "base": {
    "item": "create:copper_backtank"
  },
  "result": {
    "count": 1,
    "id": "create:netherite_backtank"
  },
  "template": {
    "item": "minecraft:netherite_upgrade_smithing_template"
  }
}
```

## type `minecraft:smoking`  (example: data/create/recipe/smoking/bread.json)
```json
{
  "type": "minecraft:smoking",
  "category": "food",
  "cookingtime": 100,
  "experience": 0.0,
  "ingredient": {
    "item": "create:dough"
  },
  "result": {
    "count": 1,
    "id": "minecraft:bread"
  }
}
```

## type `minecraft:stonecutting`  (example: data/create/recipe/cut_calcite_brick_stairs_from_stone_types_calcite_stonecutting.json)
```json
{
  "type": "minecraft:stonecutting",
  "ingredient": {
    "tag": "create:stone_types/calcite"
  },
  "result": {
    "count": 1,
    "id": "create:cut_calcite_brick_stairs"
  }
}
```

kubejs markers in jar: []

lang create: 204 item keys, 701 block keys -> create_create_items.txt
