from sqlalchemy.ext.asyncio import AsyncSession

from back.models import User
from back.schemas.users import UserIn, UserOutput


class UsersCRUD:
    @staticmethod
    async def create_or_update(db: AsyncSession, user_in: UserIn) -> int:
        """Обновление или создание новых данных
        """
        print(db)
        user = User(
            discord_id=user_in.discord_id, username=user_in.username,
            avatar=f"https://cdn.discordapp.com/avatars/{user_in.discord_id}/{user_in.avatar}.webp",
            discriminator=user_in.discriminator
        )
        print(user.avatar)
        db.add(user)
        await db.commit()
        return user.id

    @staticmethod
    async def get(db: AsyncSession, user_id: int) -> UserOutput:
        pass
