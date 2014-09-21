__author__ = 'ayost'
import time
import sys
import os

nodes_list = ['128.61.66.25', '128.61.66.26', '128.61.66.27', '128.61.66.28', '128.61.66.29']
# get sys.argv[2] number of IPs


def prepare_job():
    data_file = sys.argv[1]
    os.system("python mapper.py " + data_file + " " + str(len(nodes_list)))
    num = 0
    for node in nodes_list:
        n_ip = node
        os.system("python node_connect.py " + n_ip + " incoming_job")
        time.sleep(1)
        os.system("python send_job.py " + str(n_ip) + " inputs/block_"+str(num)+".input " + str(num))

    done = False
    while not done:
        if len([name for name in os.listdir('outputs') if os.path.isfile(name)]) == len(nodes_list):
            done = True

    for root, dirnames, filenames in os.walk('outputs'):
        filenames.sort()
        f_done = open("outputs/output.total", 'wb')
        for filename in filenames:
            f_done.write(open(filename, 'rb').read())
        f_done.close()
    print("Job stored in /outputs/output.total!")


if __name__ == "__main__":
    prepare_job()


