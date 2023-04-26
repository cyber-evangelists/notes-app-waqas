from sqlalchemy import Column, Integer, String, Boolean, LargeBinary, DateTime, BINARY
from database.config import Base
from datetime import datetime
from typing import Union


class Notes(Base):
    __tablename__ = "Notes"
    id = Column(Integer, primary_key=True, index=True)
    title = Union[int, float, str, bool]
    description = Column(String, nullable=True)
    check_in = Column(Boolean, nullable=True)
    # profile_photo = Column(BINARY, nullable=True)
    # image = Column(LargeBinary, nullable=True)
    created_at = Column(DateTime, default=datetime.utcnow)


class Users(Base):
    __tablename__ = "Users"
    id = Column(Integer, primary_key = True)
    access_token = Column(String)
    