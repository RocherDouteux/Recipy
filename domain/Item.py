import math
from enum import Enum
from typing import Optional, List, Tuple

class ItemType(Enum):
    FIRE_CRYSTAL="Fire Crystal"
    WATER_CRYSTAL="Water Crystal"
    SIDERITIS_LEAVES="Sideritis Leaves"
    AMBROSIAL_WATER="Ambrosial Water"
    CINNAMON="Cinnamon"
    LEMONETTE="Lemonette"
    PALM_SYRUP="Palm Syrup"
    PALM_SUGAR="Palm Sugar"
    TSAI_TOU_VOUNOU="Tsai Tou Vounou"

class Item:

    def __init__(self, item_type:ItemType, components: Optional[List[Tuple[int, "Item"]]] = None, yield_: int = 1, is_craftable: bool = True):
        self.item_type = item_type
        self.components = components

        self.yield_ = yield_
        self.is_craftable = is_craftable


    def yield_when_crafted(self):
        return self.yield_

    def craft(self, quantity: int, top=True):
        if not self.is_craftable or self.components is None:
            node = (quantity, self, [])
            return [node] if top else node

        total_batches = math.ceil(quantity / self.yield_)
        children = []
        for required_qty, component in self.components:
            required_total = total_batches * required_qty
            subtree = component.craft(quantity=required_total, top=False)
            children.append(subtree)

        node = (quantity, self, children)
        return [node] if top else node

    def __repr__(self):
        components_str = [ (q, c.item_type.name) for q, c in self.components ] if self.components is not None else []
        return f"Item(name={self.item_type.name}, components={components_str})"
