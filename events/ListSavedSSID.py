import json

def ListPesuSSID():
    """This function is used to list all the SSIDs of PESU. Used to verify if the strongest network is a PES Access Point"""

    with open("db/AccessPointNames.json", "r") as file:
        data = json.load(file)

    return data['SSID']

