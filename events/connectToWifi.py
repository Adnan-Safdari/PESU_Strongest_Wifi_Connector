from pywifi import PyWiFi, const, Profile
import time
import events.notify as notify

def connect_to_wifi(ssid):
    wifi = PyWiFi()  # Create a PyWiFi object
    iface = wifi.interfaces()[0]  # Get the first Wi-Fi interface

    profile = Profile()  # Create a Wi-Fi profile
    profile.ssid = ssid  # Set the SSID
    profile.auth = const.AUTH_ALG_OPEN  # Set authentication type
    # profile.akm.append(const.AKM_TYPE_WPA2PSK)  # Set encryption type
    profile.akm.append(const.AKM_TYPE_NONE) # Setting no encryption
    # profile.cipher = const.CIPHER_TYPE_CCMP  # Set cipher type
    # profile.key = password  # Commenting it as there is no password

    iface.add_network_profile(profile)  # Add the new profile

    iface.connect(profile)  # Connect to the network
    time.sleep(3)  # Wait a few seconds for the connection to establish

    if iface.status() == const.IFACE_CONNECTED:
        print(f"Connected to {ssid}")
        time.sleep(4)
        # notify.send_notification(title="Connected to Wifi", message=f"Successfully connected to {ssid}", timeout=1)
    else:
        print(f"Failed to connect to {ssid}")
        notify.send_notification(title="Failed to connect to Wifi", message=f"Connection to {ssid} Failed. Please connect manually", timeout=5)

