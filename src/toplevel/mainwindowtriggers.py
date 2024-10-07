import psutil
import ui.mainwindow

class triggers(object):

    def refreshDrives(self, mountDriveComboBox, os):
        mountDriveComboBox.clear()
        #dependancy injection is applicable?
    
    def refreshUSBDevices(self, combo, os):
        combo.clear()
        drives = self.checkUSBDevices(os)
        combo.addItems(drives)
        
        