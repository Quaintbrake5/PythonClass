from dataclasses import dataclass, field
from datetime import datetime
from typing import Dict, List, Optional

from assignments.QuickCart.Models.OrderItem import OrderItem
from assignments.QuickCart.quickcart import OrderStatus


@dataclass
class Order:
    id: int
    user_id: int
    items: List[OrderItem]
    total: float
    status: OrderStatus = OrderStatus.PENDING
    assigned_rider_id: Optional[int] = None
    created_at: str = field(default_factory=lambda: datetime.utcnow().isoformat(timespec="seconds"))

    def to_dict(self) -> Dict:
        return {
            "id": self.id,
            "user_id": self.user_id,
            "items": [i.to_dict() for i in self.items],
            "total": self.total,
            "status": self.status.value,
            "assigned_rider_id": self.assigned_rider_id,
            "created_at": self.created_at,
        }

    @staticmethod
    def from_dict(data: Dict) -> "Order":
        return Order(
            id=data["id"],
            user_id=data["user_id"],
            items=[OrderItem.from_dict(x) for x in data["items"]],
            total=data["total"],
            status=OrderStatus(data["status"]),
            assigned_rider_id=data.get("assigned_rider_id"),
            created_at=data.get("created_at", datetime.utcnow().isoformat(timespec="seconds")),
        )
