import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import requests
import whois
import re
from urllib.parse import urlparse


#check engine
def check_phishing(url):
    score = 0
    results = []

    # Ensure URL
    if not url.startswith("http"):
        url = "http://" + url

    parsed = urlparse(url)
    domain = parsed.netloc

    # 1. HTTPS check
    if url.startswith("https://"):
        results.append(("HTTPS enabled", "safe"))
    else:
        results.append(("No HTTPS (Not Secure)", "danger"))
        score += 2

    # 2. IP address not domain
    if re.match(r"\d+\.\d+\.\d+\.\d+", domain):
        results.append(("Uses IP address instead of domain", "danger"))
        score += 3

    # 3. Suspicious keywords
    keywords = ["login", "verify", "bank", "secure", "account", "update"]
    if any(k in url.lower() for k in keywords):
        results.append(("Suspicious keywords in URL", "warn"))
        score += 2

    # 4. URL length
    if len(url) > 75:
        results.append(("URL is very long", "warn"))
        score += 1

    # 5. Shortened link
    shorteners = ["bit.ly", "tinyurl", "rb.gy"]
    if any(s in url for s in shorteners):
        results.append(("URL shortener detected", "danger"))
        score += 3

    # 6. WHOIS domain age
    try:
        domain_info = whois.whois(domain)
        if domain_info.creation_date:
            results.append(("Domain exists", "safe"))
        else:
            results.append(("Domain age unknown", "warn"))
            score += 1
    except:
        results.append(("WHOIS lookup failed", "warn"))
        score += 1

    # 7. Try request
    try:
        r = requests.get(url, timeout=5)
        if r.status_code == 200:
            results.append(("Website reachable", "safe"))
        else:
            results.append(("Website returned error", "warn"))
            score += 1
    except:
        results.append(("Website not reachable", "danger"))
        score += 2

    return score, results

#Gui
class PhishingApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Phishing Detector 🔐")
        self.root.geometry("500x500")
        self.root.configure(bg="#0f172a")
        
        img = Image.open("C:/Users/iezeo/Downloads/1775013407803.jpg")  # path to your image
        img = img.resize((120, 120))  # adjust size
        self.photo = ImageTk.PhotoImage(img)

        # --- IMAGE DISPLAY ---
        tk.Label(root, image=self.photo, bg="#0f172a").pack(pady=10)

        # Title
        tk.Label(root, text="Phishing Site Checker", fg="cyan", bg="#0f172a", font=("Arial", 16)).pack(pady=10)

        # Input
        self.url_entry = tk.Entry(root, width=40)
        self.url_entry.pack(pady=10)

        # Button
        tk.Button(root, text="Check Site", command=self.run_check, bg="#22c55e").pack(pady=5)

        # Result box
        self.result_box = tk.Text(root, height=20, bg="black", fg="white")
        self.result_box.pack(pady=10, fill="both", expand=True)
        
        # ⏳ TERMINAL TYPING EFFECT
    def animate_text(self, text, delay=20):
        self.result_box.delete(1.0, tk.END)

        def type_char(index):
            if index < len(text):
                self.result_box.insert(tk.END, text[index])
                self.result_box.see(tk.END)
                self.root.after(delay, lambda: type_char(index + 1))

        type_char(0)

    def run_check(self):
        url = self.url_entry.get()

        if not url:
            messagebox.showerror("Error", "Enter a URL")
            return

        score, results = check_phishing(url)

        # Verdict
        if score >= 4:
            verdict = "🚨 HIGH RISK - Likely Phishing"
        elif score >= 2:
            verdict = "⚠️ Suspicious"
        else:
            verdict = "✅ Likely Safe"

        # Build output text
        output = f"[ SCAN RESULT ]\n\n{verdict}\n\n"
        output += "-----------------------------\n"

        for text, status in results:
            output += f"> {text}\n"

        output += "\nScan Complete."

        # 🔥 Animate instead of instant print
        self.animate_text(output)


#run
if __name__ == "__main__":
    root = tk.Tk()
    app = PhishingApp(root)
    root.mainloop()