from sqlalchemy import Column, Integer, String

from back.common.db import Base


class Title(Base):
    __tablename__ = "titles"
    id = Column("id", Integer, autoincrement=True, primary_key=True)
    name = Column("name", String(128), nullable=False)
    cover = Column("cover", String(128))
    description = Column("description", String(1024))
    type = Column("type", String(32), nullable=False)
    release_year = Column("release_year", Integer)

    positive_rates_count = Column("positive_rates_count", Integer, default=0)
    negative_rates_count = Column("negative_rates_count", Integer, default=0)
