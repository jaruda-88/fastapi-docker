from sqlalchemy import Column, Integer, String
from databases.base_class import Base

class User(Base):
    __tablename__ = "users"

    username = Column(String(100), nullable=True) 