__author__ = 'ayost'

import sys
import re


def reducer():
    f_in = open(sys.argv[1], 'rb')
    data = f_in.read()
    f_in.close()

    word_list = re.split(r'\s+', data)
    word_list.sort()

    fout = open(sys.argv[2], 'wb')
    for word in word_list:
        fout.write(word + "\n")
    fout.close()


if __name__ == "__main__":
    reducer()