from events.ListSavedSSID import ListPesuSSID
from events.ScanWifi import scan_wifi
from events.browserLogin import browser_login
from events.connectToWifi import connect_to_wifi

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
    strongest_wifi_details = [{"ssid": "Sample", "bssid":"SampleMac", "singal":"-777", "auth":"SampleAuth", "cipher":"SampleCipher"}]  # This sample data will get replaced

    # Looping through all the networks to find the strongest network
    available_pesu_netowrks=[]
    for network in networks:
        
        if network['ssid'] in ListPesuSSID():
            available_pesu_netowrks.append({"ssid": network['ssid'], "bssid":network['bssid'], "signal":network['signal'], "auth":network['auth'], "cipher": network['cipher']})
    

    for network in available_pesu_netowrks:
        print(network)
        if network['signal'] > strongest_band: # Lowest signal number is the strongest signal
            strongest_band = network['signal'] 
            strongest_wifi_details[0] = {"ssid": network['ssid'], "bssid":network['bssid'], "signal":network['signal'], "auth":network['auth'], "cipher": network['cipher']}
    print("=======================================================")
    print(f"The Router with the fastest connection is: {strongest_wifi_details}")    
    print("=======================================================")

    # Connecting to the wifi network
    ssid_to_connect = strongest_wifi_details[0]['ssid']
    connect_to_wifi(ssid=ssid_to_connect)

    browser_login(cfgs.captive_portal_address) # Calling the selenium function and giving it the local ip to login to the portal


identifying_strongest_router()
