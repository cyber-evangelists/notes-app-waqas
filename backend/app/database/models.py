from sqlalchemy import Column, Integer, String, Boolean, DateTime, BINARY, BIGINT
from database.config import Base
from datetime import datetime


class Notes(Base):
    __tablename__ = "Notes"
    id = Column(BIGINT, primary_key=True)
    title = Column(String, nullable=True)
    description = Column(String, nullable=True)
    check_in = Column(Boolean)
    # image = Column(BINARY, nullable = True)
    created_at = Column(DateTime, default=datetime.utcnow)


class ClientData(Base):
    __tablename__ = "FacebookClientData"
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=True)
    email = Column(String, nullable=True)
    access_token = Column(String, nullable=False)


class MyUser(Base):
    __tablename__ = "MyUserss"
    id = Column(Integer, primary_key = True)
    username = Column(String, unique = True, nullable = True)
    email = Column(String, unique = True)
    password = Column(String)
    otp = Column(Integer, nullable = True)
    verified = Column(Boolean, nullable = True)
    