from events.ListSavedSSID import ListPesuSSID
from events.ScanWifi import scan_wifi

def identifying_strongest_router():
    
    networks = scan_wifi()  # getting the list of available networks
    
    # printing the list of available networks
    for network in networks:
        print(f"SSID: {network['ssid']}, BSSID: {network['bssid']}, Signal: {network['signal']}, Auth: {network['auth']}, Cipher: {network['cipher']}")

    strongest_band = -9999

    for network in networks:
        if network['signal'] > strongest_band:
            strongest_band = network['signal']
    print(strongest_band)  # Prints the strongest wifi signal


identifying_strongest_router()