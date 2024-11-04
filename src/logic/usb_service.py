import psutil
import os 
from .enums.enums import Console
from pathlib import Path

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
        root = os.listdir(drive)

        found_roms_folder = False

        for folder in root:
            if folder == "roms":
                os.chdir(folder)
                #if roms folder exists go inside
                found_roms_folder = True
                print(Path(folder).resolve())
                return 
        if found_roms_folder == False:
           return self.createFolderStructure(drive)
    
    def createFolderStructure(self, drive):
        main_folder = 'roms'
        main_folder_path = os.path.join(drive, main_folder)
        os.mkdir(main_folder_path)
        for console in Console:
            console_folder_name = str(console.value)
            console_path = os.path.join(main_folder_path, console_folder_name)
            os.mkdir(console_path)
        return main_folder

    def loadContent(self, roms_folder):
        for root in os.walk(roms_folder):
            print(root)