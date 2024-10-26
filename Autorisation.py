import sys
from PySide6.QtWidgets import (
    QApplication, QMainWindow, QWidget, QVBoxLayout,
    QLineEdit, QPushButton, QLabel, QMessageBox
)
from sqlalchemy.orm import Session
from Orm_models import SessionLocal, User
class AuthApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Кафе - Вход и Регистрация")
        self.setGeometry(100, 100, 300, 200)

        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)

        self.layout = QVBoxLayout(self.central_widget)

        self.label = QLabel("Выберите действие:")
        self.layout.addWidget(self.label)

        self.username_input = QLineEdit()
        self.username_input.setPlaceholderText("Имя пользователя")
        self.layout.addWidget(self.username_input)

        self.password_input = QLineEdit()
        self.password_input.setPlaceholderText("Пароль")
        self.password_input.setEchoMode(QLineEdit.Password)
        self.layout.addWidget(self.password_input)

        self.login_button = QPushButton("Войти")
        self.login_button.clicked.connect(self.login)
        self.layout.addWidget(self.login_button)

        self.register_button = QPushButton("Регистрация")
        self.register_button.clicked.connect(self.register)
        self.layout.addWidget(self.register_button)

        self.users = {}  

    def login(self):
        username = self.username_input.text()
        password = self.password_input.text()

        if username in self.users and self.users[username] == password:
            QMessageBox.information(self, "Успех", "Вы успешно авторизовались")
        else:
            QMessageBox.warning(self, "Ошибка", "Неверное имя пользователя или пароль.")

    def register(self):
        username = self.username_input.text()
        password = self.password_input.text()

        if username in self.users:
            QMessageBox.warning(self, "Ошибка", "Пользователь уже существует.")
        else:
            self.users[username] = password
            QMessageBox.information(self, "Успех", "Регистрация прошла успешно!")
    def add_user(self):
        name = self.name_input.text()
        password = self.password_input.text()
        db: Session = SessionLocal()
        new_user = User(name=name, password=password)
        db.add(new_user)
        db.commit()
        db.refresh(new_user)
        self.result_label.setText(f'added user:{new_user.name}')
        db.close


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = AuthApp()
    window.show()
    sys.exit(app.exec())