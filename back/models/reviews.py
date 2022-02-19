from sqlalchemy import Column, Integer, ForeignKey, String, Boolean, UniqueConstraint
from sqlalchemy.orm import relationship

from back.common.db import Base


class Review(Base):
    __tablename__ = "reviews"
    id = Column("id", Integer, primary_key=True, autoincrement=True)
    user_id = Column("user_id", Integer, ForeignKey("users.id", ondelete="CASCADE"))
    title_id = Column("title_id", Integer, ForeignKey("titles.id", ondelete="CASCADE"))
    text = Column("text", String(512))
    rating = Column("rating", Boolean, nullable=False)

    __table_args__ = (UniqueConstraint("user_id", "title_id", name="review_user_title_uc"),)
    
    user = relationship("User", uselist=False)
    title = relationship("Title", uselist=False)

