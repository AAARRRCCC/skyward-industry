# Nested jar: META-INF/jarjar/dev.ryanhcode.offroad.offroad-neoforge-1.21.1-1.2.1.jar

namespaces: ['create', 'minecraft', 'offroad', 'sable']
recipe files: 14; types: ['?', 'minecraft:crafting_shaped', 'minecraft:crafting_shapeless']

## type `?`  (example: data/offroad/advancement/recipes/misc/borehead_bearing.json)
```json
{
  "parent": "minecraft:recipes/root",
  "criteria": {
    "has_ingredient": {
      "conditions": {
        "items": [
          {
            "items": "create:industrial_iron_block"
          }
        ]
      },
      "trigger": "minecraft:inventory_changed"
    },
    "has_the_recipe": {
      "conditions": {
        "recipe": "offroad:borehead_bearing"
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
      "offroad:borehead_bearing"
    ]
  }
}
```

## type `minecraft:crafting_shaped`  (example: data/offroad/recipe/borehead_bearing.json)
```json
{
  "type": "minecraft:crafting_shaped",
  "category": "misc",
  "key": {
    "G": {
      "item": "create:gearbox"
    },
    "I": {
      "item": "create:industrial_iron_block"
    },
    "S": {
      "tag": "minecraft:wooden_slabs"
    }
  },
  "pattern": [
    "S",
    "G",
    "I"
  ],
  "result": {
    "count": 1,
    "id": "offroad:borehead_bearing"
  }
}
```

## type `minecraft:crafting_shapeless`  (example: data/offroad/recipe/small_tire.json)
```json
{
  "type": "minecraft:crafting_shapeless",
  "category": "misc",
  "ingredients": [
    {
      "item": "create:shaft"
    },
    {
      "item": "minecraft:dried_kelp"
    }
  ],
  "result": {
    "count": 1,
    "id": "offroad:small_tire"
  }
}
```
lang offroad: 17 items, 8 blocks -> nested_dev.ryanhcode.offroad.offroad-neoforge-1.21.1-1.2.1_offroad_items.txt
