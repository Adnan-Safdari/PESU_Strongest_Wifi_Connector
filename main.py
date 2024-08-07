from events.ListSavedSSID import ListPesuSSID
from events.ScanWifi import scan_wifi
from events.browserLogin import browser_login

import config.settings as cfgs

def identifying_strongest_router():
    """This functions checks the signal strength and finds the strongest wifi router connection"""

    networks = scan_wifi()  # getting the list of available networks
    
    # printing the list of available networks
    print("=======================================================")
    for network in networks:
        print(f"SSID: {network['ssid']}, BSSID: {network['bssid']}, Signal: {network['signal']}, Auth: {network['auth']}, Cipher: {network['cipher']}")
    print("=======================================================")

    strongest_band = -999  # sample lowest value
    strongest_wifi_details = [{"ssid": "Sample", "bssid":"SampleMac", "singal":"-777", "auth":"SampleAuth"}]  # This sample data will get replaced

    # Looping through all the networks to find the strongest network
    for network in networks:
        if network['signal'] > strongest_band: # Lowest signal number is the strongest signal
            strongest_band = network['signal'] 
            strongest_wifi_details[0] = {"ssid": network['ssid'], "bssid":network['bssid'], "signal":network['signal'], "auth":network['auth']}
            
            #TODO: Check if the wifi SSID is a PESU Access Point
    
    print(f"strongest_wifi_details: {strongest_wifi_details}")

    #TODO: Connect to the fastest wifi access point

identifying_strongest_router()


# browser_login(cfgs.captive_portal_address) # Calling the selenium function and giving it the local ip to login to the portal
