import json
import os
from typing import List, Optional

from assignments.QuickCart.Models.Order import Order
from assignments.QuickCart.Models.Product import Product
from assignments.QuickCart.quickcart import User


class JSONStore:
    def __init__(self, path: str = "quickcart_data.json"):
        self.path = path
        self.data = {
            "users": [],
            "products": [],
            "orders": [],
            "counters": {
                "user_id": 0,
                "product_id": 0,
                "order_id": 0
            }
        }
        self._load_or_init()

    def _load_or_init(self):
        if os.path.exists(self.path):
            try:
                with open(self.path, "r", encoding="utf-8") as f:
                    self.data = json.load(f)
            except Exception:
                print("Warning: data file is corrupted. Re-initializing a fresh store.")
                self._save()
        else:
            self._save()

    def _save(self):
        with open(self.path, "w", encoding="utf-8") as f:
            json.dump(self.data, f, indent=2)

    # Users
    def add_user(self, user: User):
        self.data["users"].append(user.to_dict())
        self._save()

    def list_users(self) -> List[User]:
        return [User.from_dict(u) for u in self.data["users"]]

    def find_user_by_email(self, email: str) -> Optional[User]:
        for u in self.data["users"]:
            if u["email"].lower() == email.lower():
                return User.from_dict(u)
        return None

    def get_user(self, user_id: int) -> Optional[User]:
        for u in self.data["users"]:
            if u["id"] == user_id:
                return User.from_dict(u)
        return None

    def update_user(self, user: User):
        for idx, u in enumerate(self.data["users"]):
            if u["id"] == user.id:
                self.data["users"][idx] = user.to_dict()
                self._save()
                return

    # Products
    def add_product(self, product: Product):
        self.data["products"].append(product.to_dict())
        self._save()

    def list_products(self) -> List[Product]:
        return [Product.from_dict(p) for p in self.data["products"]]

    def get_product(self, product_id: int) -> Optional[Product]:
        for p in self.data["products"]:
            if p["id"] == product_id:
                return Product.from_dict(p)
        return None

    def update_product(self, product: Product):
        for idx, p in enumerate(self.data["products"]):
            if p["id"] == product.id:
                self.data["products"][idx] = product.to_dict()
                self._save()
                return

    # Orders
    def add_order(self, order: Order):
        self.data["orders"].append(order.to_dict())
        self._save()

    def list_orders(self) -> List[Order]:
        return [Order.from_dict(o) for o in self.data["orders"]]

    def get_order(self, order_id: int) -> Optional[Order]:
        for o in self.data["orders"]:
            if o["id"] == order_id:
                return Order.from_dict(o)
        return None

    def update_order(self, order: Order):
        for idx, o in enumerate(self.data["orders"]):
            if o["id"] == order.id:
                self.data["orders"][idx] = order.to_dict()
                self._save()
                return

    # Counters
    def next_id(self, key: str) -> int:
        self.data["counters"][key] += 1
        self._save()
        return self.data["counters"][key]