# Recipy

**Recipy** is a Python program that calculates the list of components required to craft a given quantity of an item in **Final Fantasy XIV**. It builds both a nested recipe tree and a flattened list of raw ingredients, taking into account intermediate crafting steps and yield quantities.

## Features

- ✅ Recursive crafting resolution
- ✅ Batch calculations based on recipe yield
- ✅ Flat and nested views of required materials
- ✅ JSON-based recipe loading
- ✅ Lightweight, extensible design

## How it works

Each item includes:
- `item_type`: the item's identifier (e.g. `PALM_SUGAR`)
- `is_craftable`: whether it's crafted or gathered
- `jobs`: the jobs needed to gather or craft the item (e.g. `BOTANIST`)
- `components`: list of `(quantity, item_type)` tuples for craftable items
- `yield_`: number of items produced per craft (default is 1)

The crafting logic:
1. Compute how many batches are needed based on the `yield_` and `quantity`.
2. Recursively resolve the requirements of all components.
3. Aggregate into a nested tree or a flat list.

## JSON Loading

Recipes can be stored in a JSON file using a two-pass loading algorithm:

- **First pass**: Instantiate all items without their components.
- **Second pass**: Resolve component references and build crafting dependencies.

### Example JSON

```json
[
  {
    "item_type": "PALM_SUGAR",
    "is_craftable": true,
    "jobs": [
      "CULINARIAN"
    ],
    "yield_": 3,
    "components": [
      {"quantity": 8, "item_type": "FIRE_CRYSTAL"},
      {"quantity": 6, "item_type": "PALM_SYRUP"}
    ]
  },
  {
    "item_type": "PALM_SYRUP",
    "is_craftable": false,
    "jobs": [
      "BOTANIST"
    ]
  }
]
```

This allows you to define complex recipes while ensuring all references are resolved correctly, even for nested dependencies.

## Example output

### Nested view

```
- 300x Tsai Tou Vounou
  - 800x Fire Crystal
  - 800x Water Crystal
  - 200x Sideritis Leaves
  - 200x Ambrosial Water
  - 100x Palm Sugar
    - 267x Fire Crystal
    - 200x Palm Syrup
  - 100x Cinnamon
  - 100x Lemonette
```

### Flat view

```
To craft 300 of 'Tsai Tou Vounou', you need:
- 1067x Fire Crystal
- 800x Water Crystal
- 200x Sideritis Leaves
- 200x Ambrosial Water
- 200x Palm Syrup
- 100x Cinnamon
- 100x Lemonette
```

### Job view
```
'Fire crystal' can be acquired as: Botanist, Miner
```

## Installation

Requires Python 3.10+.

```bash
git clone https://github.com/RocherDouteux/Recipy.git
cd Recipy
python main.py
```

## Project structure

```
Recipy/
├── domain/
│   ├── Item.py
│   ├── ItemRepository.py
│   ├── ItemType.py
│   └── Loader.py
├── recipes/
│   └── recipes.json
├── main.py
└── README.md
```

## Future improvements

- Inventory-aware component deduction
- UI or web interface
- Integration with real FFXIV APIs
- Sorting/filtering by Job

## License

MIT License.

