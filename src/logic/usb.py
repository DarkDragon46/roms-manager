import psutil

class USBDrive:
    def getUSBDevices():
        drives = []
        #partition checker only works on windows?
        partitions = psutil.disk_partitions()
        print(partitions)
        for partition in partitions:
            if 'removable' in partition.opts:
                drives.append(partition.device)
        return drives
    