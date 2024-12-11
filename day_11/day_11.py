import sys
import collections as c

import numpy as np

sys.setrecursionlimit(10 ** 6)
test = False
if test:
    file = open('testcase.txt', 'r')
else:
    file = open('input.txt', 'r')
line= file.readline()
arr=[int(i) for i in line.split(" ")]
cu=c.Counter(arr)
for _ in range(75):
    nc=c.Counter()
    for i in cu.keys():
        feq=cu[i]
        if i==0:
            nc[1]+=feq
        elif len(str(i))%2==0:
            num=str(i)
            nc[int(num[:len(num)//2])]+=feq
            nc[int(num[len(num)//2:])]+=feq
        else:
            nc[i*2024]+=feq
    cu=nc
print(sum(cu.values()))