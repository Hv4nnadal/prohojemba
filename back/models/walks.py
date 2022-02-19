from sqlalchemy import Column, Integer, ForeignKey, String, UniqueConstraint
from sqlalchemy.orm import relationship

from back.common.db import Base


class Walk(Base):
    __tablename__ = "walks"
    id = Column("id", Integer, autoincrement=True, primary_key=True)
    user_id = Column("user_id", Integer, ForeignKey("users.id", ondelete="CASCADE"))
    title_id = Column("title_id", Integer, ForeignKey("titles.id", ondelete="CASCADE"))
    state = Column("state", String(32), nullable=False)

    __table_args__ = (UniqueConstraint("user_id", "title_id", name="user_title_uc"),)

    user = relationship("User")
    title = relationship("Title")