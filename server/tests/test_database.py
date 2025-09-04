import pytest
from datetime import datetime
from sqlalchemy import create_engine
from sqlalchemy.orm import Session

from server.src.models import Base, Task


@pytest.fixture(scope="function")
def engine():
    # Создаем движок для временной БД в памяти
    engine = create_engine("sqlite:///:memory:", echo=False)
    Base.metadata.create_all(engine)
    yield engine
    Base.metadata.drop_all(engine)


@pytest.fixture
def session(engine):
    # Создаем сессию для тестов
    connection = engine.connect()
    transaction = connection.begin()
    session = Session(bind=connection)
    yield session
    session.close()
    transaction.rollback()
    connection.close()


def test_task_creation(session):
    # Тест создания записи без явного указания created_at
    task = Task(
        text="Test task",
        current_data="2023-01-01",
        current_time="12:00",
        number_clicked=5
    )

    session.add(task)
    session.commit()

    assert task.id is not None
    assert task.text == "Test task"
    assert task.number_clicked == 5
    assert isinstance(task.created_at, datetime)


def test_task_default_values(session):
    # Тест значений по умолчанию
    task = Task()
    session.add(task)
    session.commit()

    assert task.number_clicked is None
    assert task.text is None
    assert task.current_data is None
    assert task.current_time is None
    assert task.created_at is not None


def test_task_created_at_auto_generated(session):
    # Тест автоматического заполнения created_at
    before_creation = datetime.now()
    task = Task(text="Test")
    session.add(task)
    session.commit()

    assert task.created_at is not None
    assert before_creation <= task.created_at <= datetime.now()


def test_task_string_fields(session):
    # Тест строковых полей
    task = Task(
        text="Hello",
        current_data="2023-01-01",
        current_time="23:59:59"
    )

    assert task.text == "Hello"
    assert task.current_data == "2023-01-01"
    assert task.current_time == "23:59:59"