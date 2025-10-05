from typing import List, Optional
from assignments.QuickCart.JSON.JSONStore import JSONStore
from assignments.QuickCart.Models.Product import Product


class CatalogService:
    def __init__(self, store: JSONStore):
        self.store = store

    def list_products(self) -> List[Product]:
        return self.store.list_products()

    def add_product(self, name: str, price: float, stock: int) -> Product:
        product = Product(
            id=self.store.next_id("product_id"),
            name=name.strip(),
            price=round(float(price), 2),
            stock=int(stock)
        )
        self.store.add_product(product)
        return product

    def restock(self, product_id: int, amount: int) -> Optional[Product]:
        product = self.store.get_product(product_id)
        if not product:
            print("Product not found.")
            return None
        if amount <= 0:
            print("Restock amount must be positive.")
            return None
        product.stock += amount
        self.store.update_product(product)
        return product