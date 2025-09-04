import sys
from datetime import date, time, datetime

import requests
from PySide6.QtCore import QStringListModel
from PySide6.QtWidgets import QApplication, QMainWindow, QMessageBox

from test_tasks_ui import Ui_MainWindow


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        # Счетчик кликов
        self.click_counter = 0

        # Пагинация
        self.pagination_get = 10

        # Кнопки к обработчикам
        self.postButton.clicked.connect(self.handle_post)
        self.getButton.clicked.connect(self.handle_get)

        # Модель данных для списка
        self.model = QStringListModel()
        self.listView.setModel(self.model)

    def handle_post(self):
        """Обработчик для кнопки отправки"""
        self.click_counter += 1
        text = self.lineEdit.text().strip()

        current_data = date.today()
        current_date_time = datetime.now()
        current_time = current_date_time.time()

        if not text:
            self.show_message("Ошибка", "Поле ввода пустое!")
            return

        try:
            response = requests.post(
                "http://127.0.0.1:8000/create_tasks",
                json={"text": text, "current_data": str(current_data), "current_time": str(current_time), "number_clicked": int(self.click_counter)}
            )
            response.raise_for_status()
            self.show_message("Успех", "Данные отправлены!")
            self.lineEdit.clear()

        except Exception as e:
            self.show_message("Ошибка", f"Ошибка отправки: {str(e)}")

    def handle_get(self):
        """Обработчик для кнопки получения данных"""
        try:
            response = requests.get(
                "http://127.0.0.1:8000/tasks"
            )
            response.raise_for_status()
            data = response.json()
            task_strings = []

            for item in data[:self.pagination_get]:
                task_str = (
                    f"ID: {item['id']} | "
                    f"Текст: {item['text']} | "
                    f"Дата: {item['current_data']} | "
                    f"Время: {item['current_time']} | "
                    f"Кликов: {item['number_clicked']} | "
                    f"Создано: {item['created_at']}"
                )
                task_strings.append(task_str)
            self.model.setStringList(task_strings)
            if len(data) < self.pagination_get:
                self.show_message("Инфо", "Данные закончились!")
                return
            else:
                self.pagination_get += 10
        except Exception as e:
            self.show_message("Ошибка", f"Ошибка получения данных: {str(e)}")

    def show_message(self, title, message):
        """Вспомогательный метод для показа сообщений"""
        msg = QMessageBox(self)
        msg.setWindowTitle(title)
        msg.setText(message)
        msg.exec()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())