__author__ = 'ayost'

from socket import socket
from os import system

UDP_IP = ""
UDP_PORT = 27693

sock = socket(socket.AF_INET, socket.SOCK_DGRAM)     # UDP
sock.bind((UDP_IP, UDP_PORT))

while True:
    data = sock.recvfrom(256)
    if "status_check" in data:
        system("python status_update.py")
    elif "incoming_job" in data:
        system("python run_job.py")