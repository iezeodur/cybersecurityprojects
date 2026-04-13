import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import requests
import whois
import re
import base64
from urllib.parse import urlparse
from datetime import datetime

# 🔐 ADD YOUR API KEYS HERE
VT_API_KEY = "YOUR_VIRUS_TOTAL_API"
GSB_API_KEY = "YOUR_GOOGLE_API_KEY"


# -------------------------------
# 🔍 PHISHING CHECK ENGINE
# -------------------------------
def check_phishing(url):
    score = 0
    results = []

    if not url.startswith("http"):
        url = "http://" + url

    parsed = urlparse(url)
    domain = parsed.netloc

    if url.startswith("https://"):
        results.append(("HTTPS enabled", "safe"))
    else:
        results.append(("No HTTPS (Not Secure)", "danger"))
        score += 2

    if re.match(r"\d+\.\d+\.\d+\.\d+", domain):
        results.append(("Uses IP address instead of domain", "danger"))
        score += 3

    keywords = ["login", "verify", "bank", "secure", "account", "update"]
    if any(k in url.lower() for k in keywords):
        results.append(("Suspicious keywords in URL", "warn"))
        score += 2

    if len(url) > 75:
        results.append(("URL is very long", "warn"))
        score += 1

    shorteners = ["bit.ly", "tinyurl", "rb.gy"]
    if any(s in url for s in shorteners):
        results.append(("URL shortener detected", "danger"))
        score += 3

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

    return score, results, domain, url


# -------------------------------
# 🔑 VIRUSTOTAL API
# -------------------------------
def check_virustotal(url):
    headers = {"x-apikey": VT_API_KEY}

    try:
        url_id = base64.urlsafe_b64encode(url.encode()).decode().strip("=")
        vt_url = f"https://www.virustotal.com/api/v3/urls/{url_id}"

        response = requests.get(vt_url, headers=headers)
        data = response.json()

        stats = data["data"]["attributes"]["last_analysis_stats"]

        malicious = stats.get("malicious", 0)
        total = sum(stats.values())

        return f"VirusTotal: {malicious}/{total} flagged {'❗' if malicious > 0 else '✅'}"

    except:
        return "VirusTotal: Error ⚠️"


# -------------------------------
# 🛡 GOOGLE SAFE BROWSING API
# -------------------------------
#def check_google_safe(url):
    #endpoint = f"https://safebrowsing.googleapis.com/v4/threatMatches:find?key={GSB_API_KEY}"

#     payload = {
#         "client": {"clientId": "phishing-detector", "clientVersion": "1.0"},
#         "threatInfo": {
#             "threatTypes": ["MALWARE", "SOCIAL_ENGINEERING"],
#             "platformTypes": ["ANY_PLATFORM"],
#             "threatEntryTypes": ["URL"],
#             "threatEntries": [{"url": url}],
#         },
#     }
# 
#     try:
#         response = requests.post(endpoint, json=payload)
#         data = response.json()
# 
#         if "matches" in data:
#             return "Google Safe Browsing: Threat detected ❗"
#         else:
#             return "Google Safe Browsing: No threats found ✅"
# 
#     except:
#         return "Google Safe Browsing: Error ⚠️"


# -------------------------------
# 🌐 REPUTATION
# -------------------------------
def get_reputation(domain, url):
    rep = []

    rep.append(check_virustotal(url))
    #rep.append(check_google_safe(url))

    try:
        domain_info = whois.whois(domain)
        creation_date = domain_info.creation_date

        if isinstance(creation_date, list):
            creation_date = creation_date[0]

        if creation_date:
            age_days = (datetime.now() - creation_date).days

            if age_days < 30:
                rep.append(f"Domain Age: {age_days} days old ❗")
            elif age_days < 180:
                rep.append(f"Domain Age: {age_days} days old ⚠️")
            else:
                rep.append(f"Domain Age: {age_days} days old ✅")
        else:
            rep.append("Domain Age: Unknown ⚠️")

    except:
        rep.append("Domain Age: Lookup failed ⚠️")

    return rep


# -------------------------------
# 🧠 GUI APP
# -------------------------------
class PhishingApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Phishing Detector 🔐")
        self.root.geometry("520x600")
        self.root.configure(bg="#0f172a")

        img = Image.open("C:/Users/iezeo/Downloads/1775013407803.jpg")
        img = img.resize((120, 120))
        self.photo = ImageTk.PhotoImage(img)
        tk.Label(root, image=self.photo, bg="#0f172a").pack(pady=10)

        tk.Label(root, text="Phishing Site Checker",
                 fg="cyan", bg="#0f172a",
                 font=("Arial", 16)).pack(pady=10)

        self.url_entry = tk.Entry(root, width=45)
        self.url_entry.pack(pady=10)

        tk.Button(root, text="Check Site",
                  command=self.run_check,
                  bg="#22c55e").pack(pady=5)

        self.result_box = tk.Text(root, height=25, bg="black", fg="white")
        self.result_box.pack(pady=10, fill="both", expand=True)

    def get_risk_visual(self, score):
        max_score = 10
        percent = int((score / max_score) * 100)
        filled = int(percent / 10)
        bar = "█" * filled + "░" * (10 - filled)

        if score >= 4:
            label = "🔴 PHISHING"
        elif score >= 2:
            label = "🟡 SUSPICIOUS"
        else:
            label = "🟢 SAFE"

        return percent, bar, label

    def animate_text(self, text, delay=10):
        self.result_box.delete(1.0, tk.END)

        def type_char(i):
            if i < len(text):
                self.result_box.insert(tk.END, text[i])
                self.result_box.see(tk.END)
                self.root.after(delay, lambda: type_char(i + 1))

        type_char(0)

    def run_check(self):
        url = self.url_entry.get()

        if not url:
            messagebox.showerror("Error", "Enter a URL")
            return

        score, results, domain, url = check_phishing(url)
        reputation = get_reputation(domain, url)

        percent, bar, label = self.get_risk_visual(score)

        output = "[ SCAN RESULT ]\n\n"
        output += f"{label}\n"
        output += f"[{bar}] {percent}% Risk Score\n\n"

        output += "Reputation Check:\n"
        for item in reputation:
            output += f"- {item}\n"

        output += "\n-----------------------------\n"

        for text, _ in results:
            output += f"> {text}\n"

        output += "\nScan Complete."

        self.animate_text(output)


# -------------------------------
# ▶ RUN
# -------------------------------
if __name__ == "__main__":
    root = tk.Tk()
    app = PhishingApp(root)
    root.mainloop()
