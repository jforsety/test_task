import uvicorn
from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session


import schemas, database
from database import engine, get_db
from models import Base
from schemas import TaskResponse

Base.metadata.create_all(bind=engine)

app = FastAPI()

@app.get("/tasks")
async def request_task(db: Session = Depends(get_db)):
    return database.request_task(db=db)

@app.post("/create_tasks", response_model=TaskResponse)
async def create_task(request: schemas.TaskCreate, db: Session = Depends(get_db)):
    return database.create_task(db=db, request=request)

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)