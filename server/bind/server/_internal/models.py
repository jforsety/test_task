from datetime import datetime

from sqlalchemy import Column, String, Integer, DateTime
from sqlalchemy.orm import DeclarativeBase


class Base(DeclarativeBase):
    pass

class Task(Base):
    __tablename__ = "tasks"

    id = Column(Integer, primary_key=True, index=True)
    text = Column(String)
    current_data = Column(String)
    current_time = Column(String)
    number_clicked = Column(Integer)
    created_at = Column(DateTime, default=datetime.now)
