from src.logic.usb_service import USBService

class triggers:
    def __init__(self, usb_service: USBService):
        self.usb_service = usb_service

    def getMountedDrives(self, os):
        drives = self.usb_service.get_usb_devices(os)
        return drives

    def refreshMountedDrives(self, combo, os):
        combo.clear()
        drives = self.usb_service.get_usb_devices(os)
        combo.addItems(drives)