from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from back.models import User
from back.schemas.users import UserIn, UserOutput


class UsersCRUD:
    @staticmethod
    async def create_or_update(db: AsyncSession, user_in: UserIn) -> int:
        """Обновление или создание новых данных
        """
        result = await db.execute(select(User).where(User.id==user_in.id))
        user = result.scalars().first()
        if not user:
            user = User(**user_in.dict())

        user.update(**user_in.dict())
        db.add(user)
        return user.id

    @staticmethod
    async def get(db: AsyncSession, user_id: int) -> UserOutput:
        pass
