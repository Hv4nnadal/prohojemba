from typing import List, Optional
from sqlalchemy import select

from .base import BaseCRUD
from back.db.schemes import walks, users, titles
from back.models.walks import WalkWithUserInfo, WalkWithTitleInfo


class WalksCRUD(BaseCRUD):
    async def _update_title_rate(self, title_id: int, rate: Optional[bool]):
        pass

    async def create(self, walk_data: dict) -> int:
        query = walks.insert().values(**walk_data)
        return await self.database.execute(query)

    async def update(self, walk_id: int, walk_data: dict):
        query = walks.update().where(walks.c.id == walk_id).values(**walk_data)
        await self.database.execute(query)

    async def get_by_title_id(self, title_id: int) -> List[WalkWithUserInfo]:
        query = walks.select().join(users, users.c.id == walks.c.user_id).\
            where(walks.c.title_id == title_id)
        data = await self.database.fetch_all(query)
        print(data)
        return [WalkWithUserInfo.parse_obj(d) for d in data]

    async def get_by_user_id(self, user_id: int):
        query = walks.select().join(titles, titles.c.id == walks.c.title_id). \
            where(walks.c.user_id == user_id)
        data = await self.database.fetch_all(query)
        print(data)
        return [WalkWithUserInfo.parse_obj(d) for d in data]

    async def delete(self, walk_id: int):
        query = walks.delete().where(walks.c.id == walk_id)
        await self.database.execute(query)