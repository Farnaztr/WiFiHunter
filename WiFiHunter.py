import subprocess
import re

def wifi():
    detail = subprocess.run(['netsh', 'wlan', 'show', 'networks', 'mode=bssid'], capture_output=True, text=True)
    output = detail.stdout
    networks_list = []
    blocks = output.split('\n\n') 
    for network_info in blocks:
        ssid_search = re.search(r'SSID \d+ : (.+)', network_info)
        if not ssid_search:
            continue
        ssid = ssid_search.group(1).strip()

        encryption_search = re.search(r'Authentication\s+:\s+(.+)', network_info)
        encryption = encryption_search.group(1).strip() if encryption_search else "N\A"

        signal_search = re.search(r'Signal\s+:\s+(\d+)%', network_info)
        signal = signal_search.group(1) + "%" if signal_search else "N\A"

        networks_list.append({
            'SSID': ssid,
            'Signal': signal,
            'Encryption': encryption
        })
    return networks_list
if __name__ == "__main__":
    wifi_networks = wifi()
    for net in wifi_networks:
        print(f"SSID: {net['SSID']}, Signal: {net['Signal']}, Encryption: {net['Encryption']}")