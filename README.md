
##🛡️ Exam Guard

Windows-Based Exam Monitoring & Violation Detection System (Python)

Exam Guard is a lightweight desktop-based exam monitoring system built using Python.

It enforces predefined examination rules by actively monitoring system behavior during an exam session and generating structured violation logs.


 ## ✨ Features

✅ **Secure Rule Confirmation**  
Interactive GUI dialog ensures candidates accept exam rules before starting.

🆔 **Roll Number Verification Workflow**  
Two-step roll number validation prevents incorrect session tracking.

🖥 **Real-Time Process Monitoring**  
Continuously scans background applications for unauthorized tools.

🔄 **Active Window & Tab Detection**  
Detects window switching or browser tab changes during the exam.

🔌 **USB Activity Detection**  
Monitors USB insertion and removal events.

🧵 **Multi-Threaded Architecture**  
Concurrent monitoring threads ensure real-time detection without UI freezing.

📊 **Structured Logging System**  
All violations are logged with timestamps in `logs.csv`.

⚙ **JSON-Based Configuration**  
Rules and blocked applications are managed via configurable JSON files.

🏗 **Modular Monitoring Design**  
Each monitoring component runs independently for scalability and maintainability.

---

## ⚙️ How It Works

- Displays exam rules and requests user confirmation.  
- Prompts candidate to enter and reconfirm roll number.  
- Validates input before starting monitoring session.  
-  Launches concurrent monitoring threads to track:
  ** **
       - 🚫 Unauthorized background applications  
       - 🔄 Window or tab switching  
       - 🔌 USB device activity  

- Records violations with precise timestamps.  
- Saves structured logs in CSV format for audit and review.

## 🏗️ Tech Stack

ExamGuard is built using a lightweight but powerful Windows monitoring stack:

 **Core Language**
- Python 3.x

 **System & Monitoring**
- psutil (Process detection)
- pygetwindow (Active window tracking)
- os (System interaction)

 **Concurrency**
- threading (Real-time background checks)

 **Logging & Configuration**
- csv (Structured logging)
- json (Configuration management)
- datetime & time (Timestamp tracking)

 **Interface**
- tkinter (Desktop GUI)

 **Platform**
- Windows OS
## 📂 Log File Structure

ExamGuard generates structured CSV logs in the following format:

| Column Name   | Description |
|--------------|------------|
| Timestamp     | Date and time of event |
| Roll Number   | Student identifier |
| Event Type    | Type of monitoring event |
| Details       | Additional event information |

###  Sample Log Output

| Timestamp           | Roll Number | Event Type              | Details                                      |
|--------------------|------------|--------------------------|----------------------------------------------|
| 2026-02-16 22:50:35 | 587gh856   | SYSTEM                   | ExamGuard started                            |
| 2026-02-16 22:50:35 | 587gh856   | WINDOW_OK                | Exam window active: CODE TANTRA - Notepad    |
| 2026-02-16 22:50:35 | 587gh856   | BLOCKED_APP              | AnyDesk.exe detected                         |
| 2026-02-16 22:50:35 | 587gh856   | BLOCKED_APP              | Code.exe detected                            |


## ⚙️ Installation & Setup

```bash
git clone https://github.com/yourusername/exam-guard.git
cd ExamGuard
cd agent
pip install -r requirements.txt
python main.py
```

##📌 System Architecture Overview

.UI Layer → User confirmation & validation (tkinter)

.Monitoring Engine → Multi-threaded system tracking

.Rule Engine → JSON-configured exam policies

.Logging Module → CSV structured audit storage

##🔐 Design Considerations

.Real-time concurrent monitoring using threads

.Lightweight and minimal system resource usage

.Modular structure for scalability

.Designed to function without internet dependency

.Structured audit trail for post-exam review

##🚧 Future Improvements

.Screenshot capture on violation

.Encrypted log storage

.SHA-256 log integrity hashing

.Admin dashboard for reviewing violations

.Real-time alert notifications

##📜 License

This project is licensed under the MIT License.

##👨‍💻 Author

Developed by OMKAR REDDY

Computer Science Student (Cyber Security) | Python Developer | Systems Enthusiast
