__author__ = 'ayost'

import socket
from os import system

TCP_IP = ""
TCP_PORT = 2667


def get_job():
    # create TCP connection to server to get job
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((TCP_IP, TCP_PORT))
    s.listen()
    conn, addr = s.accept()
    data = conn.recv(268435456)
    # run reduce job on supplied data
    reducer = data.split(":")[0]
    fout = open("./incoming/reducer.py", 'w')
    fout.write(reducer)
    fout.close()
    result = system("python incoming/reducer.py incoming/data")
    # return results over socket
    conn.send(result)
    # wait for ACK
    conn.listen()
    # disconnect and delete data
    system("rm -rf incoming")
    conn.close()
    s.close()

