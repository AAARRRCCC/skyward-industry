# Nested jar: META-INF/jarjar/dev.simulated_team.simulated.simulated-neoforge-1.21.1-1.2.1.jar

namespaces: ['c', 'create', 'minecraft', 'sable', 'simulated']
recipe files: 139; types: ['?', 'create:filling', 'create:mechanical_crafting', 'create:sequenced_assembly', 'minecraft:crafting_shaped', 'minecraft:crafting_shapeless', 'simulated:portable_engine_dyeing']

## type `?`  (example: data/create/advancement/recipes/misc/white_sail.json)
```json
{
  "parent": "minecraft:recipes/root",
  "criteria": {
    "has_ingredient": {
      "conditions": {
        "items": [
          {
            "items": "simulated:white_symmetric_sail"
          }
        ]
      },
      "trigger": "minecraft:inventory_changed"
    },
    "has_the_recipe": {
      "conditions": {
        "recipe": "create:white_sail"
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
      "create:white_sail"
    ]
  }
}
```

## type `create:filling`  (example: data/simulated/recipe/filling/honey_glue.json)
```json
{
  "type": "create:filling",
  "ingredients": [
    {
      "item": "create:iron_sheet"
    },
    {
      "type": "neoforge:single",
      "amount": 500,
      "fluid": "create:honey"
    }
  ],
  "results": [
    {
      "id": "simulated:honey_glue"
    }
  ]
}
```

## type `create:mechanical_crafting`  (example: data/simulated/recipe/mechanical_crafting/docking_connector.json)
```json
{
  "type": "create:mechanical_crafting",
  "accept_mirrored": true,
  "category": "misc",
  "key": {
    "A": {
      "item": "create:brass_casing"
    },
    "B": {
      "item": "create:brass_sheet"
    },
    "C": {
      "item": "create:chute"
    },
    "E": {
      "item": "create:electron_tube"
    },
    "I": {
      "item": "create:iron_sheet"
    },
    "P": {
      "item": "minecraft:piston"
    }
  },
  "pattern": [
    "ICI",
    " C ",
    "PAP",
    "BEB"
  ],
  "result": {
    "count": 2,
    "id": "simulated:docking_connector"
  }
}
```

## type `create:sequenced_assembly`  (example: data/simulated/recipe/sequenced_assembly/engine_assembly.json)
```json
{
  "type": "create:sequenced_assembly",
  "ingredient": {
    "item": "create:iron_sheet"
  },
  "loops": 8,
  "results": [
    {
      "chance": 50.0,
      "id": "simulated:engine_assembly"
    },
    {
      "chance": 16.0,
      "id": "create:iron_sheet"
    },
    {
      "chance": 15.0,
      "id": "minecraft:iron_nugget"
    },
    {
      "chance": 10.0,
      "id": "create:industrial_iron_block"
    },
    {
      "chance": 8.0,
      "id": "minecraft:iron_bars"
    },
    {
      "id": "minecraft:iron_helmet"
    }
  ],
  "sequence": [
    {
      "type": "create:cutting",
      "ingredients": [
        {
          "item": "simulated:incomplete_engine_assembly"
        }
      ],
      "results": [
        {
          "id": "simulated:incomplete_engine_assembly"
        }
      ]
    },
    {
      "type": "create:pressing",
      "ingredients": [
        {
          "item": "simulated:incomplete_engine_assembly"
        }
      ],
      "results": [
        {
          "id": "simulated:incomplete_engine_assembly"
        }
      ]
    }
  ],
  "transitional_item": {
    "id": "simulated:incomplete_engine_assembly"
  }
}
```

## type `minecraft:crafting_shaped`  (example: data/simulated/recipe/altitude_sensor.json)
```json
{
  "type": "minecraft:crafting_shaped",
  "category": "misc",
  "key": {
    "A": {
      "item": "create:andesite_casing"
    },
    "P": {
      "item": "minecraft:paper"
    },
    "S": {
      "item": "create:iron_sheet"
    }
  },
  "pattern": [
    "P",
    "S",
    "A"
  ],
  "result": {
    "count": 1,
    "id": "simulated:altitude_sensor"
  }
}
```

## type `minecraft:crafting_shapeless`  (example: data/create/recipe/white_sail.json)
```json
{
  "type": "minecraft:crafting_shapeless",
  "category": "misc",
  "ingredients": [
    {
      "item": "simulated:white_symmetric_sail"
    }
  ],
  "result": {
    "count": 1,
    "id": "create:white_sail"
  }
}
```

## type `simulated:portable_engine_dyeing`  (example: data/simulated/recipe/crafting/portable_engine_dyeing.json)
```json
{
  "type": "simulated:portable_engine_dyeing",
  "category": "misc"
}
```
lang simulated: 36 items, 124 blocks -> nested_dev.simulated_team.simulated.simulated-neoforge-1.21.1-1.2.1_simulated_items.txt
