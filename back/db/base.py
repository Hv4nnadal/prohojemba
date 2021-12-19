from databases import Database
from sqlalchemy import create_engine, MetaData

from back import settings

engine = create_engine(url=settings.DATABASE_URI)
metadata = MetaData(bind=engine)
database = Database(url=settings.DATABASE_URI)