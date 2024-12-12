import sys

sys.setrecursionlimit(10 ** 6)
from collections import Counter

input_file = open('input.txt', 'r')
lines = input_file.readlines()
arr_1 = []
arr_2 = []
count_2 = Counter()
res = 0
for line in lines:
    num = line.split('   ')
    arr_1.append(int(num[0]))
    arr_2.append(int(num[1]))
    count_2[int(num[1])] += 1
for i in arr_1:
    res += i * count_2[i]
print(res)
arr_1 = sorted(arr_1)
arr_2 = sorted(arr_2)
res = 0
distance = 0
for i in range(len(arr_1)):
    distance = abs(arr_1[i] - arr_2[i])
    res += distance
print(res)
