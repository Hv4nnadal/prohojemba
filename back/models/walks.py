from datetime import date
from sqlalchemy import Column, Integer, ForeignKey, String, Boolean, Date, DateTime

from back.common.db import Base


class Walk(Base):
    __tablename__ = "walks"
    id = Column("id", Integer, autoincrement=True, primary_key=True)
    user_id = Column("user_id", Integer, ForeignKey("users.id", ondelete="CASCADE"))
    title_id = Column("title_id", Integer, ForeignKey("titles.id", ondelete="CASCADE"))
    state = Column("state", String(32), nullable=False)
    comment = Column("comment", String(1024))
    rate = Column("rate", Boolean, nullable=True)