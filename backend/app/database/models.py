from sqlalchemy import Column, Integer, String, Boolean, DateTime, BINARY, LargeBinary, BIGINT
from database.config import Base
from datetime import datetime


class Notes(Base):
    __tablename__ = "Notes"
    id = Column(BIGINT, primary_key=True)
    title = Column(String, nullable=True)
    description = Column(String, nullable=True)
    check_in = Column(Boolean, nullable=True)
    # profile_photo = Column(LargeBinary, nullable=True)
    # image = Column(LargeBinary, nullable=True)
    created_at = Column(DateTime, default=datetime.utcnow)


class ClientData(Base):
    __tablename__ = "FacebookClientData"
    # id = Column(String, nullable=True)
    name = Column(String, nullable=True)
    email = Column(String, primary_key=True)
    access_token = Column(String, nullable=True)
