async def create_all_tables():
    """Создание таблиц в БД по моделям приложения
    """
    from back.common.db import engine, Base
    from back.models import User, Title, Walk
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
