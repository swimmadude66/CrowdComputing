__author__ = 'ayost'

import getpass
import requests
from uuid import getnode as get_mac


def authenticate():
    # identify device
    data = dict()
    data["machine-id"] = open("/etc/machine-id", 'r').read().strip()
    data["mac"] = str(get_mac())
    # validate identify device and attempt to add
    print "\nLog in to Crowd Computing to add this device"
    validated = False
    while not validated:
        data["userName"] = str(raw_input("Username: "))
        data["thePassword"] = getpass.getpass("Password: ")
        print "Attempting to add device"
        response = requests.post("http://54.86.187.108:3000/AddNode", data)
        if (response.status_code == 200) and ("accepted" in response.text):
            validated = True
        else:
            print("Login failed, please try again.")


if __name__ == "__main__":
    authenticate()

