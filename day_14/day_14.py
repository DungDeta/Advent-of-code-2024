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