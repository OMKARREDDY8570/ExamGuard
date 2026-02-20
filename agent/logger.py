import os
import csv
from datetime import datetime

LOG_FILE =os.path.join("reports","exam_logs.csv")

def init_logger():
    os.makedirs("reports",exist_ok=True)

    if not os.path.exists(LOG_FILE):
        with open(LOG_FILE, mode="w")as file:
            writer =csv.writer(file)
            writer.writerow([
                " timestamp ",
                " student_id ",
                " event_type ",
                " details "
             ])
            

def log_event(student_id, event_type, details):
    timestamp =datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(LOG_FILE, mode="a",newline="", encoding ="utf-8")as file:
        writer =csv.writer(file)
        writer.writerow([
            timestamp,
            student_id,
            event_type,
            details
              ])

