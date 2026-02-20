import psutil
import time
from logger import log_event



def load_blocked_apps():
    with open("config/blocked_apps.txt","r")as file:
        return [line.strip().lower() for line in file if line.strip()]
    
def monitor_processes(student_id,interval):
    blocked_apps =load_blocked_apps()
    detected =set()
    i=0

    while True:
        for proc in psutil.process_iter(['name']):
            try:
                process_name=proc.info['name']
                if process_name and process_name.lower() in blocked_apps and process_name.lower() not in detected:
                    
                    detected.add(process_name.lower())
                    log_event(
                        student_id,
                        "using blocked_app",
                        f"{process_name} detected"
                    )
                        
            except(psutil.NoSuchProcess,psutil.AccessDenied):
                continue
        time.sleep(interval)
        detected.clear()
