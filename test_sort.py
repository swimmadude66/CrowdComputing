__author__ = 'ayost'


import sys
import re


f = open(sys.argv[1], 'r')
text = f.read()
f.close()
text = re.sub(r'[^A-Za-z\s]+', "", text)
words = re.split(r'\s+', text)
words.sort()
fout = open("sorted.txt", 'w')
for word in words:
    fout.write(word + "\n")
fout.close()
print "done!"
