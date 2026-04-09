# 🔐 Password Manager (Tkinter GUI)

## 📌 Overview
This is a simple **Python-based Password Manager** built with `tkinter`.  
It allows users to:
- Generate strong random passwords
- Save login credentials securely in a JSON file
- Search for stored credentials by website

The application features a graphical user interface (GUI) for ease of use.

---

## 🧠 Features

- 🔑 Random password generator (letters, numbers, symbols)
- 📋 Auto-copy password to clipboard
- 💾 Save credentials to a JSON file
- 🔍 Search saved credentials by website
- ⚠️ Error handling for missing files and empty fields
- 🖥️ User-friendly GUI built with Tkinter

---

## 🧾 How It Works

### 🔑 Password Generation
- Uses:
  - `random.choice`
  - `randint`
  - `shuffle`
- Generates:
  - 8–10 letters
  - 2–4 symbols
  - 2–4 numbers
- Combines and shuffles them into a secure password
- Automatically copies to clipboard using `pyperclip`

---

### 💾 Saving Data
- Stores data in `input_file.json`
- Structure:
```json
{
  "example.com": {
    "email": "user@email.com",
    "password": "generated_password"
  }
}
