__author__ = 'ayost'

import sys
import re
import os


def mapper():
    f = open(sys.argv[1], 'rb')
    data = f.read()
    f.close()

    num_nodes = int(sys.argv[2])
    print num_nodes
    data = re.sub(r'[^A-Za-x\s]', "", data)
    words = re.split(r'\s+', data)
    blocks = [[""]for x in range(26)]
    for word in words:
        if len(word) > 0:
            blocks[ord(word.lower()[0])-ord('a')].append(word)

    nodes = [[""]for x in range(num_nodes)]
    i = 0
    for block in blocks:
        nodeid = min(i // (len(blocks)//num_nodes), num_nodes-1)
        for word in block:
            nodes[nodeid].append(word)
        i += 1
    for y in range(len(nodes)):
        path = os.path.join("inputs", "block_"+str(y)+".input")
        fout = open(path, 'wb')
        for word in nodes[y]:
            fout.write(word+"\n")
        fout.close()


if __name__ == "__main__":
    mapper()


