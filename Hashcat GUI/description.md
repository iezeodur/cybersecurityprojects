# 🔐 HashWraith

### Advanced Hashcat GUI by afrodaemon

HashWraith is a lightweight yet powerful graphical interface for **Hashcat**, built to streamline password cracking workflows without sacrificing flexibility.

Designed for **CTF players, penetration testers, and cybersecurity professionals**, it automates setup, reduces command-line complexity, and provides a clean, real-time interface for running attacks.

---

## 🚀 Features

### 🔍 Intelligent Automation

* **Auto-detects Hashcat installation**

  * Searches common system paths
  * Falls back to system `PATH`
* **Automatic hash type detection**

  * MD5 → 32 chars
  * SHA1 → 40 chars
  * SHA256 → 64 chars
  * SHA512 → 128 chars

### 📂 Smart Resource Handling

* Built-in discovery of common wordlists (e.g., `rockyou.txt`)
* Manual file selection for:

  * Hash files
  * Wordlists
  * Rule files

### ⚔️ Attack Modes

* **Straight (Dictionary)** `-a 0`
* **Brute Force (Mask)** `-a 3`
* **Hybrid Attacks** `-a 6`

### ⚙️ Advanced Controls

* Rule-based cracking (`-r`)
* Optimized kernels (`-O`)
* Ignore potfile (`--potfile-disable`)
* CPU / GPU selection (`-D`)
* Custom output file support

### 🖥️ Real-Time Execution

* Live Hashcat output console
* Clean terminal-style UI
* Scrollable logging

### 🧵 Performance & Stability

* Threaded execution (no UI freezing)
* Automatic environment validation (OpenCL check)

---

## 🛠️ Tech Stack

* **Language:** Python 3
* **GUI Framework:** Tkinter
* **Core Engine:** Hashcat

**Libraries Used:**

* `subprocess`
* `threading`
* `os`
* `shutil`

---

## 📦 Installation

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/hashwraith.git
cd hashwraith
```

### 2. Install Requirements

No external dependencies required (uses standard Python libraries)

### 3. Install Hashcat

Download from: https://hashcat.net/hashcat/

Ensure one of the following:

* `hashcat.exe` is in the project directory
* OR inside a `/hashcat/` folder
* OR installed globally and available in your system `PATH`

---

## ▶️ Usage

```bash
python main.py
```

### 🔄 Workflow

1. Select your **hash file**
2. Hash type is **auto-detected** (or manually set)
3. Choose attack mode:

   * Dictionary
   * Brute force
   * Hybrid
4. Load:

   * Wordlist / Mask / Rules
5. Click **🚀 Start Cracking**

---

## 📸 Screenshots (Optional)

Add images like:

```
/images/gui.png
/images/output.png
/images/settings.png
```

---

## 🧠 Example Use Cases

* CTF competitions (PicoCTF, HTB, TryHackMe)
* Password auditing & recovery
* Red team engagements
* Learning hash cracking techniques

---

## ⚠️ Requirements

* Python 3.x
* Hashcat installed
* OpenCL-compatible GPU (recommended)

---

## 🔒 Disclaimer

This tool is intended for **educational and authorized security testing only**.
Unauthorized use against systems without permission is illegal.

---

## 👨‍💻 Author

**afrodaemon**
Cybersecurity | Offensive Security | CTF

---

## 🧩 Project Highlights

* Automates complex Hashcat CLI workflows
* Reduces friction for beginners
* Demonstrates offensive security tooling skills
* Strong portfolio project for cybersecurity roles

---

## ⭐ Future Improvements

* Signature-based hash detection (beyond length)
* Built-in wordlist downloader
* Session resume UI
* Cross-platform support (Linux/macOS)
* Enhanced UI/UX themes

---

## 💀 Branding

Part of the **afrodaemon Toolset** — offensive security tools with speed, precision, and control.

---
