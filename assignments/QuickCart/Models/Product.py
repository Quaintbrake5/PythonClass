from dataclasses import asdict, dataclass
from typing import Dict


@dataclass
class Product:
    id: int
    name: str
    price: float
    stock: int

    def to_dict(self) -> Dict:
        return asdict(self)

    @staticmethod
    def from_dict(data: Dict) -> "Product":
        return Product(**data)

