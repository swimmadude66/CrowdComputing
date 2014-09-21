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
    success = False
    while not validated:
        data["userName"] = str(raw_input("\tUsername: "))
        data["thePassword"] = getpass.getpass("\tPassword: ")
        print "\nAttempting to add device"
        response = requests.post("http://54.86.187.108:3000/addNode", data)
        if (response.status_code == 200) and ("Success" in response.text):
            validated = True
            success = True
        elif (response.status_code == 200) and ("er_dup_entry" in response.text.lower()):
            validated = True
            success = False
            print "Node already exists in table"
        else:
            print("Login failed, please try again.")
    if success:
        print "\n\nDevice Added!"

if __name__ == "__main__":
    authenticate()

