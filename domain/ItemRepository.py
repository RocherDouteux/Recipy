from typing import List, Optional

from domain.Item import Item, ItemType


class ItemRepository:

    def __init__(self, items: Optional[List[Item]] = None):
        self.items = items if items is not None else []

    def add_item(self, item: Item):
        self.items.append(item)

    def add_items(self, items: List[Item]):
        for item in items:
            self.add_item(item)

    def get_item(self, item_type: ItemType) -> Optional[Item]:
        for item in self.items:
            if item.item_type.name == item_type.name:
                return item

        return None

    def get_items(self) -> List[Item]:
        return self.items
