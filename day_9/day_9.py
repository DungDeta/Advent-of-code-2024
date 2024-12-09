import sys
from collections import deque
sys.setrecursionlimit(10 ** 6)
test = False
if test:
    file = open('testcase.txt', 'r')
else:
    file = open('input.txt', 'r')
line = file.read()
num=[int(i) for i in list(line)]
arr=[]
num_now=0
for i in range(len(num)):
    if i%2==0:
        for _ in range(num[i]):
            arr.append(num_now)
        num_now+=1
    else:
        for _ in range(num[i]):
            arr.append('#')
# l=0
# r=len(arr)-1
# print(arr)
# while l<r: part 1
    # if arr[l]=='#' and arr[r]!='#':
    #     arr[l],arr[r]=arr[r],arr[l]
    #     l+=1
    #     r-=1
    # elif arr[l]!='#':
    #     l+=1
    #     if arr[r] == '#':
    #         r-=1
#Sao không dùng deque nhỉ ??
arr_num=[i for i in num[::2]]
res=0
m=num_now-1
print(arr_num,m)
while m>0:
    r=arr_num[m]
    if r==0:
        m-=1
        continue
    space=0
    for i in range(len(arr)):
        if arr[i]==m:
            break
        if arr[i]=='#':
            space+=1
        else:
            space=0
        if space>=r:
            for j in range(len(arr)):
                if arr[j]==m:
                    arr[j]='#'
            for j in range(arr_num[m]):
                arr[i-j]=m
            break
    m-=1

for i in range(len(arr)):
    if arr[i]!='#':
        res+=arr[i]*i
print(res)