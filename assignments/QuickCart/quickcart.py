import sys
from typing import Dict, Optional
from OrderStatus import OrderStatus
from Role import Role
from JSONStore import JSONStore
from Order import Order
from User import User
from AuthService import AuthService
from CatalogService import CatalogService
from OrderService import OrderService

class App:
    def __init__(self):
        self.store = JSONStore()
        self.auth = AuthService(self.store)
        self.catalog = CatalogService(self.store)
        self.orders = OrderService(self.store)
        self.current_user: Optional[User] = None

    def run(self):
        self._maybe_seed_products()
        while True:
            if not self.current_user:
                self._show_menu(self._main_menu_options(), self._main_menu_actions())
            else:
                role = self.current_user.role
                if role == Role.ADMIN:
                    self._show_menu(self._admin_menu_options(), self._admin_menu_actions())
                elif role == Role.RIDER:
                    self._show_menu(self._rider_menu_options(), self._rider_menu_actions())
                else:
                    self._show_menu(self._user_menu_options(), self._user_menu_actions())

    def _maybe_seed_products(self):
        if not self.store.list_products():
            self.catalog.add_product("Bottled Water", 1.20, 50)
            self.catalog.add_product("Instant Noodles", 0.80, 100)
            self.catalog.add_product("Chocolate Bar", 1.00, 40)

    def _show_menu(self, options, actions):
        print("\n" + options['title'])
        for idx, opt in enumerate(options['items'], 1):
            print(f"{idx}. {opt}")
        choice = input("Choose an option: ").strip()
        try:
            idx = int(choice) - 1
            if 0 <= idx < len(actions):
                actions[idx]()
            else:
                print("Invalid choice.")
        except ValueError:
            print("Invalid choice.")

    # Main Menu
    def _main_menu_options(self):
        return {
            'title': "=== QuickCart ===",
            'items': [
                "Login",
                "Register as User",
                "Register as Rider",
                "Exit"
            ]
        }
    def _main_menu_actions(self):
        return [
            self._login,
            lambda: self._register(Role.USER),
            lambda: self._register(Role.RIDER),
            self._exit
        ]
    def _exit(self):
        print("Goodbye!")
        sys.exit(0)

    def _login(self):
        email = input("Email: ").strip()
        password = input("Password: ").strip()
        user = self.auth.login(email, password)
        if user:
            self.current_user = user
            print(f"Welcome, {user.name} ({user.role.value})")
        else:
            print("Invalid credentials.")

    def _register(self, role: Role):
        print(f"Register as {role.value}")
        name = input("Full name: ").strip()
        email = input("Email: ").strip()
        password = input("Password: ").strip()
        user = self.auth.register(name, email, password, role)
        if user:
            print("Registration successful. You can now login.")

    def logout(self):
        self.current_user = None
        print("Logged out.")

    # Admin Menu
    def _admin_menu_options(self):
        return {
            'title': "=== Admin Menu ===",
            'items': [
                "Add product",
                "Restock product",
                "List products",
                "View all orders",
                "Cancel an order",
                "Create admin or rider",
                "Logout"
            ]
        }
    def _admin_menu_actions(self):
        return [
            self._admin_add_product,
            self._admin_restock_product,
            self._list_products,
            self._admin_view_orders,
            self._admin_cancel_order,
            self._admin_create_user,
            self.logout
        ]
    def _admin_add_product(self):
        name = input("Product name: ").strip()
        try:
            price = float(input("Price: ").strip())
            stock = int(input("Initial stock: ").strip())
        except ValueError:
            print("Invalid price or stock.")
            return
        product = self.catalog.add_product(name, price, stock)
        print(f"Added product {product.id}: {product.name} - {product.price} ({product.stock} in stock)")

    def _admin_restock_product(self):
        try:
            pid = int(input("Product ID: ").strip())
            amount = int(input("Amount to add: ").strip())
        except ValueError:
            print("Invalid input.")
            return
        product = self.catalog.restock(pid, amount)
        if product:
            print(f"Restocked {product.name}. New stock: {product.stock}")

    def _admin_view_orders(self):
        orders = self.orders.list_all_orders()
        if not orders:
            print("No orders yet.")
            return
        for o in orders:
            print(self._format_order(o))

    def _admin_cancel_order(self):
        try:
            oid = int(input("Order ID: ").strip())
        except ValueError:
            print("Invalid input.")
            return
        self.orders.admin_cancel_order(oid)

    def _admin_create_user(self):
        print("Create user")
        name = input("Full name: ").strip()
        email = input("Email: ").strip()
        role_in = input("Role (ADMIN/RIDER): ").strip().upper()
        if role_in not in {"ADMIN", "RIDER"}:
            print("Only ADMIN or RIDER can be created here.")
            return
        password = input("Password: ").strip()
        role = Role[role_in]
        user = self.auth.register(name, email, password, role)
        if user:
            print(f"Created {role.value}: {user.name} ({user.email})")

    # User Menu
    def _user_menu_options(self):
        return {
            'title': "=== User Menu ===",
            'items': [
                "Browse products",
                "Place order",
                "View my orders",
                "Cancel my pending order",
                "Logout"
            ]
        }
    def _user_menu_actions(self):
        return [
            self._list_products,
            self._user_place_order,
            self._user_view_orders,
            self._user_cancel_order,
            self.logout
        ]
    def _list_products(self):
        products = self.catalog.list_products()
        if not products:
            print("No products available.")
            return
        print("\n-- Products --")
        for p in products:
            print(f"[{p.id}] {p.name} - {p.price} ({p.stock} in stock)")

    def _user_place_order(self):
        print("Enter product IDs and quantities. Leave product ID blank to finish.")
        cart: Dict[int, int] = {}
        while True:
            pid_raw = input("Product ID: ").strip()
            if pid_raw == "":
                break
            try:
                pid = int(pid_raw)
                qty = int(input("Quantity: ").strip())
            except ValueError:
                print("Invalid input. Try again.")
                continue
        if not cart:
            print("No items selected.")
            return
        if not self.current_user:
            print("You must be logged in to place an order.")
            return
    def _user_view_orders(self):
        if not self.current_user:
            print("No user is currently logged in.")
            return
        my_orders = self.orders.list_orders_by_user(self.current_user.id)
        if not my_orders:
            print("You have no orders.")
            return
        for o in my_orders:
            print(self._format_order(o))
            return
        for o in my_orders:
            print(self._format_order(o))

    def _user_cancel_order(self):
        try:
            oid = int(input("Order ID to cancel: ").strip())
        except ValueError:
            print("Invalid input.")
            return
        if not self.current_user:
            print("You must be logged in to cancel an order.")
            return
        self.orders.cancel_order_by_user(self.current_user.id, oid)

    # Rider Menu
    def _rider_menu_options(self):
        return {
            'title': "=== Rider Menu ===",
            'items': [
                "View unassigned pending orders",
                "Accept an order",
                "View my active orders",
                "Update order status",
                "Logout"
            ]
        }
    def _rider_menu_actions(self):
        return [
            self._rider_view_unassigned,
            self._rider_accept_order,
            self._rider_view_active,
            self._rider_update_status,
            self.logout
        ]
    def _rider_view_unassigned(self):
        orders = self.orders.list_unassigned_pending()
        if not orders:
            print("No unassigned pending orders.")
            return
        for o in orders:
            print(self._format_order(o))

    def _rider_accept_order(self):
        try:
            oid = int(input("Order ID to accept: ").strip())
        except ValueError:
            print("Invalid input.")
            return
        if not self.current_user:
            print("You must be logged in as a rider to accept an order.")
            return
        self.orders.accept_order(self.current_user.id, oid)

    def _rider_view_active(self):
        if not self.current_user:
            print("No rider is currently logged in.")
            return
        orders = self.orders.list_assigned_for_rider(self.current_user.id)
        if not orders:
            print("No active orders.")
            return
        for o in orders:
            print(self._format_order(o))

    def _rider_update_status(self):
        try:
            oid = int(input("Order ID: ").strip())
        except ValueError:
            print("Invalid input.")
            return
        if not self.current_user:
            print("No rider is currently logged in.")
            return
        print("Next status options: OUT_FOR_DELIVERY, DELIVERED")
        status_raw = input("New status: ").strip().upper()
        try:
            status = OrderStatus[status_raw]
        except KeyError:
            print("Invalid status.")
            return
        self.orders.update_status_by_rider(self.current_user.id, oid, status)

    def _format_order(self, o: Order) -> str:
        items = ", ".join([f"{i.name} x{i.quantity}" for i in o.items])
        rider = f" | Rider: {o.assigned_rider_id}" if o.assigned_rider_id is not None else ""
        return f"[Order {o.id}] User: {o.user_id} | {items} | Total: {o.total} | Status: {o.status.value}{rider} | Created: {o.created_at}"

if __name__ == "__main__":
    App().run()
