import sys
from PyQt6 import QtWidgets
from ui.mainwindow import Ui_MainWindow
from src.toplevel.mainwindowtriggers import triggers
import platform

class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        QtWidgets.QMainWindow.__init__(self, parent)
        self.setupUi(self)
        global os_type
        os_type = platform.system()

        # add triggers to main window widgets
        self.trigger_instance = triggers()
        #get connected drives
        connected_devices = self.trigger_instance.checkUSBDevices(os_type)
        #fill combobox with drives
        self.MountDriveBox.addItems(connected_devices)

        #check drives on buttonclick
        self.refreshDrivesBtn.clicked.connect(self.trigger_instance.refreshDrives(self.MountDriveBox, os_type))

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())