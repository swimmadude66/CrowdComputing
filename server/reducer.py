__author__ = 'ayost'

import sys
import re


def reducer():
    print "Reducing Data"
    f_in = open(sys.argv[1], 'rb')
    data = f_in.read()
    f_in.close()

    word_list = re.split(r'\s+', data)
    word_list.sort()

    print "Saving"
    fout = open(sys.argv[2], 'wb')
    for word in word_list:
        fout.write(word + "\n")
    fout.close()
    print "Done!"


if __name__ == "__main__":
    reducer()