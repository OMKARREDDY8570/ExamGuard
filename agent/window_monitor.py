import time
import pygetwindow as gw
from logger import log_event
from config_loader import load_config

config =load_config()

def monitor_window_focus(student_id, config):
    allowed_windows = config["allowed_windows"]
    interval = config["window_interval"]
    threshold = config["window_threshold"]

    last_title = None
    violation_start = None
    long_violation_logged = False

    while True:
        try:
            active_window = gw.getActiveWindow()
            title = active_window.title if active_window else "UNKNOWN"

            is_allowed = any(
                word.lower() in title.lower()
                for word in allowed_windows
            )

            # Window changed
            if title != last_title:
                last_title = title

                if not is_allowed:
                    log_event(
                        student_id,
                        "WINDOW_VIOLATION_SHORT",
                        f"Switched to: {title}"
                    )
                    violation_start = time.time()
                    long_violation_logged = False
                else:
                    log_event(
                        student_id,
                        "WINDOW_OK",
                        f"Exam window active: {title}"
                    )
                    violation_start = None
                    long_violation_logged = False

            # Prolonged violation check
            if not is_allowed and violation_start:
                elapsed = time.time() - violation_start

                if elapsed >= threshold and not long_violation_logged:
                    log_event(
                        student_id,
                        "WINDOW_VIOLATION_LONG",
                        f"Outside exam window for {int(elapsed)} seconds ({title})"
                    )
                    long_violation_logged = True

        except Exception:
            pass

        time.sleep(interval)
