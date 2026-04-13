# 🛡️ Phishing Detector GUI

### Real-Time URL Risk Analyzer by afrodaemon

Phishing Detector is a Python-based GUI tool that analyzes URLs for potential phishing indicators using heuristic checks, domain intelligence, and threat intelligence APIs.

Built with **Tkinter**, this tool provides a clean, interactive interface for quickly assessing whether a website is **safe, suspicious, or malicious**.

---

## 🚀 Features

### 🔍 Intelligent URL Analysis

* Detects:

  * Missing HTTPS
  * IP-based URLs (common phishing tactic)
  * Suspicious keywords (login, verify, bank, etc.)
  * Excessively long URLs
  * URL shorteners (bit.ly, tinyurl, etc.)

### 🌐 Domain Intelligence

* WHOIS lookup for:

  * Domain existence
  * Domain age analysis
* Flags newly created domains (common in phishing campaigns)

### 🧪 Threat Intelligence Integration

* **VirusTotal API**

  * Checks URL reputation across multiple security engines
  * Displays malicious detection ratio

* *(Optional)* Google Safe Browsing (code included, currently disabled)

### 📊 Risk Scoring System

* Dynamic scoring engine based on detected indicators

* Visual output:

  * 🟢 Safe
  * 🟡 Suspicious
  * 🔴 Phishing

* Includes:

  * Percentage risk score
  * Visual progress bar

### 🖥️ Interactive GUI

* Clean dark-themed interface
* Real-time animated scan output
* User-friendly input & results display

---

## 🛠️ Tech Stack

* **Language:** Python 3
* **GUI Framework:** Tkinter
* **Libraries:**

  * `requests`
  * `whois`
  * `re`
  * `base64`
  * `urllib.parse`
  * `datetime`
  * `Pillow (PIL)` for image handling

---

## 📦 Installation

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/phishing-detector.git
cd phishing-detector
```

### 2. Install Dependencies

```bash
pip install requests python-whois pillow
```

### 3. Add API Keys

Edit the script and insert your keys:

```python
VT_API_KEY = "YOUR_VIRUS_TOTAL_API"
GSB_API_KEY = "YOUR_GOOGLE_API_KEY"
```

Get API keys from:

* https://www.virustotal.com/
* https://developers.google.com/safe-browsing

---

## ▶️ Usage

```bash
python main.py
```

### 🔄 Workflow

1. Enter a URL
2. Click **Check Site**
3. View:

   * Risk level
   * Reputation results
   * Detailed findings

---

## 📊 Example Output

```
[ SCAN RESULT ]

🔴 PHISHING
[██████░░░░] 60% Risk Score

Reputation Check:
- VirusTotal: 5/70 flagged ❗
- Domain Age: 12 days old ❗

-----------------------------
> No HTTPS (Not Secure)
> Suspicious keywords in URL
> URL shortener detected

Scan Complete.
```

---

## 🧠 Detection Logic Overview

The tool combines:

* **Heuristic analysis** (URL structure patterns)
* **Threat intelligence APIs** (VirusTotal)
* **Domain metadata analysis** (WHOIS)

This layered approach improves detection accuracy for common phishing techniques.

---

## ⚠️ Requirements

* Python 3.x
* Internet connection (for API + WHOIS checks)

---

## 🔒 Disclaimer

This tool is intended for **educational and authorized security analysis only**.
Do not use it for malicious purposes or unauthorized scanning.

---

## 👨‍💻 Author

**afrodaemon**
Cybersecurity | Threat Detection | Offensive Security

---

## 🧩 Project Highlights

* Demonstrates **real-world phishing detection techniques**
* Combines **OSINT + threat intelligence APIs**
* Practical tool for **security awareness & analysis**
* Strong addition to a **cybersecurity portfolio**

---

## ⭐ Future Improvements

* Enable Google Safe Browsing integration
* Add machine learning-based detection
* Export scan results (PDF/JSON)
* URL screenshot preview
* Browser extension version

---

## 💀 afrodaemon Toolset

Part of the **afrodaemon cybersecurity toolkit** — focused on automation, detection, and offensive security workflows.

---
