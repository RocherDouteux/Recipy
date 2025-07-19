def print_flat(recipe):
    for qty, item in recipe:
        print(f"- {qty}x {item.item_type.value}")

def print_nested(recipe, level=0):
    indent = "  " * level
    for entry in recipe:
        if isinstance(entry, tuple) and len(entry) == 3:
            qty, item, children = entry
            print(f"{indent}- {qty}x {item.item_type.value}")
            print_nested(children, level + 1)
        elif isinstance(entry, list):
            print_nested(entry, level)
        elif isinstance(entry, tuple):
            qty, item = entry
            print(f"{indent}- {qty}x {item.item_type.value}")

def flatten_craft_tree(tree):
    merged = {}

    def walk(node):
        qty, item, children = node
        if not children:
            merged[item] = merged.get(item, 0) + qty
        else:
            for child in children:
                walk(child)

    for entry in tree:
        walk(entry)

    return sorted([(qty, item) for item, qty in merged.items()], key=lambda x: x[1].item_type.value)

def summary(recipe):
    print(f"Summary")
    print_nested(recipe)

    print("")

    recipe_flat = flatten_craft_tree(recipe)
    print(f"Raw materials")
    print_flat(recipe_flat)