from .base import BaseCRUD


class WalksCRUD(BaseCRUD):
    async def create(self, walk_data: dict) -> int:
        pass

    async def update(self, walk_id: int, walk_data: dict):
        pass

    async def get_by_title_id(self, title_id: int):
        pass

    async def get_by_user_id(self, user_id: int):
        pass

    async def delete(self, walk_id: int):
        pass
