import sys
from PyQt6 import QtWidgets
from ui.mainwindow import Ui_MainWindow
from src.toplevel.mainwindowtriggers import triggers
from src.logic.usb_service import USBService
import platform

class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        QtWidgets.QMainWindow.__init__(self, parent)
        self.setupUi(self)
        global os
        os = platform.system()


        # Create a USBService instance
        usb_service = USBService()

        # add triggers to main window widgets
        self.trigger_instance = triggers(usb_service)
        
        #fill combobox with drives
        self.MountDriveBox.addItems(self.trigger_instance.getMountedDrives(os))

        #check drives on buttonclick
        self.refreshDrivesBtn.clicked.connect(lambda: self.trigger_instance.refreshMountedDrives(self.MountDriveBox, os))

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())