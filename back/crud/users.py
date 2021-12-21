from typing import Sequence, Optional

from .base import BaseCRUD
from back.models import auth, users


class UsersCRUD(BaseCRUD):
    async def create(self, user_data: auth.SignInModel) -> None:
        pass

    async def get_by_id(self, user_id: int) -> Optional[users.UserOutput]:
        pass 

    async def get_by_email(self, email: str) -> Optional[users.UserOutput]:
        pass

    async def update(self, user_id: int,
                update_data: dict
            ):
        pass