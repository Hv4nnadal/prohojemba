from typing import List, Optional
from sqlalchemy import select

from .base import BaseCRUD
from back.db.schemes import walks, users, titles
from back.models.users import UserPreview
from back.models.titles import TitlePreview
from back.models.walks import WalkWithUserInfo, WalkWithTitleInfo, WalkBase


class WalksCRUD(BaseCRUD):
    async def _update_title_rate(self, title_id: int, current_rate: Optional[bool], new_rate: Optional[bool]):
        if current_rate == new_rate:
            return

        query = titles.select().where(titles.c.id == title_id)
        title = TitlePreview.parse_obj(await self.database.fetch_one(query))

        if current_rate is None and new_rate is True:
            update = {
                "positive_rates_count": title.positive_rates_count + 1
            }
        elif current_rate is None and new_rate is False:
            update = {
                "negative_rates_count": title.negative_rates_count + 1
            }
        elif current_rate is True and new_rate is None:
            update = {
                "positive_rates_count": title.positive_rates_count - 1
            }
        elif current_rate is False and new_rate is None:
            update = {
                "negative_rates_count": title.negative_rates_count - 1
            }
        elif current_rate is False and new_rate is True:
            update = {
                "negative_rates_count": title.negative_rates_count - 1,
                "positive_rates_count": title.positive_rates_count + 1
            }
        elif current_rate is True and new_rate is False:
            update = {
                "negative_rates_count": title.negative_rates_count + 1,
                "positive_rates_count": title.positive_rates_count - 1
            }

        query = titles.update().where(titles.c.id == title_id).values(**update)
        await self.database.execute(query)

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

    async def select(self, walk_id: int) -> Optional[WalkBase]:
        query = walks.select().where(walks.c.id == walk_id)
        return WalkBase.parse_obj(data) if (data := await self.database.fetch_one(query)) else None

    async def create(self, walk_data: dict) -> int:
        await self._update_title_rate(walk_data["title_id"], None, walk_data["rate"])
        query = walks.insert().values(**walk_data)
        return await self.database.execute(query)

    async def update(self, walk_id: int, walk_data: dict):
        current_walk = await self.select(walk_id)
        if not current_walk:
            return

        await self._update_title_rate(current_walk.title_id, current_walk.rate, walk_data["rate"])
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
            walks.join(titles, titles.c.id == walks.c.title_id)
        ]).where(walks.c.user_id == user_id)
        return [self._parse_walk_result_with_title(d) for d in await self.database.fetch_all(query)]

    async def delete(self, walk_id: int):
        current_walk = await self.select(walk_id)
        if not current_walk:
            return

        await self._update_title_rate(current_walk.title_id, current_walk.rate, None)
        query = walks.delete().where(walks.c.id == walk_id)
        await self.database.execute(query)
