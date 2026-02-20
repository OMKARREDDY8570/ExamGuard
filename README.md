
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

2026-02-20 10:14:32	221045	Window Switch	Switched to Chrome

2026-02-20 10:16:02	221045	Unauthorized Application	Discord running in background

2026-02-20 10:18:45	221045	USB Inserted	SanDisk USB Device


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
