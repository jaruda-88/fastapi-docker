from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from databases.base_class import Base

class Item(Base):
    __tablename__ = "items"

    description = Column(String(100), nullable=True)
    user_id = Column(Integer, ForeignKey("users.id"))

    users = relationship("User", back_populates='items')