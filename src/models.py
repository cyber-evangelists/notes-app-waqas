from sqlalchemy import  Column, Integer, String
from config import Base

class Notes(Base):
    __tablename__ ="Notes"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    description = Column(String)