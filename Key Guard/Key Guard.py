import tkinter as tk
from tkinter import ttk, messagebox
import psutil
import threading
import time

# --- CONFIG ---
SUSPICIOUS_KEYWORDS = [
    "pynput", "keyboard", "hook", "listener", "keylog"
]

SCAN_INTERVAL = 5  # seconds


# --- DETECTION LOGIC ---
def analyze_process(proc):
    try:
        name = proc.name()
        cmdline = " ".join(proc.cmdline())

        score = 0
        matches = []

        for keyword in SUSPICIOUS_KEYWORDS:
            if keyword in name.lower() or keyword in cmdline.lower():
                score += 2
                matches.append(keyword)

        # Risk level
        if score >= 4:
            risk = "HIGH"
        elif score >= 2:
            risk = "MEDIUM"
        else:
            risk = "LOW"

        return {
            "pid": proc.pid,
            "name": name,
            "risk": risk,
            "matches": ", ".join(matches) if matches else "-"
        }

    except (psutil.NoSuchProcess, psutil.AccessDenied):
        return None


def scan_system():
    results = []
    for proc in psutil.process_iter():
        info = analyze_process(proc)
        if info and info["risk"] != "LOW":
            results.append(info)
    return results


# --- GUI ---
class KeyGuard:
    def __init__(self, root):
        self.root = root
        self.root.title("KeyGuard by afrodaemon 🔐 - Keylogging Detection")
        self.root.geometry("800x500")
        self.root.configure(bg="#0f172a")

        self.running = True

        self.build_ui()
        self.start_monitoring()

    def build_ui(self):
        title = tk.Label(self.root, text="KeyGuard - Live Detection",
                         bg="#0f172a", fg="white", font=("Arial", 16, "bold"))
        title.pack(pady=10)

        # Table
        columns = ("PID", "Name", "Risk", "Matches")
        self.tree = ttk.Treeview(self.root, columns=columns, show="headings")

        for col in columns:
            self.tree.heading(col, text=col)
            self.tree.column(col, anchor="center")

        self.tree.pack(fill="both", expand=True, padx=10, pady=10)

        # Buttons
        btn_frame = tk.Frame(self.root, bg="#0f172a")
        btn_frame.pack(pady=5)

        tk.Button(btn_frame, text="🔄 Refresh", command=self.refresh,
                  bg="#3b82f6", fg="white").grid(row=0, column=0, padx=5)

        tk.Button(btn_frame, text="❌ Kill Process", command=self.kill_selected,
                  bg="#ef4444", fg="white").grid(row=0, column=1, padx=5)

    def refresh(self):
        self.tree.delete(*self.tree.get_children())

        results = scan_system()

        for r in results:
            self.tree.insert("", "end", values=(
                r["pid"], r["name"], r["risk"], r["matches"]
            ))

    def kill_selected(self):
        selected = self.tree.selection()
        if not selected:
            return

        item = self.tree.item(selected[0])
        pid = item["values"][0]

        confirm = messagebox.askyesno("Confirm", f"Kill process {pid}?")
        if confirm:
            try:
                psutil.Process(pid).terminate()
                messagebox.showinfo("Success", f"Process {pid} terminated")
                self.refresh()
            except Exception as e:
                messagebox.showerror("Error", str(e))

    def monitor_loop(self):
        while self.running:
            self.refresh()
            time.sleep(SCAN_INTERVAL)

    def start_monitoring(self):
        thread = threading.Thread(target=self.monitor_loop, daemon=True)
        thread.start()


# --- RUN ---
if __name__ == "__main__":
    root = tk.Tk()
    app = KeyGuard(root)
    root.mainloop()