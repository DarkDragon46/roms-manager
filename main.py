import sys
from PyQt6 import QtWidgets
from ui.mainwindow import Ui_MainWindow
from src.toplevel.mainwindowtriggers import triggers
import platform

class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)
        # add triggers to main window widgets
        self.trigger_instance = triggers()
        self.testButton.clicked.connect(self.on_button_click)
    
    def on_button_click(self):
        global os_type
        os_type = platform.system()
        self.trigger_instance.testing(os_type)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())