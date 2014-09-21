__author__ = 'ayost'

import socket
import sys
import os

TCP_IP = '128.61.66.25'
TCP_PORT = 2667
BUFFER_SIZE = 536870912


def send_job():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((sys.argv[1], TCP_PORT))

    reducer = open("reducer.py", 'rb').read()
    data_file = open(sys.argv[2], 'rb').read()
    data = data_file
    s.send(data)
    s.send(reducer)
    s.send(sys.argv[3])
    print("data sent")
    finished_data = ""
    while 1:
        finished_data = s.recv(4096)
        if not data:
            break
    s.send('ACK')
    s.close()

    data_parts = finished_data.split("\t")
    outfile_path = "finished_block_" + str(data_parts[0]) + ".done"
    outfile_contents = data_parts[1]

    fout = open(os.path.join("outputs", outfile_path), 'wb')
    fout.write(outfile_contents)
    fout.close()


if __name__ == "__main__":
    send_job()