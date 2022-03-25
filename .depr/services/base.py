from sqlalchemy.ext.asyncio import AsyncSession

class BaseService:
    def __init__(self, db_session: AsyncSession) -> None:
        self.db_session: AsyncSession = db_session
        