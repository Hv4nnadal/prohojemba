from typing import List, Optional
from sqlalchemy import select

from .base import BaseCRUD
from back.db.schemes import walks, users, titles
from back.models.users import UserPreview
from back.models.titles import TitlePreview
from back.models.walks import WalkWithUserInfo, WalkWithTitleInfo


class WalksCRUD(BaseCRUD):
    async def _update_title_rate(self, title_id: int, rate: Optional[bool]):
        pass

    @staticmethod
    def _parse_walk_result_with_user(data) -> WalkWithUserInfo:
        user = UserPreview.parse_obj(data)
        walk = WalkWithUserInfo.parse_obj(data)
        walk.user = user
        return walk

    @staticmethod
    def _parse_walk_result_with_title(data) -> WalkWithTitleInfo:
        title = TitlePreview.parse_obj(data)
        walk = WalkWithTitleInfo.parse_obj(data)
        walk.title = title
        return walk

    async def create(self, walk_data: dict) -> int:
        query = walks.insert().values(**walk_data)
        return await self.database.execute(query)

    async def update(self, walk_id: int, walk_data: dict):
        query = walks.update().where(walks.c.id == walk_id).values(**walk_data)
        await self.database.execute(query)

    async def get_by_title_id(self, title_id: int) -> List[WalkWithUserInfo]:
        query = select([walks, users.c.id, users.c.username, users.c.avatar], from_obj=[
            walks.join(users, users.c.id == walks.c.user_id)
        ]).where(walks.c.title_id == title_id)
        return [self._parse_walk_result_with_user(d) for d in await self.database.fetch_all(query)]

    async def get_by_user_id(self, user_id: int):
        query = select([walks, titles.c.id, titles.c.name, titles.c.cover,
                        titles.c.type, titles.c.release_year,
                        titles.c.positive_rates_count, titles.c.negative_rates_count], from_obj=[
            walks.join(users, users.c.id == walks.c.user_id)
        ]).where(walks.c.user_id == user_id)
        return [self._parse_walk_result_with_title(d) for d in await self.database.fetch_all(query)]

    async def delete(self, walk_id: int):
        query = walks.delete().where(walks.c.id == walk_id)
        await self.database.execute(query)