# Jar inspection: numismatics (1.0.20+neoforge-mc1.21.1)

namespaces: ['c', 'create', 'minecraft', 'numismatics']

recipe files: 74; distinct types: 3

## type `?`  (example: data/numismatics/advancement/recipes/misc/crafting/andesite_depositor.json)
```json
{
  "parent": "minecraft:recipes/root",
  "criteria": {
    "has_item": {
      "conditions": {
        "items": [
          {
            "items": "create:andesite_casing"
          }
        ]
      },
      "trigger": "minecraft:inventory_changed"
    },
    "has_the_recipe": {
      "conditions": {
        "recipe": "numismatics:crafting///andesite_depositor"
      },
      "trigger": "minecraft:recipe_unlocked"
    }
  },
  "requirements": [
    [
      "has_the_recipe",
      "has_item"
    ]
  ],
  "rewards": {
    "recipes": [
      "numismatics:crafting///andesite_depositor"
    ]
  }
}
```

## type `minecraft:crafting_shaped`  (example: data/numismatics/recipe/crafting/black_card.json)
```json
{
  "type": "minecraft:crafting_shaped",
  "category": "misc",
  "key": {
    "/": {
      "tag": "c:dyes/black"
    },
    "@": {
      "item": "create:precision_mechanism"
    },
    "_": {
      "tag": "c:plates/iron"
    }
  },
  "pattern": [
    "@_/"
  ],
  "result": {
    "count": 1,
    "id": "numismatics:black_card"
  }
}
```

## type `minecraft:crafting_shapeless`  (example: data/numismatics/recipe/crafting/andesite_depositor.json)
```json
{
  "type": "minecraft:crafting_shapeless",
  "category": "misc",
  "ingredients": [
    {
      "item": "create:andesite_casing"
    },
    {
      "tag": "c:plates/iron"
    }
  ],
  "result": {
    "count": 1,
    "id": "numismatics:andesite_depositor"
  }
}
```

kubejs markers in jar: []

lang numismatics: 54 item keys, 25 block keys -> numismatics_numismatics_items.txt
