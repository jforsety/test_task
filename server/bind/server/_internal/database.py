from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session

import models, schemas

# строка подключения
SQLALCHEMY_DATABASE_URL = "sqlite:///./tasks.db"

# создаем движок SqlAlchemy
engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

def create_task(db: Session, request: schemas.TaskCreate) -> models.Task:
    db_request = models.Task(
        text=request.text,
        current_data=request.current_data,
        current_time=request.current_time,
        number_clicked=request.number_clicked
    )
    db.add(db_request)
    db.commit()
    db.refresh(db_request)
    return db_request

def request_task(db: Session):
    result_get = db.query(models.Task).filter_by(id=models.Task.id, text=models.Task.text).all()
    return result_get