import sys
import os
import math
import functools
import calc_cos as c

FILE = './a2.txt'

f = open(FILE)
df = f.readlines()
l = []
for s in df:
    ltemp = {}
    stemp = s.split()
    length = len(stemp)
    ltemp[0] = stemp[0]
    for i in range(1,length):
        ltemp[i] = stemp[i].split(':')[1]
        l.append(ltemp)
os.system("pause")
f.close