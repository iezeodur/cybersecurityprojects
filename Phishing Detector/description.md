# 🔐 Phishing Detector GUI

A Python-based **Tkinter GUI application** that analyzes URLs and detects potential phishing websites using heuristic checks and real-time validation.

---

## 🚀 Features

* 🔍 URL phishing detection engine
* 🔐 HTTPS validation
* 🌐 WHOIS domain lookup
* 📡 Website availability check
* ⚠️ Suspicious keyword detection
* 🔗 URL shortener detection
* 📏 URL length analysis
* 💻 Clean GUI with terminal-style output
* ⏳ Animated typing effect for scan results

---

## 🖼️ Screenshot

```md
![Phishing Detector](screenshots/app.png)
```

---

## ⚙️ Requirements

* Python 3.x
* Required libraries:

```bash
pip install pillow requests python-whois
```

---

## 📦 Installation

```bash
git clone https://github.com/yourusername/phishing-detector.git
cd phishing-detector
python main.py
```

---

## 🧠 How It Works

The application evaluates a URL using multiple phishing indicators:

### 🔎 Detection Checks

* **HTTPS Check**

  * Secure sites use HTTPS
* **IP Address Detection**

  * Flags URLs using raw IP instead of domain
* **Suspicious Keywords**

  * Detects terms like `login`, `verify`, `bank`
* **URL Length**

  * Long URLs may indicate obfuscation
* **URL Shorteners**

  * Flags services like `bit.ly`, `tinyurl`
* **WHOIS Lookup**

  * Checks domain existence and age
* **HTTP Request Test**

  * Verifies if the site is reachable

---

## 🛠️ Usage

1. Run the application
2. Enter a website URL
3. Click **"Check Site"**
4. View the scan results in the terminal-style output

---

## 📊 Risk Scoring

The tool assigns a risk score based on findings:

* 🚨 **High Risk (Score ≥ 4)** → Likely phishing
* ⚠️ **Suspicious (Score ≥ 2)** → Potential risk
* ✅ **Safe (Score < 2)** → Likely legitimate

---

## 💻 Key Code Highlights

### Phishing Detection Engine

```python
score, results = check_phishing(url)
```

---

### WHOIS Lookup

```python
domain_info = whois.whois(domain)
```

---

### HTTP Request Validation

```python
requests.get(url, timeout=5)
```

---

### Animated Output Effect

```python
self.animate_text(output)
```

---

## 📁 Project Structure

```
phishing-detector/
│── main.py
│── screenshots/
│   └── app.png
│── assets/
│   └── logo.jpg
```

---

## 🧪 Future Improvements

* 🌍 Real-time blacklist API integration (Google Safe Browsing)
* 📊 Risk visualization (charts/score meter)
* 🧠 Machine learning phishing detection
* 🌐 Browser extension version
* 📁 Export scan results

---

## ⚠️ Disclaimer

This tool is intended for **educational and cybersecurity awareness purposes only**.
It should not be used as a sole source of truth for website safety.

---

## ⭐ Contributing

Contributions are welcome!
Feel free to fork this repo and submit pull requests 🚀

---

## 👨‍💻 Author

**Ikenna Ezeodurukwe**

---
