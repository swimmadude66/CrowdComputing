__author__ = 'ayost'

from socket import socket

UDP_IP = "128.61.66.25"
UDP_PORT = 27693
MESSAGE = "status_check"

print "UDP target IP:", UDP_IP
print "UDP target port:", UDP_PORT
print "message:", MESSAGE

sock = socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.sendto(MESSAGE, (UDP_IP, UDP_PORT))