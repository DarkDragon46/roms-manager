import psutil

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
