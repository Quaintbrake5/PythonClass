

from ast import Dict
from dataclasses import dataclass, field, asdict
from typing import List, Dict, Optional

from assignments.QuickCart.quickcart import Role


@dataclass
class User:
    id: int
    name: str
    email: str
    password_hash: str
    role: Role

    def to_dict(self) -> Dict:
        data = asdict(self)
        data["role"] = self.role.value
        return data

    @staticmethod
    def from_dict(data: Dict) -> "User":
        role = Role(data["role"])
        return User(
            id=data["id"],
            name=data["name"],
            email=data["email"],
            password_hash=data["password_hash"],
            role=role,
        )