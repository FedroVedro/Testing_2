from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout, QLineEdit, QPushButton, QMessageBox
from PySide6.QtGui import QKeyEvent
import sys
import re

class MyWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Textbox и Button с ограниченным вводом")

        # Создаем компоненты
        self.textbox1 = QLineEdit(self)
        self.textbox2 = QLineEdit(self)
        self.button = QPushButton("Копировать текст", self)

        # Создаем компоновку
        layout = QVBoxLayout(self)
        layout.addWidget(self.textbox1)
        layout.addWidget(self.button)
        layout.addWidget(self.textbox2)

        # Привязываем действия
        self.textbox1.textChanged.connect(self.validate_input)
        self.button.clicked.connect(self.copy_text)

    def validate_input(self):
        text = self.textbox1.text()
        valid_text = re.sub(r'[^a-z]', '', text)  # Удаляем все символы, кроме латинских букв нижнего регистра
        if text != valid_text:
            self.textbox1.setText(valid_text)

    def copy_text(self):
        text = self.textbox1.text()
        if text:
            self.textbox2.setText(text)
        else:
            QMessageBox.warning(self, "Предупреждение", "Textbox1 пуст!")


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = MyWindow()
    window.show()

    sys.exit(app.exec())
