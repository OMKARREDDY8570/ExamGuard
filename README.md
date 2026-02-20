
**🛡️ Exam Guard**

Windows-Based Exam Monitoring & Violation Detection System (Python)

Exam Guard is a lightweight desktop-based exam monitoring system built using Python.

It enforces predefined examination rules by actively monitoring system behavior during an exam session and generating structured violation logs.


 **Features**

. User rule confirmation using GUI dialog

. Roll number validation & re-confirmation workflow

. Real-time background process monitoring

. Active window/tab switch detection

. USB insertion & removal detection

. Multi-threaded monitoring system

. Timestamped structured logging (logs.csv)

. JSON-based rule configuration

. Modular monitoring architecture

** How It Works**

.Displays exam rules and requests confirmation.

.Prompts candidate to enter and confirm roll number.

.Starts monitoring session upon successful validation.

.Concurrent monitoring threads track:

.Unauthorized background applications

.Window/tab switching

.USB device activity

.Violations are recorded with timestamps.

.Logs are saved in structured CSV format for audit review.

**🏗️ Tech Stack**

.Language: Python 3.x

**Libraries Used:**

.threading

.psutil

.pygetwindow

.tkinter

.json

.csv

.datetime

.os

.time

.Platform: Windows OS

**📂 Log Format (Sample):**
Timestamp	Roll Number	Violation Type	Details

2026-02-16 22:50:35,587gh856,SYSTEM,ExamGuard started

2026-02-16 22:50:35,587gh856,WINDOW_OK,Exam window active: CODE TANTRA - Notepad

2026-02-16 22:50:35,587gh856,using blocked_app,AnyDesk.exe detected

2026-02-16 22:50:35,587gh856,using blocked_app,Code.exe detected

2026-02-16 22:50:41,587gh856,WINDOW_OK,Exam window active: *CODE TANTRA - Notepad

2026-02-16 22:50:47,587gh856,WINDOW_VIOLATION_SHORT,Switched to: 

2026-02-16 22:50:49,587gh856,WINDOW_VIOLATION_SHORT,Switched to: New tab - Google Chrome

2026-02-16 22:50:53,587gh856,WINDOW_VIOLATION_SHORT,Switched to: iohho - Google Search - Google Chrome

2026-02-16 22:50:59,587gh856,WINDOW_OK,Exam window active: *CODE TANTRA - Notepad

2026-02-16 22:51:07,587gh856,WINDOW_VIOLATION_SHORT,Switched to: main.py - examguard - Visual Studio Code


##**⚙️ Installation & Setup**

git clone https://github.com/yourusername/exam-guard.git

cd exam-guard

pip install -r requirements.txt

python main.py

**📌 System Architecture Overview**

.UI Layer → User confirmation & validation (tkinter)

.Monitoring Engine → Multi-threaded system tracking

.Rule Engine → JSON-configured exam policies

.Logging Module → CSV structured audit storage

**🔐 Design Considerations**

.Real-time concurrent monitoring using threads

.Lightweight and minimal system resource usage

.Modular structure for scalability

.Designed to function without internet dependency

.Structured audit trail for post-exam review

**🚧 Future Improvements**

.Screenshot capture on violation

.Encrypted log storage

.SHA-256 log integrity hashing

.Admin dashboard for reviewing violations

.Real-time alert notifications

**📜 License**

This project is licensed under the MIT License.

**👨‍💻 Author**

Developed by OMKAR REDDY

Computer Science Student (Cyber Security) | Python Developer | Systems Enthusiast
