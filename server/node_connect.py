__author__ = 'ayost'

import socket
import sys


UDP_IP = sys.argv[1]
UDP_PORT = 27693
MESSAGE = sys.argv[2]

print "UDP target IP:", UDP_IP
print "UDP target port:", UDP_PORT
print "message:", MESSAGE

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.sendto(MESSAGE, (UDP_IP, UDP_PORT))