__author__ = 'ayost'

import socket
from os import system

UDP_IP = ""
UDP_PORT = 27693

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)     # UDP
sock.bind((UDP_IP, UDP_PORT))

while True:
    data = sock.recvfrom(256)
    if "status_check" in data:
        print "Sending status update"
        system("python status_update.py")
    elif "incoming_job" in data:
        print "Listening for incoming job"
        system("python run_job.py")