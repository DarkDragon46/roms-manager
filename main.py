import sys
from PyQt6 import QtWidgets
from PyQt6.QtWidgets import QMessageBox
from ui.mainwindow import Ui_MainWindow
from src.toplevel.mainwindowtriggers import MainWindowTriggers
from src.logic.usb_service import USBService
from src.logic.messagebox_service import MessageBoxService
import platform

class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        QtWidgets.QMainWindow.__init__(self, parent)
        self.setupUi(self)

        global os
        os = platform.system()


        # Create a USBService instance
        usb_service = USBService()
        messagebox_service = MessageBoxService()

        # add triggers to main window widgets
        self.mainwindow_trigger_instance = MainWindowTriggers(usb_service, messagebox_service)

        #fill combobox with drives
        self.MountDriveBox.addItems(self.mainwindow_trigger_instance.getMountedDrives(os))

        #check drives on buttonclick
        self.refreshDrivesBtn.clicked.connect(lambda: self.mainwindow_trigger_instance.refreshMountedDrives(self.MountDriveBox, os))

        self.actionAbout.triggered.connect(self.mainwindow_trigger_instance.showAboutMessagebox)
        
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())