from sqlalchemy import Integer, String
from sqlalchemy.sql.schema import Column
from database import Base


class Notes(Base):
    __tablename__ = "notes"
    id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False)
    description = Column(String, nullable=False)
    url = Column(String, nullable=True)

