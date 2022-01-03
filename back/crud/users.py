from typing import Sequence, Optional

from .base import BaseCRUD
from back.db.schemes import users
from back.models.users import UserOutput


class UsersCRUD(BaseCRUD):
    async def create(self, user_data: dict) -> int:
        query = users.insert().values(**user_data)
        return await self.database.execute(query)

    async def get_by_id(self, user_id: int):
        pass 

    async def get_by_email(self, email: str) -> Optional[UserOutput]:
        query = users.select().where(users.c.email==email)
        return UserOutput.parse_obj(data) if (data := await self.database.fetch_one(query)) else None

    async def update(self, user_id: int,
                update_data: dict
            ):
        pass