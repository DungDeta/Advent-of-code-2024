import sys
from collections import defaultdict, deque

sys.setrecursionlimit(10 ** 6)
input_file = open('input.txt', 'r')
lines = input_file.readlines()
dict_nums: dict[int, list[int]] = {}
i = 1
line = lines[0]
while line != '\n':
    nums = line.split('|')
    key = int(nums[0])
    vaules = int(nums[1])
    if key not in dict_nums:
        dict_nums[key] = []
    if vaules not in dict_nums:
        dict_nums[vaules] = []
    dict_nums[key].append(vaules)
    line = lines[i]
    i += 1
print(dict_nums)
lines = lines[i:]
res = 0
arr_part_2 = []


def check_in(arr: list[int], dic: list[int]) -> bool:
    return all(i in dic for i in arr)


for line in lines:
    arr = [int(x) for x in line.split(',')]
    check = True
    for i in range(len(arr)):
        if not (arr[i] in dict_nums and check_in(arr[i + 1:], dict_nums[arr[i]])):
            check = False
            break
    if check:
        res += arr[len(arr) // 2]
    else:
        arr_part_2.append(arr)
print(res)


def topological_sort(arr: list[int]) -> list[int]:
    graph = defaultdict(int)
    indegree = defaultdict(int)
    node = set(arr)
    for key, values in dict_nums.items():
        if key in node:
            for value in values:
                if value in node:
                    graph[key] += 1
                    indegree[value] += 1
                    if key not in indegree:
                        indegree[key] = 0
    queue = deque()
    res = []
    for key in node:
        if indegree[key] == 0:
            queue.append(key)
    while queue:
        node = queue.popleft()
        res.append(node)
        for value in dict_nums[node]:
            indegree[value] -= 1
            if indegree[value] == 0:
                queue.append(value)
    return res


res = 0
for arr in arr_part_2:
    arr = topological_sort(arr)
    res += arr[len(arr) // 2]
print(res)
