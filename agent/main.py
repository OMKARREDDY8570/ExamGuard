from consent import get_user_consent as permission,get_roll_number
from logger import init_logger,log_event
from process_monitor import monitor_processes
from config_loader import load_config
from window_monitor import monitor_window_focus
#from get_rollno import get_roll_number
import threading

if not permission():
    print("User declined permission")
    exit()

STUDENT_ID =get_roll_number()

init_logger()
log_event(STUDENT_ID, "SYSTEM", "ExamGuard started")

config =load_config()
process_interval =config["process_interval"]

process_thread =threading.Thread(target =monitor_processes,args =(STUDENT_ID,process_interval), daemon =True)
process_thread.start()

window_thread =threading.Thread(target=monitor_window_focus,args=(STUDENT_ID,config), daemon =True)
window_thread.start()

print("ExamGuard running.....")
input("press enter to exit")