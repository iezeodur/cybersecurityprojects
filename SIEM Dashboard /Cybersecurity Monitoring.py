import tkinter as tk
from tkinter import ttk
import threading
import time
import platform
import os
import re
import sqlite3

# Optional Windows support
try:
    import win32evtlog
except ImportError:
    win32evtlog = None

MAX_LOGS = 150
LINUX_LOGS = ["/var/log/auth.log", "/var/log/syslog"]

#database
conn = sqlite3.connect("siem_logs.db", check_same_thread=False)
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS logs (
    timestamp TEXT,
    log TEXT,
    severity TEXT
)
""")
conn.commit()

def save_log(log, severity):
    cursor.execute("INSERT INTO logs VALUES (datetime('now'), ?, ?)", (log, severity))
    conn.commit()

#os check
def get_os():
    return platform.system()

def is_admin():
    try:
        if os.name == "nt":
            import ctypes
            return ctypes.windll.shell32.IsUserAnAdmin()
        else:
            return os.geteuid() == 0
    except:
        return False

# collector
def tail_file(filepath):
    with open(filepath, "r") as f:
        f.seek(0, 2)

        while True:
            line = f.readline()

            if not line:
                time.sleep(0.5)
                continue

            yield line.strip()

def stream_linux_logs():
    for path in LINUX_LOGS:
        try:
            for line in tail_file(path):
                yield line
        except PermissionError:
            continue

    yield "[!] No accessible Linux logs"

def stream_windows_logs():
    if not win32evtlog:
        yield "[!] pywin32 not installed"
        return

    server = 'localhost'
    log_types = ["Security", "Application"]

    for log_type in log_types:
        try:
            hand = win32evtlog.OpenEventLog(server, log_type)
            break
        except:
            continue
    else:
        yield "[!] Cannot access Windows logs"
        return

    flags = win32evtlog.EVENTLOG_BACKWARDS_READ | win32evtlog.EVENTLOG_SEQUENTIAL_READ
    seen = set()

    while True:
        events = win32evtlog.ReadEventLog(hand, flags, 0)

        for event in events:
            if event.RecordNumber not in seen:
                seen.add(event.RecordNumber)
                yield f"{log_type} | EventID:{event.EventID} Source:{event.SourceName}"

        time.sleep(1)

def stream_logs():
    os_type = get_os()

    if os_type == "Linux":
        yield from stream_linux_logs()
    elif os_type == "Windows":
        yield from stream_windows_logs()
    else:
        yield "[!] Unsupported OS"

#paser
def parse_log(log):
    ip_match = re.search(r'\d+\.\d+\.\d+\.\d+', log)
    user_match = re.search(r'user (\w+)', log)

    return {
        "raw": log,
        "ip": ip_match.group(0) if ip_match else None,
        "user": user_match.group(1) if user_match else None
    }

#detection
failed_attempts = {}

def detect_threat(parsed):
    log = parsed["raw"]
    ip = parsed["ip"]

    # Brute force detection
    if "Failed password" in log and ip:
        failed_attempts[ip] = failed_attempts.get(ip, 0) + 1

        if failed_attempts[ip] >= 5:
            return "HIGH", f"Brute force suspected from {ip}"

        return "MEDIUM", f"Failed login from {ip}"

    # Generic errors
    if "error" in log.lower():
        return "MEDIUM", "System error detected"

    return "LOW", None

#userinterface construct
def add_log(box, message):
    box.insert(0, message)
    if box.size() > MAX_LOGS:
        box.delete(tk.END)

def add_alert(box, message, severity):
    box.insert(0, message)

    if severity == "HIGH":
        box.itemconfig(0, {'fg': 'red'})
    elif severity == "MEDIUM":
        box.itemconfig(0, {'fg': 'orange'})

    if box.size() > MAX_LOGS:
        box.delete(tk.END)

#userinterface
class SIEMApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Mini SIEM Dashboard")

        # Layout frames
        top_frame = ttk.Frame(root, padding=5)
        top_frame.grid(row=0, column=0, sticky="ew")

        left_frame = ttk.Frame(root, padding=5)
        left_frame.grid(row=1, column=0, sticky="ns")

        right_frame = ttk.Frame(root, padding=5)
        right_frame.grid(row=1, column=1, sticky="ns")

        #status panel
        ttk.Label(top_frame, text=f"OS: {get_os()}").pack(side="left", padx=10)

        privilege = "Admin" if is_admin() else "Limited"
        ttk.Label(top_frame, text=f"Mode: {privilege}").pack(side="left", padx=10)

        #alerts
        ttk.Label(left_frame, text="Alerts").pack(anchor="w")
        self.alert_box = tk.Listbox(left_frame, width=50, height=25)
        self.alert_box.pack()

        #logs
        ttk.Label(right_frame, text="Live Logs").pack(anchor="w")
        self.log_box = tk.Listbox(right_frame, width=80, height=25)
        self.log_box.pack()

        #thread
        threading.Thread(target=self.run_pipeline, daemon=True).start()

    def run_pipeline(self):
        for log in stream_logs():
            parsed = parse_log(log)
            severity, alert_msg = detect_threat(parsed)

            save_log(log, severity)

            # UI updates
            self.root.after(0, add_log, self.log_box, log)

            if alert_msg:
                self.root.after(0, add_alert, self.alert_box, alert_msg, severity)

#.....
if __name__ == "__main__":
    root = tk.Tk()
    app = SIEMApp(root)
    root.mainloop()

