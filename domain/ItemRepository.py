from typing import List, Optional

from domain.Item import Item, ItemType, JobType


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

    def filter_by_jobs(self, filter_with: List[JobType]) -> List[Item]:
        items = []

        for item in self.items:
            current_item_jobs = item.jobs
            if all(must_have_job in current_item_jobs for must_have_job in filter_with):
                items.append(item)

        return items
