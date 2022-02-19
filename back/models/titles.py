from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from back.common.db import Base


class Title(Base):
    __tablename__ = "titles"
    id = Column("id", Integer, primary_key=True)
    name = Column("name", String(128), nullable=False)
    cover = Column("cover", String(128))
    description = Column("description", String(1024))
    type = Column("type", String(32), nullable=False)
    release_year = Column("release_year", Integer)

    current_user_review = relationship("Review", uselist=False)
    current_user_walk = relationship("Walk", uselist=False)