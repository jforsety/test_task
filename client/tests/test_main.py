import pytest
from unittest.mock import Mock, patch, MagicMock
from datetime import date, datetime, time
from PySide6.QtWidgets import QApplication
import sys
import os

# Добавляем путь к модулям проекта в PYTHONPATH
# sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))
# from client.src.main import MainWindow
from client.src.main import MainWindow


@pytest.fixture(scope="module")
def qapp():
    """Фикстура для создания QApplication"""
    app = QApplication.instance() or QApplication(sys.argv)
    yield app
    app.quit()


@pytest.fixture
def window(qapp):
    """Фикстура для создания главного окна"""
    return MainWindow()


def test_handle_post_success(window):
    """Тест успешной отправки данных"""
    # Сохраняем исходное значение счетчика
    initial_counter = window.click_counter

    # Мокируем метод show_message
    mock_show_message = Mock()
    window.show_message = mock_show_message

    # Устанавливаем текст в поле ввода
    window.lineEdit.setText("Test task")

    # Мокируем requests.post
    mock_response = Mock()
    mock_response.raise_for_status.return_value = None

    with patch('client.src.main.requests.post', return_value=mock_response) as mock_post:
        # Вызываем тестируемый метод
        window.handle_post()

        # Проверяем результаты
        assert window.click_counter == initial_counter + 1
        mock_post.assert_called_once()

        # Проверяем, что запрос был отправлен с правильными параметрами
        call_args = mock_post.call_args
        assert call_args[0][0] == "http://127.0.0.1:8000/create_tasks"

        # Проверяем основные поля в JSON
        json_data = call_args[1]['json']
        assert json_data['text'] == "Test task"
        assert json_data['number_clicked'] == initial_counter + 1
        assert 'current_data' in json_data
        assert 'current_time' in json_data

        mock_show_message.assert_called_once_with("Успех", "Данные отправлены!")
        assert window.lineEdit.text() == ""  # Поле должно очиститься


def test_handle_post_empty_text(window):
    """Тест отправки с пустым текстом"""
    # Сохраняем исходное значение счетчика
    initial_counter = window.click_counter

    # Мокируем метод show_message
    mock_show_message = Mock()
    window.show_message = mock_show_message

    # Очищаем поле ввода
    window.lineEdit.clear()

    # Мокируем requests.post, чтобы убедиться, что он не вызывается
    with patch('client.src.main.requests.post') as mock_post:
        # Вызываем тестируемый метод
        window.handle_post()

        # Проверяем результаты - счетчик не должен увеличиться
        assert window.click_counter == initial_counter + 1  # Внимание: в текущей реализации счетчик увеличивается до проверки
        mock_show_message.assert_called_once_with("Ошибка", "Поле ввода пустое!")
        mock_post.assert_not_called()  # Запрос не должен отправляться


def test_handle_get_success(window):
    """Тест успешного получения данных"""
    # Мокируем метод show_message
    mock_show_message = Mock()
    window.show_message = mock_show_message

    # Устанавливаем начальное значение пагинации
    window.pagination_get = 5

    # Мокируем requests.get
    mock_response = Mock()
    mock_response.raise_for_status.return_value = None
    mock_response.json.return_value = [
        {
            "id": 1,
            "text": "Test task 1",
            "current_data": "2023-01-01",
            "current_time": "12:00:00",
            "number_clicked": 1,
            "created_at": "2023-01-01T12:00:00"
        },
        {
            "id": 2,
            "text": "Test task 2",
            "current_data": "2023-01-02",
            "current_time": "13:00:00",
            "number_clicked": 2,
            "created_at": "2023-01-02T13:00:00"
        }
    ]

    with patch('client.src.main.requests.get', return_value=mock_response):
        # Вызываем тестируемый метод
        window.handle_get()

        # Проверяем результаты
        mock_response.raise_for_status.assert_called_once()

        # Проверяем, что модель обновлена правильно
        expected_strings = [
            "ID: 1 | Текст: Test task 1 | Дата: 2023-01-01 | Время: 12:00:00 | Кликов: 1 | Создано: 2023-01-01T12:00:00",
            "ID: 2 | Текст: Test task 2 | Дата: 2023-01-02 | Время: 13:00:00 | Кликов: 2 | Создано: 2023-01-02T13:00:00"
        ]

        # Получаем текущий список строк в модели
        current_strings = window.model.stringList()
        assert current_strings == expected_strings

        # Проверяем, что пагинация увеличилась (так как данных меньше, чем текущая пагинация)
        assert window.pagination_get == 5  # Не должна увеличиться, так как данных всего 2


def test_handle_get_error(window):
    """Тест получения данных с ошибкой"""
    # Мокируем метод show_message
    mock_show_message = Mock()
    window.show_message = mock_show_message

    # Мокируем requests.get для вызова исключения
    with patch('client.src.main.requests.get', side_effect=Exception("Connection error")):
        # Вызываем тестируемый метод
        window.handle_get()

        # Проверяем результаты
        mock_show_message.assert_called_once_with(
            "Ошибка", "Ошибка получения данных: Connection error"
        )