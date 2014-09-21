__author__ = 'ayost'

import getpass
import requests


def authenticate():
    # identify device
    data = dict()
    data["machine_id"] = open("/etc/machine-id", 'r').read().strip()
    # validate identify device and attempt to add
    print "\nLog in to Crowd Computing to add this device"
    validated = False
    while not validated:
        data["userName"] = str(raw_input("Username: "))
        data["thePassword"] = getpass.getpass("Password: ")
        print "\nAttempting to add device"
        response = requests.post("http://54.86.187.108:3000/addNode", data)
        if (response.status_code == 200) and ("granted" in response.text):
            validated = True
        else:
            print("Login failed, please try again.")
    print "\n\nDevice Added!"

if __name__ == "__main__":
    authenticate()

