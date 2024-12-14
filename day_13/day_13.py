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
block=[]
temp_block=[]
for line in lines:
    if line!='\n':
        temp_block.append(line.strip())
    else:
        block.append(temp_block)
        temp_block=[]
block.append(temp_block)
file.close()
print(block)
res=0
res_x=[]
for m in block:
    A=m[0]
    B=m[1]
    Prize=m[2]
    x_a=int(A[A.find('X+')+2:A.find(',')])
    y_a=int(A[A.find('Y+')+2:])
    x_b=int(B[B.find('X+')+2:B.find(',')])
    y_b=int(B[B.find('Y+')+2:])
    x_p=int(Prize[Prize.find('X=')+2:Prize.find(',')]) + 10000000000000
    y_p=int(Prize[Prize.find('Y=')+2:]) + 10000000000000
    # x_p=x_a*i+x_b*j
    # y_p=y_a*i+y_b*j
    # i,j must be integers
    # 3*i + j min
    o=z3.Optimize()
    i=z3.Int('i')
    j=z3.Int('j')
    cost=z3.Int('cost')
    o.add(i*x_a+j*x_b==x_p)
    o.add(i*y_a+j*y_b==y_p)
    o.add(cost==3*i+j)
    o.add(i>=0)
    o.add(j>=0)
    o.add(i<=10000000000000)
    o.add(j<=10000000000000)
    if o.check():
        c=o.model()[cost]
        if c is not None:
            print(c.as_long())
            res+=c.as_long()
print(res)