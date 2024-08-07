from events.ListSavedSSID import ListPesuSSID
from events.ScanWifi import scan_wifi
from events.browserLogin import browser_login

import config.settings as cfgs

def identifying_strongest_router():
    """This functions checks the signal strength and finds the strongest wifi router connection"""

    networks = scan_wifi()  # getting the list of available networks
    
    # printing the list of available networks
    for network in networks:
        print(f"SSID: {network['ssid']}, BSSID: {network['bssid']}, Signal: {network['signal']}, Auth: {network['auth']}, Cipher: {network['cipher']}")


    strongest_band = -9999  # sample lowest value

    # Looping through all the networks to find the strongest network
    for network in networks:
        if network['signal'] < strongest_band: # Lowest signal number is the strongest signal
            strongest_band = network['signal']
    print(strongest_band)  # Prints the strongest wifi signal


    #TODO: Get the fastest wifi access point's SSID and BSSID stored into a var/list/dict
    #TODO: Connect to the fastest wifi access point

identifying_strongest_router()


browser_login(cfgs.captive_portal_address) # Calling the selenium function and giving it the local ip to login to the portal
