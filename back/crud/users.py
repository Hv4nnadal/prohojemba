from typing import Optional
from sqlite3 import IntegrityError
from fastapi import status
from fastapi.exceptions import HTTPException

from .base import BaseCRUD
from back.db.schemes import users
from back.models.users import UserOutput


class UsersCRUD(BaseCRUD):
    async def create(self, user_data: dict) -> int:
        query = users.insert().values(**user_data)
        try:
            return await self.database.execute(query)
        except IntegrityError as e:
            raise HTTPException(
                status_code=status.HTTP_409_CONFLICT,
                detail=str(e)
            )

    async def get_by_id(self, user_id: int) -> Optional[UserOutput]:
        query = users.select().where(users.c.id == user_id)
        return UserOutput.parse_obj(data) if (data := await self.database.fetch_one(query)) else None

    async def get_by_email(self, email: str) -> Optional[UserOutput]:
        query = users.select().where(users.c.email == email)
        return UserOutput.parse_obj(data) if (data := await self.database.fetch_one(query)) else None

    async def update(self, user_id: int,
                     update_data: dict
                     ):
        query = users.update().where(users.c.id == user_id).values(**update_data)
        await self.database.execute(query)
