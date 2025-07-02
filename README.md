# WiFiHunter - Advanced Wi-Fi Scanner for Windows using Python

![Author](https://img.shields.io/badge/Author-farnaztr-grey)
![Project](https://img.shields.io/badge/Project-WiFiHunter-purple)
![Downloads](https://img.shields.io/badge/downloads-1.5k-brightgreen)
![Stars](https://img.shields.io/github/stars/farnaztr/WiFiHunter?style=social)

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

---

##📂 Usage
Clone the repository:

git clone https://github.com/farnaztr/WiFiHunter.git
cd WiFiHunter
