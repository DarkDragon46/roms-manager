import psutil
import os 

class USBService:
    def get_usb_devices(self, os):
        
        drives = []
        match os:
            case "Windows":
                partitions = psutil.disk_partitions()
                for partition in partitions:
                    if 'removable' in partition.opts:
                        drives.append(partition.device)
                return drives
            
            case "Linux":
                return drives
            
            case "Mac":
                return drives

    def getDrive(self, MountDriveBox):
        return MountDriveBox.currentText()

    def loadUSB(self, drive):
        # load drive information here
        os.walk(drive)
        root = os.listdir(drive)
        found_roms_folder = False
        for i in root:
            if root[i] == "roms":
                #if roms folder exists go inside
                found_roms_folder = True
        if found_roms_folder == False:
            os.mkdir('roms')
            
        