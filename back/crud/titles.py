from typing import List, Optional

from .base import BaseCRUD
from back.db.schemes import titles
from back.models.titles import TitlePreview, TitleInfo


class TitlesCRUD(BaseCRUD):
    async def all(self, page: int) -> Optional[List[TitlePreview]]:
        query = titles.select().limit(10).offset((page-1)*10)
        return [TitlePreview.parse_obj(data) for data in await self.database.fetch_all(query)]

    async def get_by_id(self, title_id: int) -> Optional[TitleInfo]:
        query = titles.select().where(titles.c.id == title_id)
        return TitleInfo.parse_obj(data) if (data := await self.database.fetch_one(query)) else None

    async def create(self, title_data: dict) -> int:
        title_data["positive_rates_count"] = 0
        title_data["negative_rates_count"] = 0
        query = titles.insert().values(**title_data)
        return await self.database.execute(query)

    async def update(self, title_id: int, title_data: dict):
        query = titles.update().where(titles.c.id == title_id).values(**title_data)
        await self.database.execute(query)

    async def delete(self, title_id: int):
        query = titles.delete().where(titles.c.id == title_id)
        await self.database.execute(query)