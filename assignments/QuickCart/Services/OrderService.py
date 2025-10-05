from typing import Dict, List, Optional
from assignments.QuickCart.JSON.JSONStore import JSONStore
from assignments.QuickCart.Models.Order import Order
from assignments.QuickCart.Models.OrderItem import OrderItem
from assignments.QuickCart.quickcart import ALLOWED_TRANSITIONS, OrderStatus # pyright: ignore[reportAttributeAccessIssue]


class OrderService:
    def __init__(self, store: JSONStore):
        self.store = store

    def place_order(self, user_id: int, cart: Dict[int, int]) -> Optional[Order]:
        items: List[OrderItem] = []
        total = 0.0

        # Validate and prepare items
        for pid, qty in cart.items():
            if qty <= 0:
                print(f"Invalid quantity for product {pid}.")
                return None
            product = self.store.get_product(pid)
            if not product:
                print(f"Product {pid} does not exist.")
                return None
            if product.stock < qty:
                print(f"Insufficient stock for '{product.name}'. Available: {product.stock}, requested: {qty}")
                return None
            item = OrderItem(product_id=product.id, name=product.name, quantity=qty, unit_price=product.price)
            items.append(item)
            total += item.line_total()

        # Deduct stock
        for item in items:
            product = self.store.get_product(item.product_id)
            product.stock -= item.quantity # pyright: ignore[reportOptionalMemberAccess]
            self.store.update_product(product) # pyright: ignore[reportArgumentType]

        order = Order(
            id=self.store.next_id("order_id"),
            user_id=user_id,
            items=items,
            total=round(total, 2),
            status=OrderStatus.PENDING,
            assigned_rider_id=None
        )
        self.store.add_order(order)
        print(f"Order {order.id} placed successfully. Total: {order.total}")
        return order

    def cancel_order_by_user(self, user_id: int, order_id: int) -> bool:
        order = self.store.get_order(order_id)
        if not order or order.user_id != user_id:
            print("Order not found.")
            return False
        if order.status != OrderStatus.PENDING:
            print("You can only cancel orders that are still pending.")
            return False
        self._restock_order_items(order)
        order.status = OrderStatus.CANCELLED
        self.store.update_order(order)
        print(f"Order {order.id} cancelled.")
        return True

    def admin_cancel_order(self, order_id: int) -> bool:
        order = self.store.get_order(order_id)
        if not order:
            print("Order not found.")
            return False
        if order.status in {OrderStatus.DELIVERED, OrderStatus.CANCELLED}:
            print("Order cannot be cancelled now.")
            return False
        # Restock only if not delivered yet and not already cancelled
        self._restock_order_items(order)
        order.status = OrderStatus.CANCELLED
        self.store.update_order(order)
        print(f"Order {order.id} cancelled by admin.")
        return True

    def _restock_order_items(self, order: Order):
        for item in order.items:
            product = self.store.get_product(item.product_id)
            if product:
                product.stock += item.quantity
                self.store.update_product(product)

    def list_orders_by_user(self, user_id: int) -> List[Order]:
        return [o for o in self.store.list_orders() if o.user_id == user_id]

    def list_all_orders(self) -> List[Order]:
        return self.store.list_orders()

    def list_unassigned_pending(self) -> List[Order]:
        return [
            o for o in self.store.list_orders()
            if o.status == OrderStatus.PENDING and o.assigned_rider_id is None
        ]

    def list_assigned_for_rider(self, rider_id: int) -> List[Order]:
        return [
            o for o in self.store.list_orders()
            if o.assigned_rider_id == rider_id and o.status in {
                OrderStatus.ACCEPTED, OrderStatus.OUT_FOR_DELIVERY
            }
        ]

    def accept_order(self, rider_id: int, order_id: int) -> bool:
        order = self.store.get_order(order_id)
        if not order:
            print("Order not found.")
            return False
        if order.status != OrderStatus.PENDING or order.assigned_rider_id is not None:
            print("Order is not available for acceptance.")
            return False
        order.assigned_rider_id = rider_id
        order.status = OrderStatus.ACCEPTED
        self.store.update_order(order)
        print(f"Order {order.id} accepted.")
        return True

    def update_status_by_rider(self, rider_id: int, order_id: int, new_status: OrderStatus) -> bool:
        order = self.store.get_order(order_id)
        if not order:
            print("Order not found.")
            return False
        if order.assigned_rider_id != rider_id:
            print("This order is not assigned to you.")
            return False
        if new_status not in ALLOWED_TRANSITIONS[order.status]:
            print(f"Invalid transition from {order.status.value} to {new_status.value}.")
            return False
        order.status = new_status
        self.store.update_order(order)
        print(f"Order {order.id} updated to {order.status.value}.")
        return True