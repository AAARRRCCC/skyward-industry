# Jar inspection: create-aeroworks (1.2.11+mc1.21.1)

namespaces: ['aeroworks', 'create', 'minecraft']

recipe files: 4; distinct types: 3

## type `create:mechanical_crafting`  (example: data/aeroworks/recipe/joystick.json)
```json
{
  "type": "create:mechanical_crafting",
  "accept_mirrored": false,
  "category": "misc",
  "key": {
    "L": {
      "item": "create:redstone_link"
    },
    "P": {
      "item": "create:precision_mechanism"
    },
    "S": {
      "item": "create:shaft"
    },
    "B": {
      "tag": "c:ingots/brass"
    }
  },
  "pattern": [
    " L ",
    " P ",
    " S ",
    " B ",
    "BBB"
  ],
  "result": {
    "count": 1,
    "id": "aeroworks:joystick"
  },
  "show_notification": false
}
```

## type `minecraft:crafting_shaped`  (example: data/aeroworks/recipe/mechanical_servo.json)
```json
{
  "type": "minecraft:crafting_shaped",
  "category": "misc",
  "key": {
    "A": {
      "item": "create:precision_mechanism"
    },
    "B": {
      "item": "create:sequenced_gearshift"
    },
    "C": {
      "item": "create:electron_tube"
    },
    "D": {
      "tag": "c:ingots/brass"
    }
  },
  "pattern": [
    " A ",
    "DBD",
    " C "
  ],
  "result": {
    "count": 1,
    "id": "aeroworks:mechanical_servo"
  }
}
```

## type `minecraft:crafting_shapeless`  (example: data/aeroworks/recipe/gyroscope.json)
```json
{
  "type": "minecraft:crafting_shapeless",
  "category": "misc",
  "ingredients": [
    {
      "item": "create:flywheel"
    },
    {
      "item": "simulated:gimbal_sensor"
    }
  ],
  "result": {
    "id": "aeroworks:gyroscope",
    "count": 1
  }
}
```

kubejs markers in jar: []

lang aeroworks: 0 item keys, 11 block keys -> create-aeroworks_aeroworks_items.txt
