import sys
import os
import math
import functools
import calc_cos as c
import time

count = 0

def get_mean(step1,step2):
    if len(step1.me[1]) != len(step2.me[1]):
        print('the length of the two vector dosn\'t match')
        raise SyntaxError
    length = len(step1.me[1])
    mean = {}
    for i in range(1,length):
        mean[i] = (step1.amount * float(step1.me[1][i]) + step2.amount * float(step2.me[1][i])) / (step1.amount + step2.amount)
    mean[0] = None
    return mean

def outputTree(root, file):
    if root.me[1][0] != None:
        s = ' %d [label="%s\\n" shape=box];\nn' % (root.me[0], root.me[1][0])
    else:
        s = ' %d [fontcolor=gray];\nn' % root.me[0]
    print(s, end='', file=file)
    if root.left != None:
        s = ' %d -> %d' % (root.me[0],root.left.me[0])
        s += ';\nn'
        print(s, end='', file=file)
        outputTree(root.left, file)
    if root.right != None:
        s = ' %d -> %d' % (root.me[0],root.right.me[0])
        s += ';\nn'
        print(s, end='', file=file)
        outputTree(root.right, file)

class step:
    def __init__(self,args):
        global count
        if len(args) == 1:
            self.left = None
            self.right = None
            self.me = [0,args[0]]
            self.amount = 1
        elif len(args) == 2:
            self.left = args[0]
            self.right = args[1]
            if self.left == None or self.right == None:
                self.me = None
            else:
                self.me = [0,get_mean(left,right)]
            self.amount = self.left.amount + self.right.amount
        else:
            raise TypeError
        self.me[0] = count
        count += 1

FILE = './a2.txt'
OUTPUT = './out.txt'

time1 = time.time()
f = open(FILE)
df = f.readlines()
l = []
ldf = len(df)
for s in range(ldf):
    ltemp = {}
    stemp = df[s].split()
    length = len(stemp)
    ltemp[0] = str(s + 1)
    for i in range(1,length):
        ltemp[i] = stemp[i].split(':')[1]
    l.append(step((ltemp,)))

time2 = time.time()
print('reading using time: %f' % (time2 - time1))
t = {}
while len(l) > 1:
    length = len(l)
    min_pair = [0,1]
    max_cos = 0
    for i in range(length):
        if l[i].me[0] not in t:
            t[l[i].me[0]] = {}
        for j in range(i + 1,length):
            if l[j].me[0] in t[l[i].me[0]]:
                cos = t[l[i].me[0]][l[j].me[0]]
            else:
                cos = c.calc_cos(l[i].me[1],l[j].me[1])
                t[l[i].me[0]][l[j].me[0]] = cos
            if cos > max_cos:
                max_cos = cos
                min_pair = [i,j]
    right = l.pop(min_pair[1])
    left = l.pop(min_pair[0])
    l.append(step((left,right)))

time3 = time.time()
print('clustering using time: %f' % (time3 - time2))

time3 = time.time()
out = open(OUTPUT, mode = 'w')
print('digraph {n',end = '', file = out)
outputTree(l[0] , out)
print('}' , end='',file=out)
time4 = time.time()
print('output using time: %f' % (time4 - time3))
out.close

f.close