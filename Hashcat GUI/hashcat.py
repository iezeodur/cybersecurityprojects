import tkinter as tk
from tkinter import ttk, filedialog
import subprocess
import threading

# --- MAIN APP ---
class HashcatGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("HashVat GUI 🔐")
        self.root.geometry("900x600")
        self.root.configure(bg="#0f172a")

        # --- VARIABLES ---
        self.hash_type = tk.StringVar(value="0")
        self.attack_mode = tk.StringVar(value="0")
        self.hash_file = tk.StringVar()
        self.wordlist = tk.StringVar()
        self.mask = tk.StringVar()

        # --- UI ---
        self.build_ui()

    def build_ui(self):
        frame = tk.Frame(self.root, bg="#0f172a")
        frame.pack(pady=10)

        # HASH TYPE
        tk.Label(frame, text="Hash Type (-m)", fg="white", bg="#0f172a").grid(row=0, column=0)
        ttk.Combobox(frame, textvariable=self.hash_type, values=[
            "0 - MD5",
            "100 - SHA1",
            "1000 - NTLM",
            "2500 - WPA/WPA2"
        ]).grid(row=0, column=1)

        # ATTACK MODE
        tk.Label(frame, text="Attack Mode (-a)", fg="white", bg="#0f172a").grid(row=1, column=0)
        ttk.Combobox(frame, textvariable=self.attack_mode, values=[
            "0 - Straight",
            "1 - Combination",
            "3 - Brute Force",
            "6 - Hybrid"
        ]).grid(row=1, column=1)

        # HASH FILE
        tk.Button(frame, text="Select Hash File", command=self.load_hash).grid(row=2, column=0)
        tk.Label(frame, textvariable=self.hash_file, fg="cyan", bg="#0f172a").grid(row=2, column=1)

        # WORDLIST
        tk.Button(frame, text="Select Wordlist", command=self.load_wordlist).grid(row=3, column=0)
        tk.Label(frame, textvariable=self.wordlist, fg="cyan", bg="#0f172a").grid(row=3, column=1)

        # MASK
        tk.Label(frame, text="Mask (?a?a?a)", fg="white", bg="#0f172a").grid(row=4, column=0)
        tk.Entry(frame, textvariable=self.mask).grid(row=4, column=1)

        # RUN BUTTON
        tk.Button(self.root, text="🚀 Start Cracking", bg="#22c55e", command=self.run_hashcat).pack(pady=10)

        # OUTPUT TERMINAL
        self.output = tk.Text(self.root, bg="black", fg="lime", height=20)
        self.output.pack(fill="both", expand=True)

    def load_hash(self):
        file = filedialog.askopenfilename()
        self.hash_file.set(file)

    def load_wordlist(self):
        file = filedialog.askopenfilename()
        self.wordlist.set(file)

    def run_hashcat(self):
        thread = threading.Thread(target=self.execute)
        thread.start()

    def execute(self):
        self.output.delete(1.0, tk.END)

        # Extract only numbers
        mode = self.hash_type.get().split(" ")[0]
        attack = self.attack_mode.get().split(" ")[0]

        cmd = ["hashcat", "-m", mode, "-a", attack]

        if self.hash_file.get():
            cmd.append(self.hash_file.get())

        if attack == "0":  # Straight
            cmd.append(self.wordlist.get())

        elif attack == "3":  # Brute force
            cmd.append(self.mask.get())

        elif attack == "6":  # Hybrid
            cmd.append(self.wordlist.get())
            cmd.append(self.mask.get())

        self.output.insert(tk.END, f"Running: {' '.join(cmd)}\n\n")

        try:
            process = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True)

            for line in process.stdout:
                self.output.insert(tk.END, line)
                self.output.see(tk.END)

        except Exception as e:
            self.output.insert(tk.END, f"Error: {e}")

# --- RUN ---
if __name__ == "__main__":
    root = tk.Tk()
    app = HashcatGUI(root)
    root.mainloop()