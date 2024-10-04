import sys
from PyQt6.QtWidgets import QApplication, QWidget, QMessageBox
from ui.login_form import Ui_login_form

class Login(QWidget):
    def __init__(self):
        super().__init__()

        self.ui = Ui_login_form()
        self.ui.setupUi(self)

        self.ui.pushButton.clicked.connect(self.authenticate)

        self.show()

    def authenticate(self):
        email = self.ui.lineEdit.text()
        password = self.ui.lineEdit_2.text()

        if email == 'john@test.com' and password == '123456':
            QMessageBox.information(self, 'Success!', 'You Are logged in.')
        else:
            QMessageBox.critical(self, 'Error', "invalid email or password. Please change.")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    login_window = Login()
    sys.exit(app.exec())

