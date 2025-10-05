from typing import Optional
from assignments.QuickCart.Utilities.HashPassword import hash_password
from assignments.QuickCart.quickcart import JSONStore, Role, User


class AuthService:
    def __init__(self, store: JSONStore):
        self.store = store
        self._ensure_default_admin()

    def _ensure_default_admin(self):
        # Seed default admin if none exists
        users = self.store.list_users()
        has_admin = any(u.role == Role.ADMIN for u in users)
        if not has_admin:
            admin = User(
                id=self.store.next_id("user_id"),
                name="Administrator",
                email="admin@quickcart",
                password_hash=hash_password("admin123"),
                role=Role.ADMIN
            )
            self.store.add_user(admin)

    def register(self, name: str, email: str, password: str, role: Role = Role.USER) -> Optional[User]:
        if self.store.find_user_by_email(email):
            print("Error: Email already registered.")
            return None
        user = User(
            id=self.store.next_id("user_id"),
            name=name.strip(),
            email=email.strip(),
            password_hash=hash_password(password),
            role=role
        )
        self.store.add_user(user)
        return user

    def login(self, email: str, password: str) -> Optional[User]:
        user = self.store.find_user_by_email(email)
        if not user:
            return None
        if user.password_hash != hash_password(password):
            return None
        return user