from pywifi import PyWiFi
import time

import config.settings as cfgs


def scan_wifi():
    wifi = PyWiFi()  
    iface = wifi.interfaces()[0]  # Get the first wireless interface
    
    iface.scan()  # Start scanning
    time.sleep(int(cfgs.sleepTimeToScanForAvailableNetworks))  # Wait for the scan to complete
    
    scan_results = iface.scan_results()  # Get scan results
    
    networks = []
    for network in scan_results:
        networks.append({
            'ssid': network.ssid,
            'bssid': network.bssid,
            'signal': network.signal,
            'auth': network.akm[0] if network.akm else 'None',
            'cipher': network.cipher[0] if network.cipher else 'None'
        })
    
    return networks

