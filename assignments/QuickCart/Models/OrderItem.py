from dataclasses import asdict, dataclass
from typing import Dict


@dataclass
class OrderItem:
    product_id: int
    name: str
    quantity: int
    unit_price: float

    def line_total(self) -> float:
        return self.quantity * self.unit_price

    def to_dict(self) -> Dict:
        return asdict(self)

    @staticmethod
    def from_dict(data: Dict) -> "OrderItem":
        return OrderItem(**data)