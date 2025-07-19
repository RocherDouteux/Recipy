import json

from domain.Item import Item, ItemType


def load_items_from_json(file_path):
    with open(file_path, 'r') as f:
        data = json.load(f)

    # Pass 1: create recipes without components
    item_map = {}
    for entry in data:
        item_type = ItemType[entry["item_type"]]
        is_craftable = entry.get("is_craftable", False)
        yield_ = entry.get("yield_", 1)
        item_map[item_type] = Item(item_type=item_type, is_craftable=is_craftable, yield_=yield_, components=None)

    # Pass 2: assign components (link existing Item objects)
    for entry in data:
        item_type = ItemType[entry["item_type"]]
        components_data = entry.get("components")
        if components_data:
            components = []
            for comp in components_data:
                qty = comp["quantity"]
                comp_item_type = ItemType[comp["item_type"]]
                components.append((qty, item_map[comp_item_type]))
            item_map[item_type].components = components

    return list(item_map.values())