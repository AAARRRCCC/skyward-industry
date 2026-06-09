# Nested jar: META-INF/jarjar/dev.eriksonn.aeronautics.aeronautics-neoforge-1.21.1-1.2.1.jar

namespaces: ['aeronautics', 'amendments', 'c', 'minecraft', 'musicnotification', 'neoforge', 'sable', 'simulated']
recipe files: 70; types: ['?', 'create:crushing', 'create:deploying', 'create:mechanical_crafting', 'create:mixing', 'create:splashing', 'minecraft:crafting_shaped', 'minecraft:crafting_shapeless']

## type `?`  (example: data/aeronautics/advancement/recipes/misc/adjustable_burner.json)
```json
{
  "parent": "minecraft:recipes/root",
  "criteria": {
    "has_ingredient": {
      "conditions": {
        "items": [
          {
            "items": "minecraft:redstone"
          }
        ]
      },
      "trigger": "minecraft:inventory_changed"
    },
    "has_the_recipe": {
      "conditions": {
        "recipe": "aeronautics:adjustable_burner"
      },
      "trigger": "minecraft:recipe_unlocked"
    }
  },
  "requirements": [
    [
      "has_the_recipe",
      "has_ingredient"
    ]
  ],
  "rewards": {
    "recipes": [
      "aeronautics:adjustable_burner"
    ]
  }
}
```

## type `create:crushing`  (example: data/aeronautics/recipe/crushing/end_stone_powder.json)
```json
{
  "type": "create:crushing",
  "ingredients": [
    {
      "item": "minecraft:end_stone"
    }
  ],
  "processing_time": 250,
  "results": [
    {
      "chance": 0.5,
      "id": "minecraft:end_stone"
    },
    {
      "id": "aeronautics:end_stone_powder"
    }
  ]
}
```

## type `create:deploying`  (example: data/aeronautics/recipe/deploying/deploying_envelope_black.json)
```json
{
  "type": "create:deploying",
  "ingredients": [
    {
      "item": "minecraft:black_wool"
    },
    {
      "item": "minecraft:stick"
    }
  ],
  "results": [
    {
      "count": 3,
      "id": "aeronautics:black_envelope"
    }
  ]
}
```

## type `create:mechanical_crafting`  (example: data/aeronautics/recipe/mechanical_crafting/mounted_potato_cannon.json)
```json
{
  "type": "create:mechanical_crafting",
  "accept_mirrored": true,
  "category": "misc",
  "key": {
    "C": {
      "item": "create:cogwheel"
    },
    "K": {
      "item": "minecraft:dried_kelp_block"
    },
    "P": {
      "item": "create:fluid_pipe"
    },
    "R": {
      "item": "minecraft:redstone"
    },
    "S": {
      "item": "create:copper_sheet"
    }
  },
  "pattern": [
    "SR  ",
    "KCPP",
    "SR  "
  ],
  "result": {
    "count": 1,
    "id": "aeronautics:mounted_potato_cannon"
  }
}
```

## type `create:mixing`  (example: data/aeronautics/recipe/mixing/levitite_blend.json)
```json
{
  "type": "create:mixing",
  "heat_requirement": "heated",
  "ingredients": [
    {
      "item": "aeronautics:end_stone_powder"
    },
    {
      "item": "aeronautics:end_stone_powder"
    },
    {
      "item": "aeronautics:end_stone_powder"
    },
    {
      "item": "aeronautics:end_stone_powder"
    },
    {
      "item": "create:zinc_nugget"
    },
    {
      "item": "create:zinc_nugget"
    },
    {
      "type": "neoforge:tag",
      "amount": 500,
      "tag": "c:water"
    }
  ],
  "results": [
    {
      "amount": 500,
      "id": "aeronautics:levitite_blend"
    }
  ]
}
```

## type `create:splashing`  (example: data/aeronautics/recipe/splashing/envelope_washing.json)
```json
{
  "type": "create:splashing",
  "ingredients": [
    {
      "tag": "aeronautics:shaftless_envelope"
    }
  ],
  "results": [
    {
      "id": "aeronautics:white_envelope"
    }
  ]
}
```

## type `minecraft:crafting_shaped`  (example: data/aeronautics/recipe/adjustable_burner.json)
```json
{
  "type": "minecraft:crafting_shaped",
  "category": "misc",
  "key": {
    "A": {
      "item": "create:andesite_alloy"
    },
    "C": {
      "tag": "aeronautics:burner_fire"
    },
    "R": {
      "item": "minecraft:redstone"
    },
    "S": {
      "item": "create:iron_sheet"
    }
  },
  "pattern": [
    "S S",
    "SCS",
    "ARA"
  ],
  "result": {
    "count": 1,
    "id": "aeronautics:adjustable_burner"
  }
}
```

## type `minecraft:crafting_shapeless`  (example: data/aeronautics/recipe/andesite_propeller_from_andesite.json)
```json
{
  "type": "minecraft:crafting_shapeless",
  "category": "misc",
  "ingredients": [
    {
      "item": "aeronautics:wooden_propeller"
    }
  ],
  "result": {
    "count": 1,
    "id": "aeronautics:andesite_propeller"
  }
}
```
lang aeronautics: 7 items, 46 blocks -> nested_dev.eriksonn.aeronautics.aeronautics-neoforge-1.21.1-1.2.1_aeronautics_items.txt
