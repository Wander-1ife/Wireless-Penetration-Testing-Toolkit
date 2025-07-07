# 📶 Wireless Penetration Testing Toolkit


---

## 📖 Abstract

**WiFiGuard** is a Python-based modular toolkit for **wireless penetration testing** and ethical hacking. It integrates popular security utilities like **Aircrack-ng**, **Hostapd**, **Dnsmasq**, and **Reaver** to simulate real-world Wi-Fi attacks in a controlled environment. The toolkit offers an interactive **command-line interface (CLI)** for cybersecurity students and professionals to explore wireless vulnerabilities responsibly.

---

## 📝 Introduction

Wireless networks, while convenient, are prone to security risks from weak encryption, misconfiguration, and human oversight. **WiFiGuard** was created to demonstrate and teach common Wi-Fi attack techniques in ethical, consent-based environments.

### 🎯 Key Objectives:
- Execute **deauthentication attacks** to disconnect clients.
- Simulate **rogue access points (AP)** for MITM attacks.
- Capture **WPA/WPA2 handshakes** for cracking attempts.
- Perform **MAC address spoofing** to bypass access controls.
- Deploy **captive portals for phishing credentials**.

---

## 📚 Literature Review

WiFiGuard extends the functionality of several established open-source tools:

| Tool/Concept      | Purpose                                      |
|:-----------------|:---------------------------------------------|
| Aircrack-ng       | Captures WPA handshakes & cracks passwords    |
| Hostapd & Dnsmasq | Create rogue APs and manage DHCP/DNS          |
| Macchanger        | Randomizes MAC addresses                      |
| Crunch            | Generates wordlists for brute-force attacks   |
| Reaver & Bully    | Exploit WPS vulnerabilities                   |
| Flask (Python)    | Hosts phishing portals                        |

**WiFiGuard** adheres to ethical hacking practices and should only be deployed in authorized test environments.

---

## 🛠️ Methodology

WiFiGuard is built as a collection of modular Python scripts, each responsible for a specific attack technique or utility.

### 📦 Core Modules

#### 🔹 Monitor Mode & MAC Spoofing
- `enable_monitor_mode.py` — Activates monitor mode.
- `disable_monitor_mode.py` — Restores managed mode.
- `change_mac_user_input.py` — Randomizes MAC via macchanger.

#### 🔹 Scanning & Reconnaissance
- `wifi_scanner.py` — Scans nearby networks with airodump-ng.
- `wifi_attack.py` — Captures WPA handshakes while performing deauth attacks.

#### 🔹 Rogue Access Point & Phishing
- `rogue_ap.py` — Sets up a fake AP using Hostapd/Dnsmasq.
- `captive_portal.py` — Hosts a fake login page (Flask) and logs credentials.

#### 🔹 Password Cracking
- `wifi_password_cracker.py` — Generates wordlists (Crunch) and cracks handshakes (Aircrack-ng).

#### 🔹 Tool Installation
- `tools_installer.py` — Installs required tools: Aircrack-ng, Reaver, Bettercap, etc.

#### 🔹 Main Interface
- `eth.py` — CLI-driven interface to execute all available attacks.

---

## 📊 Attack Workflow

### 📶 Reconnaissance
- Detect networks using **airodump-ng**
- Identify **BSSID**, **ESSID**, and **Channel**

### 🔨 Deauthentication Attack
- Disconnect clients via **aireplay-ng --deauth**
- Capture **WPA handshake**

### 🚨 Rogue AP Deployment
- Imitate target network with **Hostapd**
- Serve phishing pages via **Flask**

### 🔓 Password Cracking
- Generate custom wordlists (**Crunch**)
- Crack handshakes using **Aircrack-ng**

### 🕵️ MAC Spoofing
- Change MAC address to avoid detection (**macchanger**)

---

## 🛠️ Tools & Techniques

### 📌 Key Tools
| Tool         | Purpose                            |
|:-------------|:-----------------------------------|
| Aircrack-ng   | WPA/WPA2 handshake cracking        |
| Hostapd       | Rogue AP creation                  |
| Dnsmasq       | DHCP & DNS spoofing                |
| Macchanger    | MAC address spoofing               |
| Crunch        | Wordlist generation                |
| Reaver/Bully  | WPS PIN brute-forcing              |
| Flask         | Hosting phishing portals           |

### ⚙️ Techniques
✔ Monitor Mode Activation  
✔ Deauthentication Attack  
✔ WPA/WPA2 Handshake Capture  
✔ Rogue AP Setup  
✔ Captive Portal Credential Phishing  
✔ MAC Address Spoofing  
✔ Brute-Force Password Cracking  

---

## ⚖️ Ethical Considerations

WiFiGuard is intended **exclusively for educational and authorized penetration testing**. Unauthorized use on networks without explicit permission is illegal.

### ✅ Best Practices:
- Use only in **controlled lab environments**
- Obtain **written consent** before testing real networks
- Comply with **local and international cybersecurity laws**

---

## 📈 Conclusion

WiFiGuard is a hands-on learning toolkit offering practical exposure to Wi-Fi security vulnerabilities. By integrating multiple attack techniques into a cohesive CLI toolset, it supports:
- **Cybersecurity training**
- **Ethical hacking workshops**
- **Wireless security demonstrations**

### 📌 Future Enhancements:
- WPA3 attack simulations  
- Automated MITM attacks  
- Enhanced phishing templates  

---

## 📚 References

- [Aircrack-ng Documentation](https://www.aircrack-ng.org/)
- [Kali Linux Tools](https://tools.kali.org/)
- [Hostapd Guide](https://w1.fi/hostapd/)
- [IEEE 802.11 Security Standards](https://ieeexplore.ieee.org/)

---


## ⚠️ Disclaimer

**Developed strictly for educational purposes. Unauthorized use is illegal.**
