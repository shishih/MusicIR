import sys
import os
import math
import functools
import calc_cos as c

def get_mean(v1,v2):
    if len(v1) != len(v2):
        print('the length of the two vector dosn\'t match')
        raise SyntaxError
    length = len(v1)
    mean = {}
    for i in range(1,length):
        mean[0] = 'null'
        mean[i] = (float(v1[i]) + float(v2[i])) / 2
    return mean

class step:
    def __init__(self,args):
        if len(args) == 1:
            self.left = None
            self.right = None
            self.me = args[0]
        elif len(args) == 2:
            self.left = args[0]
            self.right = args[1]
            if self.left == None or self.right == None:
                self.me = None
            else:
                self.me = get_mean(left.me,right.me)
        else:
            raise TypeError

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
    l.append(step((ltemp,)))

while len(l) > 1:
    length = len(l)
    min_pair = [0,1]
    max_cos = 0
    for i in range(length):
        for j in range(i + 1,length):
            cos = c.calc_cos(l[i].me,l[j].me)
            if cos > max_cos:
                max_cos = cos
                min_pair = [i,j]
    right = l.pop(min_pair[1])
    left = l.pop(min_pair[0])
    l.append(step((left,right)))

print(l[0])

os.system("pause")
f.close