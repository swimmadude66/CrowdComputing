__author__ = 'ayost'

import socket
import os

UDP_IP = ""
UDP_PORT = 27693

sock = socket.socket(socket.AF_INET,        # Internet
                     socket.SOCK_DGRAM)     # UDP
sock.bind((UDP_IP, UDP_PORT))

while True:
    data = sock.recvfrom(256)
    if "status_check" in data:
        os.system("python status_update.py")