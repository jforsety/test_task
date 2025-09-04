from pydantic import BaseModel
from datetime import datetime

class TaskCreate(BaseModel):
    text: str
    current_data: str
    current_time: str
    number_clicked: int

class TaskResponse(BaseModel):
    id: int
    text: str
    current_data: str
    current_time: str
    number_clicked: int
    created_at: datetime

    class Config:
        orm_mode = True
