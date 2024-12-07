import numpy as np
import sys
sys.setrecursionlimit(10**6)
test=False
if test:
    file=open('testcase.txt','r')
else:
    file=open('input.txt','r')
lines = file.readlines()
res=0
def check_part1(numsum,numbers)->bool:
    try_case_number = len(numbers)
    for i in range(1<<(try_case_number-1)):
        temp = numbers[0]
        for j in range(try_case_number-1):
            if (i & (1<<j)) >0 :
                temp *= numbers[j+1]
            else:
                temp += numbers[j+1]
        if temp == sum_num:
            return True
def back_tracking(sum_now,index):
    if index == len(numbers):
        if sum_now == sum_num:
            return True
        return False
    if back_tracking(sum_now+numbers[index],index+1):
        return True
    if back_tracking(sum_now*numbers[index],index+1):
        return True
    if back_tracking(int(str(sum_now)+str(numbers[index])),index+1):
        return True
for line in lines:
    sum_num = int(line.split(':')[0])
    numbers = [int(num) for num in line.split(':')[1].split()]
    if back_tracking(numbers[0],1):
        res+=sum_num
print(res)