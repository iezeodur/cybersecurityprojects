# 🔐 HashVat GUI – Hashcat Frontend

A simple and powerful **Tkinter-based GUI** for running Hashcat without needing to use the command line.

---

## 🚀 Features

* 🔑 Select hash types (MD5, SHA1, NTLM, WPA/WPA2)
* ⚔️ Multiple attack modes:

  * Straight (wordlist)
  * Combination
  * Brute Force (mask)
  * Hybrid
* 📂 File picker for hashes and wordlists
* 📺 Real-time output display
* ⚡ Multithreaded execution (no UI freezing)

---

## 🖼️ Screenshot

```md
![HashVat GUI](screenshots/gui.png)
```

---

## ⚙️ Requirements

* Python 3.x
* Hashcat installed and added to system PATH

Check installation:

```bash
hashcat --help
```

---

## 📦 Installation

```bash
git clone https://github.com/yourusername/hashvat-gui.git
cd hashvat-gui
python main.py
```

---

## 🧠 How It Works

The GUI dynamically builds a Hashcat command based on user selections:

* `-m` → Hash type
* `-a` → Attack mode
* Wordlist or mask added depending on attack type

Example:

```bash
hashcat -m 0 -a 0 hashes.txt rockyou.txt
```

---

## 🛠️ Usage

### 1. Select Hash Type

Choose the correct algorithm:

* MD5 → `0`
* SHA1 → `100`
* NTLM → `1000`
* WPA/WPA2 → `2500`

---

### 2. Select Attack Mode

* `0` → Straight (wordlist)
* `3` → Brute force (mask)
* `6` → Hybrid

---

### 3. Load Required Files

* Hash file
* Wordlist (if needed)

---

### 4. Enter Mask (Optional)

Example:

```bash
?a?a?a?a
```

---

### 5. Start Cracking

Click:

```
🚀 Start Cracking
```

---

## 💻 Key Code Highlights

### Multithreading (Prevents Freezing)

```python
thread = threading.Thread(target=self.execute)
thread.start()
```

---

### Command Builder

```python
cmd = ["hashcat", "-m", mode, "-a", attack]
```

---

### Real-Time Output Streaming

```python
for line in process.stdout:
    self.output.insert(tk.END, line)
    self.output.see(tk.END)
```

---

## ⚠️ Notes

* Ensure Hashcat is properly installed
* WPA cracking requires `.cap` or `.hccapx` files
* Performance depends on GPU/CPU power

---

## 🧪 Future Improvements

* ✅ Progress bar (hash rate, % complete)
* ⏸️ Pause / Stop button
* 🧠 Auto-detect hash type
* 💾 Save cracked passwords
* 🎨 Advanced UI (hacker-style dashboard)

---

## 📜 Disclaimer

This project is for **educational and ethical security testing only**.
Do **not** use it on systems without permission.

---

## ⭐ Contributing

Feel free to fork, improve, and submit pull requests!

---

## 👨‍💻 Author

**Ikenna Ezeodurukwe**

---
