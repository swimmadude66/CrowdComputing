__author__ = 'ayost'

import socket
import os
import re

TCP_IP = ""
TCP_PORT = 2667


def get_job():
    # create TCP connection to server to get job
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((TCP_IP, TCP_PORT))
    print "Listening for TCP connection..."
    s.listen(5)
    conn, addr = s.accept()
    print "Accepted"
    data = ""
    while 1:
        data = conn.recv(1024)
        if not data:
            break
    # run reduce job on supplied data
    print "data received"
    os.system("rm -rf ./incoming")
    os.makedirs("./incoming/data")
    os.makedirs("./incoming/scripts")
    os.makedirs("./incoming/output")
    data_path = os.path.join("incoming/data", "block.data")
    out_path = os.path.join("incoming/output", "block.out")
    f_data = open(data_path, 'wb')
    f_data.write(data)
    f_data.close()
    reducer = ""
    while 1:
        reducer = conn.recv(1024)
        if not reducer:
            break
    fout = open("incoming/scripts/reducer.py", 'wb')
    fout.write(reducer)
    fout.close()
    nodeid = ""
    while 1:
        nodeid = conn.recv(1024)
        if not nodeid:
            break
    # reduce the file
    os.system("python incoming/scripts/reducer.py " + data_path + " " + out_path)
    print reducer
    # return results over socket
    conn.send(str(nodeid) + "\001" + open(out_path, 'rb').read())
    # wait for ACK
    conn.listen(1)
    # disconnect and delete data
    os.system("rm -rf incoming")
    conn.close()
    s.close()

if __name__ == "__main__":
    get_job()