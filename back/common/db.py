# Настройка подключения к базе данных
from sqlalchemy.orm import declarative_base, sessionmaker
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine

from back.core import config

Base = declarative_base()
engine = create_async_engine(config.DATABASE_URI, echo=True if config.DEBUG else False)
Session = sessionmaker(bind=engine, class_=AsyncSession)