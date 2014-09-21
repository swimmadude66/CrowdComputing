__author__ = 'ayost'


import psutil
import requests


def check_usage():
    status = dict()
    status["cpuusage"] = int(psutil.cpu_percent(interval=1))
    status["memufree"] = int(psutil.virtual_memory().free)
    status["swapfree"] = int(psutil.swap_memory().free)
    status["netusage"] = str(psutil.network_io_counters())
    response = requests.post("http://54.86.187.108:3000/sendNodeStatusUpdate", status)


if __name__ == "__main__":
    check_usage()