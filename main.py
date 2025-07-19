from domain import Utils

from domain.Loader import load_items_from_json
from domain.ItemRepository import ItemRepository
from domain.Item import ItemType


def main():
    items = load_items_from_json("recipes/recipes.json")

    items_repository = ItemRepository()
    items_repository.add_items(items)

    recently_added_item = items_repository.get_item(ItemType.TSAI_TOU_VOUNOU)
    quantity = 300

    recipe_nested = recently_added_item.craft(quantity=quantity)
    Utils.summary(recipe_nested)

if __name__ == '__main__':
    main()
