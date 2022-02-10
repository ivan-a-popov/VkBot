import typing
from hashlib import sha256
from typing import Optional

from app.base.base_accessor import BaseAccessor
from app.admin.models import Admin

if typing.TYPE_CHECKING:
    from app.web.app import Application


class AdminAccessor(BaseAccessor):
    async def connect(self, app: "Application"):
        email = app.config.admin.email
        password = app.config.admin.password
        await self.create_admin(email, password)

    async def get_by_email(self, email: str) -> Optional[Admin]:
        for each in self.app.database.admins:
            if each.email == email:
                admin = each
                return admin
            return None

    async def create_admin(self, email: str, password: str) -> Admin:
        hashed_password = sha256(password.encode()).hexdigest()
        admin = Admin(id=self.app.database.next_admins_id, email=email, password=hashed_password)
        self.app.database.admins.append(admin)
        return admin
