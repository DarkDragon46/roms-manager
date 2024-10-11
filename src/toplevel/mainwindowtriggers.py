from src.logic.usb_service import USBService
from src.logic.messagebox_service import MessageBoxService

class MainWindowTriggers:
    def __init__(self, usb_service: USBService, messagebox_service: MessageBoxService, parent=None):
        self.usb_service = usb_service
        self.messagebox_service = messagebox_service
        self.parent = parent

    def getMountedDrives(self, os):
        drives = self.usb_service.get_usb_devices(os)
        return drives

    def refreshMountedDrives(self, combo, os):
        combo.clear()
        drives = self.usb_service.get_usb_devices(os)
        combo.addItems(drives)
    
    def showAboutMessagebox(self):
        return self.messagebox_service.aboutBox(self.parent)