__author__ = 'ayost'

import socket

UDP_IP = "128.61.66.25"
UDP_PORT = 27693
MESSAGE = "status_check"

print "UDP target IP:", UDP_IP
print "UDP target port:", UDP_PORT
print "message:", MESSAGE

sock = socket.socket(socket.AF_INET,        # Internet
                     socket.SOCK_DGRAM)     # UDP
sock.sendto(MESSAGE, (UDP_IP, UDP_PORT))