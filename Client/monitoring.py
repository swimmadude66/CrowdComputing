__author__ = 'ayost'


import psutil
import os


def check_usage():
    cpucount = psutil.cpu_count()
    cpuusage = psutil.cpu_percent(interval=1)
    memufree = psutil.virtual_memory().free
    swapfree = psutil.swap_memory().free
    netusage = psutil.network_io_counters()
    psutil.disk_partitions()
    print(os.system('python reducer.py'))


if __name__ == "__main__":
    check_usage()