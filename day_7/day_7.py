import numpy as np
import sys
sys.setrecursionlimit(10**6)
test=False
if test:
    sys.stdin=open('testcase.txt', 'r')
else:
    sys.stdin = open('input.txt', 'r')
lines = sys.stdin.readlines()
sys.stdin.close()
print(lines)