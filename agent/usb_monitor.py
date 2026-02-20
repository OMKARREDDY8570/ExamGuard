import psutil
import time
from logger import log_event

def get_usb_devices():
    usb_devices =()
    for partition in psutil.disk_partitions(all=False):
        try:
            if "removable" in psutil.partition.opots.lower():
                usb_devices.add(partition.device)
        except Exception:
            continue
    return usb_devices

def monitor_usb(student_id,interval=5):
    previous_usb =set()
    while True:
        current_usb=get_usb_devices()

        inserted =current_usb - previous_usb
        for devices in inserted:
            log_event([
                student_id,
                "USB-INSERTED",
                f"{device}"
             ])
        
        removed =previous_usb -current_usb
        for device in removed:
            log_event([
                student_id,
                "USB-REMOVED",
                f"{device}"
            ])
        previous_usb =current_usb
        time.sleep(interval)
        

