import collections
import sys
import numpy as np
import z3
from functools import *
d4 = [(0, 1), (0, -1), (1, 0), (-1, 0)]
sys.setrecursionlimit(10 ** 9)
test = False
if test:
    file = open('testcase.txt', 'r')
else:
    file = open('input.txt', 'r')
lines = file.readlines()
data = []
for line in lines:
    pv = line.split(' ')
    pos = pv[0][pv[0].find('p=') + 2:].split(',')
    v = pv[1][pv[1].find('v=') + 2:].split(',')
    data.append([int(pos[0]), int(pos[1]), int(v[0]), int(v[1])])
    # y,x,vy,vx
print(data[-1])
row=103
col=101
# row=7
# col=11
output=open('output.txt','w')
for T in range(10000):
    map = [['.' for i in range(col)] for j in range(row)]
    dupe=False
    for i in data:
        nx=(i[1]+i[3]*T) % row
        ny=(i[0]+i[2]*T) % col
        # if ny==(col-1)//2 or nx==(row-1)//2:
        #     continue
        # left=(ny<=(col-1)//2)
        # up=(nx<=(row-1)//2)
        # count[(left,up)]+=1
        if map[nx][ny]=='#':
            dupe=True
        map[nx][ny]='#'
    if not dupe:
        output.write('T='+str(T)+'\n')
        for i in map:
            output.write(''.join(i)+'\n')
        output.write('\n')
# print(count)
# p=1
# for i in count.values():
#     p*=i
# print(p)