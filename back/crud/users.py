from typing import Sequence, Optional

from .base import BaseCRUD
from back.db.schemes import users


class UsersCRUD(BaseCRUD):
    async def create(self, user_data: dict) -> None:
        query = users.insert().values(**user_data)
        await self.database.execute(query)

    async def get_by_id(self, user_id: int):
        pass 

    async def get_by_email(self, email: str):
        pass

    async def update(self, user_id: int,
                update_data: dict
            ):
        pass