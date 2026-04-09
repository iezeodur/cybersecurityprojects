# 🏴‍☠️ CTF Writeups – picoCTF & CTFLearn

Collection of walkthroughs from various CTF challenges.

## 📁 PICO I

### 🔢 The Numbers
- Converted numbers to letters (A1Z26 cipher)
- Flag: picoCTF{THENUMBERSMASON}

### 🔄 Mod 26 (ROT13)
- Used ROT13 decoder
- Flag: picoCTF{next_time_I'll_try_2_rounds_of_rot13_ZNMldSDw}

### 🔐 Caesar Cipher
- Brute forced shifts
- Result: crossingtherubicon...

### 📡 Morse Code
- Decoded audio using morsecode.world

### 🔑 Vigenère Cipher
- Used CyberChef with provided key

### 🕵️ Insp3ct0r
- Found flags in HTML/CSS/JS source

### 🔐 Base64 Login
- Decoded base64 from index.js

### 🎂 MD5 Collision
- Used known collision files, renamed to PDF

### ⚙️ Assembly Required
- Followed hidden file paths

### 📶 Wireshark Capture
- Follow TCP stream → decode Base64

### 🖼️ Steganography
- Used Stegsolve stereogram solver

### 💉 SQL Injection
- Payload: " or 1=1 --

---

## 📁 PICO II

### 🧩 Pixelated
- Combined images using Stegsolve

### 🦈 Wireshark
- Extracted GET request → ROT13 decode

### ⚙️ Speeds and Feeds
- Used G-code viewer

### 🧭 Scavenger Hunt
- Explored:
  - index.html
  - mycss.css
  - myjs.js
  - robots.txt
  - .htaccess
  - .DS_Store

### 🤖 Robots.txt
- Found hidden directories

### 🪆 Matryoshka Doll
- Used binwalk recursively

### 🖼️ Tunnel Vision
- Fixed BMP header using hex editor

### 📡 POST Practice
- Sent POST request manually

### 🕵️ Headers
- Modified headers using Burp Suite

---

## 📁 PICO III

### 🍪 Logon
- Modified cookies

### 🌐 Who Are You
- Manipulated HTTP headers

### 🔁 FindMe
- Intercepted redirects using Burp

### 🛰️ Whois
- Looked up IP ownership

### 📦 FindAndOpen
- Extracted Base64 → unlocked archive

---

## 📁 CTF 2023

### 🦊 Firefox Decrypt
- Used NirSoft Prefetch Viewer
- Flag: flag{97f33c9783c21df85d79d613b0b258bd}

### 🍪 Cookie Manipulation
- Decoded Base64 cookie
- Modified timestamp
- Re-encoded and reused

### 📡 API Payloads
- Payload = data sent in HTTP request

---

## 🧰 Tools Used

- Wireshark
- Burp Suite
- CyberChef
- Stegsolve
- Binwalk
- Hexed.it
- NirSoft Prefetch Viewer

---

## 🧠 Key Takeaways

- Inspect source files
- Analyze network traffic
- Decode everything
- Manipulate headers & cookies
- Use forensics tools
