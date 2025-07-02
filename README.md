# WiFiHunter - Advanced Wi-Fi Scanner for Windows using Python
<p align="center">
  <img src="https://img.shields.io/badge/Author-farnaztr-grey" />
  <img src="https://img.shields.io/badge/Project-WiFiHunter-purple" />
  <img src="https://img.shields.io/github/stars/farnaztr/WiFiHunter?style=social" />
</p>

---

## Overview

**WiFiHunter** is a lightweight, Python-powered toolkit for scanning and analyzing nearby Wi-Fi networks on **Windows**.  
Whether you're a **network analyst**, **ethical hacker**, or simply a curious developer, this tool provides valuable insights into the wireless environment around you.

---

## Features

-  Fast & accurate Wi-Fi scanning via `netsh` (no third-party dependencies)
-  Displays SSID, signal strength, and encryption type
-  Supports WEP, WPA, WPA2, WPA3 detection
-  100% native Windows support (no admin rights needed in most cases)
-  Clean, beginner-friendly Python code
-  Fully customizable for your needs

---

## Requirements

- **Python 3.6+**
- Works only on **Windows OS**
- No additional libraries required (uses built-in modules)

---

## How It Works

WiFiHunter uses the native Windows `netsh wlan show networks mode=bssid` command to collect Wi-Fi network data.  
It then parses the output using **regex** and presents key info in a readable format:

```bash
SSID: MyNetwork, Signal: 87%, Encryption: WPA2-Personal
```
---

##📂 Usage
Clone the repository:

```bash
git clone https://github.com/farnaztr/WiFiHunter.git
cd WiFiHunter
```
Run the script:

```bash
python wifihunter.py
```
## Sample Output

```bash
SSID: HomeWiFi, Signal: 78%, Encryption: WPA2-Personal
SSID: Cafe_Free, Signal: 32%, Encryption: Open
SSID: TP-LINK_1234, Signal: 50%, Encryption: WPA3
```
## Limitations!!

1.Only works on Windows

2.Cannot connect to networks – it’s a scanner, not a client

3.May require terminal with UTF-8 support for full compatibility



